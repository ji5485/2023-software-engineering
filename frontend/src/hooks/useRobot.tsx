import { useEffect, useState } from 'react'
import { useQuery } from '@tanstack/react-query'
import { instance } from '../utils/axios'
import useLog from './useLog'

type RobotType = {
  x: number
  y: number
  direction: number
}

type ResponseBodyType = {
  finished: boolean
  position: RobotType
  direction: number
}

export default function useRobot(enabled: boolean) {
  const [finished, setFinished] = useState<boolean>(false)
  const [delayedEnabled, setDelayedEnabled] = useState<boolean>(enabled)
  const [robot, setRobot] = useState<RobotType | null>(null)

  const { addLog } = useLog()
  const { data } = useQuery({
    queryKey: ['robot'],
    queryFn: () => instance.post<ResponseBodyType>('/robot', {}),
    refetchInterval: !finished ? 3000 : false,
    refetchOnMount: false,
    refetchOnWindowFocus: false,
    enabled: !finished && delayedEnabled,
  })

  const handleSetRobot = (robot: RobotType) => setRobot(robot)

  useEffect(() => {
    if (enabled) setTimeout(() => setDelayedEnabled(true), 3000)
    else setDelayedEnabled(false)
  }, [enabled])

  useEffect(() => {
    if (data?.data.finished) {
      setFinished(true)
      addLog('탐색 완료')
    } else if (data) addLog('로봇 이동')
  }, [data, addLog])

  return { robot, handleSetRobot }
}
