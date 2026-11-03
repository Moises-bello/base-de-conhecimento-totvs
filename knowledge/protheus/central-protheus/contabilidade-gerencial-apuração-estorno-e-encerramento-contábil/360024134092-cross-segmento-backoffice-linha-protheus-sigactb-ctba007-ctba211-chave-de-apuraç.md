---
article_id: 360024134092
category: Contabilidade Gerencial - Apuração, Estorno e Encerramento Contábil
content_hash: 188d7821d2ea502c27a5cb5a6d904cc1786fcf062b65a478f3e2e8f77b77b1b6
fetched_at: '2026-06-28T22:41:05.040224+00:00'
product: protheus
section_id: 1500001548342
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA007/ CTBA211 - Chave
  de Apuração (CW0)
type: support-article
updated_at: '2025-01-22T22:42:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024134092-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA007-CTBA211-Chave-de-Apura%C3%A7%C3%A3o-CW0
---

**Ocorrência**Qual é a composição da chave de apuração criada pela rotina CTBA211?

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
  
**Solução**Ao realizar a apuração de resultados, a rotina **CTBA211** cria uma chave de apuração na tabela **CW0.**

CW0 + tabela LP,

**Exemplo🚩️:** Campo **CW0\_DESC01** =**20181231011Z**= **ano**+ **mês** + **dia**+ **moeda** + **saldo** + **Z ou P**

**Z**= Zerado (Sem conta ponte)

**P**= Conta Ponte (Apuração com conta Ponte)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022392251)

É possível visualizar também através da rotina **CTBA007**

* Clique em visualize  
  ![](https://totvssuporte.zendesk.com/attachments/token/piy1fTG6uLyb3EnKhX4YBYGl5/?name=inline-628510093.png)

​

Saiba mais:

[Como realizar Apuração de resultados dentro do Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005048472-MP-SIGACTB-Como-realizar-Apura%C3%A7%C3%A3o-de-resultados-dentro-do-Protheus-?source=search)

[CTBA211 Exemplo - Apuração Trimestral : Apuração Sem conta PONTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041554693-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Trimestral-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)

[CTBA211 Exemplo - Apuração Anual : Apuração Sem conta PONTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041555313-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Anual-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)

[CTBA211 Exemplo - Apuração Com Conta PONTE, Contas Transitórias e Encerramento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041533493--MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Com-Conta-PONTE-Contas-Transit%C3%B3rias-e-Encerramento?source=search)

[CTBA211 Exemplo - Apuração Com Conta PONTE, Contas de Resultados e Encerramento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041053194--MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Com-Conta-PONTE-Contas-de-Resultados-e-Encerramento?source=search)
