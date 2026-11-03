---
article_id: 360025886312
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 34d5d8895c7f4307551b0c1007c5f5640266634bd23a8882df879484d7e20955
fetched_at: '2026-06-28T22:39:58.504758+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - SAO PAULO:
  Conteudo TributacaoRPS'
type: support-article
updated_at: '2026-06-22T18:55:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025886312-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-SAO-PAULO-Conteudo-TributacaoRPS
---

**Dúvida**  
Definição para os conteúdos da tag TributacaoRPS do município de São Paulo-SP  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**  
O significado do conteúdo da tag <TributacaoRPS> a prefeitura de São Paulo esclarece no manual de integração disponível no link abaixo:

http://nfpaulistana.prefeitura.sp.gov.br/arquivos/manual/NFe\_Web\_Service.pdf

T – Tributado em São Paulo  
F – Tributado Fora de São Paulo  
A – Tributado em São Paulo, porém Isento  
B – Tributado Fora de São Paulo, porém Isento  
M – Tributado em São Paulo, porém Imune  
N – Tributado Fora de São Paulo, porém Imune  
X – Tributado em São Paulo, porém Exigibilidade Suspensa  
V – Tributado Fora de São Paulo, porém Exigibilidade Suspensa  
P – Exportação de Serviços

Para composição dessa tag são usados os campos **F4\_ISSST (Legado) ou F4\_NATOPNF** (Configurador de Tributos), além de que para as tributações que envolvem os tipos Isento, Imune e Exigibilidade também deve ser usado o campo B1\_MEPLES.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097052074)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099358233)

A tributacaoRPS será gerada com **P - Exportação de Serviços** conforme documentação própria abaixo:  
[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Exportação de Serviços São Paulo-SP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041232294-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Exporta%C3%A7%C3%A3o-de-Servi%C3%A7os-S%C3%A3o-Paulo-SP)  
  
**Importante:** Usar versão **2.00** no wizard.config da rotina FISA022.
