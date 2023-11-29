import styled from 'styled-components'

type RobotProps = {
  x: number
  y: number
  direction: number
}

const Wrapper = styled.div`
  position: absolute;
  display: grid;
  place-items: center;
  width: 80px;
  height: 80px;
  transition: all 1s ease-in-out;
`

const Icon = styled.img`
  max-width: 60%;
`

export default function Robot({ x, y, direction }: RobotProps) {
  return (
    <Wrapper
      style={{
        bottom: 80 * y,
        left: 80 * x,
        transform: `rotate(${direction * 90}deg)`,
      }}
    >
      <Icon src="robot.png" />
    </Wrapper>
  )
}
