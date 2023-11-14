import styled, { createGlobalStyle } from 'styled-components'
import Coordinate from './components/Coordinate'
import Log from './components/Log'
import Pause from './components/Pause'

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
  return (
    <>
      <GlobalStyle />

      <Coordinate width={10} height={6} />
      <Section>
        <Log />
        <Pause />
      </Section>
    </>
  )
}
