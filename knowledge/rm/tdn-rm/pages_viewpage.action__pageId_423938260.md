---
content_hash: b8645de5da8b96269741da9e715a4fe5a164a33f62f63baeb297335eaa829a36
fetched_at: '2026-06-29T00:09:26.102251+00:00'
page_id: '423938260'
product: rm
source: tdn-rm
title: CNPJ/CPF Autorizados a Visualizar o XML na SEFAZ
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938260
version: 6
---

Para a criação dos campos de CNPJ/CPF autorizados a visualizar o XML do Documento Eletrônico (ex: CT-e) no site da SEFAZ, deverão ser criados os devidos campos complementares no movimento.  
Os campos deverão ser do tipo Alfanumérico e no tamanho 20.  
Poderão ser criados até 5 campos com os nomes (Não é necessário criar os 5):

|  |  |
| --- | --- |
| **Nome** | **Descrição** |
| CNPJCPF1 | CNPJ/CPF Para Acesso 1 |
| CNPJCPF2 | CNPJ/CPF Para Acesso 2 |
| CNPJCPF3 | CNPJ/CPF Para Acesso 3 |
| CNPJCPF4 | CNPJ/CPF Para Acesso 4 |
| CNPJCPF5 | CNPJ/CPF Para Acesso 5 |

Para que os Campos Complementares criados sejam visíveis no movimento, deve-se acessar os parâmetros Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento |  na etapa Mov - Campos Complementares | adicionar os campos complementares visíveis. A tag preenchida no XML com CNPJ/CPF é a AutXml.

Embasamento Legal

* [Nota Técnica 2015.002 e 2015.003](http://hom.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=tW+YMyk/50s=)
