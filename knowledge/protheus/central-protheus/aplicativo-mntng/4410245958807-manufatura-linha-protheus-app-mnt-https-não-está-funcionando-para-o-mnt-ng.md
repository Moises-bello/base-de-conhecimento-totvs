---
article_id: 4410245958807
category: 'Aplicativo MNTNG '
content_hash: 12ddef7cf8f7e6de2f35d4431dc57f7be2e498892508fcdde73bc5d16bb57bf5
fetched_at: '2026-06-28T22:42:37.703778+00:00'
product: protheus
section_id: 360010992174
source: central-protheus
title: Manufatura - Linha Protheus - APP MNT - Https não está funcionando para o MNT
  NG
type: support-article
updated_at: '2022-05-10T18:21:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410245958807-Manufatura-Linha-Protheus-APP-MNT-Https-n%C3%A3o-est%C3%A1-funcionando-para-o-MNT-NG
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:00:30 min****Ocorrência**No **Aplicativo MNTNG** ocorre a mensagem **Detalhes relacionados a utilização de certificados/protocolo Https**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Aplicativo MNTNG - Todas as versões  
  
**Causa**Essa mensagem ocorre porque o certificado **autoassinado** não é suportado pelo aplicativo.  
  
**Solução**

* Certificado **autoassinado** não é suportado pelo aplicativo;
* Certifique-se da data de validade do certificado;
* Recomendamos a validação do certificado por portais como [SSL Server Test](https://www.ssllabs.com/ssltest/) ou [SSL Checker](https://www.sslshopper.com/ssl-checker.html)
