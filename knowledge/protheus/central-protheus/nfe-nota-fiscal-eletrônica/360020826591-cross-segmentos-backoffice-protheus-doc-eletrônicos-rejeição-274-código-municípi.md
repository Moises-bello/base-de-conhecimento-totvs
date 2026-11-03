---
article_id: 360020826591
category: NFe - Nota Fiscal Eletrônica
content_hash: 59cc42a95b03f17d037759d229b1201993377769ededdc607c0476dc215dabb5
fetched_at: '2026-06-28T22:40:03.703549+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Rejeição 274:
  Código Município do Destinatário: dígito inválido ao transmitir Nota fiscal eletrônica'
type: support-article
updated_at: '2024-09-09T21:15:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020826591-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Rejei%C3%A7%C3%A3o-274-C%C3%B3digo-Munic%C3%ADpio-do-Destinat%C3%A1rio-d%C3%ADgito-inv%C3%A1lido-ao-transmitir-Nota-fiscal-eletr%C3%B4nica
---

**Dúvida**Como corrigir a rejeição 274: Código Município do Destinatário: dígito inválido ao transmitir Nota fiscal eletrônica ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Esta rejeição ocorre quando o código do Município informado na *tag*Cmun conforme descrição está errada no cadastro do cliente ou fornecedor:

1- É necessário ajustar a informação no cadastro do cliente e o campo deve ser composto por 07 dígitos.

Se for cadastro de **cliente** preencher:

**A1\_EST** (dois primeiros digitos são representados pelo do cadastro do estado) e **A1\_COD\_MUN** (demais cinco próximos digitos do código do municipio)

Exemplo abaixo o código do municipio é **3550308** referente ao múnicipio de São Paulo, desta forma o preenchimento fica:

**A1\_EST** = SP

**A1\_COD\_MUN** = 50308

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059159754)

Se cadastro de **fornecedor** preencher:

**A2\_EST** (dois primeiros digitos são representados pelo do cadastro do estado) e **A2\_COD\_MUN** (demais cinco próximos digitos do código do municipio)

O padrão segue o mesmo abaixo o código do municipio é **3550308** referente ao múnicipio de São Paulo, desta forma o preenchimento fica:

**A1\_EST** = SP

**A1\_COD\_MUN** = 50308

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059160014)

2- Após isso, exclua a nota e gere novamente.

Dúvidas sobre o Código de Município podem ser esclarecidas no site do IBGE através do link:

<https://www.ibge.gov.br/explica/codigos-dos-municipios.php>

O código do estado fica gravado na tabela CC2.
