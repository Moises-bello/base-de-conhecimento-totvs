---
content_hash: 6d3e67b051ecd7f1bfc54a5c85df005e5e9e894eab07abe810271dec5a8b7d49
fetched_at: '2026-06-29T00:10:30.510006+00:00'
page_id: '520101874'
product: rm
source: tdn-rm
title: Folha analítica e GPS - Incidência Exclusiva do segurado e Incidência Exclusiva
  do Empregador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520101874
version: 7
---

false

**A partir das Versões:**

* 12.1.24.234
* 12.1.25.168
* 12.1.26.117

# Objetivo:

---

Apresentar os tratamentos que foram realizados na GPS e Folha analítica para as novas incidências (**Incidência exclusiva do segurado** e **Incidência exclusiva do empregador**) no cadastro de eventos.

---

11Cadastro dos eventosCadastro dos eventos

Segue abaixo parametrização realizada no cadastro de eventos para realização do teste:

* Evento T001 - PROV - EXC. SEGURADO : provento do tipo valor, com a Incidência exclusiva do segurado marcada.

* Evento T002 - PROV - EXC. EMPREGADOR : provento do tipo valor, com a Incidência exclusiva do empregador marcada.

* Evento T003 - DESC - EXC SEGURADO : desconto do tipo valor, com a Incidência exclusiva do segurado marcada.

* Evento T004 - DESC - EXC EMPREGADOR : desconto do tipo valor, com a Incidência exclusiva do empregador marcada.

**Observação:**Para a liberação do campo "**Incidência exclusiva do segurado"** na versão 12.1.24 é necessário executar o Script Oracle(ESOCIALFOP01-10695.ORA) ou SQL server (ESOCIALFOP01-10695.SQL) de acordo com seu banco de dados. Disponível na central de downloads.

true1Geração dos relatórios Geração dos relatórios 

No envelope de pagamento foi lançado os eventos criados anteriormente (aba "Cadastro de Eventos") com os seguintes valores:

* Na aba Incidências o sistema está considerando o valor dos eventos que tem incidência de **INSS** + **Incidência exclusiva do segurado =** 3.333,33 (HORAS NORMAIS) + 2.000,00 (PROV - EXC. SEGURADO) - 100,00 (DESC- EXC. SEGURADO)= 5.233,33

* Ao gerar a GPS, o sistema irá considerar como **Base de INSS** o valor dos eventos que tem incidência de **INSS** + **Incidência exclusiva do empregador=** 3.333,33 (HORAS NORMAIS) + 3.000,00 (PROV - EXC. EMPREGADOR) - 200,00 (DESC- EXC. EMPREGADOR) = 6.133,33

* Na Folha analítica criamos um novo campo (**Base INSS - Envelope**) e adaptamos o calculo do campo **Base INSS** que passou a ser chamado de **Base INSS - GPS**.

Segue abaixo exemplo do relatório gerado para o envelope demonstrado acima:

* **Base INSS - GPS**: o sistema considerou o valor dos eventos que tem incidência de **INSS** + **Incidência exclusiva do empregador=** 3.333,33 (HORAS NORMAIS) + 3.000,00 (PROV - EXC. EMPREGADOR) - 200,00 (DESC- EXC. EMPREGADOR)= 6.133,33.
* **Base INSS - Envelope**:  o sistema considerou o valor dos eventos que tem incidência de **INSS** + **Incidência exclusiva do segurado =** 3.333,33 (HORAS NORMAIS) + 2.000,00 (PROV - EXC. SEGURADO) - 100,00 (DESC- EXC. SEGURADO)= 5.233,33.
