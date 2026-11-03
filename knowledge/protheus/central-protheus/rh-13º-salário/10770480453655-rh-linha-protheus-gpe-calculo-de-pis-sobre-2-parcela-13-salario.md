---
article_id: 10770480453655
category: RH - 13º salário
content_hash: 0ba669811e66667d7a01f996d8b18717edcdc1a8a9178e9d00e58bbf2f82f89a
fetched_at: '2026-06-28T22:44:00.476280+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Calculo de PIS sobre 2° Parcela 13° Salario
type: support-article
updated_at: '2025-08-11T11:08:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10770480453655-RH-Linha-Protheus-GPE-Calculo-de-PIS-sobre-2-Parcela-13-Salario
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18873302386199) Tempo aproximado para leitura: **00:03:00****min** **Dúvida**Como é calculo PIS sobre a 2° Parcela do 13° Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Com a revogação da IN RFB 247/2002, foi publicada a Solução de Consulta COSIT nº 113/2020, que estabelece o recolhimento do PIS sobre o adiantamento da parcela do Décimo Terceiro, ou seja, o PIS deverá ser aplicado sobre os adiantamentos ou gratificações ocorridas no mês e recolhidos até o 20º dia do mês subsequente ao do pagamento do salário. 

Para que as verbas entrem como base para o cálculo do PIS é necessário que o campo **PIS** que fica na aba **Incidências** no cadastro da verba esteja configurado com **Sim**. Para ajustar o cadastro da verba acesse **Atualizações > Definições de Cálculos > Verbas (GPEA040)**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18873345360791)  
  
**2° Parcela**No calculo da 2º parcela do 13º, a base do PIS calculada na 1º parcela **será abatida** do total da base da 2º parcela de forma automática, a verba com **id 0183** - Desconto de Antecipação do 13º Salário deve ser configurada com **Não** no **campo PIS (RV\_PIS).**  
  
**Calculo roteiro 132**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29239448800919)

**Calculo Folha**De acordo com a versão S-1.3 do eSocial, os valores relativos ao PIS do 13º salário não devem ser somados à folha de pagamento. Assim, o recolhimento do PIS/PASEP sobre o 13º salário é demonstrado de forma separada, ou seja, cada recolhimento é registrado em seu respectivo roteiro.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/29239448801431)**

**Documentação Técnica:** [Cálculo incorreto de PIS na folha de dezembro](https://tdn.totvs.com/pages/releaseview.action?pageId=904047252) **Saiba Mais**[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)[RH - Linha Protheus - GPE - Calculo de PIS sobre 1° Parcela do 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10244840162711-RH-Linha-Protheus-GPE-Calculo-de-PIS-sobre-1-Parcela-do-13%C2%BA-Sal%C3%A1rio?source=search)  
[RH - Linha Protheus - GPE - Calculo de PIS sobre Parcela única](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10770707424279-RH-Linha-Protheus-GPE-Calculo-de-PIS-sobre-Parcela-%C3%BAnica?source=search)
