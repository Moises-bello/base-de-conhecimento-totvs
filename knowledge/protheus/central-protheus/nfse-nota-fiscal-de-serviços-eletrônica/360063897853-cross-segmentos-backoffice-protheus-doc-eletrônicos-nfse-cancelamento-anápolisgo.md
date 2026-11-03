---
article_id: 360063897853
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: dad76f9b7f4dc60f6e7dcd2dfe49f584ab4817b4a868e9142d5470eb115d261f
fetched_at: '2026-06-28T22:39:56.342617+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Cancelamento
  Anápolis/GO - E160 (Arquivo Enviado Fora da Estrutura)
type: support-article
updated_at: '2025-06-25T13:17:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063897853-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Cancelamento-An%C3%A1polis-GO-E160-Arquivo-Enviado-Fora-da-Estrutura
---

**Dúvida**Ao transmitir um cancelamento para Anápolis-GO ocorre: ***"E160-ARQUIVO ENVIADO FORA DA ESTRUTURA DO ARQUIVO XML DE ENTRADA. ENVIE UM ARQUIVO DENTRO DO SCHEMA DO ARQUIVO XML DE ENTRADA."***  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - a partir da versão 12.1.23.  
 **Solução**O código do cancelamento é obrigatório para esse município.  
Habilite o parâmetro **MV\_CODCANC = .T.**  
Dessa forma, ao transmitir o cancelamento, será apresentado uma tela com as opções de cancelamento para seleção e transmissão.
