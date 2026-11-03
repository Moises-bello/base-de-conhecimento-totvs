---
article_id: 360051265733
category: RH - Folha de Pagamento
content_hash: 7e8a57c75866956aa30d12b0b68a847c115af47d534aa65c53163755729ed24c
fetched_at: '2026-06-28T22:44:14.626313+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como parametrizar o mnemônico  P_LDIFINC
type: support-article
updated_at: '2025-10-06T13:20:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051265733-RH-Linha-Protheus-GPE-Como-parametrizar-o-mnem%C3%B4nico-P-LDIFINC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16997641910423) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como parametrizar o mnemônico P\_LDIFINC?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

Criado mnemônico P\_LDIFINC (valor padrão .F.) para que seja possível parametrizar se haverá o cálculo da diferença nessa situação ou não. Para configurar o mnemônico acesse **Atualizações > Definições de Cálculos > Mnemônicos (GPEA300)**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26412126504087)  
  
**P\_LDIFINC = .T.** → Gera diferença de férias e de 13º quando houver lançamento de verbas que incorporarem ao salário que não foram consideradas no cálculo anterior (ou de férias ou de 13º);

**P\_LDIFINC = .F.** (padrão) → Não gera diferença de férias e nem de 13º quando houver lançamentos de verbas que incorporam salário na folha.  
  
**Observação:**

O mnemônico P\_LDIFINC não se refere a diferença de médias, mas sim a diferença gerada em cima da verba que incorpora ao salário, portanto pode ser que mesmo com P\_LDIFINC = .F. a verba Dif. 2ª Parc.13º seja gerada com base na diferença de médias.

**Saber Mais:**

[RH - Definições de Cálculos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011913513-RH-Defini%C3%A7%C3%B5es-de-C%C3%A1lculo)

[RH - Linha Protheus - GPE - Qual a teoria do pagamento da Diferença de férias na folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060307373-RH-Linha-Protheus-GPE-Qual-a-teoria-do-pagamento-da-Diferen%C3%A7a-de-f%C3%A9rias-na-folha?source=search)

[RH - Linha Protheus - GPE - Apuração da diferença das médias de férias P\_LDIFMED](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028807072-RH-Linha-Protheus-GPE-Apura%C3%A7%C3%A3o-da-diferen%C3%A7a-das-m%C3%A9dias-de-f%C3%A9rias-P-LDIFMED?source=search)

[RH - Linha Protheus - GPE - Para que servem e como alterar os valores dos mnemônicos P\_VLLIMDIRF e P\_VLLIMOUT para DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022215951-RH-Linha-Protheus-GPE-Para-que-servem-e-como-alterar-os-valores-dos-mnem%C3%B4nicos-P-VLLIMDIRF-e-P-VLLIMOUT-para-DIRF?source=search)
