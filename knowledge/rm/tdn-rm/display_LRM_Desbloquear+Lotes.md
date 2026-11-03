---
content_hash: 006748f94ae1027e2a9f08f82418f4e61295b371335245568d01bc129de49a86
fetched_at: '2026-06-29T00:09:28.577680+00:00'
page_id: '423938715'
product: rm
source: tdn-rm
title: Desbloquear Lotes
type: documentation
url: https://tdn.totvs.com/display/LRM/Desbloquear+Lotes
version: 2
---

***Atenção!***

Esta funcionalidade só está disponível para as bases já migradas para o Novo Modelo do BackOffice.

Bloquear um lote significa colocá-lo sob o domínio de um determinado usuário, tornando-o indisponível aos outros usuários. O bloqueio do lote, normalmente, será executado pelo processo Bloquear Lotes.

Quando um processo, seja de Integração de Lotes ou de Agrupamento de Lançamentos, estiver sendo executado para determinado lote, internamente o sistema também bloqueia este lote para o usuário que o estiver executando. Se por algum motivo o processo que estiver sendo executado não chegar ao final ou for interrompido, o lote permanecerá bloqueado com o usuário que o estava executando, impossibilitando a manutenção no mesmo por outros usuários.

O processo **Desbloquear Lotes** tem por objetivo, então, desbloquear os lotes que estejam bloqueados com usuários, seja porque o usuário que o bloqueou já finalizou o uso desejado, seja porque o lote permaneceu bloqueado indevidamente, tornando-o a partir deste processo, disponível novamente para o uso de outros usuários.

O desbloqueio só pode ser executado pelo próprio usuário com o qual o lote está bloqueado ou por um usuário que tenha perfil de Supervisor. Para isto, pode-se primeiro selecionar o(s) lote(s) desejado(s) e em seguida acionar o processo Desbloquear Lotes. O(s) lote(s) selecionado(s) já estará relacionado no processo sendo possível neste momento adicionar novos lotes ou excluir lotes relacionados. No final deste processo o(s) lote(s) ficará desbloqueado.
