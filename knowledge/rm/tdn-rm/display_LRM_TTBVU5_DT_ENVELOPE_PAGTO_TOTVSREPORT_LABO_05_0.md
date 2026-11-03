---
content_hash: 3db283e7b9c0548b341643d6bc040460a817e6bfbc8f7ef2d558c564037462b1
fetched_at: '2026-06-29T00:06:07.746924+00:00'
page_id: '201737590'
product: rm
source: tdn-rm
title: TTBVU5_DT_ENVELOPE_PAGTO_TOTVSREPORT_LABO_05_0
type: documentation
url: https://tdn.totvs.com/display/LRM/TTBVU5_DT_ENVELOPE_PAGTO_TOTVSREPORT_LABO_05_0
version: 2
---

# RELATÓRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Emissão de Relatório pelo TotvsReport* |
| **Situação/Requisito:** | *Emissão do Envelope de pagamento pelo TotvsReport considerando Histórico e data de* *Transferência* |
| **Solução/Implementação:** | Foi otimizado o relatório "FOPREL25.0025 - 2.004.101 - Envelope de pagamento - Labo 05.0.TotvsReport" para considerar históricos de competências anteriores e data de transferência do funcionário. Emitindo informações como Seção, Situação, Salário, Função e Ficha Financeira de acordo com a competência e parâmetros informados.  O "Labo 05.0" Solicita os seguintes parâmetros:   1. "Descrição para o Período" onde deve ser informado a descrição para o período do envelope; 2. "Considerar Históricos de Seção, Função e Situação Até a Data" o sistema considerará as últimas mudanças de histórico que sejam anteriores ou igual a data aqui informada. 3. "Ano de Competência, Mês de Competência e Nro. Período" serão utilizados para obter os eventos de pagamento e suas bases.   Funcionários que possuem data de transferência posterior a data informada no parâmetro  "Considerar Históricos de Seção, Função e Situação Até a Data" não serão considerados para emissão do envelope de pagamento. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTBVU5 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
