---
article_id: 7732749872919
category: Materiais - Compras (SIGACOM)
content_hash: 794d32e48d222b5a81199d40dc895174a44649b91cb90f6bbbef76c4ed754766
fetched_at: '2026-06-28T22:41:14.391318+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Central de Compras
  - Previsão de Consumo
type: support-article
updated_at: '2022-07-26T17:06:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7732749872919-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Central-de-Compras-Previs%C3%A3o-de-Consumo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02 min** **Dúvida**

Como é calculado a Previsão de Consumo ?

![consumo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7732581672087/consumo.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões

**Solução**

É determina a previsão de consumo para o produto na filial em questão, sendo :

**1.** Se parametrizado por **Demanda Gerada**, o consumo é calculado pelas demandas geradas na rotina [Gerar Demanda](https://tdn.totvs.com/pages/viewpage.action?pageId=312156967) mais os dias de cobertura informados na parametrização inicial.

**2.** Se parametrizado por **Média de Venda**s, deve ser calculada a média de vendas (média aritmética) ocorridas no período informado  na parametrização, desconsiderando as notas que não atualizaram estoque e remessas para terceiros e subtraindo devoluções ocorridas. A média obtida é incrementada conforme percentual informado na parametrização. Por fim, a média incrementada é multiplicada pelos dias de cobertura.

**3.** Se parametrizado por **Previsão de Vendas**, o consumo é a soma das quantidades de todas as previsões de venda existentes no período informado na parametrização.

***Saiba Mais:***

[Central de Compras - MATA179](https://tdn.totvs.com/x/MK9GJg)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
