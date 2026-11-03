---
content_hash: c37b1b94675282e8880f40f05f54d68d08442a8842c317da396528a070a9fb72
fetched_at: '2026-06-29T00:09:29.719045+00:00'
page_id: '425451481'
product: rm
source: tdn-rm
title: 5159592 FINANCEIRO01-9561 DT Registro online de boletos
type: documentation
url: https://tdn.totvs.com/display/LRM/5159592+FINANCEIRO01-9561+DT+Registro+online+de+boletos
version: 2
---

# Registro online de boletos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Registro online de boletos |
| **Situação/Requisito:** | O processo de registro online de boletos, quando no cadastro de convênio utiliza fórmulas de associação, o processo executa com demora. |
| **Solução/Implementação:** | Para melhorar a performance do processo de registro online, foi implementado a execução em paralelo, ou seja, para cada processador físico da máquina onde o host esta sendo executado, será rodado simultaneamente 5 processos.  Obs.: Para cada processo executado será aberto uma conexão de banco de dados. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 5159592 |
| **Requisito:** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-9561> |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
