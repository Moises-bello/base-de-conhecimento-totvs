---
content_hash: 498035d2680218f9896f46b02ffc933136199ef820b27fbb7365d6efb339849a
fetched_at: '2026-06-29T00:09:29.297468+00:00'
page_id: '423938867'
product: rm
source: tdn-rm
title: Reajustar Preço de Produto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938867
version: 6
---

Através desse Processo é reajustado o preço dos registros selecionados.

**Preço:** Selecione quais dos preços encontrados em Produto | Preço sofrerá reajuste.

**Tipo de Reajuste:** Selecione por qual maneira o reajuste será executado. Fórmula, Percentual ou Valor.

**Aplicar:**

* Fórmula: Só estará disponível caso o Tipo de Reajuste seja Fórmula. Selecione a fórmula que será utilizada para o reajuste.
* Efeito: Só estará disponível caso o Tipo de Reajuste seja Percentual. Selecione se o Efeito será Acréscimo ou Decréscimo.
* Percentual: Defina qual será o Percentual de ajuste no preço.
* Valor: Caso o reajuste definido seja Valor, aparecerá esse campo.

**Arredondamento:** Só ficará disponível caso o reajuste seja por Percentual ou Fórmula.

* No primeiro campo define-se qual será o nível de Arredondamento: Não Arredonda, Centavos, Dezena, Centena.
* No campo **Limite** informe até quantas casas decimais deverão ser arredondadas.

Regra aplicada para cada nível de Arredondamento:

| Nível de Arredondamento | Regra |
| --- | --- |
| Não Arredonda | Não aplica arrendamento em centavos, dezena e centena. |
| Centavos | Se parte fracionária do valor \* 100 > limite, arredonda uma unidade acima. |
| Dezena | Se o resto da divisão inteira do valor por 10 >= limite, soma (10 – valor do resto); caso contrário diminui do valor do resto. |
| Centena | Se o resto da divisão inteira do valor por 100 >= limite, soma (100 – valor do resto); caso contrário diminui do valor do resto. |

**Motivo:** Explicite o motivo da alteração do preço.

Processo não disponível para produto de grade numerada (produto gerado a partir de um produto base para grade numerada).
