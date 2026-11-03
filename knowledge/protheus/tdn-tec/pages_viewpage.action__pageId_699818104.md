---
content_hash: 0ef573f38374a13b713b078b5fae2e7345eb21a0c09eaf511be3634c2d545e6d
fetched_at: '2026-07-02T19:24:27.952096+00:00'
page_id: '699818104'
product: protheus
source: tdn-tec
title: Melhoria - Função ADUserValid passa a mostrar mensagem no arquivo de log em
  caso de erro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=699818104
version: 1
---

Melhoria - Função ADUserValid passa a mostrar mensagem no arquivo de log em caso de erro

|  |  |
| --- | --- |
| Situação | A função ADUserValid responsável pela validação de usuário e senha de domínio Active Directory da Microsoft retorna apenas verdadeiro (.T.) ou falso (.F.), sendo que nenhuma mensagem de erro é retornada em caso de falha na autenticação. |
| Ocorrência | Necessidade de uma avaliação mais criteriosa do usuário ou administrador do domínio em caso de falha na autenticação da função ADUserValid. |
| Melhoria | Caso a camada de autenticação da Microsoft gere um erro no processo de autenticação do usuário de domínio Active Directory, o TOTVS SmartClient incluirá uma entrada em seu arquivo de log com o código e mensagem de erro gerados. |
| Informações adicionais | * Leia sobre a . * Veja como ativar o . * Referente ao chamado: 14240529 * Referente à ocorrência: DTCLIENT01-3490 * Disponível em builds iguais ou superiores a 20.3.0.4 e 20.3.1.0 |
