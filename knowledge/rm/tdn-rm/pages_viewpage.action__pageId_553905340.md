---
content_hash: 70d81c152fd201acde9f6af07ec3876661ec37b24d8685b7e8e2d386ce37074d
fetched_at: '2026-06-29T00:10:45.969445+00:00'
page_id: '553905340'
product: rm
source: tdn-rm
title: Avanço físico afeta medição de contrato (App Minha obra)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553905340
version: 1
---

A partir do APP Minha Obra é possível criar/alterar medições de itens de contrato através dos apontamentos de Avanço Físico dos itens da Folha Tarefa, sendo via coletor ou apontamento manual. Para que essa incidência ocorra, é necessário vincular o contrato desejado ao item associado à folha tarefa, porém é necessário considerar algumas premissas:

* A tarefa deve ser definida antes do contrato;
* As datas início e fim do contrato devem fazer interseção com as datas início e fim da folha tarefa;
* A tarefa selecionada deve estar associada ao contrato;
* Ao salvar a associação do contrato ao item, caso o parâmetro de medição acima de 100% estiver diferente de SEMPRE PERMITIR, será verificado se a quantidade planejada do item da folha é maior que a quantidade do saldo do item no contrato, o que não deve ser permitido.

No processo de Validar Apontamento de Avanço Físico o parâmetro de medição acima de 100% também é verificado e se estiver diferente de SEMPRE PERMITIR, e a quantidade apontada do item da folha for maior que a quantidade do saldo do item nocontrato, um alerta será exibido, não permitindo a execução.

No processo de Atualizar PERT o parâmetro de medição acima de 100% também é verificado e se estiver diferente de SEMPRE PERMITIR, e a quantidade apontada do item da folha for maior que a quantidade do saldo do item no contrato, um alerta será exibido, não permitindo a execução. Caso as validações estejam aprovadas, a quantidade apontada do item será incorporada à medição do item no contrato, no respectivo período que corresponde à DATA DE APONTAMENTO do item da folha. Se o período do contrato estiver liberado, a medição não será inserida e o erro deverá ser exposto.

Na tela de medição de itens, nos períodos do contrato, é possível consultar os apontamentos que influenciaram na medição do item corrente, basta selecionar o item no grid e clicar no botão .
