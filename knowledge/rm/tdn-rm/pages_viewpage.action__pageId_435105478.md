---
content_hash: 1752480c5b1060f20887c6bd3a9c57654cbdf2de6b91281c45206867d1b26ae6
fetched_at: '2026-06-29T00:09:50.289462+00:00'
page_id: '435105478'
product: rm
source: tdn-rm
title: Parâmetros - Integração Financeira - Bloqueio de Lançamento na Venda
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105478
version: 6
---

* **Executar processos de geração. exclusão e efetivação do plano em background (Venda, aditivo e distrato):** Marque esta opção para habilitar a execução dos processos relativos ao plano de financiamento (geração, efetivação, exclusão do plano de financiamento) em segundo plano, permitindo que o usuário utilize outros cadastros/telas do TCGI durante a execução dos mesmos. Caso esta opção esteja desmarcada, o sistema somente liberará a tela para o usuário ao término de execução de um destes processos;
* **Calcular o saldo devedor do seguro prestamista com deságio:** Marque esta opção para que o sistema, quando utilizando a modalidade de venda PRICE, calcule o deságio do saldo devedor do seguro prestamista, quando este compor o saldo da venda;
* **Bloqueio de lançamento venda:** Nesse parâmetro é possível definir como deve ser realizado o bloqueio de um lançamento na venda, possui as seguintes opções:
  + **Bloqueado:** Ao selecionar esta opção os lançamentos gerados na venda são irão compor nenhum relatório do módulo financeiro; ou
  + **Provisionado:** Ao selecionar esta opção os lançamentos gerados na venda serão considerados como provisionados e irão compor os relatórios do módulo financeiro.
* **Alteração Financeira com uso de Data Base:** Ao marcar esse parâmetro o sistema irá bloquear as alterações de dados financeiros e baixas, quando estiver usando Data Base e o mês competência da alteração for diferente do mês de competência do reajuste.

[Voltar](http://tdn.totvs.com/pages/viewpage.action?pageId=435104757)

Veja Também

---
