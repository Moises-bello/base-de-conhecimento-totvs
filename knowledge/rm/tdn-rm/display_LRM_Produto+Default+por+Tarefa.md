---
content_hash: bda9791fff5ad8491c303e57b3817196d9e3d64a8cfb45816cb9a89226bd3bc5
fetched_at: '2026-06-29T00:12:16.372719+00:00'
page_id: '985681086'
product: rm
source: tdn-rm
title: Produto Default por Tarefa
type: documentation
url: https://tdn.totvs.com/display/LRM/Produto+Default+por+Tarefa
version: 5
---

Este anexo possibilita informar um produto default para cada tarefa associada ao contrato, assim; sempre que efetuar uma medição para uma tarefa, o produto informado será usado na geração do movimento na integração com o suprimentos:

A relação tarefa/produto se aplica tanto a contrato de serviço quanto de insumo.

No **contrato de serviço**, a ordem de utilização do produto para geração do movimento é:

1) Rateio de Produto específico (cadastrado diretamente na medição do item no período);

2) Rateio por Produto Default (cadastrado na associação do item ao contrato);

3) Anexo de Produto Default por Tarefa (será usado quando não houver nenhum dos dois informados anteriormente);

4) Na aba default do cadastro do contrato;

5) Caso nenhum dos campos acima estejam preenchidos, será usado o produto informado na geração do movimento.

No caso do **contrato de insumo**, essa definição está subordinada ao parâmetro de projeto que define o produto da liberação, pois este parâmetro que determinará o produto que será utilizado na geração do movimento: **Associado** ao insumo, ou **Default** cadastrado no contrato ou por tarefa:

A ordem de utilização do produto default para o contrato de insumo é: primeiro produto cadastrado para a tarefa em questão no respectivo anexo de Produto Default por Tarefa e; se não tiver para uma tarefa em questão, o produto default do contrato será utilizado.
