import { ChangeEvent } from 'react'
import styled from 'styled-components'

type FormProps = {
  form: Record<string, string>
  handleChange: (event: ChangeEvent<HTMLInputElement>) => void
}

const Wrapper = styled.div`
  height: 400px;
`

export default function Form({ form, handleChange }: FormProps) {
  return <Wrapper>abc</Wrapper>
}
