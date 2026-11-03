---
content_hash: 37269c69977df81c4426b3c04aca4ddb66e4ac20f0e233abe43d94632ec4ff79
fetched_at: '2026-06-29T00:08:46.381775+00:00'
page_id: '317293338'
product: rm
source: tdn-rm
title: RMCTB00002_Alteração de Distribuição Gerencial (Estrutura/Execução)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=317293338
version: 5
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS - Gestão Contábil |
| **Versões:** | 12.1.17 |
| **Ocorrência:** | Alteração de Distribuição Gerencial (Estrutura/Execução) |
| **Ambiente:** | Novo Modelo BackOffice |
| **Passo a passo:** | **Definição do processo:**    Permite a alteração global e automatizada da distribuição gerencial das contas contábeis que possuem em seu cadastro a opção de rateio marcada.  A alteração de distribuição gerencial pode ser utilizada entre outros, para correção de rateios já efetuados ou mudança do cenário gerencial em determinado período.    **Regras Gerais:**   * Uma regra essencial é que, após a alteração, não há como retornar ao cenário anterior, ou seja, cancelando a alteração.     As alterações podem ser feitas manualmente com a informação das contas de origem, destino e percentual da nova distribuição ou utilizando-se uma estrutura pré-definida com as informações das contas e percentuais do novo rateio.  Recomendamos basear os filtros nas contas contábeis, no período e nos lotes que deverão ser alterados, objetivando evitar alterações indevidas na base de dados.    **Parametrização Necessária:**    1 - Quando as alterações forem  mais complexas, temos a opção de cadastrar uma estrutura contendo todas as parametrizações da mesma. Vejamos abaixo:        Ao incluir uma  nova estrutura insira os dados obrigatórios, para conseguir informar os moldes da alteração:        Obs: Caso a flag Usar Conta Contábil esteja desmarcada, só será possível cadastrar um molde.    Ao serem informados os dados de identificação passamos para o cadastro dos moldes, conforme figura abaixo:        Agora já podemos executar o processo, usando as opções que permitem a informação de uma estrutura. Vejamos abaixo:        Dados essenciais a serem informados são os lotes que sofrerão alteração, bem como o período, podendo ser ativados filtros de conta contábil, filial e centro de custo ou ainda usando um filtro genérico contendo várias opções:        Há duas opções que permitem o uso de estrutura, vejam:    1 - Redistribuir Conta Gerencial        2 - Informar Distribuição Gerencial:        As demais opções são apresentadas abaixo:    1 - Distribuição Gerencial do Plano de Contas      2 - Trocar de Conta Gerencial    O usuário pode, facilmente, trocar uma conta gerencial origem por uma de destino adicionando as alterações que deseja realizar a uma lista de contas gerenciais: |
| **Observações:** | Para maiores detalhes acesse a FAQ [RMCTB00006\_Alteração de Distribuição Gerencial](http://tdn.totvs.com/pages/viewpage.action?pageId=286749035) dentro do menu Escrituração Contábil/Lançamentos e Lotes.  Para exemplos acesse o WiKihelp: <http://wikihelp.totvs.com.br/WikiHelp/CTB/CTB.AlteracaoDistribGerencial_Execucao.aspx> |
