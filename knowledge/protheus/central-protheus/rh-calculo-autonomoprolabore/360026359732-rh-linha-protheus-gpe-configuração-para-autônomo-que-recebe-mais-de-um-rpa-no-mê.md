---
article_id: 360026359732
category: RH - Calculo Autonomo/Prolabore
content_hash: bda6f954434a7cde2011ff5506fdfcf601c55513f03af7120a88b0c523dd29a7
fetched_at: '2026-06-28T22:43:15.178963+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Configuração para Autônomo que recebe mais de um
  RPA no mês
type: support-article
updated_at: '2025-05-07T14:21:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026359732-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-para-Aut%C3%B4nomo-que-recebe-mais-de-um-RPA-no-m%C3%AAs
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25168107706135)**Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Configuração para Autônomo que recebe mais de um RPA no mês  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão Pessoal - A partir da versão 12  
  
**Solução**É possível efetuar vários pagamentos para autônomos dentro do mesmo período, e por ser gerado encargos referente ao valor da prestação de serviço, é necessário fechar o número de pagamento utilizado para o cálculo. Desta forma, as informações de bases de IR e de INSS serão consideradas para o próximo cálculo de RPA do autônomo, dentro do período.

É necessário amarrar os autônomos que recebem mais de um pagamento no mês em um processo separado dos autônomos mensal, por padrão do Protheus é disponibilizado dois processos para atender a necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025861672)

Processo 00003 - para os Pro-labores/ Autônomos que recebem em uma unica folha (Mensal).  
Processo 00004 - para os Pro-labores/ Autônomos que possuem vários pagamentos dentro do mesmo período (Semanal).

**O intuito de separar os processos é devido a necessidade de fechar o número de pagamento anterior para que seja possível calcular o próximo, pois somente com o fechamento o sistema enxergará as bases de IR e INSS para o próximo desconto.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025871351)

**Saiba Mais:**

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
