---
article_id: 360052226154
category: Financeiro - Caixinha
content_hash: cfc7c788c2e0ef7a15be8165d238ba4817653e1354f9a03f9038c2c29093fae4
fetched_at: '2026-06-28T22:37:53.902065+00:00'
product: protheus
section_id: 1500001550702
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA550 - Existe alguma
  forma de efetuar movimentos no caixinha sem gerar reposição e que o  saldo fique
  negativo
type: support-article
updated_at: '2022-06-21T01:41:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052226154-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA550-Existe-alguma-forma-de-efetuar-movimentos-no-caixinha-sem-gerar-reposi%C3%A7%C3%A3o-e-que-o-saldo-fique-negativo
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Existe alguma forma de efetuar os movimentos no caixinha sem efetuar a reposição do mesmo?  
  
**Exemplo:**  
Tenho um caixa (cx) de 15.000,000 ao fazer as movimentações quando utilizo todo o saldo, o mesmo deseja não fazer a reposição e continuar a efetuar as movimentações até que o saldo fique negativo.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA550 - Todas as versões  
  
**Solução**No padrão do sistema **Protheus**, o **caixinha** não tem como ficar com saldo negativo, se faz necessário a **reposição** do mesmo para dar continuidade nas movimentações.

O **caixinha** autoriza que caso o banco de onde fará a retirada do dinheiro não tenha saldo, o sistema permite a transação através deste parâmetro:

**MV\_CXSLBCO =** Permitir que o saldo do caixinha seja reposto mesmo quando o Banco não possuir saldo suficiente.
