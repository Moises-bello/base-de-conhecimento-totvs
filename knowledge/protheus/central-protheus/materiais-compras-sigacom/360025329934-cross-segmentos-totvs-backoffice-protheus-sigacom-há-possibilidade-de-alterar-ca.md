---
article_id: 360025329934
category: Materiais - Compras (SIGACOM)
content_hash: 6a47e01b481bd61a9a33f9eb7027d523c5fce1d4e3015b18a47d1bc72a92dd30
fetched_at: '2026-06-28T22:41:18.755431+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Há possibilidade de
  alterar campos das abas "Danfe", "NF Eletrônica" e "Inf. Adicionais"?
type: support-article
updated_at: '2022-05-18T20:54:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025329934-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-H%C3%A1-possibilidade-de-alterar-campos-das-abas-Danfe-NF-Eletr%C3%B4nica-e-Inf-Adicionais
---

**Dúvida**

Há possibilidade de alterar campos das abas "Danfe", "NF Eletrônica" e "Inf. Adicionais".

**Ambiente**

Protheus – Compras – A partir da versão 11.80  
  
**Solução**

O Ponto de Entrada **M103NFEL**pode ser utilizado para inserir informações nas abas "Nota Fiscal Eletrônica", "Informações DANFE" e "Informações Adicionais" no momento da inclusão e da classificação da nota, para que as informações fiquem visíveis no momento da digitação da nota.

A chamada do Ponto de Entrada M103NFEL ocorre em 4 momentos distintos:

1 - Na validação do campo F1\_FORNECE no momento da digitação do cabeçalho da nota na inclusão  
2 - Na validação do campo F1\_LOJA no momento da digitação do cabeçalho da nota na inclusão  
3 - Na validação do campo F1\_EST no momento da digitação do cabeçalho da nota na inclusão  
4 - No momento da classificação da nota  
  
Em ambos os casos, o ponto de entrada recebe como parâmetro a identificação do campo que está sendo validado.

Verificar detalhes no link:<http://tdn.totvs.com/pages/viewpage.action?pageId=378274361>
