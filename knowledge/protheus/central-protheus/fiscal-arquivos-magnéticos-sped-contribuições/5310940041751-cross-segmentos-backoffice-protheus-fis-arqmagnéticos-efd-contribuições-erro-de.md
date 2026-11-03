---
article_id: 5310940041751
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 5b640dd39103903f584400e40fd94800f800ec2f3775f59e234087f5c8612273
fetched_at: '2026-06-28T22:42:06.607454+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  erro de sincronismo ao gerar o arquivo do EFD Contribuições
type: support-article
updated_at: '2023-03-06T14:26:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5310940041751-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-erro-de-sincronismo-ao-gerar-o-arquivo-do-EFD-Contribui%C3%A7%C3%B5es
---

**Ocorrência**  
Ao tentar gerar o arquivo do **Sped Contribuições** através da rotina abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5310723814167/mceclip0.png)  
  
Ocorre o seguinte  erro de sincronismo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5310763118487/mceclip1.png)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (**Linha Protheus**) -  A partir da versão **12.1.25**  
  
**Causa**  
Esse incidente ocorre, pois a parametrização do sistema está incorreta para *MULTITHREAD*  
  
**Solução**Para correção do erro os parâmetros **MV\_QTAEC** e  **MV\_QTDTAEC** devem ser ser configurados conforme abaixo:  
  
**MV\_QTAEC = 5**  
**MV\_QTDTAEC = 5**  
  
Após alteração dos parâmetros saia do sistema, gere novamente a apuração e por fim o arquivo magnético.
