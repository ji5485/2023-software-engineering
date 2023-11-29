import { ReactNode, useCallback, useState } from 'react'
import styled from 'styled-components'
import { format } from 'date-fns'
import useLog, { LogContext } from '../hooks/useLog'

type ContextProps = {
  children: ReactNode
}

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
  const { logs } = useLog()

  return (
    <Wrapper>
      {logs.map(({ date, log }, index) => (
        <Item key={index}>
          <Time>{date}</Time>
          <Description>{log}</Description>
        </Item>
      ))}
    </Wrapper>
  )
}

Log.Context = function Context({ children }: ContextProps) {
  const [logs, setLogs] = useState<Array<{ date: string; log: string }>>([])

  const addLog = useCallback((log: string) => {
    const date = format(new Date(), 'HH:mm:ss')
    setLogs(prev => [...prev, { date, log }])
  }, [])

  return (
    <LogContext.Provider value={{ logs, addLog }}>
      {children}
    </LogContext.Provider>
  )
}
