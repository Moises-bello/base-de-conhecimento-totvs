---
content_hash: ccbf3508a247d3c1a9584edeffc7a45a03140ddfa1af50e7a1fb634de5a1b5d5
fetched_at: '2026-06-29T00:09:46.039832+00:00'
page_id: '435104761'
product: rm
source: tdn-rm
title: Parâmetros - Contrato - Tabela de Preço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104761
version: 6
---

**Etapa 1 - Tabela de Preço**

* **Utiliza múltiplas tabelas de preço na venda por subunidade:** Quando marcado o sistema permite a inclusão e efetivação de mais de uma tabela de preço em situação "Efetivada" no mesmo período para o mesmo empreendimento, para a mesma unidade e as mesmas subunidades. Porém cada subunidade poderá ter apenas uma tabela de preço do tipo "Padrão" e uma ou mais tabelas de preço do tipo "Secundária" em situação "Efetivada". Assim poderá ser selecionada na venda qualquer tabela de preço "Efetivada", associada a uma subunidade. Ao desmarcar o parâmetro, só será permitido pelo sistema, a efetivação de uma tabela de preço por período, para o mesmo empreendimento, para a mesma unidade e as mesmas subunidades. E o sistema irá permitir na venda somente a tabela do tipo "Padrão".
* **Valor do item da venda:** Permite determinar se o valor da subunidade da venda poderá ou não ser alterado em relação a tabela de preço informada;
  + Edita: O campo "Valor" do item de contrato da venda fica habilitado, dessa forma será permitido a edição do valor da subunidade pelo usuário;
  + Mostra: O campo "Valor" do item de contrato da venda fica desabilitado, dessa forma não permitindo a edição do valor da subunidade pelo usuário.
* **Valor do item da venda no aditivo:**
  + Edita: O campo "Valor" do item de contrato da venda fica habilitado para edição ao incluir um aditivo;
  + Mostra: O campo "Valor" do item de contrato da venda fica desabilitado para edição ao incluir um aditivo.
* **Filtrar somente subunidade da tabela de preço:** Este parâmetro faz com que o sistema retorne somente as subunidades que estejam na tabela de preços informada ao gerar um Contrato de Venda se estiver, selecionado. Do contrário trará todas as subunidades da unidade informada no contrato de Venda.

**Etapa 2 - Tabela de Preço**

* **Bloquear edição de preço de tabela de preço efetivada:** Esta parâmetro indica para o sistema que a edição de preço manual deve ser bloqueada mesmo após a efetivação da tabela de preço para o tipo "Secundária" quanto para o tipo "Padrão".
* **Validar vigência tabela de preço:** Ao efetivar uma tabela de preço ou venda, valida se a venda possui a data de venda maior que data final de vigência da tabela de preço associada ao item da venda, não permitindo efetivar a nova tabela de preço ou venda com data de vigência inconsistente.
