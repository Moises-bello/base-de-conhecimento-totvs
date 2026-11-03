---
content_hash: ae3894e2993aa46834803e063f57635072ed6d5139999423c9834fd4c1236595
fetched_at: '2026-07-02T19:24:19.631954+00:00'
page_id: '243634285'
product: protheus
source: tdn-tec
title: Melhoria - Reconexão SSL para HTTP e email
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243634285
version: 1
---

Essa buil contém uma melhoria para erro na conexão SSL para HTTP e email.

|  |  |
| --- | --- |
| Situação | Erro na configuração de SSL no ini do appserver impedia a conexão HTTP e de email. |
| Ocorrência | Caso a configuração de protocolos SSL realizada nas seções SSLConfigure e Mail estivessem incorretas, a conexão HTTP e de email não eram realizadas e era necessário a readequação da configuração do ini. Como a configuração do ini é global ao AppServer, não era possível ter configurações SSL diferentes para URLs diferentes, seja de HTTP ou de email. |
| Melhoria | Criado nas seções Mail e SSLconfigure a chave TryPrototcols, que permite habilitar a reconexão SSL, aletrando o protocolo utilizado, em caso de erro de conexão. Uma vez que a conexão é bem sucedida, é mantido uma lista com a URL e a configuração utilizada, fazendo com que as próximas conexões utilizem essa configuração ao invés da configuração do arquivo ini. Essa lista fica em memória e é limpa sempre que o AppServer é fechado. |
| Informações adicionais | * Não há chamado relacionado * Referente à ocorrência: TEC-7191 * Disponível em builds superiores a 7.00.131227A com data de geração superior a 30/06/2016. |
