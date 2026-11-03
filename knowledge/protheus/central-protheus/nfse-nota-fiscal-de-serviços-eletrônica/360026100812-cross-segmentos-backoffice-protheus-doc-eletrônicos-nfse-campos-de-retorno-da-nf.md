---
article_id: 360026100812
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 09b101ff73e4dbd08e32902dd26a22ceac1de82c71584e9cddbe47d8238cf47c
fetched_at: '2026-06-28T22:39:56.340543+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Campos de
  Retorno da NFSe
type: support-article
updated_at: '2026-06-22T21:12:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026100812-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Campos-de-Retorno-da-NFSe
---

**Dúvida**  
Quais são os campos que carregam os dados de retorno da prefeitura com autorização da nota de serviços?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**  
Os campos abaixo existem nas tabelas SF2, SFT e SF3.

Esses campos tem a finalidade de guardar algumas informações da NFSe gerada na prefeitura.

\_NFELETR -> Numero da NFSE gerada na prefeitura ou governo  
\_CODNFE  -> Numero do protocolo de autorização ou chave de autorização (emissor nacional)  
\_EMINFE   -> Data de autorização  
\_HORNFE  -> Hora de autorização  
Obs: Na tabela SE1 também é gerado o E1\_NFELETR

**O preenchimento dos campos acontece após monitoramento (FISA022 > Monitor) de uma nota autorizada.**  
Os campos F3\_CODRET e F3\_CODRSEF também são alterados após transmissão e monitoramento de uma nota.  
  
**IMPORTANTE:**  
Caso utilize essa documentação para a rejeição E10 - RPS Já Informado, onde o município não possui Consulta RPS para atualizar de forma automática o status, **não deverá ser monitorada a nota**, caso contrário os dados preenchidos manualmente serão perdidos e serão considerados o da própria rejeição.
