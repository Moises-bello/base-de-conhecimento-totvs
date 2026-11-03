---
article_id: 13269701588247
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 77be7422970233f6221a1a364ec7688fbbb438cb9c1baacbb0b1381e71ba38f9
fetched_at: '2026-06-28T22:39:30.486675+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS -  Como fazer complemento
  de ICMS ST com base de cálculo nota fiscal de saídas?
type: support-article
updated_at: '2024-02-01T11:35:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13269701588247-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-fazer-complemento-de-ICMS-ST-com-base-de-c%C3%A1lculo-nota-fiscal-de-sa%C3%ADdas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18163033327255) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como fazer Complemento de ICMS ST nota fiscal de saídas?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

O complemento de ICMS ST com base de calculo do ICMS ST somente pela rotina Mata920 em livros fiscais

Livros fiscais / Atualizações / Movimentos / Nota fiscal manual de saídas

Tipo da nota fiscal = **Complemento de ICMS**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/21023034390679)**

TES

**Configuração da TES:**

Credita ICMS **(F4\_CREDICM)** = Não  
Calcula ICMS **(F4\_ICM)** = Não  
Agrega Solidário **(F4\_INCSOL)** =  Não

Agrega Valor = Sim

L. Fiscal ICMS **(F4\_LFIMC)** = ICMS Zerado  
Sit.trib.ICMS **(F4\_SITTRIB)** = 10, 30, 70 e 90

Fórmula**(F4\_FORMULA)** = Amarrar uma fórmula com conteúdo texto = "Complemento" para que o sistema não destaca o ICMS normal nos livros, apenas o ICMS retido

Informe o mesmo Produto da nota de origem

Informe Valor Unitário e Valor Total "Valor do ICMS ST" a ser complementado.

Informa a N.F Orig, Serie Orig. e Ir. Doc Orig

Informe a base do ICMS ST no campo Ret ICMS

Informe valor do ST no campo ICMS Solid

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21023054655255)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21023034424343)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21023054688023)
