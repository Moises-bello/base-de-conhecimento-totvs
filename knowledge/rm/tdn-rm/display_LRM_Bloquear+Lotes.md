---
content_hash: 092a3b5e8e4e57b5fefe436e8acbc22d34fd123dbd2294aae4d0fee019d1f9b9
fetched_at: '2026-06-29T00:09:28.024774+00:00'
page_id: '423938628'
product: rm
source: tdn-rm
title: Bloquear Lotes
type: documentation
url: https://tdn.totvs.com/display/LRM/Bloquear+Lotes
version: 4
---

***Atenção!***

Esta funcionalidade só está disponível para as bases já migradas para o Novo Modelo do BackOffice.

Bloquear um lote significa colocá-lo sob o domínio de um determinado usuário, tornando-o indisponível aos outros usuários, impossibilitando assim a manutenção em seus lançamentos por outro usuário que não seja o seu dono. Dizemos que o lote, a partir da execução deste processo, ficou bloqueado com o usuário que o executou.

Qualquer usuário, desde que tenha permissão em seu perfil para esta ação, pode bloquear um lote para seu uso.

Quando um lote estiver bloqueado com um determinado usuário, na janela principal onde se tem uma visão geral dos lotes cadastrados, o nome do usuário ficará relacionado ao lote em questão.

Através deste processo será possível Bloquear Lotes. Para isto, pode-se primeiro selecionar o(s) lote(s) desejado(s) e em seguida acionar o processo Bloquear Lotes. O(s) lote(s) selecionado(s) já estará relacionado no processo sendo possível neste momento adicionar novos lotes ou excluir lotes relacionados. Em seguida deve-se obrigatoriamente informar um Motivo para realização deste processo. Se entre os lotes selecionados existir algum já bloqueado, ele não será bloqueado novamente, ou seja, o processo não irá transferir o domínio (bloqueio) do lote para o usuário em questão sendo o processo realizado, então, somente para os lotes que estiverem desbloqueados, tornando-os a partir deste momento bloqueados com o usuário que executou o processo.

**Dicas**

Este processo pode ser bastante utilizado com o intuito de além de não permitir que nenhuma manutenção por outro usuário seja feita em lançamentos cujo lote esteja bloqueado, nenhum processo também possa ser executado para o lote enquanto o mesmo permanecer bloqueado, evitando, por exemplo, que se integre indevidamente um lote sem que antes os seus lançamentos tenham sido conferidos pelo usuário responsável. Enquanto um lote estiver bloqueado, nenhum processo poderá ser executado para este lote, nem mesmo pelo próprio usuário que o bloqueou.

**Observação**

Quando algum processo, seja de Integração de Lotes ou de Agrupamento de Lançamentos, estiver sendo executado para determinado lote, internamente o sistema também bloqueia este lote para o usuário que o estiver executando. Se por algum motivo o processo que estiver sendo executado não chegar ao final ou for interrompido, o lote permanecerá bloqueado com o usuário que o estava executando, impossibilitando a manutenção no mesmo por outros usuários.
