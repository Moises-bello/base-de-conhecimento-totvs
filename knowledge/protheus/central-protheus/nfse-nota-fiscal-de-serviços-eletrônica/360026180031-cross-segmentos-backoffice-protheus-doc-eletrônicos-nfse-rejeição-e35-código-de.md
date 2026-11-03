---
article_id: 360026180031
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: bb96ae82216f7e97aec0ce4e3defc090dbde15fddf73bede62cb34d2867713a4
fetched_at: '2026-06-28T22:39:58.468611+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Rejeição
  E35: Código de tributação inexistente'
type: support-article
updated_at: '2025-06-02T12:12:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026180031-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Rejei%C3%A7%C3%A3o-E35-C%C3%B3digo-de-tributa%C3%A7%C3%A3o-inexistente
---

**Dúvida**Como corrigir a rejeição: E35 - Código de tributação inexistente?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**Informe no campo B1\_TRIBMUN o Código de Tributação Municipal de acordo com sua prefeitura.  
  
Se o **conteúdo informado no B1\_TRIBMUN estiver no XML** e o erro persistir, deverá entrar em contato com a prefeitura questionando o código de tributação municipal válido (conteúdo e formato).  
  
**Obs.**: O campo padrão seria o B1\_TRIBMUN, porém poderá variar se por exemplo utilizar Indicadores de Produtos (BZ\_TRIBMUN) ou a rotina de alíquotas de ISS, onde caso será considerado o que gravar no F3 e FT\_TRIBMUN - a qual é de responsabilidade da equipe Fiscal.
