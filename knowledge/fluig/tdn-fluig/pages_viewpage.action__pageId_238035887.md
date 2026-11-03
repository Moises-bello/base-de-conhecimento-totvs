---
content_hash: a333bd659febf00a1e0abd8b6f6c7c512d92537f30b8f14783dcfbc7fe07600c
fetched_at: '2026-06-28T21:35:22.642492+00:00'
page_id: '238035887'
product: fluig
source: tdn-fluig
title: BPM 035 - É permitido retorno após converter a solicitação?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=238035887
version: 8
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** fluig

**Versão:**Todas as versões

# Ocorrência

Desenvolvemos um processo cujo os fluxos foram configurados para permitir retorno. Devido a uma necessidade interna da empresa, fizemos uma mudança e tivemos que converter algumas solicitações já existentes, logo depois da conversão a tarefa que podia retornar a anterior começou a não dar mais esta possibilidade.

Criei um fluxo em desenvolvimento para testar e ver se era por causa da conversão e pude identificar que sim. Gostaria de saber qual procedimento devo tomar? Pois estamos com 4 tarefas paradas com o presidente da empresa e o mesmo não consegue voltar a tarefa para onde deve.

# Solução

O fluxo de retorno apenas é possível para a versão do processo corrente durante a movimentação. Por isso, caso uma solicitação seja convertida para uma outra versão, **durante a primeira movimentação da solicitação** **após a conversão, essa solicitação não pode retornar a atividade anterior**, pois neste caso a solicitação terá uma nova movimentação representando sua conversão e portanto perderá a possibilidade de retorno imediato.

Para mais informações, consulte nossa documentação sobre [Fluxos.](http://tdn.totvs.com/x/DRgwDg)
