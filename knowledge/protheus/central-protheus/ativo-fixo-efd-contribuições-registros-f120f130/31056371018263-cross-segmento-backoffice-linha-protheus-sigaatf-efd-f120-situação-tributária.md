---
article_id: 31056371018263
category: Ativo Fixo - EFD Contribuições - Registros F120/F130
content_hash: 9309b298c0e6ec900afc7f6cd5f66d3980dc539aa961428fc17d861e0b877124
fetched_at: '2026-06-28T22:41:36.191650+00:00'
product: protheus
section_id: 31045161075991
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - EFD - F120 - SITUAÇÃO
  TRIBUTÁRIA
type: support-article
updated_at: '2025-03-31T18:40:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31056371018263-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-EFD-F120-SITUA%C3%87%C3%83O-TRIBUT%C3%81RIA
---

Dúvida: É possível utilizar uma situação tributária diferente daquela registrada no documento fiscal de entrada para a apuração do EFD nos blocos F120?

Ambiente:

Microsiga Protheus - Ativo Fixo - Todas as versões

**Solução:**

A apuração dos blocos F120 pode ser realizada com base nos dados cadastrados no módulo de Ativo Fixo. Dessa forma, o cliente pode optar por utilizar uma situação tributária específica para a escrituração do documento fiscal de entrada e outra para a apuração de créditos relacionados ao ativo fixo.

O campo determinante para esta configuração é o Base PIS/COF(N1\_CBCPIS), que deve ser configurado como 2.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31056418906391)

Funcionamento do campo Base PIS/COF(N1\_CBCPIS):

**Base PIS/COF (N1\_CBCPIS) = 1 (Normal):** O sistema utiliza, para os cálculos de apuração, as informações contidas na TES (Tipos de Entrada e Saída) e no documento fiscal de entrada.

**Base PIS/COF (N1\_CBCPIS) = 2 (Cadastro do Bem)**: O sistema prioriza os dados cadastrados no módulo de Ativo Fixo, utilizando as informações fiscais específicas do bem.

Com o valor 2 configurado no campo Base PIS/COF(N1\_CBCPIS), o sistema processa os cálculos na CL2 (apuração EFD), seguindo as informações fiscais registradas diretamente no cadastro do bem no módulo de Ativo Fixo.

Essa flexibilidade permite que as empresas adaptem suas apurações fiscais de acordo com suas necessidades específicas, mantendo a conformidade com a legislação vigente.
