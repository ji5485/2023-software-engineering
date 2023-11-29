import { useEffect } from 'react'
import { useAudioRecorder } from 'react-audio-voice-recorder'
import { useMutation } from '@tanstack/react-query'
import { instance } from '../utils/axios'
import useLog from './useLog'

export default function useInputVoiceCommand() {
  const { startRecording, stopRecording, recordingBlob, isRecording } =
    useAudioRecorder()
  const { addLog } = useLog()
  const { mutate, isPending } = useMutation({
    mutationFn: (voice: Blob) =>
      instance.post(
        '/voice',
        { voice },
        { headers: { 'Content-Type': 'multipart/form-data' } },
      ),
    onSuccess: () => {
      addLog('음성 인식 성공')
    },
    onError: e => {
      addLog('음성 인식 실패')
      console.log(e)
    },
  })

  useEffect(() => {
    if (recordingBlob) mutate(recordingBlob)
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
