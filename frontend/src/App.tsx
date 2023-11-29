import styled, { createGlobalStyle } from 'styled-components'
import Coordinate from './components/Coordinate'
import Log from './components/Log'
import Form from './components/Form'
import Button from './components/Button'
import useInputVoiceCommand from './hooks/useInputVoiceCommand'
import useCreateMap from './hooks/useCreateMap'

const GlobalStyle = createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Pretendard, 'Noto Sans KR', sans-serif;
  }

  html, body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
  }

  #root {
    display: flex;
    justify-content: center;
    gap: 80px;
  }
`

const Section = styled.div`
  display: grid;
  grid-template-rows: 1fr 50px;
  grid-gap: 20px;
  width: 300px;
  min-height: 400px;
`

export default function App() {
  const { map, form, handleChange, handleCreate } = useCreateMap()
  const { startRecording, stopRecording, isRecording, isPending } =
    useInputVoiceCommand()

  return (
    <>
      <GlobalStyle />

      {map ? <Coordinate {...map} /> : null}

      {!map ? (
        <Section>
          <Form form={form} handleChange={handleChange} />
          <Button onClick={() => console.log()}>재난 지역 모델 생성</Button>
        </Section>
      ) : (
        <Section>
          <Log />
          <Button
            onClick={isRecording ? stopRecording : startRecording}
            disabled={isRecording}
          >
            {isRecording ? '녹음 중...' : '일시정지'}
          </Button>
        </Section>
      )}
    </>
  )
}
