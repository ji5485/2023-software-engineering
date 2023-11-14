import styled from 'styled-components'

export const Wrapper = styled.button`
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

export default function Pause() {
  return <Wrapper>일시정지</Wrapper>
}
