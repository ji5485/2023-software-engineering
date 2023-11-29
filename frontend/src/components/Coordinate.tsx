import { ReactNode, useMemo } from 'react'
import styled from 'styled-components'
import Node from './Node'
import Spot from './Spot'
import { Position, SpotType } from '../utils/type'

type CoordinateProps = {
  map: { width: number; height: number }
  predefined: Position[]
  hazard: Position[]
  colorBlob: Position[]
  children: ReactNode
}

export const Wrapper = styled.div`
  position: relative;
  display: grid;
`

export default function Coordinate({
  map: { width, height },
  predefined,
  hazard,
  colorBlob,
  children,
}: CoordinateProps) {
  const spots = useMemo(
    () => [
      ...predefined.map(position => ({
        ...position,
        type: SpotType.PREDEFINED,
      })),
      ...hazard.map(position => ({ ...position, type: SpotType.HAZARD })),
      ...colorBlob.map(position => ({
        ...position,
        type: SpotType.COLOR_BLOB,
      })),
    ],
    [predefined, hazard, colorBlob],
  )

  return (
    <Wrapper
      style={{ gridTemplate: `repeat(${height}, 1fr) / repeat(${width}, 1fr)` }}
    >
      {Array.from({ length: width * height }).map((_, index) => {
        const coordX = index % width
        const coordY = height - Math.floor(index / width) - 1
        const spot = spots.find(({ x, y }) => x === coordX && y === coordY)

        return (
          <Node key={index}>
            <Spot type={spot?.type} />
          </Node>
        )
      })}

      {children}
    </Wrapper>
  )
}
