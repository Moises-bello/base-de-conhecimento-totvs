---
article_id: 26622142593047
category: Originação de Grãos (OG)
content_hash: 0a64a328cd308320f4554dbfe8a1ca25d7a412bf27e4db62b46effaff62b4915
fetched_at: '2026-06-28T22:45:41.136052+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Operação Venda Futura - Comercialização Clássica
type: support-article
updated_at: '2025-04-22T20:36:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26622142593047-Agro-Linha-Protheus-AGR-Opera%C3%A7%C3%A3o-Venda-Futura-Comercializa%C3%A7%C3%A3o-Cl%C3%A1ssica
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26622127198103) Tempo aproximado para leitura: **00:02:30 min**

**Dúvida**Como é realizado um **Exemplo de Utilização de Operação Venda Futura em Comercialização Clássica**?  
  
**Ambiente**TOTVS Agro – TOTVS Agro – Comercialização (Linha Protheus) - Originação de Grãos (OG) – Versão 12  
  
**Solução**Abaixo são descrito os passos para realizar o acompanhamento no contrato de venda.

**1 - Contrato de Venda :**

* Incluir um novo contrato conforme orientações na documentação da rotina: .
* Informar no contrato que o mesmo é destinado para operação Futura.

![EX.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26622127203223)

![EX1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26622142563223)

**2 - Romaneio s/ Pesagem para emitir NF-e Simples faturamento:**

Incluir **Romaneio de Saída Venda** e informar uma **TES** que deve estar parametrizada para atualizar duplicada e não atualizar estoque.

**Exemplo :**

![EX2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26622142566807)

**![EX3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26622127214487)**

**3 - Romaneio c/ Pesagem para emitir NF-e Saída Mercadoria**

Incluir **Romaneio de Saída Venda** e informar uma **TES** que deve estar parametrizada para atualizar estoque  e não atualizar duplicada.

**Exemplo :**

![EX4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26622127220631)

![EX5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26622127222551)
