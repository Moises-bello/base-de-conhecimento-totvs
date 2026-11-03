---
article_id: 31149947210519
category: 'RH - Verbas '
content_hash: 5d270be57101efbddf0edd698ebc289781980f4f501169198f0f889b695b1ce3
fetched_at: '2026-06-28T22:43:19.907484+00:00'
product: protheus
section_id: 360010838314
source: central-protheus
title: RH - Linha Protheus - GPE - Como cadastrar as verbas de desconto do eConsignado
  (Programa Crédito do Trabalhador)
type: support-article
updated_at: '2026-04-23T18:49:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31149947210519-RH-Linha-Protheus-GPE-Como-cadastrar-as-verbas-de-desconto-do-eConsignado-Programa-Cr%C3%A9dito-do-Trabalhador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31149947193751) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como cadastrar a verba de Empréstimo Consignado para atender à Medida Provisória que institui o Crédito do Trabalhador (MP 1.292/2025).   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - TOTVS Gestão de Pessoal - Todas as versões  
  
**Solução**  
O Crédito do Trabalhador é uma iniciativa do Governo Federal que tem como objetivo facilitar o acesso ao crédito para trabalhadores do setor privado, incluindo empregados rurais, domésticos e Microempreendedores Individuais (MEI), o programa foi introduzido pela **Medida Provisória nº 1.292/2025**

Para cadastrar as verbas de desconto para Empréstimo Consignado acesse **Atualizações> Definições de Cálculo> Verbas** e selecione a opção **incluir.**

As verbas devem ser de **tipo Desconto** para dedução do valor e o campo de **Empréstimo Consignado** preenchidas com **1-Sim**, para que seja respeitado o limite de 35% do Valor Liquido. Além disso, deve ser informado a **Natureza de Rubrica 9253 e Incidência FGTS 31**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31160914284951)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31160914286871)**

Na aba Bloqueio de Lançamentos, deixe o campo **Futuros** com **1-Sim**, para que a verba possa ser incluída na rotina de Valores Futuros.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32420369571735)

**IMPORTANTE:**  
-Caso a Natureza 9253 **não esteja disponível**, [atualize a S047.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052764613-RH-Linha-Protheus-GPE-Natureza-de-verba-indispon%C3%ADvel-na-Tabela-S047-Natureza-das-Rubricas)   
-Somente **novos empréstimos**, contratados por essa modalidade e através da CTPS Digital, podem ter as verbas com Natureza de Rubrica 9253 - Empréstimo eConsignado - Desconto.  
- Caso o funcionário tenha **mais de um empréstimo** será necessário **criar novas verbas** para o desconto dos demais contratos. Ex. 4 contratos, 4 verbas e informá-las na tabela **S154 - Verbas Crédito do Trabalhador** em **Atualizações > Definições de Cálculo - Manutenção de Tabelas**.

OBs. Realizado ajuste para reutilização de verba já utilizada em outros empréstimos, caso o campo Situação esteja como Pago ou Descontinuado. 

**Saiba Mais**  
[Crédito Trabalhador - MP 1.292/2025](https://tdn.totvs.com/pages/releaseview.action?pageId=925350852)  
[RH - Linha Protheus - GPE - Como calcular na folha de pagamento o Credito Trabalhador eConsignado Medida Provisória nº 1.292/2025](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31152092269591-RH-Linha-Protheus-GPE-Como-calcular-na-folha-de-pagamento-o-Credito-Trabalhador-eConsignado-Medida-Provis%C3%B3ria-n%C2%BA-1-292-2025)
