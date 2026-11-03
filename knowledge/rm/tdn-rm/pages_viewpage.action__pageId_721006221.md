---
content_hash: 24c1f738939bf377d318063ab4445d1a7547e552a8c791c704b953126a15cb6e
fetched_at: '2026-06-29T00:11:26.850691+00:00'
page_id: '721006221'
product: rm
source: tdn-rm
title: Processo Conciliar/Desconciliar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=721006221
version: 5
---

**Conciliar**

O botão é habilitado quando selecionados registros **não** Conciliados e que tenha partidas do tipo Débito e Crédito **por conta contábil e** **coligada**.

O processo irar conciliar todas as partidas do lançamento que contém a conta contábil selecionada.

---

**Desconciliar**

O botão é habilitado quando selecionado **um ou mais** registros Conciliados.

O processo irá desconciliar todas os registros **por coligada** que foram conciliadas no mesmo processo de Conciliação, ou seja, possuem o mesmo identificador. Dessa forma, a utilização fica mais simples, uma vez que não será necessário selecionar cada um dos registros.

Versões de mercado

Como a Conciliação Contábil foi disponibilizada nas versões de mercado a partir dos patches 12.1.34.178 e 12.1.2205.116, os lançamentos que foram conciliados nessa versão receberam o mesmo número identificador.  
Sendo assim, caso migre para a versão atual, para estes lançamentos, ao selecionar algum e rodar o processo de Desconciliar, todos esses lançamentos de mesmo identificador serão desconciliados juntos.

---

### Regras

Não será permitido fazer a **Conciliação** quando:

* nenhum registro for selecionado
* os registros selecionados não possuírem o mesmo estado de conciliação
* Não for selecionado pelo menos uma partida de cada tipo, Débito e Crédito **por conta contábil e coligada** (mesmo que tenha diferenças Débito X Crédito)

Será permitido fazer a **Conciliação com Diferença** quando:

* Existirem registros do tipo Débito e Crédito selecionados **por conta contábil e coligada**, independente da diferença de Débito X Crédito **por conta contábil e coligada.**  
  Neste caso, será exibido um alerta informando detalhes da diferença **por conta contábil e coligada**, caso queira conciliar será necessário uma confirmação para fazer a **Conciliação.**

  Visualização da tela
