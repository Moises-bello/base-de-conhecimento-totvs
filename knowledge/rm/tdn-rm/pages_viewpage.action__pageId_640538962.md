---
content_hash: 8c07a1524709dbd8ae11329b2f0be21aa3f1eb3a3ebe205106e0d26c7e940efe
fetched_at: '2026-06-29T00:11:09.597930+00:00'
page_id: '640538962'
product: rm
source: tdn-rm
title: Reajustar Preços do Produto da Tabela de Preço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=640538962
version: 3
---

Através desse processo é reajustado o preço dos registros selecionados.

**Tipo de Reajuste:** Selecione por qual maneira o reajuste será executado. Fórmula, Percentual ou Valor.

**Aplicar:**

* Fórmula: Só estará disponível caso o Tipo de Reajuste seja Fórmula. Selecione a fórmula que será utilizada para o reajuste.
* Efeito: Só estará disponível caso o Tipo de Reajuste seja Percentual. Selecione se o Efeito será Acréscimo ou Decréscimo.
* Percentual: Defina qual será o Percentual de ajuste no preço.
* Valor: Caso o reajuste definido seja Valor, aparecerá esse campo.

**Arredondamento:** Só ficará disponível caso o reajuste seja por Percentual.

* No primeiro campo define-se qual será o nível de Arredondamento: Não Arredonda, Centavos, Dezena, Centena.
* No campo **Limite** informe até quantas casas decimais deverão ser arredondadas.

Regra aplicada para cada nível de Arredondamento:

| Nível de Arredondamento | Regra |
| --- | --- |
| Não Arredonda | Não aplica arrendamento em centavos, dezena e centena. |
| Centavos | Se parte fracionária do valor \* 100 > limite, arredonda uma unidade acima. |
| Dezena | Se o resto da divisão inteira do valor por 10 >= limite, soma (10 – valor do resto); caso contrário diminui do valor do resto. |
| Centena | Se o resto da divisão inteira do valor por 100 >= limite, soma (100 – valor do resto); caso contrário diminui do valor do resto. |

No término do cálculo do reajuste do preço será aplicado a quantidade de casas decimais definidas na pasta Preço do cadastro de . Caso o produto não possua esta configuração será aplicado o valor de casas decimais definido nos .
