---
content_hash: 7b9fc9c19949f12f17a9bdb2a70b102daad514a0e68a1f40add8b44adcc26fd7
fetched_at: '2026-06-29T00:11:05.916282+00:00'
page_id: '63275225'
product: rm
source: tdn-rm
title: MetaDados com Action Anexas
type: documentation
url: https://tdn.totvs.com/display/LRM/MetaDados+com+Action+Anexas
version: 1
---

Este documento tem por objetivo orientar o usuário utilizar uma Action em anexo a um projeto MetaDados.

Desenvolvimento/Procedimento

Para esse exemplo, criei uma tabela simples para a aplicação TOTVS Gestão Patrimonial, chamada ZM PATRIMONIO com  apenas com duas colunas(CODPAT,CODCOL):

Para esse exemplo simples, não criei relacionamento entre outras tabelas. Criei um Modelo de Negócios simples, chamado PATRIMONIO conforme abaixo:

No menu de Formulários, é configurado a forma com que o Projeto será apresentado e também onde é informado uma Action pra utilizada como Anexa ao projeto. Após criar a identificação do Formulário, clique na aba Action Anexas:

Nessa aba, para utilizar nesse exemplo adicionei a Action PatPatrimonioAction, referente ao menu de Funcionários do TOTVS Gestão Patrimonial. Para adicionar esse Action, clique no Botão Adicionar e busque o nome da Action desejada, nesse nosso exemplo PatPatrimonioAction. Feito esse procedimento, é necessário relacionar as colunas da tabela do Projeto com as chaves primárias da Action.

Feito esses procedimentos, basta criar e gerar o nosso Projeto. Após gerar o Projeto, basta acessá-lo na tela que foi disponibilizado. Incluir no Projeto os valores para código de patrimônio 1 e código de coligada 1, conforme abaixo.

Selecione o valor inserido e no Menu\Anexos selecione a Action Cadastro de Patrimônio

Feito esse procedimento, a partir dos parâmetros do Código do Patrimônio e Código da coligada, a Action irá trazer o mesmos resultado da tela de Cadastro de Patrimônio, do TOTVS Gestão Patrimonial:
