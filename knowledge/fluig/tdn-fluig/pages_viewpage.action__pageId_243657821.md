---
content_hash: 775ae74eb71a96a06c67c15388ffd415dad68bcba79bec7ed4c7eda51bd1d607
fetched_at: '2026-06-28T21:35:23.077422+00:00'
page_id: '243657821'
product: fluig
source: tdn-fluig
title: BPM 052 - Como movimentar uma atividade com mecanismo de atribuição através
  de atividades automáticas sem interação com usuário?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243657821
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

# Ocorrência

Usuário deseja movimentar uma atividade automaticamente, por meio de eventos de processo ou *Web Service*, através de uma atividade automática para uma outra atividade comum, porém a movimentação não é concluída.

# Causa

Isso ocorre pois a atividade destino está configurada para "Sempre" selecionar destinatários, portanto mesmo havendo só uma opção, ela deve ser selecionada posteriormente e, como não há essa opção em uma movimentação sem ser pela interface do fluig, a solicitação é retornada à atividade anterior.

# Solução

Configurar a atividade destino para "Quando houver mais de uma opção", assim quando houver apenas uma opção o colaborador será atribuído automaticamente.
