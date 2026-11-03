---
content_hash: 19a9b3d5ca267f985ecd560fd29458488265b96ebf1511375449bdf3fbfabbda
fetched_at: '2026-07-02T19:24:25.150651+00:00'
page_id: '499105680'
product: protheus
source: tdn-tec
title: Falha do componente WsdlManager no uso do método SendSoapMsg tendo como parâmetro
  o XML-SOAP a ser enviado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=499105680
version: 2
---

|  |  |
| --- | --- |
| Ocorrência | Incompatibilidade entre mensagem XML-SOAP montada e submetida por requisição POST e a composição de alguns campos do header da requisição (elementos usados pertinentes à versão 1.1 do SOAP que não era o default - 1.2). |
| Correção | Acréscimo da propriedade nSOAPVersion à classe WsdlManager para forçar o uso interno do protocolo SOAP efetivamente usado. |
| Informações adicionais | * Referente ao chamado: TTEC-3182 * Disponível em builds iguais ou superiores a [13.1.3.44](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.1.3.44) e [13.2.3.44](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.2.3.44). |
