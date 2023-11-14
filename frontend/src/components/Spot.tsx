import styled from 'styled-components'
import { SpotType } from '../utils/type'

type SpotProps = {
  type: SpotType
}

const Wrapper = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
`

const Target = styled.img`
  max-width: 60%;
`

export default function Spot({ type }: SpotProps) {
  return (
    <Wrapper>
      <Target src={`${type}.png`} alt={type} />
    </Wrapper>
  )
}
