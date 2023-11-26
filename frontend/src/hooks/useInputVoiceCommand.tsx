import { useEffect } from 'react'
import { useAudioRecorder } from 'react-audio-voice-recorder'
import { useMutation } from '@tanstack/react-query'
import axios from 'axios'

export default function useInputVoiceCommand() {
  const { startRecording, stopRecording, recordingBlob, isRecording } =
    useAudioRecorder()
  const { mutate, isPending } = useMutation({
    mutationFn: (voice: Blob) =>
      axios.post(
        '/voice',
        { voice },
        {
          headers: { 'Content-Type': 'multipart/form-data' },
          baseURL: import.meta.env.VITE_SERVER_ENDPOINT,
        },
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
