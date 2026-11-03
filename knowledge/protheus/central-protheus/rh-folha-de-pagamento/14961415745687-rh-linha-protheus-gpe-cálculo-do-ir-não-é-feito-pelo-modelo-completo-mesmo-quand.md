---
article_id: 14961415745687
category: RH - Folha de Pagamento
content_hash: ca5d3c9c980814a579192738a56df07ec7b539a960da7ff0d711ed7905db4669
fetched_at: '2026-06-28T22:44:12.121230+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo do IR não é feito pelo modelo completo
  mesmo quando a soma do INSS e dependentes é maior que a dedução simplificada
type: support-article
updated_at: '2024-09-05T18:18:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14961415745687-RH-Linha-Protheus-GPE-C%C3%A1lculo-do-IR-n%C3%A3o-%C3%A9-feito-pelo-modelo-completo-mesmo-quando-a-soma-do-INSS-e-dependentes-%C3%A9-maior-que-a-dedu%C3%A7%C3%A3o-simplificada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19426848806295) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Cálculo do IR não é feito pelo modelo completo mesmo quando a soma do INSS e dependentes é maior que a dedução simplificada.  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.33.  
  
**Causa**Parametrização incorreta de verbas.  
  
**Solução**Isso pode ocorrer quando tanto a verba de ID 0064-INSS Folha quanto a verba de ID 0167-Dedução INSS Base IR Folha estão com SIM para IR, pois o sistema se perde no cálculo, então considera o cálculo simplificado no IR.  
  
Para ajuste, entre na rotina de **Verbas** pelo caminho **>Atualização >Definição de Cálculos >Verbas**, e na aba **Incidências**, deixe apenas **um** dos IDs com SIM para IR (ou o ID 0064 ou o ID 0167), desta forma o cálculo será feito de forma correta:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14961296749975)

**Saiba Mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - MP-1.171/2023 - Como configurar a nova forma de cálculo de IR no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14626756121367)[DOU - MEDIDA PROVISÓRIA nº 1.171, de 30 de ABRIL de 2023](https://www.in.gov.br/en/web/dou/-/medida-provisoria-n-1.171-de-30-de-abril-de-2023-480184173)

[FAQ da Consultoria de Segmentos](https://tdn.totvs.com.br/pages/releaseview.action?pageId=758481181)

[Espaço Fiscal - Totvs](https://www.totvs.com/blog/fiscal-clientes/novo-calculo-de-imposto-de-renda/)
