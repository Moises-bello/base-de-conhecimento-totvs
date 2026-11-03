---
content_hash: cef8b1011ef53a15d227ccc8e3b9de17509e75c558612a8e76a62ac461c19849
fetched_at: '2026-06-29T00:10:21.729359+00:00'
page_id: '492712543'
product: rm
source: tdn-rm
title: 4001299 MATESTCNTFTOF01-3615 DataServer de Defaults Contábeis do Produto no
  WebService
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=492712543
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM. |
| Segmento: | BackOffice. |
| Módulo: | TOTVS Gestão de Estoque, Compras e Faturamento. |
| Função: | Listar Visão (ReadView) e Ler Registro (ReadRecord). |
| Ticket: | 4001299. |
| Requisito/Story/Issue (informe o requisito relacionado) : | MATESTCNTFTOF01-3615. |

## **02. SITUAÇÃO/REQUISITO**

Ao consumir o DataServer de Defaults Contábeis do Produto (**EstPrdContData**) via WebService não era possível ler os registros de defaults contábeis de um determinado produto, pois a chave primária da tabela principal (**TPRODUTO**) não estava definida.

## **03. SOLUÇÃO**

Foi realizado o ajuste para definir a chave primária da tabela principal (**TPRODUTO.CODCOLIGADA** e **TPRODUTO.IDPRD**) para que seja possível realizar a pesquisa dos Defaults Contábeis do produto informando o **Código da Coligada** e o **Identificador do Produto** ao consumir o serviço.

## **04. DEMAIS INFORMAÇÕES**

**ReadView**: O método para listar a visão, ao ser consumido retornará a mensagem ***O método ou a operação não está implementada***. Este DataServer não possui a funcionalidade de listar os registros na visão, uma vez que a sua visualização é feita por produto. Por isso, deve ser utilizado o **ReadRecord**.

## **05. ASSUNTOS RELACIONADOS**

* # [Como Expor os Web Services do RM através do Host (recomendado)](http://tdn.totvs.com/pages/viewpage.action?pageId=89620766)
* # [WebService TOTVS Gestão de Estoque, Compras e Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=315905019)
