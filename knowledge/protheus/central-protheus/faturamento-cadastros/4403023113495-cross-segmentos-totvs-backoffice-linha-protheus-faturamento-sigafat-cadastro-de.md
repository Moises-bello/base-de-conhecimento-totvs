---
article_id: 4403023113495
category: Faturamento - Cadastros
content_hash: 1712b67d087e06c180ab97c505698f562a916a5bd2d8bac20dce84abec035a87
fetched_at: '2026-06-28T22:38:35.568436+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-Faturamento (SIGAFAT)- Cadastro
  de Clientes - Campo A1_VM_OBS
type: support-article
updated_at: '2021-06-23T12:41:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403023113495-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Cadastro-de-Clientes-Campo-A1-VM-OBS
---

**Dúvida**O campo A1\_VM\_OBS não grava conteúdo.  
  
**Ambiente**Cross Segmentos-TOTVS Backoffice (Linha Protheus)-Faturamento (SIGAFAT) - A partir da versão 12.1.17  
  
**Solução**

O campo **A1\_VM\_OBS** é um campo virtual, portanto, esse tipo de campo não é salvo em banco,   
  
Este campo é utilizado nos Módulos CRM (rotina **CRMA980**)  e Comercio Exterior (Rotina **Eecin100**), porém, por se tratar de um campo padrão, pode ser utilizado a qualquer momento pelo ERP em outras rotinas (por isso não sugerimos o uso diferente pelo qual ele foi criado).
