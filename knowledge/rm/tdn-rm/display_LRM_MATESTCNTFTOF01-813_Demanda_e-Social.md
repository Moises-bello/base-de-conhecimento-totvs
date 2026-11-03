---
content_hash: d610abadf8805639adf99c95aa49f5d3fe82e4dca825715e83d4310562776656
fetched_at: '2026-06-29T00:08:46.141524+00:00'
page_id: '315903214'
product: rm
source: tdn-rm
title: MATESTCNTFTOF01-813_Demanda_e-Social
type: documentation
url: https://tdn.totvs.com/display/LRM/MATESTCNTFTOF01-813_Demanda_e-Social
version: 94
---

# Informação para o e-Social registro S-1250

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Função:** | Não se aplica. |
| **Situação/Requisito:** | Registro S-1250 do e-Social |
| **Solução/Implementação:** | Serviço de geração informação para uso do TOTVS Gestão de Recursos Humanos, que retornará dados necessários para a geração da rotina eSocial, mais especificamente o registro S-1250.     * Em **Tributos e Valores | Tributos**, na grid de edição de tributos foi incluída uma nova coluna chamada **Valor Ret. Suspensa Judicialmente**. Essa coluna conterá o valor que não foi retido do imposto devido decisão/ordem proferida em processo judicial e será preenchida manualmente pelo usuário para cada tributo em que couber tal informação. * Essa coluna vai estar sempre visível, mas somente poderá ser editada quando o tributo correspondente for do tipo (DTRIBUTO.TIPOTRIBFISC) "INSS" ou "FUNRural". |
| **Conversores e Parâmetros:** | É necessário executar o atualizar de base para ativação dos recursos;  Versões 12.1.17 e 12.1.18 é necessário entrar em contato com suporte TOTVS para liberação do script. |
| **Tickets relacionados:** | Não se aplica. |
| **Requisito:** | MATESTCNTFTOF01-813 |

divs
