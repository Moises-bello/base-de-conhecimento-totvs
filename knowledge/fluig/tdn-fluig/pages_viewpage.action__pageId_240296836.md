---
content_hash: 7825010f239634cd77cd2adb44a4db8058551a27f173c1833ea742220c5a6e81
fetched_at: '2026-06-28T21:35:22.796763+00:00'
page_id: '240296836'
product: fluig
source: tdn-fluig
title: BPM 044 - Por que certo usuário não aparece na lista de pessoas disponíveis
  para transferência de tarefa?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240296836
version: 6
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

**Versão:** todas

# Ocorrência

Ao tentar transferir uma solicitação para um usuário, o mesmo não aparece na lista de pessoas disponíveis. Apenas após colocar o usuário como Gestor do processo foi possível realizar a transferência.

# Causa

Usuário para o qual se deseja transferir a tarefa não se encaixa no mecanismo de atribuição da atividade.

# Solução

Somente será possível transferir uma solicitação para um usuário pertencente ao mecanismo de atribuição da atividade em questão. Por exemplo, o processo X está na atividade2, esta atividade está configurada para atribuição por executor de atividade1, ou seja, somente o usuário que executou a atividade1 (e o gestor) será apto a executar a atividade2.

Para que seja possível transferir a atividade2 para outro usuário, você precisará alterar o mecanismo de atribuição desta atividade, colocando atribuição por papel, por exemplo, será possível transferir a atividade para qualquer usuário cadastrado no papel. Após alterar esta atividade, você precisará liberar uma nova versão do processo e realizar a conversão da solicitação em questão através do menu Converter solicitações.

# Observações

Este comportamento não foi alterado na versão 1.5, desde as primeiras versões do fluig não é possível transferir uma atividade para um usuário que não se encaixa no mecanismo de atribuição da mesma.
