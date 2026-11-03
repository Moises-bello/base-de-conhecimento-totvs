---
content_hash: 10d688e8762b85389b45c4413c603069b283bfbe076b40010e8b328758055717
fetched_at: '2026-06-29T00:09:55.634117+00:00'
page_id: '448599934'
product: rm
source: tdn-rm
title: 4378230 FISCAL01-7175 DT Escrituração Fiscal - Valor Situação Tributária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=448599934
version: 3
---

# Escrituração Fiscal - Valor Situação Tributária

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Processo de Escrituração Fiscal |
| **Situação/Requisito:** | No processo de Escrituração Migrada, quando há mais de uma Situação Tributária, o Valor Contábil não é gerado corretamente  para Natureza de Operação que está parametrizada com Redução de Base de Calculo. |
| **Solução/Implementação:** | Ajuste no Calculo do Valor Contábil da Situação Tributaria quando na Natureza de Operação está parametrizada com Redução de Base de Calculo.  Obs.: O Parâmetro dos Tributos de ICMS do Nucleus deve estar marcado para utilizar "Base Cheia", só assim o sistema irá calcular corretamente  o Fator de Redução e assim o Valor Contábil da Situação Tributaria. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |
| **Documento de Referência:** | N/A. |
