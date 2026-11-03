---
article_id: 35527881997719
category: NFCOM - Nota Fiscal Fatura de Serviço de Comunicação Eletrônica
content_hash: 290335a96d2865089bebc326a5a7b34734413228a132f52bab1d429305e73b83
fetched_at: '2026-06-28T22:39:55.192451+00:00'
product: protheus
section_id: 33828030194199
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFCOM - Rejeição
  537 (Dados do contrato são obrigatórios para tipo de faturamento normal e centralizado)
type: support-article
updated_at: '2025-10-09T18:56:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35527881997719-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-Rejei%C3%A7%C3%A3o-537-Dados-do-contrato-s%C3%A3o-obrigat%C3%B3rios-para-tipo-de-faturamento-normal-e-centralizado
---

**Ocorrência**  
Ao realizar a transmissão de uma NFCOM ocorre a rejeição **537 - Dados do contrato são obrigatórios para tipo de faturamento normal e centralizado.**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Causa**  
Se o tipo de faturamento da NFCom for DIFERENTE de 2 (Cofaturamento) (tag: tpFat): Devem ser informados número do contrato (tag: nContrato) e data do início do contrato (tag: dContratoIni) Exceção: Essa regra não deverá ser aplicada quando informado o indicador de Cessão de Meios de Rede do grupo ide (tag: indCessaoMeiosRede).  
- <https://dfe-portal.svrs.rs.gov.br/Nfcom/ConsultaRegrasValidacao>   
  
**Solução**  
Para correção, as tags nContrato e dContratoIni devem ser geradas no XML.  
Ou seja, os campos  **FX\_NUMCONT**, **FX\_DINCONT** e **FX\_DFICONT** devem ser preenchidos no Complemento Fiscal (Tabela SFX).
