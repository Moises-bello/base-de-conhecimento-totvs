---
article_id: 10211078234391
category: ACOMPANHA CUSTOS - JORNADA DE FECHAMENTO (NOVO)
content_hash: 749bea60b648ef2ec6f2a84d4e17a3ad1505214360d7328c1ffc593564b495d0
fetched_at: '2026-06-28T22:38:48.091432+00:00'
product: protheus
section_id: 5367899706647
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - ERR_CERT_COMMON_NAME_INVALID
  rotina Acompanha Custos
type: support-article
updated_at: '2025-03-12T12:23:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10211078234391-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-ERR-CERT-COMMON-NAME-INVALID-rotina-Acompanha-Custos
---

**Dúvida**Ao tentar efetuar o acesso a rotina MATA038 - Acompanha Custos, é apresentado a mensagem de "não é possível acessar esse site", destinando o caminho e o erro ERR\_CERT\_COMMON\_NAME\_INVALID, como resolver?  
  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33.

**Solução**

Esse erro é comum para ambientes cujo certificado em uso é o padrão, disponível no pacote do TOTVS | Application Server liberado no Portal de Suporte TOTVS.

O erro de (ERR\_CERT\_COMMON\_NAME\_INVALID e ERR\_CERT\_INVALID ) esta atrelado na validação do host/IP não corresponde ao listado em seu certificado SSL, onde você utiliza o padrão da TOTVS disponibilizado na pasta AppServer.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10211008744215)

## Como resolver este problema?

Para abordar a solução deste cenário, vamos supor os seguintes dados do Servidor de Aplicação:

| Hostname do servidor | IP do servidor |
| --- | --- |
| PRD-MATRIZ | 10.41.1.7 |

Para o correto funcionamento do ambiente, será necessário gerar um novo certificado, prevendo o hostname e/ou ip do servidor de aplicação.

Para tal, o procedimento abaixo pode ser utilizado como base para geração do certificado:

### Passo 1

Para gerar o certificado, na máquina onde está o servidor de aplicação, execute:  totvs\_certificates -host "hostname" -host "IP"  
*[Download do totvs\_certificates...](https://tdn.totvs.com/pages/viewpage.action?pageId=630370186#Acessoaoambientegeraaocorr%C3%AAnciadamensagemdeerro:ERR_CERT_COMMON_NAME_INVALIDouERR_CERT_AUTHORITY_INVALID-ttvs_certificate)*

Exemplo:

```
c:\totvs>totvs_certificates.exe -host PRD-MATRIZ -host 10.41.1.7
TOTVS - certificate generator (Version: 1.0)

Generating certificate for: "TOTVS certificate CA - PRD-MATRIZ"


Adding hosts: PRD-MATRIZ 10.41.1.7

--- Generated ---
Certificate : totvs_certificate.crt
Key : totvs_certificate_key.pem
```

**Lembre-se**

O [hostname] e/ou [ip] do servidor de aplicação devem (ou deveriam) ser os mesmo utilizados na seção [TCP] do smartclient.ini que atende aos clients ou os mesmos utilizados para acesso via browse.

### Passo 2

Após a geração dos arquivos de certificado (totvs\_certificate.crt) e chave (totvs\_certificate\_key.pem), utilize-os para a configuração do appserver.ini do ambiente.

**Lembre-se**

Faça uma cópia dos arquivos gerados para a pasta do TOTVS | Application Server em uso.

### Passo 3

Nas máquinas onde é executado o SmartClient deve-se fazer a instalação do Certificado da certificadora TOTVS (totvs\_certificate\_CA.crt).

Este arquivo é distribuído junto com o pacote do TOTVS | Application Server baixado do Portal de Suporte.

Dúvidas posteriores, contatar o time "**Protheus Framework**".

**Saiba mais**

*[Geração de Certificado e Download do executável totvs\_certificates.exe](https://tdn.totvs.com/pages/viewpage.action?pageId=548376390)*

*[Instalação de Certificado](https://tdn.totvs.com/pages/viewpage.action?pageId=539526365)*

*[Application Server - Porta Multiprotocolo](https://tdn.totvs.com/display/tec/Application+Server+-+Porta+Multiprotocolo)*

*[Porta Multiprotocolo - Instalação de Certificado](https://tdn.totvs.com/pages/viewpage.action?pageId=539526365)*

*[Porta Multiprotocolo - Geração de Certificado](https://tdn.totvs.com/pages/viewpage.action?pageId=548376390)*

*[Clique aqui e veja mais artigos sobre a Nova Jornada de Fechamento no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/5367899706647-ACOMPANHA-CUSTOS-JORNADA-DE-FECHAMENTO-NOVO-)*
