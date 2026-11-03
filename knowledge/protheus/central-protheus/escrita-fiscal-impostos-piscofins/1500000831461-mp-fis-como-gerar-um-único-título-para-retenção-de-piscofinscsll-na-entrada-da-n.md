---
article_id: 1500000831461
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: c649e66fcd30ff00f82917631ae492ebf8c549c330eebee3dde3f7cd0141c2dd
fetched_at: '2026-06-28T22:39:36.981445+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: MP - FIS - Como gerar um único título para retenção de PIS/COFINS/CSLL na entrada
  da NF?
type: support-article
updated_at: '2021-04-28T18:58:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000831461-MP-FIS-Como-gerar-um-%C3%BAnico-t%C3%ADtulo-para-reten%C3%A7%C3%A3o-de-PIS-COFINS-CSLL-na-entrada-da-NF
---

**Dúvida**

Como gerar um único título para retenção de PIS/COFINS/CSLL na entrada da NF?  
  
**Ambiente**

Microsiga Protheus - Livros Fiscais - a partir da versão 11.80  
  
  
**Solução**

O Sistema permite criar um único título, aglutinando os três tributos, na geração do **Documento de Entrada** retendo o **PIS/COFINS e CSLL**.

**Com esta finalidade está disponível o parâmetro MV\_AG10925**configurado conforme segue:

**Tipo:** Caracter

**Descrição:** Permite que sejam aglutinados os impostos PIS, COFINS e CSLL em apenas um titulo (Código de Retenção 5952).

**Conteúdo:**1 - Aglutina, 2 - Não aglutina

Para este título será considerada a **Natureza Padrão** a do parâmetro **MV\_PISNAT**no entanto se for necessário crie uma nova **Natureza** e informe-a neste parâmetro.

Informações adicionais:

<https://tdn.totvs.com/pages/releaseview.action?pageId=51252325>

<https://tdn.totvs.com/pages/releaseview.action?pageId=6076816>
