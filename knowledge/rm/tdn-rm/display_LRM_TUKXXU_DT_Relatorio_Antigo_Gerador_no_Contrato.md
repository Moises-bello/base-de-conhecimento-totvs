---
content_hash: 820c6f27b674849468cf5056e014d744af97d0d3003ad660ef3fa86d18849ea5
fetched_at: '2026-06-29T00:08:04.822875+00:00'
page_id: '235582829'
product: rm
source: tdn-rm
title: TUKXXU_DT_Relatorio_Antigo_Gerador_no_Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/TUKXXU_DT_Relatorio_Antigo_Gerador_no_Contrato
version: 116
---

# IMPRIMIR BOLETO NO CONTRATO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | Imprimir boleto no menu contrato |
| **Situação/Requisito:** | *Ao imprimir boleto através do menu Contrato, o sistema não obedece o filtro do relatório criado no gerador antigo, por exemplo somente lançamentos em aberto.* |
| **Solução/Implementação:** | Alterado o processo "Imprimir Boleto" do menu Contratos, caso selecione um relatório criado no antigo gerador de relatório (Delphi), o sistema passará a obedecer o filtro original do relatório quando estiver marcado o parâmetro Educacional/Tesouraria/Relatório/ "Utiliza filtro do relatório antigo (delphi) na impressão do boleto".     Nas versões anteriores, o relatório somente filtrava os boletos do aluno selecionado, ignorando os demais filtros originais do relatório. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
