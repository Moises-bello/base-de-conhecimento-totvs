---
content_hash: 2d619f544002fbc8a10461fa101ab373142766357e94c5710f6189a0b8a60c4c
fetched_at: '2026-06-29T00:09:03.412278+00:00'
page_id: '381040138'
product: rm
source: tdn-rm
title: '2291028 CONTROLADORIA01-1745 DataServer de Defaults de Cliente/Fornecedor:
  FinCFODEFData'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=381040138
version: 3
---

# DataServer de Defaults de Cliente/Fornecedor: FinCFODEFData

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | DataServer de Defaults de Cliente/Fornecedor |
| **Situação/Requisito:** | Ao tentar realizar a inserção de um default do cliente/fornecedor através de conceito o sistema retorna mensagem:  O metodo DoReadView da classe FinCFODEFData não está disponivel. Entre em contato com o responsável. |
| **Solução/Implementação:** | Implementação do método DoReadView no DataServer FinCFODEFData para que o mesmo possa ser utilizado em importações via conceito. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 2291028 |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A. |
