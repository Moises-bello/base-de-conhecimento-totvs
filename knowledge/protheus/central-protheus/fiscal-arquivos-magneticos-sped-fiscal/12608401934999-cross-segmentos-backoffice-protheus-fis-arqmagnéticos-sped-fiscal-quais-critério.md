---
article_id: 12608401934999
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 20774967532685e9b5d656d12f56aaf29d8efb56d6e60cf1c43cb8cd28f4e58b
fetched_at: '2026-06-28T22:42:03.620751+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Sped Fiscal
  - Quais critérios do campo 08 registro C197 com códigos de lançamentos SP90090106
  e SP40090227 no Sped Fiscal?
type: support-article
updated_at: '2023-02-22T18:46:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12608401934999-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Quais-crit%C3%A9rios-do-campo-08-registro-C197-com-c%C3%B3digos-de-lan%C3%A7amentos-SP90090106-e-SP40090227-no-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Em cumprimento à portaria **CAT54/2020**, quais são as validações do campo **08** do registro **C197 Outras obrigações tributárias** do Sped Fiscal para os códigos **SP90090106** e **SP40090227**?  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão **12.1.25**  
  
**Solução**

Quando utilizado o código de lançamento **SP90090106** o valor apresentado no campo **08** será alimentado com a origem do campo **FT\_MARGEM**, na tabela **SFT**.

Quando utilizado o código de lançamento **SP40090227** existe um cálculo específico, onde irá verificar qual a posição do **Livro de ICMS**.

**L. Fiscal ICMS  - F4\_LFICM** = **T** irá buscar do **FT\_VALICM**

**L. Fiscal ICMS - F4\_LFICM -**  **O** irá fazer o seguinte cálculo:

Buscar o valor do campo **FT\_OUTRICM \* CDA\_ALIQ / 100**.

O resultado do valor será coerente com o conteúdo do campo **08** do registro **C197**.

**Documentações complementares:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=635753743>  
<https://tdn.totvs.com.br/pages/releaseview.action?pageId=607590424>  
<https://tdn.totvs.com/pages/releaseview.action?pageId=571772637>
