---
content_hash: cfdff9768adf0ec14b0bde293a18c0498bb87b1d856822d507f3956253be420d
fetched_at: '2026-06-29T00:08:50.211312+00:00'
page_id: '331869442'
product: rm
source: tdn-rm
title: RMCTB00001_Cadastro do Histórico Padrão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=331869442
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Contábil |
| **Versões:** | 12.1.18 |
| Ocorrência: | **Cadastro de Histórico Padrão** |
| **Ambiente:** | Novo Modelo BackOffice |
| **Passo a passo:** | **Definição do Processo:**  O cadastro de Históricos Padrões tem como finalidade a utilização de expressões iguais para o registro de fatos semelhantes, simplificando a inclusão dos lançamentos contábeis.  Estes históricos podem conter em suas descrições apenas um texto ou a combinação de textos mais variáveis.  **Atenção:**  Nos parâmetros do sistema (Ambiente / Parâmetros / Totvs Gestão Contábil / Lançamentos / Histórico Padrão / Tipo de Código de Histórico Padrão), deve-se definir o tipo de código a ser utilizado no cadastro dos Históricos Padrões, indicando quais caracteres poderão ser utilizados para os códigos, sendo eles: Qualquer caracter, Apenas Letra ou Apenas Número.    **DESENVOLVIMENTO/PROCEDIMENTO:**  1- Para inclusão do Histórico Padrão ir em: Cadastros / Históricos Padrões / informe o Código e a Descrição que desejar:      Após cadastrar o histórico padrão, na inclusão das partidas, no campo Histórico, informe o código do histórico desejado que o sistema carrega automaticamente sua descrição:      2- Para otimizar ainda mais a inclusão das partidas dos lançamentos, na Descrição do histórico padrão poderão ser incluídas as variáveis sendo: " # ", que poderão ser substituídas por quaisquer caracteres e " @ ", que poderão ser substituídas apenas por número, devendo ser incluído um @ para cada número a ser incluído, muito utilizada para datas.  Já as variáveis pré-definidas buscam informações na base de dados.  Veja o exemplo abaixo:  Cadastramos outro histórico padrão informando o complemento como obrigatório e solicitamos algumas variáveis pré-definidas (número do documento, dia atual, mês atual e ano atual do lançamento)  Ressaltamos que marcada a opção complemento obrigatório, obrigatoriamente terá que informar algo no complemento do histórico da partida.  Selecione a variável desejada na opção: Variáveis pré-definidas e clique na seta azul, veja que as varíáveis irão ser apresentadas na posição que desejar de acordo com o campo descrição informado:      Ao informar o código do histórico padrão, veja como ficará na partida do lançamento:      3- Outro exemplo é quando informamos as variáveis " # e " @ " segue abaixo:      Na inclusão das partidas ao incluir o código do histórico será possível informar os dados e a data desejar:      4- Utilizando a opção: Não Permite Complemento, esta opção quando marcada, não permitirá cadastrar complemento nas partidas que estiverem utilizando este histórico. Outro detalhe é que, caso este histórico já tenha sido utilizado em outra partida sendo informado o complemento, este não poderá ser marcado esta opção, onde deverá ser criado um novo código de histórico, segue abaixo:      Repare que na partida informando o código de histórico padrão, o campo complemento ficará bloqueado:      5- Para a opção de Histórico de Fechamento, deverá ser criado um novo código de histórico, onde este provavelmente será utilizado no processo de **:**      Veja como ficará as partidas do processo de Transferência de Grupos Contábeis, onde foi informado o histórico de fechamento: |
| **Observações:** | Obtenha mais informações e também variáveis pré-definidas de outros módulos através do link: **<http://wikihelp.totvs.com.br/WikiHelp/CTB/CTB.historicosPadroes.aspx>** |
