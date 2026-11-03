---
article_id: 360057989493
category: RH - Calculo Autonomo/Prolabore
content_hash: a330c8b29a38cba873182c7221d9f9c89ce1cdd57f8f2978bc1c980da00c5084
fetched_at: '2026-06-28T22:43:15.135317+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar o sistema para calcular FGTS para
  pró-labore
type: support-article
updated_at: '2025-06-13T11:33:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057989493-RH-Linha-Protheus-GPE-Como-configurar-o-sistema-para-calcular-FGTS-para-pr%C3%B3-labore
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27283637621143) Tempo aproximado para leitura: **00:01:30 min  
  
Dúvida**Como configurar o sistema para calcular FGTS para pró-labore?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Para que seja calculado o FGTS de pró-labore, é necessária a configuração abaixo. Acesse **Atualizações > Funcionários > Contribuinte Individual (GPEA011)**:

* No Cadastro de funcionários, **o campo % fgts** deve estar com **8%.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27283637625879)**

* No cadastro de funcionários a categoria da **SEFIP** deve estar preenchida de forma correta conforme o manual da SEFIP.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27283590071319)

Também é necessário verificar se o cadastro da verba de id 0217 Pagamento Pro Labore está configurada com SIM para FGTS na aba Incidências. Para verificar a configuração acesse **Atualizações > Definições de Cálculos > Verbas (GPEA040)**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27283637631383)

**Importante**

Caso o sistema **não** apresente os campos no cadastro do **Contribuinte Individual** podemos incluir campos conforme documentação [RH - Linha Protheus - GPE - Como configurar os campos que serão apresentados no cadastro de Autônomos/Contribuinte Individual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009855832-RH-Linha-Protheus-GPE-Como-configurar-os-campos-que-ser%C3%A3o-apresentados-no-cadastro-de-Aut%C3%B4nomos-Contribuinte-Individual).

**Saiba mais:**

[RH - Funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011909593-RH-Funcion%C3%A1rios)
