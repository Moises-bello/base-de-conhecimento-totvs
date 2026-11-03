---
content_hash: cf9d9740d9d1df11f2387e9cefe91bee8e9620550cba070456c78ad87f6acaff
fetched_at: '2026-06-29T00:05:51.685126+00:00'
page_id: '105316820'
product: rm
source: tdn-rm
title: TBC - Sincronização de Registros via atividade de Fórmula Visual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=105316820
version: 1
---

Visando facilitar a sincronização de dados em massa entre o RM e sistemas integrados via Mensagem Única TOTVS, foi desenvolvida uma atividade de fórmula visual que se responsabiliza por, a partir de alguns parâmetros, obter os dados necessários e solicitar o envio da Mensagem Única TOTVS para o sistema de destino.

Basicamente é necessário informar a esta atividade somente a lista de chaves dos registros que se deseja integrar, qual a Mensagem Única a enviar e qual o objeto de negócio (DataServer) responsável por retornar as informações do registro. A partir destas informações a atividade se responsabiliza pela leitura, transformação e envio dos dados ao sistema de destino, oferecendo como retorno o Log de integração.

Todas as mensagens trafegadas também constarão no monitor da fila de integração, para posterior conferência.

Acesse os boletins técnicos abaixo:
