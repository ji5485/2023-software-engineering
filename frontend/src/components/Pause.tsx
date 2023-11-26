import styled from 'styled-components'

type PauseProps = {
  onClick: () => void
  isRecording: boolean
}

export const Wrapper = styled.button<{ $isRecording: boolean }>`
  border-radius: 8px;
  border: 0;
  background: #7950f2;
  font-size: 15px;
  font-weight: 600;
  color: #ffffff;
  outline: none;
  cursor: pointer;
  transition: background 0.15s;

  &:hover {
    background: #6741d9;
  }
`

export default function Pause({ onClick, isRecording }: PauseProps) {
  return (
    <Wrapper onClick={onClick} $isRecording={isRecording}>
      {isRecording ? '녹음 중...' : '일시정지'}
    </Wrapper>
  )
}
