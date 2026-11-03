---
article_id: 360025250052
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: c8bcc77a647110ae08aeab45b770f4e870e29557c3249baa04b16ca700eab6fb
fetched_at: '2026-06-28T22:39:57.345268+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - E160: Arquivo
  enviado fora da estrutura do arquivo XML de entrada'
type: support-article
updated_at: '2025-06-10T18:41:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025250052-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-E160-Arquivo-enviado-fora-da-estrutura-do-arquivo-XML-de-entrada
---

**Dúvida**Como solucionar a rejeição E160: Arquivo enviado fora da estrutura do arquivo XML de entrada?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**A rejeição E160 na maioria das vezes está relacionada a ausência da **Inscrição Municipal do Prestador** dos Serviços.

Caso identifique no XML a tag <IncricaoMunicipal> do prestador em branco, deve realizar o procedimento abaixo para corrigir o erro.

- Acesse o cadastro da filial e preencha o campo Inscrição Municipal (M0\_INSCM);  
- Acesse rotina FISA022 e refaça o wizard.config, essa ação irá atualizar a IM na tabela SPED001a do TSS;  
- Retransmita e monitore a nota.
