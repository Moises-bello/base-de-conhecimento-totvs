---
content_hash: 6fa51b1c2bf32d03b7e38355f9d6c809c529c5785db7840a479d3cdf6c3e97ee
fetched_at: '2026-06-29T00:11:12.241787+00:00'
page_id: '65208592'
product: rm
source: tdn-rm
title: Certificado Digital - Troca Certificado Digital
type: documentation
url: https://tdn.totvs.com/display/LRM/Certificado+Digital+-+Troca+Certificado+Digital
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NF-e                        **Versão:***todas* |
| **Processo** | **:** | Certificado Digital - Troca Certificado Digital |
| **Subprocesso** | **:** | Certificado Digital - Troca Certificado Digital |
| **Data da publicação** | **:** | 04/07/2013 |

**Introdução:**

Para realizar a emissão de notas fiscais eletrônicas, é necessário utilizar o Certificado Digital, que é a assinatura da empresa na Nota Fiscal Eletrônica. O mesmo tem uma data de validade, e após esta data de validade, é necessário adquirir um novo arquivo certificado e realizar a troca do mesmo no sistema.

**OBSERVAÇÃO: Realize a preparação do certificado digital antes de executar o procedimento. A documentação esta disponível nos Documentos da comunidade R@ NFE, arquivo “Como Fazer - Certificado Digital - Preparar Certificado Digital para Emissão de NF-E”.**

**1º Passo:**

O primeiro passo para realizar a troca do certificado digital, é realizar a exclusão dos arquivos referentes ao certificado digital no TSS. Para isto, acesse a pasta raiz de instalação do TSS ( O diretório padrão é C:/totvssped ) e realize a exclusão de TODOS arquivos com a extensão “.PEM” da pasta CERTS:

**OBSERVAÇÃO: Caso existam mais filiais que realizam a emissão de notas fiscais eletrônicas, os arquivos referentes ao certificado digital também serão excluídos no TSS. Após realizar o envio da primeira NF-e ou a execução do processo “Monitor Sefaz”, os arquivos serão recriados.**

**2º Passo:**

Após realizar a exclusão dos arquivos, acesse a pasta BIN, subpasta APPSERVER e abra o arquivo APPSERVER. Este arquivo tem a extensão “Parâmetro de Configuração”.

Realize a exclusão das linhas com as iniciais “CertificateClient” e “Keyclient”, que apontam os arquivos referentes ao certificado na pasta CERTS:

**3º Passo:**

Será necessário reiniciar o serviço TSS para finalizar a exclusão dos arquivos certificado no aplicativo. Acesse o menu Iniciar, Painel de controle, Ferramentas administrativas, serviços. Clique no serviço “TSS” e clique em “Reiniciar”:

**4º Passo:**

No RM Nucleus, acesse o menu Opções, Parâmetros, RM Nucleus, Integrações, Fiscal, etapa Parâmetros por Filial. Selecione a filial que ocorrerá a troca do certificado digital e de um "duplo clique" sobre ela:        

Na etapa 3 – Certificação Digital ½, realize o preenchimento do diretório do arquivo certificado digital e senha. Salve os parâmetros avançando até o final.

**5º Passo:**

Para finalizar a troca do certificado digital, é necessário enviar uma nova NF-E através do menu Utilitários, SPED, NF-e (Estadual), processos, “Enviar NF-E” ou a execução do processo “Monitor Sefaz”. Após o envio ou a execução do Monitor, serão criados os novos arquivos referentes ao certificado digital.

**Para maiores informações:**

**[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica)
