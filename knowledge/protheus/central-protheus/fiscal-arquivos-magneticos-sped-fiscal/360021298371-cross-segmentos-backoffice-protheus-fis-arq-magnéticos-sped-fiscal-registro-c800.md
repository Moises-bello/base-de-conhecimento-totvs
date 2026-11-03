---
article_id: 360021298371
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 04f77548c048dd63f7136bdd7254418ed52ec8e5b0b1eae8d53617ce4f832ce6
fetched_at: '2026-06-28T22:42:02.426619+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Registro C800: Cupom Fiscal Eletrônico – SAT (CF-E-SAT) (Código 59) / C850: Registro
  Analítico do CF-E-SAT (Código 59)'
type: support-article
updated_at: '2025-02-11T21:30:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021298371-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Registro-C800-Cupom-Fiscal-Eletr%C3%B4nico-SAT-CF-E-SAT-C%C3%B3digo-59-C850-Registro-Anal%C3%ADtico-do-CF-E-SAT-C%C3%B3digo-59
---

**Dúvida**Como gerar o registro C800: Cupom Fiscal Eletrônico – SAT (CF-E-SAT) (Código 59) / C850: Registro Analítico do CF-E-SAT (Código 59)

**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

**Parâmetros**

**MV\_ESPECIE:** 01=SATCE  --> 01 é a série que está amarrada à espécie SATCE para correta gravação **FT\_ESPECIE** e **F3\_ESPECIE**.

1- O Item do Cupom, deve conter no Campo **FT\_ESPECIE** com a Espécie " SATCE " (Código 59);

2- O Item do Cupom, deve conter no campo **FT\_TIPOMOV** igual a S (Saída);

3- Wizard SPEDFISCAL

![C800.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360017846491/C800.JPG)
