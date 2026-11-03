---
article_id: 360021668251
category: RH - Férias
content_hash: c09f64ad87befe22095a688ab303d7c3c423428a4f82dd02e34e07a223843e2e
fetched_at: '2026-06-28T22:43:59.237668+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema não permite calculo de férias inferior
  a 30 dias para colaboradores menor de 18 anos ou maior de 50 anos
type: support-article
updated_at: '2025-08-14T12:36:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021668251-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-permite-calculo-de-f%C3%A9rias-inferior-a-30-dias-para-colaboradores-menor-de-18-anos-ou-maior-de-50-anos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26611112388503) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Sistema não permite calculo de férias inferior a 30 dias para colaboradores menor de 18 anos ou maior de 50 anos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26764602555159)

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões

**Solução**

Isso ocorre pois antes da Reforma Trabalhista não era permitido o calculo de férias inferior a 30 dias quando menor de 18 anos e maior de 50 anos.   
Com a Reforma Trabalhista foi Revogado esse impedimento possibilitando as férias serem fracionadas

A validação do calculo ocorre através do parâmetro **MV\_REFTRAB** que deve ter seu conteúdo **FSRI**, onde **F**= Férias, **S**= Contribuição Sindical, **R**= Regime Parcial e **I** = Insalubridade Gestante.   
  
Se, por exemplo, o conteúdo do parâmetro **MV\_REFTRAB** estiver "**RSI**", o sistema não valida a Reforma Trabalhista e impede o calculo das férias caso inferior a 30 dias para menores de 18 anos e maiores de 50 anos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26764602565527)

Documentação completa: [Implementações da reforma trabalhista](https://tdn.totvs.com/pages/viewpage.action?pageId=312149147)

**Saiba Mais:**

[RH - Férias](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597291-RH-F%C3%A9rias)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)

<https://tdn.totvs.com/pages/releaseview.action?pageId=312149147>
