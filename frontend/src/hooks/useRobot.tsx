import { useCallback, useEffect, useState } from 'react'
import { useQuery } from '@tanstack/react-query'
import { instance } from '../utils/axios'
import { Position, SpotType } from '../utils/type'
import useLog from './useLog'
import useMap from './useMap'

type RobotType = { position: Position; direction: number }

type ResponseBodyType = {
  error: string | null
  finished: boolean
  robot: RobotType
  is_predefined: boolean
  ratio: string
  sensor_data: {
    hazard: Position
    color_blob: Position[]
    positioning: boolean
  }
}

export default function useRobot(enabled: boolean) {
  const [finished, setFinished] = useState<boolean>(false)
  const [delayedEnabled, setDelayedEnabled] = useState<boolean>(enabled)
  const [robot, setRobot] = useState<RobotType | null>(null)

  const { addLog } = useLog()
  const { handleDetectSpot } = useMap()
  const { data, refetch } = useQuery({
    queryKey: ['robot'],
    queryFn: () => instance.post<ResponseBodyType>('/robot', {}),
    // refetchInterval: !finished ? 3000 : false,
    refetchOnMount: false,
    refetchOnWindowFocus: false,
    retry: false,
    enabled: !finished && delayedEnabled,
  })

  const handleSetRobot = useCallback((robot: RobotType) => setRobot(robot), [])

  useEffect(() => {
    if (enabled) setTimeout(() => setDelayedEnabled(true), 3000)
    else setDelayedEnabled(false)
  }, [enabled])

  useEffect(() => {
    if (!data) return

    const { robot, finished, error, is_predefined, sensor_data } = data.data

    if (is_predefined)
      setTimeout(() => addLog(`탐색 완료 (${data.data.ratio})`), 0)

    if (finished) {
      setFinished(true)
      if (error) setTimeout(() => addLog(error), 0)
    }

    if (sensor_data.positioning) addLog('로봇 위치 재설정')

    if (sensor_data.hazard) {
      handleDetectSpot(SpotType.HAZARD, sensor_data.hazard)
      addLog('위험 지점 탐지')
    }

    if (sensor_data.color_blob.length > 0) {
      sensor_data.color_blob.forEach(position =>
        handleDetectSpot(SpotType.COLOR_BLOB, position),
      )
      addLog('중요 지점 탐지')
    }

    if (robot) handleSetRobot(data.data.robot)
  }, [data, addLog, handleDetectSpot, handleSetRobot])

  return { robot, handleSetRobot, refetch }
}
