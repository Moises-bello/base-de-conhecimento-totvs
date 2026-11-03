---
content_hash: 323aecdf8c58fa4c39691377f863d966e5c001049b747802980e2b0848ee754d
fetched_at: '2026-06-29T00:09:07.769885+00:00'
page_id: '385846451'
product: rm
source: tdn-rm
title: FISCAL01-5770 DT Estorno de Escrituração .Net - Alteração no processo de estorno
  para melhorar a performance
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=385846451
version: 2
---

# Alteração no processo de estorno para melhorar a performance

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Totvs Gestão Fiscal |
| **Função:** | Estorno de Escrituração .Net |
| **Situação/Requisito:** | Ao tentar estornar lotes muito grandes, a rotina não está sendo executada pois está estourando o erro abaixo ao executar o select que traz os lançamentos a serem estornados para que seja montado o contexto:  ***"An expression services limit has been reached. Please look for potentially complex expressions in your query, and try to simplify them"***  Esta exceção está sendo levantada pelo banco pois existe muitos "OR" na consulta. Exemplo da Consulta em anexo.  Deverá ser feita uma alteração na lógica, para buscar menos Lançamentos de cada vez no banco e ir adicionando estes lançamentos na lista de contextos.  Outra oportunidade de melhoria é nas validações realizadas no "DoValidateContext" da classe "FisEstornoEscrituracaoSbc". Lá são feitas várias verificações como, por exemplo, se o Lote Fiscal está aberto, se o Período de Apuração está aberto, Se existem Guias, etc. Porém, para cada lançamento do Contexto é feito um select no banco para cada uma destas verificações. O ideal é fazer um cache para as consultas que são executadas para cada item do Contexto, como para verificar se o período está aberto.   * Verifica se o período já está no cache. Se estiver, recupera ele Se não estiver, carrega do banco, grava no cache e recupera ele Efetua a validação sobre o período do cache |
| **Solução/Implementação:** | Ajuste no processo de estorno da escrituração .Net:    Select que busca os lançamentos a serem estornados foi otimizado para ser executado de 500 em 500 lançamentos, pois antes o resultado da query estava estourando devido a quantidade de linhas retornadas na consulta; Foram criadas listas internas na classe do subscriber para evitar varios SQLs no método DoValidateContext para validações de Periodo de Apuração e Validações de Lote na escrituração. |
