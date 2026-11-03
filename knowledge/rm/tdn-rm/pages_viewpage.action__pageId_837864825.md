---
content_hash: 77c2b1d8beee164774c2fe585f6b26e74fca3d934fc8a53392e334a6d7fd7bfc
fetched_at: '2026-06-29T00:11:49.743609+00:00'
page_id: '837864825'
product: rm
source: tdn-rm
title: 06.2 - Renovação da Recorrência na Rematrícula, após seleção do plano de pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=837864825
version: 19
---

---

A partir da versão **12.1.2406,** será possível fazer a renovação da recorrência aplicada ao contrato anterior para o próximo período letivo, através da rematrícula online.

Isso elimina a necessidade de acessar o extrato financeiro para reativar essa função.

Regras para Renovação da Recorrência

Antes de exibir a opção de renovar a recorrência para o usuário, alguns pontos devem ser validos e em caso positivo a opção de renovação exibida:

Para a exibição da opção da renovação da recorrência, alguns critérios devem ser seguidos:

* Para utilizar essa funcionalidade, é necessário que  o campo "**Período letivo anterior**" no cadastro de Período Letivo (**Currículo e Oferta | Períodos letivos**) esteja devidamente preenchido:
* Serviços do plano de pagamento selecionados, estão vinculados e com recorrências habilitada ao contrato anterior do aluno
* Se o usuário que habilitou a recorrência no(s) serviço(s) é o mesmo que esta realizando o processo de matricula. (A opção de renovar a recorrência na rematrícula deve ser restringir ao usuário que habilitou a recorrência no contrato/serviço 'anterior'. O usuário `dono da recorrência origem` deve ser o mesmo que esta realizando a rematrícula.)

Também deve ser mantidos os mesmos parâmetros da Recorrência :

* O pagamento automático deve estar habilitado (Educacional | Tesouraria | Geral 3/4)
* Os serviços vinculados as recorrências do contrato anterior devem continuar permitindo cadastrar recorrência.

Se uma recorrência estiver cadastrada para um ou mais serviços no período letivo anterior, e entre esses serviços estiver incluído algum serviço do plano de pagamento selecionado que não possui recorrência no período letivo atual, o sistema exibirá a seguinte mensagem ao usuário quando avançar para a etapa de seleção do plano de pagamento. Esta mensagem mostrará todos os serviços que tinham recorrência no período letivo anterior, mas que não possuem no período letivo atual, entre os serviços das parcelas do plano de pagamento selecionado

Caso o usuário opte por renovar a recorrência, ele deve acionar o botão "Sim" e selecionar pelo menos um serviço que deseja renovar. Ao finalizar a rematrícula, após o último passo, o sistema irá cadastrar uma recorrência para os serviços selecionados no contrato gerado ou atualizado na rematrícula online. Nesse processo, os mesmos cartões da carteira digital que estavam associados às recorrências no período letivo anterior serão mantidos.

Contrato criado após rematrícula com a renovação da recorrência.

Se o usuário retornar ao processo de rematrícula após ter concluído, para fazer ajustes ou seleção um novo plano de pagamento, a opção de renovação da recorrência deve ser exibida indicando apenas serviços que atendam aos critérios e que o usuário já não tenha habilitado para o contrato atual na primeira execução da rematrícula.
