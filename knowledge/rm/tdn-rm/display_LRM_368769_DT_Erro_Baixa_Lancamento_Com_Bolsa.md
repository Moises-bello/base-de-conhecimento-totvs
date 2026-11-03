---
content_hash: e0c15de33dbfd6fe058f4f1071b7fe23ce6f2b08e9c60fba38bf8060d71aa402
fetched_at: '2026-06-29T00:08:26.346604+00:00'
page_id: '271175806'
product: rm
source: tdn-rm
title: 368769_DT_Erro_Baixa_Lancamento_Com_Bolsa
type: documentation
url: https://tdn.totvs.com/display/LRM/368769_DT_Erro_Baixa_Lancamento_Com_Bolsa
version: 111
---

# BAIXA DE LANÇMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Baixa de lançamentos financeiros* |
| **Situação/Requisito:** | *Ao baixar um lançamento financeiro, oriundo do educacional, que tenha bolsa condicional definida para o campo opcional de desconto (não usa escalonamento de bolsas) e que tenha um desconto qualquer atribuído para o campo valor opcional VALOROP1, o sistema entende que o valor do campo VALOROP1 é o valor da bolsa e invalida a baixa devido o valor atual não ser o mesmo do valor gerado para a bolsa.* |
| **Solução/Implementação:** | *Foi realizada otimização do processo de baixa de lançamentos financeiros de forma que o sistema consiga baixar um lançamento que tenha bolsa condicional quando o sistema estiver parametrizado para não utilizar escalonamento de bolsas e tenha um desconto concedido no momento da baixa.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.16* |
| **Versão Corrigida:** | *12.1.16* |
| **Versão Expedida:** | *12.1.16* |

divs
