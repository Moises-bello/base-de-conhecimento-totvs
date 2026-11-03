---
article_id: 360017924151
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 07e3de69a06d156049c04bd4d02186d96c82637c7b6cb06e6b83c1e0deed9e8f
fetched_at: '2026-06-28T22:39:56.198798+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Parâmetro
  MV_NFSEDED (Valor de Dedução de Base de Cálculo no XML)
type: support-article
updated_at: '2025-07-18T14:50:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017924151-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Par%C3%A2metro-MV-NFSEDED-Valor-de-Dedu%C3%A7%C3%A3o-de-Base-de-C%C3%A1lculo-no-XML
---

**Dúvida**Configuração para que seja destacado o Valor de Dedução de Base de Cálculo no XML.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**  
No Configurador (**SIGACFG**), acesse Ambientes/Cadastros/Parâmetros e acrescente o parâmetro a seguir:

**Nome:** MV\_NFSEDED **Tipo:**L ***Cont. Por.:*** .T. **Descrição:**Este parâmetro determina quando o valor do desconto do item soma no valor deduções  
 **Obs.: Após a configuração do parâmetro o Protheus deverá ser reiniciado, caso contrário a configuração não terá efeito.**Segue abaixo a documentação complete referente à essa configuração.  
- <http://tdn.totvs.com/display/public/PROT/TVRLDL_DT_NFSE_PARAMETRO_MV_NFSEDED>
