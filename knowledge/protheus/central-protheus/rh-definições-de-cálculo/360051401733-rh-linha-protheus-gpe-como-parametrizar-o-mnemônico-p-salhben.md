---
article_id: 360051401733
category: RH - Definições de Cálculo
content_hash: a673d3029dbaf32838f9c4fba17305294fcef7e855d3149a26c1af23695f9f5d
fetched_at: '2026-06-28T22:43:22.574390+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Como parametrizar o mnemônico P_SALHBEN
type: support-article
updated_at: '2025-09-30T17:24:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051401733-RH-Linha-Protheus-GPE-Como-parametrizar-o-mnem%C3%B4nico-P-SALHBEN
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26998104117399) Tempo aproximado para leitura: **00:01:30 min****Dúvida**Como parametrizar o mnemônico P\_SALHBEN?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

Criado o mnemônico P\_SALHBEN para definir se o sistema deve se basear no lançamento mensal, ou no cadastro de funcionários para calcular o desconto do vale transporte do funcionário horista. Para configurar o mnemônico acesse Atualizações > Definições de Cálculos > Mnemônicos (GPEA300)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26998104119703)

Configuração do mnemônico **P\_SALHBEN com conteúdo .F.** (Padrão):

O sistema realiza o cálculo utilizando as horas do cadastro de funcionários.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26998104121367)

Configuração do mnemônico **P\_SALHBEN com conteúdo .T.** :

Caso exista lançamento com a verba Salário Horista (ID 0032) o sistema considera esse lançamento para calcular DSR e o valor de desconto do Vale Transporte.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26998104122391)

**Importante:**

Caso seja feito o lançamento da verba de Salário Horista e de DRS Horista (ID 0033) o sistema considera as duas verbas para o cálculo do Vale transporte.

**Saiba mais:**

[RH - Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011913513-RH-Defini%C3%A7%C3%B5es-de-C%C3%A1lculo)
