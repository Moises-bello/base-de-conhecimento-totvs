---
content_hash: 575645ca6cd4f4c2e85f4f28836c300b25c9397f7b878f2a336250c90f368388
fetched_at: '2026-06-29T00:11:36.470295+00:00'
page_id: '772805562'
product: rm
source: tdn-rm
title: Parâmetros Locais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=772805562
version: 17
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Informações Complementares**
4. **Tela Parâmetros Locais**
   1. **Outras Ações / Ações relacionadas**
5. **Tela Parâmetros Locais**
   1. **Principais Campos e Parâmetros**
6. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Este recurso deverá ser utilizado quando tem vários usuários acessando a mesma coligada no processamento das rotinas da Folha de Pagamento e necessitam trabalhar em períodos, mês e/ou ano caixa diferentes dos demais usuários. Assim, os usuários trabalharão integrados dentro de uma mesma competência, porém necessitando processar rotinas do módulo TOTVS Folha de Pagamento em períodos diferentes e até em caixas diferentes, conforme à necessidades específicas de cada um.

Desta forma os Parâmetros Locais deverão ser acionados em Configurações | Parâmetros | Locais,  no qual o usuário, localmente, poderá definir um mês/ano caixa, um período e/ou um dia de pagamento diferentes dos informados em Configurações | Parâmetros | Parametrizador | 06.01 - Folha de Pagamento | 06.01.01 - Configurações de Competência.

## **02. EXEMPLO DE UTILIZAÇÃO**

Em configurações de competência está com as informações abaixo:

* Usuário 00001 responsável em processar rescisão no período 01, caixa 03.
* Usuário 00002 responsável em processar férias no período 02.
* Usuário 00003 responsável em processar o pagamento mensal no período 03, caixa 04, pagamento dia 05.

Como o usuário 00001 irá processar a rescisão no período e caixa informados na configuração de competência, não será necessário informar nos parâmetros Locais.

O usuário 00002 irá processar as férias e nos parâmetros locais irá informar período 02 e clicar em 'OK' e confirmar a alteração clicando em 'Sim':

  Após a alteração e recarregar o módulo, as informações serão exibidas no rodapé e nas informações do sistema:

E o usuário 00003, irá processar o pagamento mensal e nos parâmetros locais irá informar período 03, mês 04 e dia pagamento 05 e clicar em 'OK' e confirmar a alteração clicando em 'Sim':

Após a alteração e recarregar o módulo, as informações serão exibidas no rodapé e nas informações do sistema:

Observação

Quando é acionado os parâmetros locais é armazenado na tabela GUSRPAR incluindo no campo PREFERENCIAS as informações referente ao parâmetros locais do usuário. São armazenados os campos Dia de pagamento Local, Período local, Ano caixa local, Mês caixa local e o indicativo que está usando parâmetros locais:

Estas informações não são armazenadas para os usuários que não acionam os parâmetros locais.

## **03. INFORMAÇÕES COMPLEMENTARES**

* Quando é informado um mês caixa local diferente do informado na competência global é retornado uma mensagem relacionado ao caixa do cálculo de IRRF.
* O sistema apenas dá acesso aos campos relativos a Caixa (Ano e Mês), Período e Dia do Pagamento.
* As informações de mês/ano competência, mês caixa e período podem ser visualizadas no rodapé do sistema.
* Caso usuário esteja com parâmetros locais ativado e altere as informações nas configurações de competência, as mesmas não serão alteradas para este usuário.
* Uma vez confirmados, se o sistema for reiniciado e logado com o mesmo usuário, os parâmetros locais permanecerão ativados. Para desativá-los, deve-se clicar no botão **Valores Default.**
* Ao clicar em valores default, as preferências de usuários não são apagadas, mas o indicativo de que o usuário está usando parâmetros locais é alterado para falso.

## **04. TELA PARÂMETROS LOCAIS**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Valores Default | Clicando neste botão irá carregar os valores informados na configuração de competência do parametrizador e o campo indicativo que o usuário está usando parâmetros locais irá alterar para falso caso clicado em 'OK' e em seguida em 'Sim'. |
| OK | Fazendo alguma alteração das informações no cadastro de Parâmetros locais, ao clicar em OK retornará uma mensagem informativa aguardando a afirmação do usuário para inserir/atualizar as preferências de usuário. |
| Cancelar | Não será inserido/atualizado as preferências de usuário e a tela fechará. |
| Sim | Irá atualizar/inserir as informações dos parâmetros locais no campo PREFERENCIAS na tabela  GUSRPAR. |
| Não | Os parâmetros locais não serão inseridos/atualizados e retornará uma mensagem para o usuário. |

## **05. TELA PARÂMETROS LOCAIS**

****Principais Campos e Parâmetros****

| Agrupador | Campo | Descrição |
| --- | --- | --- |
| Competência | Ano | Campo que retorna o Ano da Competência atual da base. Este campo é somente de leitura sendo alterado somente através do processo de Liberação de Competência. |
| Mês | Campo que retorna o Mês da Competência atual da base. Este campo é somente de leitura sendo alterado somente através do processo de Liberação de Competência |
| Caixa | Ano | Campo que retorna o Ano Caixa. Este campo só aceita o mesmo valor do Ano Competência quando o mês competência for entre 01 e 11 (Janeiro a Novembro) e no caso do mês da competência 12 (Dezembro), poderá informar o ano subsequente caso o mês caixa seja 01 (Janeiro). |
| Mês | Campo que retorna o Mês Caixa. Este campo só aceita os valores entre 1 a 12, sendo que o mesmo deve ser igual ao mês competência atual da base ou o mês subsequente. No caso de Mês competência 12 (Dezembro), só aceito mês caixa 01 (Janeiro) se o ano caixa também for o subsequente ao ano da competência. |
| Período | Nrº Período | Campo onde dever ser informado o período que será executados os processos. O mesmo deve ser maior que 0. |
| Dia do Pagamento | O dia do pagamento deve ser informado conforme o mês caixa. Por exemplo: se for mês caixa 03 - Março é validado entre 01 a 31 ou então, se for mês caixa 04 - Abril é validado entre 01 a 30. |

## **06. TABELAS UTILIZADAS**

* GUSRPAR
