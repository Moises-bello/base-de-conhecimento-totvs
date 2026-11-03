---
content_hash: aefc5dd10bb8bcbdaef0ea28115413d629451f5cb6c7332fa4b267ca145431e4
fetched_at: '2026-06-29T00:10:27.561760+00:00'
page_id: '516625073'
product: rm
source: tdn-rm
title: Guia INSS e Folha Analítica - Histórico de Percentuais para INSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=516625073
version: 2
---

# Histórico de Percentuais para INSS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Ler os percentuais da Empresa, Acidente de Trabalho e Terceiros informados no cadastro do histórico de percentuais INSS na vigência correspondente a geração da Folha Analítica e da Guia de INSS, podendo ser na competência atual ou retroativa, de forma a atender Produtores Rurais que podem optar pelo recolhimento via comercialização ou folha de pagamento. Manter os históricos para serem usados em caso de retificação. |
| **Situação/Requisito:** | Criação do cadastro "Histórico de percentuais de INSS" anexo ao cadastro de seção, de forma a ser lido dinamicamente na geração da Guia de INSS e Folha Analítica de acordo com o Mês/Ano parametrizado e a existência de % Empresa, % Acidente Trabalho e % Terceiros no histórico para vigência em questão. |
| **Solução/Implementação:** | Criação de anexo de seção para cadastrar os históricos de percentuais para INSS de forma a serem lidos na geração da Guia de INSS e Folha Analítica.  A utilização do histórico está vinculada ao parâmetro "Habilita Histórico de INSS no Cadastro de Seção" em: Parametrizador | Folha Mensal | Encargos Sociais. |
| **Documento de Referência:** | ["Habilita Histórico de INSS no Cadastro de Seção (Produtor Rural)"](http://tdn.totvs.com.br/pages/viewpage.action?pageId=496388652). |
