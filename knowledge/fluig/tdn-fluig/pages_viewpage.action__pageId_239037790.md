---
content_hash: c25fa13179f43ffb5daaf719c3071181c3a74ce9c857e130ef3b9dc51fead393
fetched_at: '2026-06-28T21:35:22.756911+00:00'
page_id: '239037790'
product: fluig
source: tdn-fluig
title: BPM 041 - Por que as notificações de tarefas atrasadas estão sendo enviadas
  fora do horário de expediente?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=239037790
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

**Versão:**Todas as versões

# Ocorrência

Notificações de tarefas atrasadas estão sendo enviadas fora do horário de expediente.

# Solução

O envio dessas notificações, de tarefas atrasadas por exemplo, depende do Agendador de Tarefas. Por gentileza verifique em Painel de Controle → Agendador de Tarefas.

Caso haja agendamento de Tarefas Atrasadas todos os dias, será disparada a notificação, independente de ser fim de semana ou feriado.

Não é possível alterar tarefas previamente cadastradas no Agendador, portanto caso queira alterar o horário de envio das notificações, remova a tarefa e cadastre-a novamente.

# Observações

Através de desenvolvimento sobre a plataforma é possível utilizar o evento beforeSendNotification, que possibilita o cancelamento de notificações. Para mais detalhes acesse .
