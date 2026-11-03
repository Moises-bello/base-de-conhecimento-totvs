---
content_hash: 18b974995462fa66da70353dfaad6ab89becca7e5ea1f74fbd18a7491d699cc5
fetched_at: '2026-06-29T00:09:08.405148+00:00'
page_id: '388235415'
product: rm
source: tdn-rm
title: Salário Composto vinculado à Tabela Salarial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=388235415
version: 88
---

# Salário Composto

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Composição Salarial com uso da tabela salarial* |
| **Situação/Requisito:** | I) No modulo de cadastro do salário composto foi vinculado a tabela salarial do Vitae permitindo que o modulo de Alteração salarial busque o valor atual da tabela salarial para atualizar o salário do funcionário.  II) Permitir editar tabela salarial independente da tabela vinculada ao funcionário pela seção / função. Para isso os parâmetros: "Utiliza Tabelas Salariais para evento de Salário Composto" e "Edita Tabelas Salarias nos Eventos de Salário Composto" devem estar marcado. III) Incluído botão para permitir ao usuário a atualização imediata do salário sem a necessidade de acesso ao menu para alteração do salário. IV) O campo valor hora na composição salarial, quando integrado com o vitae e usa tabela salarial na composição do salário, seguirá o comportamento do parâmetro do Vitae "Permite alteração manual do salário". Quando marcado permitirá edição, quando desmarcado não será editável. Além das demais regras aplicado ao respectivo campo no cadastro do funcionário V) Os campos para definição do salarial composto de acordo com a tabela salarial fica disposto da seguinte forma: 1º Tabela salarial, precisa ser a primeira para poder definir o filtro de nível e faixa; 2º Nível; 3º Faixa. |
| **Solução/Implementação:** | **Para o item I)* No modulo de cadastro do salário composto foi vinculado a tabela salarial do Vitae permitindo que o modulo de Alteração salarial* *busque o valor atual da tabela salarial para atualizar o salário do funcionário*  *Para o item II) *Foi criado o parâmetro "Edita Tabelas Salarias nos Eventos de Salário Composto" em Folha de Pagamento / Funcionário / Restrições Cadastrais. Marcando este parâmetro será permitido selecionar tabelas salariais diferente da vinculada ao funcionário referente a sua função / seção. Observação: O parâmetro "*Utiliza Tabelas Salariais para evento de Salário Composto" deverá está marcado.***  ***Para o Item III) Ao clicar no botão  o valores serão atualizados de acordo com a tabela, nível e faixa. Este botão só será visível se os parâmetros **"*Utiliza Tabelas Salariais para evento de Salário Composto" e **"Edita Tabelas Salarias nos Eventos de Salário Composto" tiverem sido marcados e houve mudança de tabela, nível ou faixa. Clicar no botão OK ou Salvar também efetua o recálculo e os valores são atualizados..********  ********Para o item IV) Marcando o parâmetro do Vitae "Permite alteração manual do salário" o campo valor hora será habilitado para edição e seu valor alterado independente da Tabela Salarial Informado.********  ********Para o item V) A fim de poder filtrar o nível e faixa conforme a tabela salarial se fez necessário solicitar a tabela salarial antes do nível e da faixa.********  *Caso se trate de uma edição, o campo "Motivo Alteração" aparece e o registro só pode ser salvo após o preenchimento deste campo.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TSHEZW |
| **Requisito (ISSUE):** | FOPCALCULO01-4145 |

divs
