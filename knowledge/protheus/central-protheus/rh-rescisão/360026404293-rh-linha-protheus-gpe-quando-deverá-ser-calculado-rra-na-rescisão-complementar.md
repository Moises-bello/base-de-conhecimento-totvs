---
article_id: 360026404293
category: RH - Rescisão
content_hash: 5821da7844dba8350dfd5048ec4dfb484b0d486ce4e7ad81bc5a86d2cd130001
fetched_at: '2026-06-28T22:43:50.855421+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Quando deverá ser calculado RRA na rescisão complementar
type: support-article
updated_at: '2025-05-05T21:01:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026404293-RH-Linha-Protheus-GPE-Quando-dever%C3%A1-ser-calculado-RRA-na-rescis%C3%A3o-complementar
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26468806055831)***Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Em quais situações é calculado RRA na rescisão complementar?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) GPE - Gestão de Pessoal - A partir da Versão 11.8  
  
**Solução**RRA - Rendimentos Recebidos Acumuladamente, será calculado em rescisões complementares quando estas forem realizadas em anos posteriores da rescisão original e houver mudanças na tabela de IR em relação ao ano da rescisão original, para que seja calculado RRA na rescisão complementar é necessário que os IDs abaixo estejam relacionados a uma verba na rotina Verba:

|  |  |
| --- | --- |
| **Codigo** | **Descricao** |
| 0974 | Base IR RRA |
| 0975 | Contr. Previdenciaria RRA |
| 0976 | Pensao Aliment. RRA |
| 0977 | Liquido RRA |
| 0978 | IR RRA |
| 0979 | Base IR 13º.RRA |
| 0980 | Contr. Previdenciaria 13º. RRA |
| 0981 | Pensao Aliment. 13º. RRA |
| 0982 | Liquido RRA 13º |
| 0983 | IR RRA 13º |
| 0986 | Dif. Dissidio RRA - Provento |
| 0987 | Dif. Dissidio RRA - Desconto |

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)

[MP - GPE - Porque mensagem "Identificador de complemento do RRA não foi preenchido..." é exibida em rescisões complementares](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028388212)
