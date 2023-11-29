import styled from 'styled-components'
import Node from './Node'
import Spot from './Spot'
import { Position, SpotType } from '../utils/type'

type CoordinateProps = {
  map: { width: number; height: number }
  predefined: Position[]
  hazard: Position[]
  colorBlob: Position[]
}

export const Wrapper = styled.div`
  display: grid;
`

export default function Coordinate({
  map: { width, height },
  predefined,
  hazard,
  colorBlob,
}: CoordinateProps) {
  return (
    <Wrapper
      style={{ gridTemplate: `repeat(${height}, 1fr) / repeat(${width}, 1fr)` }}
    >
      {Array.from({ length: width * height }).map((_, index) => (
        <Node key={index}>
          <Spot type={SpotType.COLOR_BLOB} />
        </Node>
      ))}
    </Wrapper>
  )
}
