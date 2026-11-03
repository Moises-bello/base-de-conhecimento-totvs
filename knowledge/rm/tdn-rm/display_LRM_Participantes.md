---
content_hash: e551c4ed391ebf6721ed4f978addf3cf149c19f47d312687e68bdd678eb036ab
fetched_at: '2026-06-29T00:09:29.081150+00:00'
page_id: '423938801'
product: rm
source: tdn-rm
title: Participantes
type: documentation
url: https://tdn.totvs.com/display/LRM/Participantes
version: 6
---

**O que é cadastro de Participante?**

É um conjunto de informações para identificar as pessoas físicas e jurídicas com as quais a empresa tenha alguns tipos específicos de relacionamentos. Somente devem ser cadastrados como Participantes, os clientes/fornecedores ou filiais com os quais a empresa tenha um dos relacionamentos definidos na tabela anexa ao Ato Declaratório Cofis nº 36/07. Uma vez cadastrados os Participantes, todos os lançamentos contábeis resultantes de transações efetuadas que se enquadrem em algum destes relacionamentos e estiverem dentro do período definido para o relacionamento deverão ter o campo participante devidamente identificado. As informações destes lançamentos, assim como a relação dos Participantes cadastrados serão enviadas para o SPED Contábil.   
Neste cadastro você deve informar o participante (filial ou cliente/fornecedor), seu tipo de relacionamento com a empresa, o período válido para o relacionamento e os processos a serem executados nos sistemas que já migraram para o novo modelo de BackOffice (nova plataforma .NET) para os quais o relacionamento com este participante será válido.

*Atenção!*  
Os novos recursos do cadastro de Participantes abaixo estão disponíveis somente para clientes que já converteram suas bases de dados para o Novo Modelo do BackOffice.

Todo cadastro de participante terá um Status. No momento da inclusão ou alteração de um participante, este receberá o status 'Atualização Pendente'. Ao rodar o processo de Atualização do Participante nos Lançamentos Contábeis este status passará para 'Atualizado'.

**Importante**: O processo de geração do SPED Contábil somente será executado se o status de todos os Participantes cadastrados na base estiver igual à 'Atualizado'.  
A exclusão de um Participante somente poderá ser realizada se ele não estiver associado a nenhuma partida. Caso seja necessário excluir algum cadastro de Participante que esteja associado a alguma partida, execute primeiramente o processo 'Remover vínculo do Participante com o Lançamento Contábil'. Após a remoção do vínculo, o Participante poderá ser excluído.

**Observações:**

* As contabilizações geradas automaticamente por transações realizadas nos sistemas que já migraram para o novo modelo de BackOffice (nova plataforma .NET) terão o campo Participante preenchido automaticamente em suas partidas conforme o cadastro e processos válidos e período de relacionamento para o Participante aqui definido. Para verificar exemplos clique aqui.
* Caso seja necessário acrescentar ou alterar alguma informação já definida no cadastro do Participante, será necessário executar o processo de Atualização do Participante nos Lançamentos Contábeis para que os vínculos com os lançamentos sejam atualizados.

Veja Também


* Remover Vínculo do Participante com o Lançamento Contábil
