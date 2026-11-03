---
article_id: 32288956493847
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 6d970a88a75a697362d15fa0bf99b6ae8418f76bdd10f1ff239db58eb2fca9fd
fetched_at: '2026-06-28T22:38:57.281380+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Por quê em Transferencias
  entre Filiais acontece da data de validade na Filial Destino vir diferente da Filial
  Origem?
type: support-article
updated_at: '2025-05-22T17:11:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32288956493847-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Por-qu%C3%AA-em-Transferencias-entre-Filiais-acontece-da-data-de-validade-na-Filial-Destino-vir-diferente-da-Filial-Origem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32288956480919) Tempo aproximado para leitura: **00:02:37 min** **Dúvida**Por quê em Transferências entre Filiais pode acontecer da data de validade na Filial Destino vir diferente da Filial Origem em determinados produtos?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Normalmente isso acontece quando este lote já teve saldo na filial de destino. Exemplo abaixo.

**Filial 01**

**Produto: XPTO**

**Lote: 123**

**Quantidade: 10**

**Validade: 10/12/2028**

**Filial 02**

**Produto: XPTO**

**Lote: 123**

**Quantidade: 0**

**Validade: 10/12/2026**

Se houver uma transferência dos 10 itens da Filial 01 para a Filial 02 deste produto e lote, ele chegará na Filial 02 com validade em 10/12/2026, pois, uma vez que o lote já existia na filial de destino, com uma característica de validade (10/12/2026), por mais que ele receba mais saldo (e isso independe da forma que este saldo é alimentado), ele precisa chegar na Filial 02 com a mesma validade que ele já tinha outrora. Isso garante a integridade do saldo no arquivo SB8 (Saldos por Lote).

Para comprovar esse comportamento, se o usuário você entrar com um Documento de Entrada de um produto e lote que já teve histórico na filial em que está incluindo o Documento de Entrada e inserir outra validade, ele vai receber um help alertando que não é possível entrar com o mesmo lote, em outra validade. Porque o registro da SB8 já está lá de histórico, mesmo que tenha acabado o saldo e comprado outro saldo, o que caracteriza o lote é a validade dele.

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32288956481943)

Ou seja, se a Transferência entre Filiais (que é um facilitador que gera o Documento de Saída e Documento de Entrada nas filiais origem e destino respectivamente) tentasse manter a validade neste caso, o usuário não conseguiria efetuá-la pois enfrentaria o help **A240DTVALI**.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
