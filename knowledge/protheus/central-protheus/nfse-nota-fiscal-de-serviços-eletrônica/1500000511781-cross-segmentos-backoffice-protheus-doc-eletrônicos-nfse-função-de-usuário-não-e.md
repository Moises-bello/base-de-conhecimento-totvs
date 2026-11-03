---
article_id: 1500000511781
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 9aeda0e9f0d7823b00e10c4fbcc0b6b420e15d747db6881ccbeaebd8aabef5af
fetched_at: '2026-06-28T22:39:57.455918+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Função de
  usuário não está com U_nfseXMLEnvpositório
type: support-article
updated_at: '2023-03-13T17:14:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000511781-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Fun%C3%A7%C3%A3o-de-usu%C3%A1rio-n%C3%A3o-est%C3%A1-com-U-nfseXMLEnvposit%C3%B3rio
---

**Dúvida**

Na tentativa de transmissão de uma NFSe na rotina FISA022 ocorre o erro abaixo:  
  
**Função de usuário não está com U\_nfseXMLEnvpositório**  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000558222/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**O erro ocorre porque o rdmake **NFSEXMLENV** não existe no RPO do Protheus.  
Para solução, compile o rdmake NFSEXMLENV disponível no link abaixo:  
- <https://suporte.totvs.com/portal/p/10098/download#detail/1083728>
