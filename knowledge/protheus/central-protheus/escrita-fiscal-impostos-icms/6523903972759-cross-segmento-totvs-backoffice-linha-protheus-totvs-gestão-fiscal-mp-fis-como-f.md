---
article_id: 6523903972759
category: Escrita Fiscal - Impostos - ICMS
content_hash: 711da78f3b5f5a2f4665eee239c64e3600b6b950871c21a45c79f9a75bea1dc2
fetched_at: '2026-06-28T22:39:24.079222+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal -
  MP FIS Como fazer uma nota fiscal de estorno de ICMS de MG?
type: support-article
updated_at: '2022-06-03T17:24:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6523903972759-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-MP-FIS-Como-fazer-uma-nota-fiscal-de-estorno-de-ICMS-de-MG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida**Como fazer uma nota fiscal de estorno de ICMS de MG?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Legislação de como emitir a Nota fiscal de estorno de ICMS

“Art. 73. Para efeitos de estorno do imposto creditado, será emitida NF-e de ajuste, sem destaque do imposto, constando: I – nos campos “Natureza da Operação” e “Descrição do Produto”: estorno de crédito do ICMS; II – no campo “Data de Emissão”: o último dia do período de apuração do ICMS a que se refere o estorno de crédito; III – no campo “CFoP”: o código 5949; IV – nos campos “valor Total dos Produtos” e “valor Total da Nota”: o valor a ser compensado; V – no campo “Informações Complementares”: a observação “a emissão da nota se deu para fins de estorno do valor do imposto anteriormente creditado”, seguida do respectivo fundamento legal.

* 1° Na hipótese do estorno de crédito ter sido efetuado em virtude de autorização dada em regime especial, o contribuinte deverá mencionar no campo próprio da NF-e, o número do e-PTA.
* 2° Para fins da Escrituração Fiscal Digital – EFD, o valor referente ao crédito a ser estornado deverá ser escriturado no registro C197 (ajuste de documento), utilizando o código de ajuste: “MG50000999, estorno de crédito, outros ajustes”.

Dentro do Protheus

Tipo de nota fiscal = Normal  

TES

5949

Calcula icms = não

L fiscal icms = observações

Formula = preenchido

Agrega valor = sim

F4\_ajuste = S

Quantidade zerada = sim  

IV – nos campos “valor Total dos Produtos” e “valor Total da Nota”: o valor a ser compensado; Valor do ICMS a ser estornado
