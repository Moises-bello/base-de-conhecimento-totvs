---
article_id: 15973684667159
category: RH - Folha de Pagamento
content_hash: b5e7576c8cc5f760a85ec4411a081042dfa2f5a40e52dc12e00029463a3ce52d
fetched_at: '2026-06-28T22:44:12.094661+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de IR não considera modelo completo mesmo
  quando soma do INSS mais pensão é maior que a dedução simplificada
type: support-article
updated_at: '2025-04-22T18:49:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15973684667159-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-IR-n%C3%A3o-considera-modelo-completo-mesmo-quando-soma-do-INSS-mais-pens%C3%A3o-%C3%A9-maior-que-a-dedu%C3%A7%C3%A3o-simplificada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15973658091159) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Cálculo de IR não considera modelo completo mesmo quando soma do INSS mais pensão é maior que a dedução simplificada.  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.33.  
  
**Causa**A verba de desconto de pensão não esta relacionada no cadastro de beneficiário.  
  
**Solução**Para o cálculo do IR seguindo a MP 1171, para o sistema conseguir identificar que a verba de desconto é referente a pensão alimentícia e então considerar ela como dedução legal, deve existir o cadastro de beneficiário, e na coluna Verba Folha deve ser informada a verba de desconto de pensão que é lançada/calculada na folha, caso não exista esse relacionamento, o sistema não consegue identificar que é uma verba de desconto de pensão.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19426037026839)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19426037051415)

Para cadastrar o beneficiário, siga a documentação a seguir:  
[RH - Linha Protheus - GPE - Como parametrizar o Sistema para cálculo de pensão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049721974)

**Saiba Mais:**

[RH - Linha Protheus - GPE - MP-1.171/2023 - Como configurar a nova forma de cálculo de IR no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14626756121367)  
[DOU - MEDIDA PROVISÓRIA nº 1.171, de 30 de ABRIL de 2023](https://www.in.gov.br/en/web/dou/-/medida-provisoria-n-1.171-de-30-de-abril-de-2023-480184173)  
[FAQ da Consultoria de Segmentos](https://tdn.totvs.com.br/pages/releaseview.action?pageId=758481181)  
[Espaço Fiscal - Totvs](https://www.totvs.com/blog/fiscal-clientes/novo-calculo-de-imposto-de-renda/)
