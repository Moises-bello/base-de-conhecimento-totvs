---
article_id: 360024874454
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 5f740bace8c85d63756bfc7c678f4735602a71397f7db502fea3a52f95ae139c
fetched_at: '2026-06-28T22:39:58.462797+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Rejeição
  E181: O documento XML de entrada do serviço está fora do padrão especificado'
type: support-article
updated_at: '2025-06-25T20:56:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024874454-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Rejei%C3%A7%C3%A3o-E181-O-documento-XML-de-entrada-do-servi%C3%A7o-est%C3%A1-fora-do-padr%C3%A3o-especificado
---

**Dúvida**Ao transmitir um RPS para prefeitura ocorre a rejeição abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038374414/mceclip0.png)

**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**Essa rejeição pode ocorrer em duas situações:  
1 - Quando há caracter especial no conteúdo da nota.  
2 - Quando a Inscrição Municipal do Prestador do serviço está vazia no lote.  
  
**Para a questão dos caracteres especiais**, revise todos os cadastros, especialmente a discriminação dos serviços.  
**Para a Inscrição municipal do contribuinte,**  preencha o campo Inscrição Municipal no cadastro da filial, em seguida acesse a rotina FISA022 e reconfigure o wizard config. dessa forma a IM será atualizada nas tabelas do TSS.
