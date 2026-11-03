---
article_id: 4411036496151
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 4fc74b2068b1d4bed60369a39a1a85fdfe4bddf5a9117df777e6c7c107d9603f
fetched_at: '2026-06-28T22:42:03.694166+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - C197 - Duplicidade
  de ocorrência da chave COD_AJ, COD_ITEM
type: support-article
updated_at: '2021-10-19T15:10:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411036496151-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C197-Duplicidade-de-ocorr%C3%AAncia-da-chave-COD-AJ-COD-ITEM
---

**Dúvida**

Ao validar o arquivo da EFD ICMS/IPI é apresentado a inconsistência abaixo:

C197 - Duplicidade de ocorrência da chave COD\_AJ, COD\_ITEM

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411036118167/mceclip0.png)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - Todas as versões  
  
**Solução**

O registro **C195** é o registro pai do registro **C197**.   
  
Em situações em que tenha mais de um **CFOP** para o mesmo Código de Lançamento  deverá ser configurado, no **TES**, campo de **Observação de Lançamento Fiscal** (CC7\_IFCOMP), um código diferente para cada CFOP.   
  
Caso isso não ocorra, apenas um registro **C195** será escriturado, o que ocasionará erro na validação do arquivo da EFD ICMS/IPI.
