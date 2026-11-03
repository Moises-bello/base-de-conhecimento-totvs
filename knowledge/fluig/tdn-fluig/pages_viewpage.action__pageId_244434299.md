---
content_hash: 32ec8dffe1d7fe480a882b3b250d15455c1c023fc60920eb6cdd919b11f7af31
fetched_at: '2026-06-28T21:35:23.218195+00:00'
page_id: '244434299'
product: fluig
source: tdn-fluig
title: BPM 058 - Por que a solicitação fica presa/parada em uma atividade automática?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244434299
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

# Ocorrência

Usuário tem uma solicitação que ficou parada em uma atividade automática e não consegue movimentar.

# Causa

Se esta atividade for seguida de outra atividade automática, na sequência houver uma atividade atribuída Por Campo de Formulário configurada para "Sempre" selecionar destinatários e a movimentação não foi feita pela interface do fluig, a solicitação pode ficar parada na atividade automática.

**Exemplo: Atividade Automática 1 → Automática 2 → Atividade por campo de formulário.**

**Atribuição "por Campo de Formulário" e Seleciona Colaboradores "Sempre".**

# Solução

1. Configurar um gestor para o processo.
2. Na Central de tarefas do usuário que foi selecionado como gestor, acessar a aba **Minhas tarefas sob gerência** e localizar a solicitação.
3. Abrir a solicitação e clicar no botão **Enviar**.
4. Selecionar a atividade de destino e enviá-la para a próxima atividade.

# Observações

Para futuros casos, [consulte esta FAQ](http://tdn.totvs.com/x/XeyFDg)[.](http://tdn.totvs.com/x/XeyFDg)
