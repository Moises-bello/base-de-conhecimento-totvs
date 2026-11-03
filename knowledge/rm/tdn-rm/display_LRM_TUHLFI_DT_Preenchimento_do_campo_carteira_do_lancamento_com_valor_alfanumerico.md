---
content_hash: 742dd205d5d7198f4bdcd2573459ab9e1bd11d16a4a840b65045d5e43105e350
fetched_at: '2026-06-29T00:06:27.953450+00:00'
page_id: '233740782'
product: rm
source: tdn-rm
title: TUHLFI_DT_Preenchimento_do_campo_carteira_do_lancamento_com_valor_alfanumerico
type: documentation
url: https://tdn.totvs.com/display/LRM/TUHLFI_DT_Preenchimento_do_campo_carteira_do_lancamento_com_valor_alfanumerico
version: 117
---

# PREENCHIMENTO DO CAMPO CARTEIRA DO LANÇAMENTO COM VALOR ALFANUMÉRICO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | **Geração de Lançamentos** |
| **Situação/Requisito:** | *Geração de lançamentos era abortada quando tínhamos o campo CARTEIRA do convênio preenchido com um valor alfanumérico.* |
| **Solução/Implementação:** | *Sistema passou a verificar o preenchimento do campo CARTEIRA do convênio default da conta caixa. Se o valor preenchido for numérico, o campo FLAN.CARTEIRA será preenchido, caso contrário, essa informação não será preenchida no lançamento financeiro.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | TUKCRU |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.9 / 12.1.10 / 12.1.11* |
| **Versão Corrigida:** | **12.1.9 / 12.1.10 / 12.1.11** |
| **Versão Expedida:** | *12.1.9* |

divs
