---
content_hash: e5628bae9cde0842581fc322e7c87a3e49e5334a0d0d4a0b49d3a523fd1889c8
fetched_at: '2026-06-29T00:09:18.094238+00:00'
page_id: '421388664'
product: rm
source: tdn-rm
title: Verificar Impactos  - Novo Boleto Registrado 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388664
version: 2
---

O verificador é a ferramenta responsável por analisar os cadastros e Consultas SQL no sistema, para correção de Fórmulas, Relatórios, Eventos Contábeis, Filtros na Visão de Lançamento, Planilhas .Net, Gerador de Saídas, Relatórios e até mesmo em VIEWS no Banco de Dados, para campos referentes à integração bancária que deixarão de ser preenchidos nos lançamentos(FLAN), para serem preenchidos no Boleto(FBOLETO).

Esta ferramenta está disponível no menu Utilitários | Impacto de Conversão / Verifica Impactos Novo Boleto Registrado.

O verificador disponibiliza filtros para otimizar a busca no sistema, sendo possível filtrar pelos Sistemas: Financeiro (F), Educacional (E, S, U), Incorporação (X) e Estoque Compras e Faturamento (T).

Importante ressaltar que não é recomendado desmarcar o Financeiro, pois é o sistema que poderá apresentar maior número de impactos. Caso o filtro "Carregar consultas SQL, Fórmulas e Relatórios apenas dos produtos selecionados" seja desabilitado, o processo será executado para todos os sistemas da linha RM indicados, o que pode ocasionar um aumento considerável no tempo de processamento.

Após a execução do processo, será gerado o Log apresentando todos os cadastros onde foram encontrados os campos que deverão ser modificados. Corrigido todos os cadastros indicados no LOG, deve ser executado o validador para verificar se ainda existe algum dado divergente.
