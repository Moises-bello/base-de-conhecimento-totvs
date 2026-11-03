---
content_hash: 2cb16ba7d56d6b3f35a50e2cbf73236069052ba562b78486a5107c19105c7b20
fetched_at: '2026-06-29T00:08:24.857199+00:00'
page_id: '270907614'
product: rm
source: tdn-rm
title: Ligação Sob Demanda (Gerador de saídas)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270907614
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | **RM** |
| **Versões:** | **11.80 / 12.1.X** |
| **Ocorrência:** | **Retornar informações de uma consulta SQL para um layout do gerador de saídas utilizando como parâmetro um campo do registro do layout** |
| **Ambiente:** | **Gerador de saídas / Integração** |
| **Passo a passo:** | ***O objetivo desse documento é orientar como retornar uma informação adicional do seu conjunto de dados utilizando uma consulta SQL no gerador de saídas.***    Para retornar uma informação adicional no layout do gerador de saídas que não esteja presente em seu contexto conjunto de dados, será necessário utilizar uma consulta SQL e o recurso Ligação Sob Demanda. Para criar esse exemplo irei utilizar um contexto Conjunto de dados que retora os campos CNPJ, Código da coligada e o Nome da coligada oriundos da tabela GCOLIGADA.    Após criar esse contexto, adicionei um novo registro no layout com o nome de Conjunto de dados tabela. Através do botão (Campo Adicionar novo campo) inseri 3 linhas correspondentes ao Código da coligada, CNPJ e Nome e arrastei os campos citados acima para essas linhas.    Ao salvar esse layout dessa maneira, o mesmo será executado e retornará o código da coligada, o CNPJ e o Nome da coligada. Iremos inserir a consulta SQL que irá receber o campo de parâmetro. Essa consulta irá retornar o nome da filial de acordo com o código da coligada:    Acesse a Tela de contextos e adicione consulta SQL através do Menu Adicionar Contexto\Consulta SQL    Ao acessar esse menu, será exibido o novo contexto. Nesse novo contexto (Contexto02), em propriedades busque pelo código de sua consulta SQL. Após adicionar a SQL, em Modo de Carga altere de Carregado no inicio da geração para Carregado SobDemanda, conforme abaixo.    Consulta inserida, volte no Registro Conjunto de dados tabela e na aba LigaçãoSobDemanda e arraste a consulta SQL recém inserida para a aba citada. Repare que ao inserir a consulta, o parâmetro criado na sentença será exbido junto com o tipo de dados. Volte para a tela de contextos, expanda o Contexto 01, referente ao conjunto de dados da tabela GCOLIGADA e arraste o campo código da coligada para o parêmetro, de forma que no campo de Ligação, seja exibido o nome Registro, conforme abaixo:      No botão (Campo Adicionar novo campo) , adicione uma nova linha e arraste o campo da consulta SQL para essa nova linha.      Ao configurar o layout do gerador de saídas, a SQL será executada recebendo o campo configurado como parâmetro.  A ligação SobDemanda não deve ser utilizada como estrutura Pai-Filho, tendo em vista que a função desse tipo de ligação é complementar as informações que o contexto conjunto de dados retorna. Para utilizar estrutura Pai e filho, deverá ser utilizado o relacionamento entre as tabelas no contexto conjunto de dados. |
| **Observações:** |  |
