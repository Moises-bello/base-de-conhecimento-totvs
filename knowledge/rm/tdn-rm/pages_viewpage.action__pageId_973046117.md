---
content_hash: 0e9584fc494e6acead61c5b7ec306df1081d1323a45d5f4fc9b8ff43f4b23a65
fetched_at: '2026-06-29T00:12:15.186288+00:00'
page_id: '973046117'
product: rm
source: tdn-rm
title: Nota Técnica 2025.001
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=973046117
version: 22
---

# Conteúdo

2Conteúdononenone

# 1. Sobre

A **NT 2025.001**, publicada em 25 de março de 2025, tem mudanças na emissão e validação da **Nota Fiscal Eletrônica (NF-e)** e da **Nota Fiscal de Consumidor Eletrônica (NFC-e)**, com foco na simplificação operacional, aumento da segurança e padronização dos processos fiscais.

# 2. Cronograma

Esta Nota Técnica entra em vigor a partir de:

* Homologação a partir de **01/06/2025.**
* Produção a partir de **01/09/2025.**

# 3. Principais Alterações

A solução está disponível a partir dos patches:

Biblioteca RM

* 12.1.2410.282
* 12.1.2502.185
* 12.1.2506.126

TSS:



Com estes patches foram realizadas as seguintes alterações na montagem do xml da Nota:

## 3.1 QR-Code Versão 3 para NFC-e

Sempre que nos parâmetros "Ambiente NFC-e" os campos referente ao código de segurança estiverem em branco, será gerada a versão 3.0 do QRCode

Ambiente NFC-e

### Parâmetros Não preenchidos = Versão 3.0

#### Para a NFC-e emitida “on-line:

Composição =  URL + Chave de acesso | Versão QR-Code | Tipo Ambiente |   
  
https:// endereco-consultaQRCode?p=<chave\_acesso>|<versao\_qrcode>|<tipo\_ambiente>|

xml4QR-Code - 3.0
https://hom.sat.sef.sc.gov.br/nfce/consulta?p=42250859269654000672650000000001261376978478|3|2
https://hom.sat.sef.sc.gov.br/nfce/consulta
]]>

#### Para a NFC-e emitida em contingência “off-line:

Composição = URL + Chave de acesso | Versão QR-Code | Tipo Ambiente | Dia data Emissão | Valor Total NFCe | Tipo ID Destinatário | ID Destinatário | Assinatura  
  
https:// endereco-consulta-QRCode?p=<chave\_acesso>|<versao\_qrcode>|<tpAmb>|<dia\_data\_emissao>|<vNF>|<tp\_idDest>|<idDest>|<assinatura>

xml4QR-Code - 3.0
https://hom.sat.sef.sc.gov.br/nfce/consulta?p=42250859269654000672650000000001259381321528|3|2|08|10.00|1|59269654000672|4d4467617356526a4b307a5642627851704a6b4d6c5459664535413d
https://hom.sat.sef.sc.gov.br/nfce/consulta
]]>

### Parâmetros preenchidos = Versão 2.0

#### Para a NFC-e emitida “on-line:

Composição =  URL + Chave de acesso | Versão QR-Code | Tipo Ambiente | Identificador CSC | Código Hash  
  
https:// endereco-consultaQRCode?p=<chave\_acesso>|<versao\_qrcode>|<tipo\_ambiente>|<identificador\_csc>|<codigo\_hash>

xml4QR-Code - 2.0
https://hom.sat.sef.sc.gov.br/nfce/consulta?p=42250859269654000672650000000001231256690084|2|2|1|DC7BA13B573CBFFFCEA101B76A7A5F0842B19FBE
https://hom.sat.sef.sc.gov.br/nfce/consulta
]]>

#### Para a NFC-e emitida em contingência “off-line:

Composição = URL + Chave de acesso | Versão QR-Code | Tipo Ambiente | Dia data Emissão | Valor Total NFCe | Dígito Verificador | Identificador CSC | Código Hash  
  
http:// endereco-consultaQRCode?p=<chave\_acesso>|<versao\_qrcode>|<tipo\_ambiente>|<dia\_data\_emissao>|<valor\_total\_nfce>|<digVal>|<identificador\_csc>|<codigo\_hash>

xml4QR-Code - 2.0
https://hom.sat.sef.sc.gov.br/nfce/consulta?p=42250859269654000672650000000001279251314372|2|2|08|10.00|5459722b6973556766566d4a6e5a49762f49323442735a475978343d|1|ED517879C7167628BE9A9F448DE46483CF219680
https://hom.sat.sef.sc.gov.br/nfce/consulta
]]>

Para mais informações consulte:

## 3.2 Dados de Cobrança

De acordo com a regra de validação abaixo, o XML da nota fiscal **não** incluirá parcelas quando a forma e a condição de pagamento forem "à vista", evitando assim a rejeição 853.

> **Y09-40:** Se informado o grupo de Parcelas de cobrança (tag:dup, Id:Y07) com apenas uma ocorrência e a Data de vencimento (dVenc, id:Y09) for igual à data de emissão (dhEmi, id:B09, desconsiderando a hora). (NT 2025.001)
>
> **853/Rejeição:** Dados de cobrança não devem ser informados para pagamento a vista

Para mais informações consulte:

## 3.3 Dados de Pagamento

De acordo com a regra de validação abaixo, o grupo de pagamento passa a enviar a tag: Card, quando for NF-e e tipos de pagamento = cartões de credito ou cartões de Debito ou Pix.

> **YA04-10:** Se informado o grupo de pagamentos (tag:pag): Se o Pagamento for por cartão (tag:tPag=03, 04), ou PIX (tpag=17), deve ser informado o grupo de cartões (tag:card)
>
> Exceção: A regra de validação não se aplica, em produção, para Nota Fiscal com Data de Emissão anterior a 01/04/2016. (NT 2015.002)
>
> **391/Rejeição:** Não informados os dados do cartão de crédito / débito nas Formas de Pagamento da Nota Fiscal [nOcor:999]

Para mais informações consulte:

## 3.4 Transmissão Assíncrona

O TSS foi alterado para enviar de forma síncrona lotes que possuem apenas 1 documento,  evitando assim a rejeição abaixo

> **GAP03a-3:** Solicitação de resposta assíncrona (indSinc=0) para lote com somente 1 (uma) NF-e. (NT 2025.001)
>
> **452/Rejeição:** Solicitada resposta assíncrona para Lote com somente 1 (uma) NF-e

Para mais informações consulte:

# 4. Legislação

Este documento foi elaborado com base na [Nota Técnica 2025.001 v.1.01 - Publicada em 26/06/2025](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=uE%20fQh6OuYw=) no portal da NF-e.
