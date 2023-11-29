import { ChangeEvent, useState } from 'react'
import { useMutation } from '@tanstack/react-query'
import { instance } from '../utils/axios'
import { Position } from '../utils/type'
import useLog from './useLog'

type RequestBody = {
  map: string
  start: string
  predefined: string
  hazard: string
  colorBlob: string
}

type ResponseBody = {
  map: { width: number; height: number }
  robot: { position: Position; direction: number }
  predefined: Position[]
  hazard: Position[]
  colorBlob: Position[]
}

export default function useCreateMap() {
  const [map, setMap] = useState<Omit<ResponseBody, 'robot'>>()
  const [form, setForm] = useState<RequestBody>({
    map: '',
    start: '',
    predefined: '',
    hazard: '',
    colorBlob: '',
  })
  const { mutateAsync } = useMutation({
    mutationFn: (body: RequestBody) => instance.post<ResponseBody>('/', body),
  })
  const { addLog } = useLog()

  const handleChange = (event: ChangeEvent<HTMLInputElement>) =>
    setForm(prev => ({ ...prev, [event.target.name]: event.target.value }))

  const handleCreate = async () => {
    if (!Object.values(form).every(value => !!value)) return

    const {
      data: { robot, ...data },
    } = await mutateAsync(form)

    setMap({
      ...data,
      map: { width: data.map.width + 1, height: data.map.height + 1 },
    })
    addLog('재난 지역 모델 생성')

    return robot
  }

  return { map, form, setMap, handleChange, handleCreate }
}
