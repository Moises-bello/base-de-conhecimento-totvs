---
article_id: 7726019726487
category: Materiais - Compras (SIGACOM)
content_hash: 45b44f58446a6d4ee5ad02d9cb84bfe60ed1e781cb3f44dbfb864f63a0cbb426
fetched_at: '2026-06-28T22:41:14.387584+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Central de Compras
  - O que determina o saldo na filial para os produtos ?
type: support-article
updated_at: '2022-07-26T14:04:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7726019726487-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Central-de-Compras-O-que-determina-o-saldo-na-filial-para-os-produtos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02 min** **Dúvida**

O que determina o saldo na filial para os produtos ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12  
  
**Solução**

O saldo é calculado considerando todos os armazéns de estoque do produto, exceto o armazém de transito – MV\_LOCTRAN – a menos que seja parametrizado saldo em trânsito e considerando-se a parametrização efetuada.

Abaixo seguem os campo correspondentes na tabela de saldos:

* Considera estoque B2\_QATU
* Reservas B2\_RESERVA
* Empenhos B2\_QEMP + B2\_QEMPSA
* Previsões de Entrada B2\_SALPEDI
* Pedidos de Venda em Carteira B2\_QPEDVEN
* Saldo em Trânsito B2\_QATU do B2\_LOCAL igual a MV\_LOCTRAN
* Disponível Ponto de Entrada para informar os armazéns a considerar no cálculo. Este PE passa como parâmetros, a Filial e Produto e recebe como retorno um *array* de Armazéns a considerar no cálculo.
* Disponível Ponto de Entrada que retorna a quantidade de saldo em trânsito, quando não conste na regra do padrão (saldo em trânsito: B2\_QATU do B2\_LOCAL igual a MV\_LOCTRAN). Este PE passa como parâmetros a Filial e Produto e recebe como retorno o valor a  considerar em trânsito para a filial e produto em questão.

***Saiba Mais:***

**[Central de Compras - Calculos](https://tdn.totvs.com/pages/viewpage.action?pageId=642166576)**

**[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)**

**[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)**
