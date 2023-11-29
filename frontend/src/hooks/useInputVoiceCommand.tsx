import { useEffect } from 'react'
import { useAudioRecorder } from 'react-audio-voice-recorder'
import { useMutation } from '@tanstack/react-query'
import { instance } from '../utils/axios'

export default function useInputVoiceCommand() {
  const { startRecording, stopRecording, recordingBlob, isRecording } =
    useAudioRecorder()
  const { mutate, isPending } = useMutation({
    mutationFn: (voice: Blob) =>
      instance.post(
        '/voice',
        { voice },
        { headers: { 'Content-Type': 'multipart/form-data' } },
      ),
    onSuccess: () => console.log('success'),
    onError: e => {
      console.log('error')
      console.log(e)
    },
  })

  useEffect(() => {
    if (recordingBlob) mutate(recordingBlob)
  }, [mutate, recordingBlob])

  return { startRecording, stopRecording, isRecording, isPending }
}
