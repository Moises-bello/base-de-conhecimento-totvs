---
content_hash: bbfe5f3a94b6dcbe23cbc75b9546a0cc314af253835527f1a4112774f43a6c5d
fetched_at: '2026-06-29T00:05:55.645313+00:00'
page_id: '143655277'
product: rm
source: tdn-rm
title: TBC - Lista de DataServers disponíveis (wsDataServer).
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=143655277
version: 3
---

**Data Server (wsDataServer)**

Este serviço disponibiliza acesso direto aos objetos de negócio RM (DataServer).

WebMethods:

* AutenticaAcesso: Autentica o usuário no ambiente RM. O usuário e senha devem ser informados via SOAP, criando um Token para isto.
* AutenticaAcessoAuth: Autentica o usuário no ambiente RM.
* GestSchema ou GestSchemaAuth : Faz a leitura do DataServer (regra de negócio RM) informado.
* ReadRecord ou ReadRecordAuth : Faz a leitura do DataServer (regra de negócio RM) e retorna o registro específico (XML), conforme chave primária.
* ReadView ou ReadViewAuth : Faz a leitura do DataServer (regra de negócio RM) e retorna conjunto de registros (XML), conforme definido no filtro.
* SaveRecord ou SaveRecordAuth: Insere um registro no DataServer (regra de negócio RM). Este método somente irá incluir o registro se este for válido de acordo com as regras de negócio definidas pelo DataServer.

*Nota: Os WebMethods que possuem no final do nome a expressão “Auth”, não utilizam Token e podem ser consumidos através do Browser.*

Lista de DataServers disponíveis para os métodos acima:
