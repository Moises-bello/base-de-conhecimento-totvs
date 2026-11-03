---
content_hash: 95295e60db8a7c8d3a47b70fcbcb894add1439e301d99997e779715dc72dd216
fetched_at: '2026-06-29T00:08:26.364270+00:00'
page_id: '271177006'
product: rm
source: tdn-rm
title: Estrutura Pai e Filho no Gerador de saídas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271177006
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | **RM** |
| **Versões:** | **12.1.X** |
| **Ocorrência:** | **Utilizar estrutura Pai e Filho no gerador de saídas** |
| **Ambiente:** | **Gerador de saídas / Integração** |
| **Passo a passo:** | ***O objetivo desse documento é orientar a maneira de criar um layout com relacionamento entre duas tabelas com estrutura Pai-Filho.***    Para realizar tal procedimento, em meu exemplo criei um novo contexto conjunto de dados utilizando a tabela GCOLIGADA, onde selecionei os campos CODCOLIGADA, CGC e NOME DA COLIGADA. Irei adicionar nesse contexto alguns dados da tabela GFILIAL. Para localizar essa tabela, expanda o campo chave da tabela principal (em meu exemplo GCOLIGADA.CODCOLIGADA) e localize a descrição da tabela desejada (em meu exemplo Filiais). Expanda a lista de campos da tabela desejada e selecione de acordo com sua necessidade, utilizei os campos Nome fantasia, código da filial e número da inscrição estadual, todos da tabela Filiais(GFILIAL).      Após criar o contexto Conjunto de dados, criei o Registro 001 e arrastei para a aba de ligação o Contexto 01.GCOLIGADA e inseri os campos correspondentes a tabela GCOLIGADA, conforme abaixo. Ao gerar o relatório dessa forma, o arquivo TXT vai ser salvo somente com esses dados.    Para criar a estrutura Pai-Filho, selecione o Registro 001 e clique no botão Adicionar Registro    Será adicionado um novo registro em seu layout. Renomeie esse registro e adicione o Contexto 01.GCOLIGADA na aba de ligação do registro. Feito isso, insira os campos referente a GFILIAL.    Ao gerar o layout dessa maneira, o Registro 001 vai ser gerado para enquanto o Registro 002 possuir dados, conforme abaixo    Para que o Registro principal (Registro 001) seja gerado apenas uma vez independentemente da quantidade de vezes que o Registro Filho (Registro 002), selecione um campo do Registro 001 que não altere o seu valor e em Modo, defina-o como Chave Primária, conforme abaixo    Dessa forma, o arquivo será gerado imprimindo o registro Pai apenas uma vez, independentemente da quantidade de registros filhos ele possuir, conforme abaixo.    Segue layout exemplo em anexo. 250 |
| **Observações:** |  |
