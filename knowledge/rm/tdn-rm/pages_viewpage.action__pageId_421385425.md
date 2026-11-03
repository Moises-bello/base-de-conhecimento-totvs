---
content_hash: c24989ddeaf793ef1cfea5abbf73eca60f0dd2635dbe019f5943c0cb239f5ac5
fetched_at: '2026-06-29T00:09:15.600830+00:00'
page_id: '421385425'
product: rm
source: tdn-rm
title: Insumos (F6)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385425
version: 6
---

## **Opções de Arredondamento para insumos não fracionáveis:**

##### Marque a opção que indica a forma de arredondamento das quantidades dos insumos que não podem ser fracionados.

As opções disponíveis são: Para cima: Nesse caso, a quantidade do insumo será arredondada para o primeiro número inteiro maior que a quantidade informada.

Mais próximo: Nesse caso a quantidade do insumo será arredondada para o primeiro número inteiro mais próximo da quantidade informada.

Baixo: Nesse caso, a quantidade do insumo será arredondada para o primeiro número inteiro menor que a quantidade informada.

**Exemplos:**

Arredondar sempre para cima (default)

Para a quantidade de insumo 1,00000001, se o insumo não puder ser fracionado e a opção "Arredondar sempre para cima", a quantidade é arredondada para 2.

Para a quantidade de insumo 1,50000000, se o insumo não puder ser fracionado e a opção "Arredondar sempre para cima", a quantidade é arredondada para 2.

Para a quantidade de insumo 1,99999999, se o insumo não puder ser fracionado e a opção "Arredondar sempre para cima", a quantidade é arredondada para 2.

Arredondar para o inteiro mais próximo

Para a quantidade de insumo 1,00000001, se o insumo não puder ser fracionado e a opção "Arredondar para o inteiro mais próximo", a quantidade é arredondada para 1.

Para a quantidade de insumo 1,49999999, se o insumo não puder ser fracionado e a opção "Arredondar para o inteiro mais próximo", a quantidade é arredondada para 1.

Para a quantidade de insumo 1,50000000, se o insumo não puder ser fracionado e a opção "Arredondar para o inteiro mais próximo", a quantidade é arredondada para 2.

Para a quantidade de insumo 1,99999999, se o insumo não puder ser fracionado e a opção "Arredondar para o inteiro mais próximo", a quantidade é arredondada para 2.

Arredondar sempre para baixo

Para a quantidade de insumo 1,00000001, se o insumo não puder ser fracionado e a opção "Arredondar sempre para baixo", a quantidade é arredondada para 1.

Para a quantidade de insumo 1,50000000, se o insumo não puder ser fracionado e a opção "Arredondar sempre para cima", a quantidade é arredondada para 1.

Para a quantidade de insumo 1,99999999, se o insumo não puder ser fracionado e a opção "Arredondar sempre para cima", a quantidade é arredondada para 1.

## Opções de **Equalização de Insumo Por Projeto ou Por Obra**.

* Por Projeto, os campos informativos da Equalização consideram o total do Projeto.

* Por Obra, os campos informativos levam em consideração o total por Obra.

Habilitando a opção **calcular equalização Automaticamente**, qualquer alteração referente ao recurso, tanto na atividade associada quanto ao cadastro do mesmo, ao selecioná-lo automaticamente a Equalização será calculada.

## Opções de  Vínculo: Insumo x Produto

Este parâmetro define como os produtos podem ser vinculados aos insumos.

---

### Opção 1: Produto só pode estar vinculado a um insumo

* Um produto pode ser associado a **somente um insumo**;
* Não é permitido reutilizar o mesmo produto em outros insumos, independentemente de ser principal ou não.

**Observação:**

* Ao tentar vincular um produto que já esteja associado a outro insumo:
  + A ação será **bloqueada**;
  + Será necessário remover o vínculo existente antes de realizar um novo.

---

### Opção 2: Produto pode estar vinculado a mais de um insumo, desde que não seja o principal em outro insumo

Permite que um produto seja utilizado em múltiplos insumos, com restrição para definição como principal.

**Observação:**

* Um produto pode ser vinculado a **vários insumos**;
* O produto pode ser definido como **principal em apenas um insumo**;
* Não é permitido que o produto seja principal em mais de um insumo simultaneamente.
