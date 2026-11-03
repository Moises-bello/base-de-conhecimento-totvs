---
content_hash: cdd4a7a5ebdd747f719753cbc7dc6c7f1d06397d9c751e43f3368fd047bc603a
fetched_at: '2026-06-29T00:06:00.122686+00:00'
page_id: '192104311'
product: rm
source: tdn-rm
title: ER_Melhorias_CIPA
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Melhorias_CIPA
version: 9
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Segurança e Saúde Ocupacional | **Módulo** | SSO |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** |  | **IRM1** |  |
| **Requisito1** |  | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** |  |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 O objetivo deste documento é descrever melhorias que serão desenvolvidas nas funcionalidades relacionadas a Comissões CIPA.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Cadastro de Comissões da CIPA | Alteração | Cadastros > CIPA > Comissões da CIPA | - |
| Cadastro de Candidatos de Eleições CIPA | Alteração | Cadastros > CIPA > Comissões da CIPA > Candidatos | - |
| Cadastro de Representantes da CIPA | Alteração | Cadastros > CIPA > Comissões da CIPA > Representantes | - |
| Portal | Alteração | Portal > CIPA > Candidatar | - |
| Portal | Alteração | Portal > CIPA > Votar | - |
| Scripts de atualização | Criação | - | - |

**Req. 1 – Cadastro de Comissões da CIPA**

Seções

O Cadastro de Comissões da CIPA será alterado para permitir que seja possível vincular quantas seções sejam desejadas, desde que sejam da filial informada no momento do cadastro. As seções serão informadas num *lookup multirecords* que só estará disponível se a Filial for informada. Se o usuário trocar a filial, todas as seções que tenham sido informadas deverão ser removidas.

 Só será permitido fazer a vinculação de seções no momento da criação de uma Comissão da CIPA. Após ser salva, as seções serão apenas para visualização. Assim como já acontece hoje, só poderão ser vinculadas seções "folha".

Tipos de Funcionários

Atualmente, nas Comissões da CIPA, funcionários com situação “E” – Estatutário – não podem participar de eleições, seja votando ou candidatando-se. Será feita uma melhoria no cadastro de Comissões da CIPA para incluir a possibilidade de informar Tipos de Funcionários que poderão participar de uma eleição CIPA. A validação do Tipo de Funcionário, que hoje é fixa, deverá ser ajustada para respeitar os Tipos definidos no cadastro da comissão. Esses tipos serão incluídos num *lookup multirecords* que será incluído no cadastro da comissão da CIPA.

**Req. 2 – Eleições CIPA**

O cadastro de candidatos eleições da CIPA permite que sejam incluídos apenas funcionários da seção que foi informada no Cadastro da Comissão da CIPA, se houver. A partir do momento que várias seções podem ser vinculadas à Comissão, funcionários de todas essas seções poderão ser incluídos como candidatos.

A inclusão de candidatos deverá permitir que sejam vinculados apenas funcionários dos tipos estabelecidos no cadastro da comissão.

Na apuração do resultado de eleições de CIPA, devem ser considerados para o cálculo os funcionários das seções e dos tipos definidos no cadastro da comissão.

**Req. 3**–**Representantes**

A inclusão de representantes da CIPA, seja como representante do Empregado ou do Empregador, deverá permitir que sejam vinculados apenas funcionários dos tipos estabelecidos no cadastro da comissão.

Quando são incluídos representantes dos empregados, deve ser indicado um candidato participante da eleição da CIPA. Consequentemente ele deverá pertencer a uma seção informada no cadastro da Comissão, pois isso é necessário para que ele tenha entrado na eleição. A regra, que é persistida no momento da indicação do candidato, deverá ser estendida para ser contemplada na indicação de representante dos empregados.

**Req. 4 – Portal**

Votação e candidatura

Nas opções de Votação e Candidatura do Portal, o usuário só visualiza opções que permitam que ele interaja.

Caso a Comissão da CIPA tenha em seu cadastro o vínculo com uma ou mais seções, o funcionário logado só poderá votar ou se candidatar na eleição dessa comissão se ele pertencer a uma das seções vinculadas. Além disso deverá ser um Tipo de Funcionário contemplado entre os tipos permitidos, de acordo com o cadastro da comissão.

Refazer candidatura

Atualmente o sistema não permite que um funcionário que se candidatou a uma eleição da CIPA pelo Portal e em seguida cancelou sua candidatura, possa novamente se candidatar.

Esta regra deverá ser revista para permitir uma nova candidatura. Isso será feito apagando a data de cancelamento, o que fará com que a candidatura volte a ficar ativa.

Não haverá histórico de candidaturas e cancelamentos.

**Req. 5 – Atualização do legado**

A criação de tabelas para permitir a vinculação de várias seções e vários tipos de funcionários relacionados a comissões da CIPA exige que seja elaborado um script para atualizar os dados já existentes na base de dados dos clientes.

Para o caso das seções, deverá ser disponibilizado um script que inclua, para todas as comissões que possuam o “CODSECAO” preenchido, uma linha na nova tabela informando a seção da comissão. O campo CODSECAO, bem como os valores existentes, não serão removidos da tabela original. Porém esse campo deixará de ser utilizado pelo sistema.

Para o caso do tipo de funcionário, deverá ser disponibilizado um script que inclua, para todas as comissões, registros para todos os tipos de funcionários existentes, exceto o tipo “E” – Estatutário.

**Restrições**

- Não está incluído neste escopo a atualização de relatórios que utilizam o campo CODSECAO, que deixará de ser utilizado pelo sistema.

- Como a vinculação de seções e tipos de funcionários é feita apenas na criação de comissões da CIPA, não será possível editar os dados das comissões já existentes na base de dados. Apenas os novos registros terão esse recurso disponível.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
