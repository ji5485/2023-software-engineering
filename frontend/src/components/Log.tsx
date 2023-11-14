import styled from 'styled-components'

export const Wrapper = styled.div`
  display: flex;
  flex-direction: column;
  gap: 5px;
  padding: 15px;
  border-radius: 7px;
  background: #f3f0ff;
`

export const Item = styled.div`
  display: flex;
  gap: 10px;
`

export const Time = styled.div`
  padding-right: 10px;
  border-right: 1px solid #5f3dc4;
`

export const Description = styled.div`
  font-weight: 300;
`

export default function Log() {
  return (
    <Wrapper>
      <Item>
        <Time>15:30:14</Time>
        <Description>앞으로 1칸 이동</Description>
      </Item>
      <Item>
        <Time>15:30:16</Time>
        <Description>시계 방향 90도 회전</Description>
      </Item>
    </Wrapper>
  )
}
