import { useEffect } from 'react'
import { useAudioRecorder } from 'react-audio-voice-recorder'
import { useMutation } from '@tanstack/react-query'
import { instance } from '../utils/axios'
import useLog from './useLog'
import useMap from './useMap'

export default function useInputVoiceCommand() {
  const { addLog } = useLog()
  const { handleAddSpot } = useMap()
  const { startRecording, stopRecording, recordingBlob, isRecording } =
    useAudioRecorder()
  const { mutate, isPending } = useMutation({
    mutationFn: (voice: FormData) =>
      instance.post('/voice', voice, {
        headers: { 'Content-Type': 'multipart/form-data' },
      }),
    onSuccess: result => {
      console.log(result)
    },
    onError: e => {
      addLog('음성 인식 실패')
      console.log(e)
    },
  })

  useEffect(() => {
    if (recordingBlob) {
      const file = new File([recordingBlob], 'voice.wav', { type: 'audio/wav' })
      const data = new FormData()
      data.append('voice', file)

      mutate(data)
    }
  }, [mutate, recordingBlob])

  const handleStartRecord = () => {
    startRecording()
    addLog('음성 인식 시작')
  }

  const handleStopRecord = () => {
    stopRecording()
    addLog('음성 인식 종료')
  }

  return { handleStartRecord, handleStopRecord, isRecording, isPending }
}
