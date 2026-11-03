---
article_id: 360020242732
category: ADVPL - Classe e Função
content_hash: 34e0bf178ef22190b61b9bf99ac354afffdb47f91f1593c0432442c94e75c486
fetched_at: '2026-06-28T22:40:17.090719+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Protocolo CIPHER
type: support-article
updated_at: '2022-06-13T17:31:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020242732-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Protocolo-CIPHER
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**Gostaria de saber se existe alguma forma de configurar os protocolos "cipher" na Classe TWSDLMANAGER?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Verificamos internamente e na classe TWSDLMANAGER só existe a propriedade [nSSLVersion](http://tdn.totvs.com/display/tec/TWsdlManager%3AnSSLVersion), que determina o protocolo SSL/TLS utilizado pela classe.  
Entendendo como "ciphers", é um conjunto formado por protocolo seguro de transporte + algoritmos de criptografia + alguns opcionais, temos na camada do servidor do Protheus hoje: [Seção [SSLConfigure].](http://tdn.totvs.com/pages/viewpage.action?pageId=6064865)  
- Protocolos seguros de transporte: SSLv2, SSLv3, TLSv1.0, TLSv1.1, TLSv1.2  
- Algoritmos de criptografia suportados - para as funções Advpl: MD5,SHA1, RIPEMD160, MD5\_SHA1, SHA256WithRSA, SHA256  
- Opcionais ("Schemas " de padding) - para as funções Advpl: PKCS1, SSL, PKCS1\_OAEP, X931.  
  
Segue documentação para configuração do protocolo de transporte seguro SSL / TLS <http://tdn.totvs.com/pages/viewpage.action?pageId=319789062>
