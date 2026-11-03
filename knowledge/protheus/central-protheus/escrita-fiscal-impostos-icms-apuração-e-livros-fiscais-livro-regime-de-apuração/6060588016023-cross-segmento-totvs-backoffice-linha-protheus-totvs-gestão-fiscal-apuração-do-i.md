---
article_id: 6060588016023
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: e4a6ae894470d328e30917362e15f54c909a5184ff4566ec9efcd2b9f5739d86
fetched_at: '2026-06-28T22:39:22.123640+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal -
  Apuração do icms zerada como corrigir?
type: support-article
updated_at: '2022-05-13T13:42:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6060588016023-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-Apura%C3%A7%C3%A3o-do-icms-zerada-como-corrigir
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida**Apuração do icms zerada como corrigir?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

APURACAO ICMS ZERADA

Verifique os procedimentos abaixo:

1) è necessário gerar a apuração do icms em :

miscelânea/apurações/apuração do icms

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6060474470551/mceclip0.png)

2) Na impressão do relatório matr940 -  P9 a pergunta

Concilia apurações = NAO

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6060563273623/mceclip1.png)

Verificar se  na pasta system é gravado o arquivo Ax22numero da empresa e filial.IC0

exemplo mês de abril/2022

AD220101.ic0

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Nomenclatura do Arquivo de Apuração de Impostos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019082872-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Nomenclatura-do-Arquivo-de-Apura%C3%A7%C3%A3o-de-Impostos?source=search)

Dessa forma será apresentado valores no relatório de apuração do icms P9
