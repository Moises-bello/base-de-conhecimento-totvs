---
content_hash: 942029dc7f6014dda246076424219163984a4c40bc64ff93cc5bc231262949ea
fetched_at: '2026-06-29T00:10:59.706566+00:00'
page_id: '615383222'
product: rm
source: tdn-rm
title: Regras Adicionais
type: documentation
url: https://tdn.totvs.com/display/LRM/Regras+Adicionais
version: 8
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Itens gerais**
3. **Obrigar Aceite Médico para Itens Liberados com Ressalva**
   1. **Obrigar Justificativa Médica para Itens Liberados com Ressalva**

Regras adicionaisVisão Geral

## **01. VISÃO GERAL**

Conteúdo de armazenamento para as regras que se aplicam dentro da prescrição médica.

Itens gerais

## **02.****ITENS GERAIS**

* **Observação padrão**  
  No RM, em Cadastros -> Prescrição médica -> Padrões de prescrição, em um determinado principio ativo, existe a opção de várias apresentações. Em cada apresentação, existe a possibilidade de se amarrar vários padrões de prescrição, que neste caso possuem relação com Via, Frequência e/ou Diluição. Em cada padrão de prescrição, existe a possibilidade de se vincular uma observação padrão, independente da via, frequência ou diluição. No PEP RM, ao selecionar um item que obedeça essas regras, a observação cadastrada no item será importada para o campo observação na tela de prescrição.
* **Itens restritos - Mat/Med - Tipo "Proibido"**  
  No RM, em cadastro das condições contratuais é possível inserir um tipo de restrição para um determinado item em determinado convênio, seja ele medicamentos, materiais ou outros. Neste momento, estamos considerando os itens proibidos por convênio. Ou seja, caso o usuário tente inserir um item que esteja cadastrado como proibido para o convênio do paciente, ele será informado e não conseguirá inserir o item.

* **Opções para prescrições como "se necessário" e "a critério médico"**

No prontuário, ao marcar o checkbox “Se necessário” ou “A critério médico” na modal de prescrição médica ou de especialidades, será exibida uma mensagem de alerta orientando o usuário a selecionar apenas uma dessas opções para o item:

Obrigar Aceite Médico para Itens Liberados com Ressalva

## **03. Obrigar Aceite Médico para Itens Liberados com Ressalva**

É possível obrigar o aceite do médico para itens **“Liberados com Ressalva”** pela farmácia clínica, acessando: **Cadastro →** **Unidade de Atendimento → Prontuário Eletrônico → Prescrição Médica → Parâmetro: Obrigar aceite médico para itens com “Liberado com Ressalva”.**

Com o parâmetro ativo, o médico responsável, ao realizar qualquer atualização na prescrição médica, ao tentar liberar um item cuja condição **“Ciente da Ressalva”** esteja disponível, indica que o item ainda não foi validado pelo médico, gerando a seguinte mensagem de erro:

Os itens ‘Liberados com Ressalva’ ficam o título em vermelho, facilitando a identificação para validação dos mesmos:

Ao acessar o item, se a opção **“Ciente da Revisão”** estiver disponível, significa que o item ainda não foi revisado. Ao clicar no botão, o item será atualizado e a mensagem de erro não será exibida novamente.

**Observação:** enquanto houver pelo menos um item aguardando revisão e o parâmetro estiver ativo, a mensagem de erro continuará sendo gerada.

## **03.01 Obrigar Justificativa Médica para Itens Liberados com Ressalva**

É possível obrigar uma justificativa para o aceite médico para itens **“Liberados com Ressalva”** pela farmácia clínica, acessando: **Cadastro →** **Unidade de Atendimento → Prontuário Eletrônico → Prescrição Médica → Parâmetro: Obrigar justificativa médica para itens “Liberado com Ressalva”.**

Com o parâmetro ativo, o médico responsável, ao tentar dar a **Ciência da Ressalva**, o sistema exigirá uma justificativa por escrito, bloqueando o botão de **'Ciente da Ressalva'**

O botão só ficará disponível caso no campo **Justificativa de uso para item liberado com ressalva**, seja escrito uma quantidade mínima de caracteres.

**OBS: O campo de Justificativa de uso para item liberado com ressalva é totalmente desvinculado das outras justificativas de uso dos itens.**
