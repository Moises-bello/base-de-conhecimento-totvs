---
content_hash: 870937a16dfad6e99166120844817a653298129d4908ab7870172b9a48c263c6
fetched_at: '2026-06-29T00:12:16.509597+00:00'
page_id: '990772617'
product: rm
source: tdn-rm
title: Aluguel em Dobro - CTO Dobrado e Fundo Promocional Percentual.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=990772617
version: 2
---

### Resumo da Regra de Cálculo

Quando há **fundo percentual (FPP)** parametrizado para **dobrar em determinada competência**, o sistema vai se valer das regras:

* **O percentual do fundo (FPP)** deve ser aplicado sobre o **CTO em dobro**,
* **Sem a dedução do condomínio ou o próprio FPP**.
* Ou seja, o sistema deve recalcular o fundo diretamente sobre o CTO dobrado.

### Exemplo

* **CTO Mínimo** = 50.000,00
* **Aluguel dobrado** = 44.642,86 (50.000 ÷ 1,12)
* **FPP dobrado 12%** = 5.357,14
* **CTO dobrado** = 50.000,00

---

Em resumo: **em vez de dobrar o percentual sobre o CTO líquido (após deduções), o sistema deve calcular o FPP diretamente sobre o CTO dobrado, garantindo que o fundo incida novamente sobre o valor cheio.**
