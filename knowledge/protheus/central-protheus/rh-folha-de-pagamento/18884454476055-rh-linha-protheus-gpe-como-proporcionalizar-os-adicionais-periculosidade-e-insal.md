---
article_id: 18884454476055
category: RH - Folha de Pagamento
content_hash: 87c8e38864646233fc09ee94423615adb41f8105fdeb9b1caeb4fe8910de39a1
fetched_at: '2026-06-28T22:44:14.705702+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como proporcionalizar os adicionais Periculosidade
  e Insalubridade na Base do FGTS para funcionários afastados por acidente de Trabalho
type: support-article
updated_at: '2025-09-15T19:14:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18884454476055-RH-Linha-Protheus-GPE-Como-proporcionalizar-os-adicionais-Periculosidade-e-Insalubridade-na-Base-do-FGTS-para-funcion%C3%A1rios-afastados-por-acidente-de-Trabalho
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18884462809495) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como proporcionalizar os adicionais Periculosidade e Insalubridade na Base do FGTS para funcionários afastados por acidente de Trabalho?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Devido a vários entendimentos distintos, sobre a necessidade da periculosidade e insalubridade serem proporcionalizados ou não na montagem da base do FGTS, criamos um mnemônico para que o usuário possa definir como será realizado o cálculo.

O mnemônico **P\_ADCFGTS** é numérico e tem conteúdo padrão "0", que consiste em somar a periculosidade e a insalubridade integralmente na base do FGTS, e não apenas os valores referentes aos dias trabalhados.

As seguintes situações são possíveis a partir da configuração do mnemônico:

| Conteúdo | Resultado |
| --- | --- |
| 0 | Base do FGTS será composta pelo valor integral da insalubridade e periculosidade. Comportamento padrão. |
| 1 | Base do FGTS será composta pelo valor integral da insalubridade e pelo valor pago (proporcional) de periculosidade. |
| 2 | Base do FGTS será composta pelo valor integral da periculosidade e pelo valor pago (proporcional) de insalubridade. |
| 3 | Base do FGTS será composta pelo valor pago (proporcional) da insalubridade e e da periculosidade. |

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34956613683863)

Exemplo:

Funcionário com salário de 3000,00, com 30% de periculosidade e 10% de insalubridade, afastado do dia 01/04 até o dia 15/04:

| Mnemônico | Periculosidade Total | Periculosidade Proporcional | Insalubridade Total | Insalubridade Proporcional | Base FGTS |
| --- | --- | --- | --- | --- | --- |
| 0 | 900,00 | 450,00 | 300,00 | 150,00 | 3000,00 + 900,00 + 300,00 = 4200,00 |
| 1 | 900,00 | 450,00 | 300,00 | 150,00 | 3000,00 + **450,00** + 300,00 = 3750,00 |
| 2 | 900,00 | 450,00 | 300,00 | 150,00 | 3000,00 + 900,00 + **150,00** = 4050,00 |
| 3 | 900,00 | 450,00 | 300,00 | 150,00 | 3000,00 + **450,00** + **150,00** = 3600,00 |

**Saiba Mais:**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[Documentação Técnica](https://tdn.totvs.com/pages/viewpage.action?pageId=617180686)
