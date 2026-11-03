---
content_hash: 902c2cbcca7b2899023737220225ba5d2f034ef6c9ebe91ccac8b5996ac59939
fetched_at: '2026-06-29T00:08:03.977696+00:00'
page_id: '235332301'
product: rm
source: tdn-rm
title: TUPMH6_DT_Baixa_IRRF_PF
type: documentation
url: https://tdn.totvs.com/display/LRM/TUPMH6_DT_Baixa_IRRF_PF
version: 116
---

# Baixa - IRRF-PF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Gestão Financeira. |
| **Função:** | Baixa - IRRF-PF |
| **Situação/Requisito:** | Ao baixar mais de um lançamento Geradores de INSS e IRPF no mesmo mês, onde o valor dos lançamentos ultrapassem o teto de desconto de INSS, o valor de desconto de INSS no IRPF está ultrapassando o valor do teto de INSS permitido. |
| **Solução/Implementação:** | Ajustes do serviço de geração do IRPF para que não utilize valor maior que o teto INSS ao calcular o valor desse desconto durante o cálculo do IRPF. |
| **Conversores e Parâmetros:** | NA. |
| **Chamados relacionados:** | NA |
| **Requisito (ISSUE):** | FINTRF000174. |

divs
