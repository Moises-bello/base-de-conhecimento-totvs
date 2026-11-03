---
article_id: 5976267208983
category: RH - Contabilização
content_hash: a67cc88291a542c3dbad22af96538ea86517a6fc47fcd24d1c7b2c4b87a8ebb7
fetched_at: '2026-06-28T22:43:45.978230+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Lançamentos contábeis desordenados (MV_ORDLCTB)
type: support-article
updated_at: '2025-07-24T14:12:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5976267208983-RH-Linha-Protheus-GPE-Lan%C3%A7amentos-cont%C3%A1beis-desordenados-MV-ORDLCTB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33687630756247) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Na contabilização da folha, os lançamentos contábeis estão desordenados.  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Causa**Esse incidente ocorre devido a configuração do parâmetro  MV\_ORDLCTB.   
  
**Solução**Permite que seja escolhida a ordem de contabilização nas rotinas de Lançamento Contábil.

* **E -** Contabilizar por ordem de entrada (Campo Recno) que respeitará a ordem de cada centro de custo sem observar se o tipo de lançamento é partida dobrada, crédito ou débito.
* **L -** Contabilizar por ordem de lançamento padrão. Nesta configuração, como exemplo temos 3 Lançamentos padrão: A01-crédito / A02 - Débito / A03 - Partida dobrada. O sistema apresentará os lançamentos contábeis como todas as verbas de débito (A01), em seguida todas de crédito (A02) e depois todas as verbas de partida dobrada (A03).
* **T -** Tipo de Saldo.

A configuração deste parâmetro impactará somente na forma com que os dados serão apresentados na tela "Mostra Lançamento" ao contabilizar um fato contábil.

Em cenários onde há mais um de lançamento sendo executado ao mesmo tempo para o mesmo fato contábil (Pai/Filho) como por exemplo Folha de Pagamento, Documento de Entrada e etc, **aconselhamos** **a configuração com valor "E" para facilitar a conferencia dos registros.**

**Saiba Mais:**  
<https://tdn.totvs.com/display/public/PROT/CTB0085_Parametro_MV_ORDLCTB>
