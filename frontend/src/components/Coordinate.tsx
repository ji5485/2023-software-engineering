import styled from 'styled-components'
import Node from './Node'
import Spot from './Spot'
import { SpotType } from '../utils/type'

type CoordinateProps = { width: number; height: number }

export const Wrapper = styled.div`
  display: grid;
`

export default function Coordinate({ width, height }: CoordinateProps) {
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
