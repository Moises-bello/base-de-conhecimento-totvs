---
content_hash: 1823e0cd6b586b5fbdb709e33a45d0696e73514e1be5133e0ff72b5e154330c7
fetched_at: '2026-06-29T00:10:43.940215+00:00'
page_id: '551433687'
product: rm
source: tdn-rm
title: 'Módulo: Educacional - SGE'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=551433687
version: 13
---

|  |  |
| --- | --- |
| Descrição | Novidades do Template por Módulo: Educacional |
| Observações | Aplicável para SESI/SENAI. |

---

# Módulo: Educacional

## LGPD Anonimização do Funcionário da Empresa Parceira

**Objetivo**

Possibilitar anonimizar o funcionário da empresa parceira que disponibiliza vagas de  estágio/emprego.

Para atender a Lei Nº 13.709/18 foi criado o processo "anonimizar funcionários“. Este processo irá verificar se o funcionário da empresa possui algum vínculo com vagas ou solicitações de funcionários em vagas de estágio. Se não possuir, o processo irá excluir o funcionário, mas caso este possua algum vínculo o sistema irá verificar algumas regras e se o funcionário for elegível para anonimizar o sistema irá alterar os campos permitidos e definidos para um valor fictício (ex: 000).

**Regras Para** **Anonimizar** **Funcionários**

O funcionário que não possuir vínculo com nenhum dos itens abaixo será excluído do sistema, mas caso possua, o sistema irá mascarar. Os vínculos são:

* Estar vinculado a uma termo de compromisso

    de estágio.

* Estar vinculado uma solicitação de estágio.

**Habilitação do Processo**

Para ter acesso ao processo é necessário que seja

concedida permissão ao item de menu no perfil

desejado:

**Processo**

O processo será executado com base na visão de funcionários da empresa, sendo necessário somente selecionar o(s) funcionário(s) que o sistema irá executar o processo:

O processo será executado em segundo plano e seu resultado poderá ser consultado no rodapé do TOTVS Educacional:

Log do Processo:

Dados do usuário anonimizado:

## Simplificação da Alteração do Contexto nos Módulos do Educacional

**Objetivo**

Nova tela para seleção dos contextos educacionais, mais simples e com a possibilidade de ordenar os contextos favoritos para visualização

Foram adicionados botões na tela de contexto que permite ao usuário mover os contextos favoritos para cima e para baixo, de forma a criar uma ordenação para visualização tanto na tela de contexto quando no menu cascata:

**Utilização**

O usuário terá duas possibilidades para movimentar o contexto na lista de favoritos, movendo uma posição por vez através dos botões     e   ou diretamente para a primeira/última posição da lista utilizando os botões   e     .

Os botões de ordenação só estarão disponíveis na visão que exibe a lista de contextos favoritos, na visão de últimos contextos acessados os botões não serão exibidos.

## Cadastro de Horários Possibilita 3 Dígitos

**Situação / Requisitos**

Ao criar um novo horário, o sistema permite no campo aula valores que vão de 01 até 99.

**Solução**

Foi alterado no cadastro de horário e no processo de geração de horário no turno, para que permita que o campo aula tenha até três dígitos, ou seja, de 001 até 999.
