---
content_hash: 894c2659b550768927a010ec9b04478f11be9d9a10d84a6d4036082f85b39e6a
fetched_at: '2026-06-29T00:08:42.128270+00:00'
page_id: '287053181'
product: rm
source: tdn-rm
title: RMCTB00009_Rastrear Origem da Contabilização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=287053181
version: 10
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS - Gestão Contábil |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Rastrear Origem da Contabilização |
| **Ambiente:** | Novo Modelo BackOffice |
| **Passo a passo:** | **Definição do processo:**  Esta funcionalidade tem como objetivo mostrar de forma gráfica e estruturada toda a operação que deu origem ao lançamento contábil e suas respectivas partidas.  Este recurso possibilita ainda consultar diretamente a origem do lançamento, bastando dar duplo clique no diagrama apresentado para que a tela de entrada do sistema de origem seja aberta, sem a necessidade de acessar diretamente o sistema de origem para realizar tal consulta.    **Regras Gerais:**  Muitas operações efetuadas em sistemas externos ao da contabilidade podem gerar automaticamente no Totvs Gestão Contábil um lançamento contábil correspondente. Se desejar saber informações sobre a operação que deu origem a este lançamento, sem ter que acessar diretamente o sistema de origem, basta selecionar o lançamento e acessar o Anexo ‘Rastrear origem’ que uma tela gráfica com diagramas contendo informações sobre a operação de origem e as respectivas partidas geradas será mostrada.        O sistema irá mostrar de forma gráfica a origem do lançamento, como também dará acesso à tela do sistema que deu origem ao lançamento contábil. Vejamos abaixo:        Neste caso rastreamos um lançamento do TOTVS - Gestão Financeira. Desta forma, o sistema mostrará a tela que originou o lançamento na contabilidade:      **Importante:**  Para rastrear a origem dos lançamentos contábeis, é preciso que o sistema de origem já tenha sido convertido para o Novo Modelo de BackOffice da linha RM e esteja gerando os lançamentos nesta nova plataforma .Net.  A origem de tais lançamentos pode ser consultada tanto para os lançamentos que ainda estiverem no **lote N** como para os que já estiverem no lote oficial da contabilidade (**lote zero**). |
| **Observações:** | Não é possível rastrear lançamentos originados do TOTVS Gestão de Folha de Pagamento por não possuir o módulo de rastreabilidade implementado no contábil. |
