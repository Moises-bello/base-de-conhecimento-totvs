---
article_id: 18492977100183
category: Escrita Fiscal - Impostos - ISS
content_hash: 33a8ea1eb1f7dff758058cebe395895fa9dd17ea8c6ce7b841c0e41467f25711
fetched_at: '2026-06-28T22:39:35.247097+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Relacionamento de
  Código de Serviço (MATA963)
type: support-article
updated_at: '2024-10-08T21:16:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18492977100183-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Relacionamento-de-C%C3%B3digo-de-Servi%C3%A7o-MATA963
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18492992808087) Tempo aproximado para leitura: **00:05:00 min****DESCRIÇÃO**

Disponibilizado a rotina Relacionamento de Códigos de Serviço (MATA963) para que seja realizada a amarração dos códigos de serviço, códigos da Lei Complementar 116/03 e tabela 6 do EFD Reinf.

**PROCESSO PARA UTILIZAR**

No módulo Livros Fiscais (SIGAFIS), acesse Atualizações / Cadastros / Relac. Cód. Serviço (MATA963):

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| Descrição (CDN\_DESCR) | Descrição do serviço |
| Cód. Produto (CDN\_PROD) | Código do item/serviço |
| Filial (CDN\_FILIAL) | Filial do sistema |
| Cod. ISS(CDN\_CODISS) | Código de serviço |
| Cod. LST (CDN\_CODLST) | Código de serviço, conforme Lei Complementar 116/03 |
| Tipo de Serviço (CDN\_TPSERV) | Tipo de serviço, conforme a tabela 6 do EFD Reinf |

No campo Tipo de Serviço (CDN\_TPSERV) serão apresentados os dois dígitos finais do código de tipo de serviço da tabela 6 do EFD Reinf, ao realizar a extração dos dados para o TAF o código será gerado e enviado no arquivo do Extrator completo, de forma automática. Não é permitido incluir novos códigos pois irá ocasionar a Rejeição MS2002 no momento da transmissão do REINF.

[CROSS Segmentos - Backoffice Protheus - TAF - REINF - Rejeição MS2002](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22926177241239-CROSS-Segmentos-Backoffice-Protheus-TAF-REINF-Rejei%C3%A7%C3%A3o-MS2002?source=search)

O conteúdo do campo Cod. LST(CDN\_CODLST) deve estar preenchido conforme Código de Serviço Prestado:

[Tabela de Códigos](http://sped.rfb.gov.br/pagina/show/1601)

Por exemplo:

Código no campo Tipo de Serviço (CDN\_TPSERV) = 01

Código na tabela 6 do EFD Reinf = 100000001

No Extrator Fiscal (campo 29 do registro T007 e campo 43 do registro T015) = 100000001

**IMPORTANTE**

É necessário o preenchimento de todos os campos no cadastro do Relacionamento de Códigos de Serviço (MATA963).

Exemplo:

![](https://totvssuporte.zendesk.com/attachments/token/O9311yqWfclkZ1oHUqO4GLqWL/?name=inlineImage.png)

Deve constar na tabela SFT o campo FT\_TIPO = S e FT\_CODISS = o código informado no cadastro do MATA963 do campo Cod. ISS(CDN\_CODISS).

Para ser preenchido os campos FT\_TIPO e FT\_CODISS é necessário que a TES esteja com o campo L. Fiscal ISS (F4\_LFISS) = Tributado/Outros/Isento e o cadastro do Produto, campo Cód. Serv. ISS (B1\_CODISS) preenchido.

Os campos FT\_TIPO e FT\_CODISS não podem ser alterados via Acertos Fiscais (MATA900), pois irá gerar erro no REINF e não irá reconhecer o Tipo de Serviço.

https://tdn.totvs.com/pages/releaseview.action?pageId=346488949
