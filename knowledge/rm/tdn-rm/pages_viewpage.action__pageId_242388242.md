---
content_hash: 39e9eb76f88ecce97d5cc9c44fac8e55ac51da051faf28868b26df668e4e4c14
fetched_at: '2026-06-29T00:08:11.261050+00:00'
page_id: '242388242'
product: rm
source: tdn-rm
title: TTMHDC_DT_Integração_Bancária_Geração_de_Código_de_Barras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=242388242
version: 112
---

# Integração Bancária - Geração de Código de Barras

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Financeira |
| **Função:** | Integração Bancária - Geração de Código de Barras |
| **Situação/Requisito:** | Habilitar a leitura de código de barras para boletos do Educacional na sessão de caixa. |
| **Solução/Implementação:** | Inclusão de novo parâmetro "Gravar histórico de boleto ao gerar código de barras/IPTE via fórmula." com o intuito de substituir o parâmetro interno que tratava deste procedimento.  Este parâmetro fará com que ao imprimir um boleto que possua a formula CodBarraBoleto(-1) e/ou IPTEBoleto(-1) possam ser consultados na tela de sessão de caixa. Esta tratativa serve para os boletos do educacional que têm seu código de barra gerados a partir da impressão do mesmo.  O Parâmetro se encontra em: 02.02.02.01 - Manutenção de baixas Baixa a receber Parâmetro "Gravar histórico de boleto ao gerar código de barras/IPTE via fórmula.". |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | FIN000024 |

divs
