---
article_id: 8769882633367
category: Comércio Exterior - Easy Import Control - Embarque
content_hash: edb290bbbfe2965f7b680411aa3e2def6d566ed93ec61dd719dbd86073653647
fetched_at: '2026-06-28T22:39:48.777154+00:00'
product: protheus
section_id: 1500001538381
source: central-protheus
title: ' Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Campo "B2_SALPEDI"
  não está sendo atualizado após a gravação da Purchase Order.'
type: support-article
updated_at: '2023-01-13T20:29:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8769882633367--Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Campo-B2-SALPEDI-n%C3%A3o-est%C3%A1-sendo-atualizado-ap%C3%B3s-a-grava%C3%A7%C3%A3o-da-Purchase-Order
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **03:00 min** **Dúvida**A Consulta ao Estoque "**Qtd Entrada Prevista - B2\_SALPEDI**" não está sendo atualizada após a gravação da Purchase Order.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8769399016215/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**Conforme orientação do Produto, o **SIGAEIC** não faz atualizações referentes a estoque. Neste caso, o **Módulo de Compras** será o responsável por eventuais atualizações de saldos.  
O Módulo de Compras também possui uma regra, que quando o item utilizado dentro do Pedido possuir uma **TES** vinculada e esta **TES** estiver parametrizada para **Não atualizar estoque,** não ocorrerá nenhuma atualização de saldo referente a Previsão de Entrega.  
Desta forma, a atualização de Saldo só será efetuada caso o item não possua nenhuma **TES** vinculada a ele ou possuindo a **TES**, que a mesma esteja parametrizada para **Atualizar Estoque.**
