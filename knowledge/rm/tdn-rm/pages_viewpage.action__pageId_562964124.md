---
content_hash: 849e33d21ce2f07676575b712621dcf2e2727ccdc4fc9d9e06d6be0326fb46d4
fetched_at: '2026-06-29T00:10:50.738936+00:00'
page_id: '562964124'
product: rm
source: tdn-rm
title: Saídas (Layout Ernst & Young)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=562964124
version: 14
---

Através desse layout é possível extrair os dados detalhados do ativo imobilizado assim como informações sobre adições, alienações e depreciação, para apoio nas auditorias das demonstrações financeiras realizadas pela Ernst & Young. Uma vez extraído o arquivo deve ser enviado à EY.

| Ordenação | Descrição | Origem dos Dados | Observações |
| --- | --- | --- | --- |
| 1 | Número do ativo | Código do patrimônio presente no cadastro. |  |
| 2 | Descrição do ativo | Descrição do patrimônio. |  |
| 3 | Localização do Ativo | Nome do local em que o ativo está. |  |
| 4 | Posse do Ativo | Campo não aderente ao layout. |  |
| 5 | Categoria de ativo | Descrição do grupo ao qual o patrimônio foi associado. |  |
| 6 | Tipo de ativo | Título (grau superior) ao qual o patrimônio está vinculado. |  |
| 7 | Depreciação de ativos | Valor fixo 'Y'. |  |
| 8 | Método de depreciação | Valor fixo 'SL'. |  |
| 9 | Custo de compra | Valor da aquisição presente no cadastro do patrimônio. |  |
| 10 | Saldo residual | Corresponde ao valor residual ao final da vida útil existente em alguns processos como Avaliação Patrimonial e Revisão de Vida Útil. |  |
| 11 | Percentual do saldo redutor | Não será gerado |  |
| 12 | Vida útil (anos) | Vida útil do patrimônio em anos. | O cálculo é feito pela divisão de 100 pela taxa de depreciação corrente. |
| 13 | Vida útil restante no início do Período | Campo opcional. Não está sendo calculado. |  |
| 14 | Vida útil restante no Encerramento do Período | Campo opcional. Não está sendo calculado. |  |
| 15 | Data capitalizada | Data da primeira depreciação do patrimônio. |  |
| 16 | Data de alienação | Data da baixa mais recente existente dentro do período que está sendo auditado. |  |
| 17 | Data de transferência | Data da transferência mais recente existente dentro do período que está sendo auditado. |  |
| 18 | Custo no início do Período | Valor base corrigido do patrimônio no início do período que está sendo auditado. |  |
| 19 | Custo de Adição | Soma dos acréscimos e avaliações que incidiram no patrimônio durante o período selecionado. |  |
| 20 | Custo de Transferência | Soma das transferências realizadas pelo patrimônios de origem durante o período que está sendo auditado. |  |
| 21 | Custo de Alienação | Soma das baixas realizadas pelo patrimônio durante o período que está sendo auditado. |  |
| 22 | Custo no fechamento do Período | Valor base corrigido no fechamento do período que está sendo auditado. |  |
| 22 | Depreciação no início do Período | Depreciação acumulada corrigida existente na última linha de cálculo anterior a data de início da auditoria. Caso o patrimônio seja avaliado será somada a depreciação acumulada, da linha de cálculo principal, com a depreciação acumulada da avaliação. |  |
| 24 | Depreciação cobrada durante o período | Soma da depreciação ajustada das linhas de cálculo existentes no período que está sendo auditado. |  |
| 25 | Depreciação transferida | Soma do ajuste da depreciação acumulada corrigida, existente no cálculo de depreciação, gerado pelas ocorrências de transferência monetária. |  |
| 26 | Depreciação Alienada | Soma do ajuste da depreciação acumulada corrigida, existente no cálculo de depreciação, gerado pelas ocorrências de baixa. |  |
| 27 | Depreciação de Fechamento | Depreciação acumulada corrigida existente na última linha de cálculo do período que está sendo auditado. Caso o patrimônio seja avaliado será somada a depreciação acumulada, da linha de cálculo principal, com a depreciação acumulada da avaliação. |  |
| 28 | Valor Líquido na abertura | Valor contábil do patrimônio no início do período que está sendo auditado. | O cálculo é feito pela subtração dos campos Custo no Início do Período e a Depreciação no Início do Período existentes no layout. |
| 29 | Valor Líquido no fechamento | Valor contábil do patrimônio no final do período que está sendo auditado. | O cálculo é feito pela subtração dos campos Custo no Fechamento do Período e a Depreciação de Fechamento existentes no layout. |
| 30 | Valor Líquido de alienações | Valor líquido de custo e depreciação acumulada dos patrimônios que foi baixado durante o período que está sendo auditado. | O cálculo é feito pela subtração dos campos Custo de Alienação e a Depreciação Alienada existentes no layout. |
| 31 | Valor Líquido de transferências | Valor líquido de custo e depreciação acumulada dos patrimônios de origem que realizaram transferências durante o período que está sendo auditado. | O cálculo é feito pela subtração dos campos Custo de Transferência e a Depreciação Transferida existentes no layout. |
