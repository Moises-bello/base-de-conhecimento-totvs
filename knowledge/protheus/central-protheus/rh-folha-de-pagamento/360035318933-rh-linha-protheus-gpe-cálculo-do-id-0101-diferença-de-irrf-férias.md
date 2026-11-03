---
article_id: 360035318933
category: RH - Folha de Pagamento
content_hash: 2b781626f9e697ebb0003f56ca301059d14225ca09f4cb26af074ae20ea4d361
fetched_at: '2026-06-28T22:44:12.113275+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo do ID 0101 - Diferença de IRRF Férias
type: support-article
updated_at: '2025-08-26T20:03:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035318933-RH-Linha-Protheus-GPE-C%C3%A1lculo-do-ID-0101-Diferen%C3%A7a-de-IRRF-F%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25990966382359) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Sistema está calculando o **ID 0101** - Diferença imposto de renda férias

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Verifique as verbas que estão sendo demonstradas na folha de pagamento, que são verbas de férias, se estão com a configuração correta, ou seja, com **SIM para IRRF e SIM para Ref. Férias** no cadastro de verbas na rotina **Verbas** em **Atualizações > Definições de cálculos > Verbas (GPEA040).**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/34466538381079)**

Verifique se existe verbas de diferença de férias pagas na folha de pagamento, o que explica a geração da Diferença de IRRF. Verifique se houve a dedução correta de dependentes de imposto de renda nas férias caso tenha dependente de IRRF e se também está sendo deduzido na folha, pois pode ocorrer o seguinte cenário:

Data de gozo férias em: 12/08/2019

Data pagamento das férias: 08/08/2019

Férias calculadas: 07/2019

Data Base do sistema: 07/2019

Cadastro de dependentes: 01, sendo data de nascimento 24/07/1997, no mês de julho completa 22 anos.

As férias mesmo sendo no mês de agosto, foi calculada no mês de julho, data base do sistema estava com data de 07/2019, o sistema valida a data base para calcular o dependente, a dedução ocorre até o termino de 21 anos, 1 mês antes de completar 22.

Nas férias o sistema deduziu o dependente mas ao calcular a folha o sistema entenderá que o dependente tem 22 anos e que não deveria ter ocorrido a dedução, neste caso irá realizar o reprocessamento do cálculo gerando a verba com id 0101. Se a data base do sistema estivesse com data de 01/08/2019, por exemplo, o sistema entenderia que a este empregado não tem dependentes.

**Saiba Mais:**

[RH - Linha Protheus - GPE - Dedução de Imposto de Renda ate o mês em que beneficiário completa 22 anos (RA\_DEPIR)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033931534-RH-Linha-Protheus-GPE-Dedu%C3%A7%C3%A3o-de-Imposto-de-Renda-ate-o-m%C3%AAs-em-que-benefici%C3%A1rio-completa-22-anos-RA-DEPIR?source=search)

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
