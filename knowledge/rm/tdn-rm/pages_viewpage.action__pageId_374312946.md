---
content_hash: 9fd7a923ee043e370e410f91feaab650872bd70cead559af53d0ea631a359f88
fetched_at: '2026-06-29T00:09:01.645079+00:00'
page_id: '374312946'
product: rm
source: tdn-rm
title: 2926154 MATESTCNTFTOF01-2405 DT Cancelamento de Nota Fiscal utilizada em Cópia
  por Referência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=374312946
version: 2
---

# CANCELAR MOVIMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Cancelamento de Movimento. |
| **Situação/Requisito:** | Sistema está permitindo cancelar o movimento de Nota Fiscal, mesmo que esta nota fiscal possua movimento de baixa relacionado através do processo de cópia por referência para realizar a baixa no Protheus. Neste caso, ao realizar o cancelamento o sistema perde a referência entre o movimento de Baixa de Estoque e o movimento de Ordem de Serviço (OS). |
| **Solução/Implementação:** | Ao executar as ações de Cancelar e/ou Excluir Movimento de nota fiscal, caso exista movimento de baixa de estoque gerado através de Cópia por Referência selecionando esta nota fiscal, o sistema não permitirá o cancelamento/exclusão do movimento e apresentará mensagem de consistência ao usuário. |
| **Tickets relacionados:** | 2926154. |
| **Requisito:** | Cancelar Movimento. |
| **Documento de Referência:** | <http://wikihelp.totvs.com.br/WikiHelp/EST/EST.CancelamentoMovimento.aspx>. |
| **Pacote:** | Informe o [linkdopacote] |
