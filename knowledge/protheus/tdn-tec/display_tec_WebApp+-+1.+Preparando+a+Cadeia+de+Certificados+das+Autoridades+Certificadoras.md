---
content_hash: e49d6207d4a01d134de404dd9c9927e71a602368417ac56af9a92b23fb4edafe
fetched_at: '2026-07-02T19:24:24.820948+00:00'
page_id: '490316948'
product: protheus
source: tdn-tec
title: WebApp - 1. Preparando a Cadeia de Certificados das Autoridades Certificadoras
type: documentation
url: https://tdn.totvs.com/display/tec/WebApp+-+1.+Preparando+a+Cadeia+de+Certificados+das+Autoridades+Certificadoras
version: 5
---

Uma Autoridade Certificadora (AC) é uma entidade, pública ou privada, responsável por emitir, distribuir, renovar, revogar e gerenciar certificados digitais. Tem a responsabilidade de verificar se o titular do certificado possui a chave privada que corresponde à chave pública que faz parte do certificado. Cria e assina digitalmente o certificado do assinante, onde o certificado emitido pela AC representa a declaração da identidade do titular, que possui um par único de chaves (pública/privada). Os certificados dessas Autoridades são chamados de cadeias de certificação ou hierarquia de certificação.

Para a validação de um certificado de cliente, como o e-CPF, é necessário que ele seja assinado pelas Autoridades Certificadoras. Você pode baixar as Cadeias de Certificados dos sites das Certificadoras:

* **[Certisign](https://www.certisign.com.br/atendimento-suporte/downloads/hierarquias/icp-brasil/e-cpf)**
* **[Serasa](https://serasa.certificadodigital.com.br/instalacaoa3/)**
* **[Caixa Economica Federal](http://www.caixa.gov.br/empresa/identidade-digital/Paginas/default.aspx)**

Entre outras. Clique **[aqui](http://www.iti.gov.br/icp-brasil/estrutura)** para a lista completa.

Apos isso, você deverá realizar preparações especificas para o tipo de conector que esta usando.

# Utilizando conector APR

Para a utilização da cadeia de certificados pelo conector ARP, é necessário concatenar os arquivos dos certificados, ordenados da mais alta (AC Raiz) para as intermediarias.

Você pode fazer isso usando os comandos:

**Windows**

|  |
| --- |
| `type` `ACRaizBrasileira_v2.cer ACRFBv3.cer AC_Certisign_RFB_G4.cer > TrustCACerts.cer` |

**Linux**

|  |
| --- |
| `cat` `ACRaizBrasileira_v2.cer ACRFBv3.cer AC_Certisign_RFB_G4.cer > TrustCACerts.cer` |

Isso irá gerar o arquivo **TrustCACerts.cer**, contendo os 3 certificados da cadeia.

Próximo passo: **[Configurando o AppServer](http://tdn.totvs.com/display/tec/WebApp+-+2.+Configurando+o+AppServer)**
