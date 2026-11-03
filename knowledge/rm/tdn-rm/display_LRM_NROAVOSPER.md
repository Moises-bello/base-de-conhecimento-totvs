---
content_hash: bbf7ed87786b88ddd84de28aea52d879a94b6013cb80044b965fb46ba46f652a
fetched_at: '2026-06-29T00:10:30.302651+00:00'
page_id: '519716456'
product: rm
source: tdn-rm
title: NROAVOSPER
type: documentation
url: https://tdn.totvs.com/display/LRM/NROAVOSPER
version: 1
---

Criada a função NROAVOSPER.

Essa função retorna o número de avos do funcionário.

O usuário quem irá definir o mês de referência para a contagem dos avos.

**Exemplos:**

Fórmula NROAVOSPER(12).

Resultado 12.

Fórmula NROAVOSPER(11).

Resultado 11.  
   
**Observação:**  
Está variável também considera as faltas e os afastamentos do funcionário. Os tipos de afastamentos que estão sujeitos à redução de avos durante o afastamento no ano corrente são: **P** (Afast.Previdência), **L** (Licença s/venc ), **M** (Serv.Militar) e **U** (Outros). Os funcionários afastados por **T** (Af.Ac.Trabalho) só terão avos reduzidos caso o parâmetro "Meses de afastamentos por acidente de trabalho reduz avos de 13º" esteja marcado no Parametrizador l 13 Salario l Calculo.
