---
article_id: 360062588253
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: e9da104639682d6c965870f145886e9a1ef1ffef03b33a5300900dcef880e7c9
fetched_at: '2026-06-28T22:39:57.370317+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - E330 - LOCAL
  DA PRESTAÇÃO DIFERENTE DO LOCAL DA OBRA (GINFES)
type: support-article
updated_at: '2025-07-08T19:54:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062588253-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-E330-LOCAL-DA-PRESTA%C3%87%C3%83O-DIFERENTE-DO-LOCAL-DA-OBRA-GINFES
---

**Ocorrência**Ao realizar a transmissão de um RPS onde o município utiliza o provedor GINFES ocorre a rejeição: ***E330 - LOCAL DA PRESTAÇÃO DIFERENTE DO LOCAL DA OBRA.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100964414/mceclip0.png)***  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**Essa rejeição ocorre pelo fato das informações entre Código da Obra x Município de Prestação informados no XML não estarem alinhados com o mesmo município.  
  
*Obs.: O código da obra possui a relação com um município X de acordo com cada prefeitura, portanto é de extrema importância verificar e solicitar essa informação para a prefeitura ao utilizar serviços relacionados a obra.*  
  
**Solução**Após verificado com a prefeitura, deixar alinhados os campos abaixo para a montagem correta do XML com o mesmo município:  
  
**C5\_OBRA** = Código da Obra  
**C5\_ESTPRES e C5\_MUNPRES** = Munícipio de Prestação do Serviço (caso não informados ambos os campos é considerado por padrão o município do cadastro do cliente).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103138593/mceclip0.png)
