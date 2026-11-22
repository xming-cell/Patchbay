<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { requestJson } from '../api/client'

const status = ref('loading')

onMounted(async () => {
  try {
    const data = await requestJson<{ status: string }>('/api/health')
    status.value = data.status
  } catch {
    status.value = 'error'
  }
})
</script>

<template>
  <p>Health: {{ status }}</p>
</template>