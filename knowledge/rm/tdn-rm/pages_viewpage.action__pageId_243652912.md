---
content_hash: 0c690c6de58758e2413dfd98f2df219e5f559cac16b7ac9e3c2a67879a9a3b13
fetched_at: '2026-06-29T00:08:12.873231+00:00'
page_id: '243652912'
product: rm
source: tdn-rm
title: TUZHSM_DT_Integração_Bancária_Retorno_de_Cobrança
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243652912
version: 117
---

Integração Bancária - Retorno de Cobrança

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Financeira |
| **Função:** | Integração Bancária - Retorno de Cobrança |
| **Situação/Requisito:** | Ao importar arquivo de retorno o sistema exibe o seguinte erro:  "Linha 00003 Erro Boleto Ref.:80855 - Não foi possível baixar o boleto Ref. 80855 referente à linha 3 do arquivo C:\Chamados\retorno petrine teste 02062016.txt. Provavelmente, o sistema está parametrizado para Não baixar com diferença a menor. Valor da diferença: 2,56Valor Pago: 2.589,16"  O erro se dá pelo não preenchimento do campo DATAPAGTOBANCO antes dos cálculos dos valores. Deste modo, a fórmula de Juros não é validada conforme esta data e o sistema calcula Juros indevido para o lançamento. |
| **Solução/Implementação:** | Otimização no processo de importação de retorno de cobrança. Agora o sistema respeita a utilização do campo DATAPAGTOBANCO, campo data complementar, nas formulas durante o cálculo do valor líquido. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | FIN000169 |

divs
