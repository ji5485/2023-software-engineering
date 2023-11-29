import axios from 'axios'

export const instance = axios.create({
  baseURL: import.meta.env.VITE_SERVER_ENDPOINT,
  headers: { 'Content-Type': 'application/json' },
})
