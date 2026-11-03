---
article_id: 360058184994
category: RH - FGTS / SEFIP
content_hash: ba8c9a21d61adbc63f4d031d4c76e40d1503ec52bb95f51a57c6129f92ff3bf8
fetched_at: '2026-06-28T22:43:41.350219+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao enviar a SEFIP apresenta o seguinte erro: 300072-
  Registro do Tomador/Obra não encontrado para empresa indicada. Código de recolhimento
  exige tomador de serviços'
type: support-article
updated_at: '2021-07-17T03:07:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058184994-RH-Linha-Protheus-GPE-Ao-enviar-a-SEFIP-apresenta-o-seguinte-erro-300072-Registro-do-Tomador-Obra-n%C3%A3o-encontrado-para-empresa-indicada-C%C3%B3digo-de-recolhimento-exige-tomador-de-servi%C3%A7os
---

**Ocorrência**Ao enviar a SEFIP apresenta o seguinte erro : 300072- Registro do Tomador/Obra não encontrado para empresa indicada. Código de recolhimento exige tomador de serviços.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Esse erro ocorre pois  no arquivo SEFIP.RE o registro de Tomador/Obra (registro 20). está com o código de recolhimento errado ou nos parâmetros de geração da SEFIP não está preenchido corretamente.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Ao gerar o arquivo **nos parâmetros de geração da SEFIP na pergunta (Gerar Sefip por?) usar a opção Centro de custo, e não a opção Por filial.**

**Saiba Mais**

Para adquirir mais conhecimento acesse o(s) *link*(s) abaixo:

<https://tdn.totvs.com/display/public/PROT/FGTS>
