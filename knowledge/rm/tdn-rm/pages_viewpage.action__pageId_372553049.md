---
content_hash: 16c98e4e7b7df584148f26ce8cde7dd64f46ff7e392b06fb2bfe06442d60b21b
fetched_at: '2026-06-29T00:09:01.186235+00:00'
page_id: '372553049'
product: rm
source: tdn-rm
title: 2883932 MATESTCNTFTOF01-2301 DT Produto Número do Fabricante
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=372553049
version: 1
---

# CADASTRO DE PRODUTO/SERVIÇOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Cadastro de Produto. |
| **Situação/Requisito:** | Ao editar um produto e apagar a informação contida no **Número do Produto no Fabricante** ao salvar o sistema copia o código do produto e insere no número do produto no fabricante. |
| **Solução/Implementação:** | Removido do serviço de inclusão/alteração de Produto o preenchimento do campo **Número do Fabricante no Produto**.  Ao realizar a inclusão via tela do sistema, quando o **Código do Produto** estiver preenchido o **Número do Produto no Fabricante** receberá o mesmo valor do campo Código do Produto, permitindo que o usuário altere a informação do Número do Produto no Fabricante antes de salvar o registro.  Caso seja realizada a inclusão e/ou alteração de Produto via webService, para preencher o valor do campo Número do Produto no Fabricante informe no xml a tag <NUMNOFABRIC>NUMERO</NUMNOFABRIC> |
| **Conversores e Parâmetros:** | Não se aplica. |
| **Tickets relacionados:** | 1829770; 2573732. |
| **Requisito:** | Cadastro de Produtos/Serviços (EstPrdAction). |
| **Documento de Referência:** | <http://wikihelp.totvs.com.br/WikiHelp/EST/EST.Produto.aspx>. |
| **Pacote:** | Informe o [linkdopacote] |
