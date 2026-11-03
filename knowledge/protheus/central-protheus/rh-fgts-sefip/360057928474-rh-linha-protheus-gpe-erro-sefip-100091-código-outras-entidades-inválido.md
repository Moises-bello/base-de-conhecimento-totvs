---
article_id: 360057928474
category: RH - FGTS / SEFIP
content_hash: eb83e887855d8c70b0c0d821d062dc83a528c6c0ba771aa7419d1383fd5f4302
fetched_at: '2026-06-28T22:43:41.263951+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Erro SEFIP 100091 - Código Outras Entidades Inválido.
type: support-article
updated_at: '2025-08-14T17:39:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057928474-RH-Linha-Protheus-GPE-Erro-SEFIP-100091-C%C3%B3digo-Outras-Entidades-Inv%C3%A1lido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34185469392663) Tempo aproximado para leitura: 00:01:30 min  
  
Ocorrência**Ao importar o arquivo SEFIP.RE gerado no Protheus, o validador do programa SEFIP apresenta o seguinte erro 100091 - CÓDIGO OUTRAS ENTIDADES INVALIDO.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Esse erro ocorre pois o código de outras entidades lançado em **Manutenção de tabelas - S038 Outras Entidades**, esta incorreto.

**Solução**

Verifique em **Atualizações/Definições de Cálculo/Manutenção de Tabelas na tabela S038** se o campo **"Cod Terceiros"** está preenchido, caso não esteja preencha e gere o arquivo novamente e/ou informe código valido para programa SEFIP.   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100423793)

Gere a SEFIP Novamente após ajuste e efetue a importação.

**Saiba mais:  <https://tdn.totvs.com/display/public/PROT/FGTS>**
