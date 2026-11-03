---
article_id: 23768888024855
category: RH – DIRF
content_hash: d5b23955d147a69696d78230d80301512841e7e683abafed65fed79c4f30b5bd
fetched_at: '2026-06-28T22:44:06.956357+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Dedução Simplificada para Funcionário com Multiplos
  Vinculos na DIRF
type: support-article
updated_at: '2025-06-16T19:28:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23768888024855-RH-Linha-Protheus-GPE-Dedu%C3%A7%C3%A3o-Simplificada-para-Funcion%C3%A1rio-com-Multiplos-Vinculos-na-DIRF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23768866691991) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como é gerado o valor de Dedução Simplificada na DIRF quando o funcionário possui Multiplos Vinculos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.1.33.  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acesse: Miscelanea / DIRF / Manutenção Arquivo (GPEM560), Informe o ano Calendário e veja que quando o funcionário possui mais de um vínculo, será apresentado um registro para cada matrícula com o mesmo CPF:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23768866699671)  
  
2. Ao Consultar o cálculo da Folha, Verifique se o Modelo de Tributação do Imposto de Renda foi o Simplificado:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23768866701335)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23768888002455)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23768888006295)  
  
3. Na rotina Manutenção Arquivo (GPEM560), ao Visualizar cada uma destas matrículas, serão carregados os valores de acordo com a configuração da incidência das Verbas para a DIRF, e se o desconto de Imposto de Renda mais benéfico ao funcionário for no modelo Simplificado, na coluna "Dedução Simplificada" será apresentado o valor de R$528,00:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23768866710039)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23768866711191)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23768888007831)  
  
4. Ao gerar o arquivo Magnético da DIRF, mesmo que tenha sido gerado o valor de Dedução Simplificada para as 3 matrículas, será gerado apenas o valor de R$528,00:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23768888008471)

**Saiba Mais:**

[Consultoria de Segmentos - Cálculo Simplificado do IRRF](https://tdn.totvs.com/pages/releaseview.action?pageId=758481181#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosC%C3%A1lculoSimplificadodoIRRF-2.11.1Paraempregadosquepossuemmaisdeumvinculoemempresasdiferentes,poder%C3%A1utilizarparadedu%C3%A7%C3%A3ooINSSdoprimeirovinculo?)   
[RH - DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
