---
article_id: 360051583834
category: PMS - Projetos
content_hash: 496176f89d49be28d55cd8d309525769738075d34e9826d8168942a10f9fd5b0
fetched_at: '2026-06-28T22:37:14.999188+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: MP - PMS - COMO ALTERAR UM ORÇAMENTO SE JÁ POSSUI O PROJETO CRIADO
type: support-article
updated_at: '2021-04-29T21:12:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051583834-MP-PMS-COMO-ALTERAR-UM-OR%C3%87AMENTO-SE-J%C3%81-POSSUI-O-PROJETO-CRIADO
---

**Ocorrência**

Foi gerado um orçamento (**PMSA100**) e transformado em projeto, porem o orçamento foi gerado errado e será necessário ter alterações. Como efetuar este procedimento visto que o projeto já foi criado?

**Ambiente**  
Protheus – A partir da release 11.80.  
   
**Solução**  
 1. Altero a fase do orçamento, para uma fase que não gera projetos (**AF1\_FASE**).  
 2. Deleto o projeto que tinha sido gerado pelo orçamento  
 3. E gero um novo projeto com o orçamento atualizado (**PMSA110**)

Saiba mais sobre o cadastro de fases:

[**PMS0035 - Fases\_do\_Projeto\_e\_Orçamento**](https://tdn.totvs.com/pages/releaseview.action?pageId=538493522)
