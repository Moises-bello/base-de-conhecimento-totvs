---
article_id: 22837325234071
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 799df5ac5764d120d41273fdd3e3a01fa6e27338f930c4242c0d5909d3adf3f7
fetched_at: '2026-06-28T22:39:57.404218+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Element
  ''TipoRecolhimento'': This element is not expected.'
type: support-article
updated_at: '2024-06-13T18:45:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22837325234071-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Element-TipoRecolhimento-This-element-is-not-expected
---

**Dúvida**Qual é a correção para o erro de schema abaixo?  
  
*Element 'TipoRecolhimento': This element is not expected. Expected is one of (InscricaoMunicipalObra, ServicoObra, CodigoAtividade).*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24164484199191)  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**Esse erro ocorre para prefeituras que trabalham com o provedor DSFNET.  
Nesse layout o **CNAE (Atividade)** é obrigatório e sempre que estiver vazio ocorrerá o erro de schema.  
  
Veja abaixo todas as possibilidades de preenchimento do CNAE no Protheus:  
**[CNAE x Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061751034-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Possibilidades-de-montagem-de-C%C3%B3digo-de-Servi%C3%A7o-C%C3%B3digo-de-Tributa%C3%A7%C3%A3o-e-CNAE-NFSEXMLENV)**
