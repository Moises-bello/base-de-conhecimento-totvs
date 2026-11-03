---
content_hash: 65e884372ff03bb8b31b6e9962593a132144b67c05b9648923d5372b6c30bf48
fetched_at: '2026-06-29T00:08:19.441617+00:00'
page_id: '267786467'
product: rm
source: tdn-rm
title: TVLYCY_DT_Retorno_Debito_Automatico
type: documentation
url: https://tdn.totvs.com/display/LRM/TVLYCY_DT_Retorno_Debito_Automatico
version: 111
---

# Retorno de Débito Automático

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Financeira* |
| **Função:** | *Retorno de Débito Automático* |
| **Situação/Requisito:** | *Ao efetuar um retorno com valor a menor, era apresentada mensagem de erro ""Não foi possível baixar o boleto Ref. XXXX referente à linha 2 do arquivo C:\XXXX.txt. Provavelmente, o sistema está parametrizado para Não baixar com diferença a menor. Valor da diferença: ###,## Valor Pago: ###,## Débito Efetuado* |
| **Solução/Implementação:** | *Quando um retorno de débito automático for com um valor a menor ou maior, que a diferença seja jogada no campo desconto e juros respectivamente, conforme ocorre nas versões anteriores a 11.80* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | FIN000184 |

divs
