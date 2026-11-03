---
article_id: 360027333532
category: Cálculo
content_hash: d3bf9a58f0560791392c73c1dfc88a2166d1b72f6a5a351811948ddfe48c7f7d
fetched_at: '2026-06-28T22:46:29.225002+00:00'
product: rm
section_id: 1500000861662
source: central-rm
title: RH - RM - PTO - Calcular ocorrências customizadas em eventos separados
type: support-article
updated_at: '2025-10-24T23:35:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027333532-RH-RM-PTO-Calcular-ocorr%C3%AAncias-customizadas-em-eventos-separados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16503236661655)**Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Como calcular ocorrências customizadas em eventos separados?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 12.1  
  
**Solução**Para realizar o cálculo de ocorrências customizadas em eventos separados no **Automação de Ponto**, siga os passos abaixo.

1. Acesse a guia **Configurações** e selecione o menu **Tipos de Ocorrências**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29221055662103)
2. Crie a ocorrência customizada desejada através do menu **Incluir**. No exemplo abaixo, a ocorrência que criamos é de Faltas por suspensão.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29221080125591)
3. Após a criação da ocorrência, deverá realizar a modificação de ocorrências, transformando as ocorrências originais do dia do funcionário na ocorrência que foi criada. No exemplo, o dia de falta do funcionário será transformado em Falta por Suspensão (ocorrência criada). Nos links abaixo, contém os passos de como realizar a modificação de ocorrência:  
   [RH - RM - PTO - Modificação de ocorrências individual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000929287)  
   [RH - RM - PTO - Realizar modificação de ocorrências de forma global](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019944691)  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29221055670039)
4. Cadastre um evento de código de cálculo 0043 e associe ao evento a ocorrência criada. Para cadastrar o evento, acesse o menu **Eventos** na guia **Configurações**. No link abaixo contem os passos de realizar o cadastro:  
   [RH - RM - PTO - Cadastrar eventos por tipo de ocorrência (código de cálculo 0043)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019943891)  
     
   ![exemplo.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29221055675799)
5. Associe o evento criado ao sindicato do funcionário, na etapa **Eventos. Abaixo segue os passos de como realizar a associação:**[RH - RM - PTO - Cadastrar eventos no sindicato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043969074)  
    **![](https://centraldeatendimento.totvs.com/hc/article_attachments/29221080133527)**
6. Após realizar todos os passos realize o recalculo do ponto. E o evento criado irá reconhecer a ocorrência alterada no Passo 3 e realizará o cálculo no evento.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29221080143767)

**Saiba Mais**  
Para maiores informações sobre modificação de ocorrências e cadastros de eventos de código de cálculo acesse o link abaixo:

[Processo de vínculo de tipos de ocorrências customizadas (Código de cálculo 0043)](https://tdn.totvs.com/pages/releaseview.action?pageId=185755635)  
[Código de cálculo 0043 x Banco de Horas e Alteração de Atitude](https://tdn.totvs.com/pages/releaseview.action?pageId=728647367#1-1)
