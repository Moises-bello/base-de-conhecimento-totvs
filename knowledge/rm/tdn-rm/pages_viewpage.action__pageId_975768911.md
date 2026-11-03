---
content_hash: 18f48f52a392704c1998437ff03711cc19dc69726484784dfa5e5eeb1acdb59b
fetched_at: '2026-06-29T00:12:15.288251+00:00'
page_id: '975768911'
product: rm
source: tdn-rm
title: Geração do QR-Code - Informações Suplementares
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=975768911
version: 20
---

## 2nonenone

# 1.Visão Geral

A Nota Fiscal de Consumidor Eletrônica (NFC-e) é um documento digital que substitui o tradicional cupom fiscal em estabelecimentos comerciais, proporcionando maior praticidade, segurança e agilidade nas operações de venda. Um dos elementos essenciais da NFC-e é o QR-Code, um código bidimensional que facilita a consulta e a validação da nota fiscal pelo consumidor e pelos órgãos fiscalizadores.

O QR-Code gerado na NFC-e contém informações importantes, como a chave de acesso da nota, dados do estabelecimento e a assinatura digital, permitindo que qualquer pessoa com um smartphone ou leitor específico possa consultar a autenticidade e os detalhes da nota em tempo real, diretamente no site da Secretaria da Fazenda.

# 2. Versão 2.0 do QR-Code

A versão 2.0 Do QR-Code será gerada quando nos parâmetros da NFC-e os dados de Autenticação estiverem Preenchidos:

Imagem  
  
  
Em ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por filial, Edite a Filial - etapa Ambiente NFC-e.  
Quando preenchido os campos: Código de Segurança e ID Código de Segurança, o QR-Code será gerado na versão 2.0.

## 2.1 Montagem da URL na versão 2.0:

### Para a NFC-e emitida “on-line:

Composição =  URL + Chave de acesso | Versão QR-Code | Tipo Ambiente | Identificador CSC | Código Hash  
  
https:// endereco-consultaQRCode?p=<chave\_acesso>|<versao\_qrcode>|<tipo\_ambiente>|<identificador\_csc>|<codigo\_hash>

xml4QR-Code - 2.0
https://hom.sat.sef.sc.gov.br/nfce/consulta?p=42250859269654000672650000000001231256690084|2|2|1|DC7BA13B573CBFFFCEA101B76A7A5F0842B19FBE
https://hom.sat.sef.sc.gov.br/nfce/consulta
]]>

### Para a NFC-e emitida em contingência “off-line:

Composição = URL + Chave de acesso | Versão QR-Code | Tipo Ambiente | Dia data Emissão | Valor Total NFCe | Dígito Verificador | Identificador CSC | Código Hash  
  
http:// endereco-consultaQRCode?p=<chave\_acesso>|<versao\_qrcode>|<tipo\_ambiente>|<dia\_data\_emissao>|<valor\_total\_nfce>|<digVal>|<identificador\_csc>|<codigo\_hash>

xml4QR-Code - 2.0
https://hom.sat.sef.sc.gov.br/nfce/consulta?p=42250859269654000672650000000001279251314372|2|2|08|10.00|5459722b6973556766566d4a6e5a49762f49323442735a475978343d|1|ED517879C7167628BE9A9F448DE46483CF219680
https://hom.sat.sef.sc.gov.br/nfce/consulta
]]>

# 3. Versão 3.0 do QR-Code

A versão 3.0 Do QR-Code será gerada quando nos parâmetros da NFC-e os dados de Autenticação não estiverem Preenchidos:

Imagem  
  
  
Em ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por filial, Edite a Filial - etapa Ambiente NFC-e.  
Quando não preenchido será gerado na versão 3.0.

## 3.1 Montagem da URL na versão 3.0:

### Para a NFC-e emitida “on-line:

Composição =  URL + Chave de acesso | Versão QR-Code | Tipo Ambiente |   
  
https:// endereco-consultaQRCode?p=<chave\_acesso>|<versao\_qrcode>|<tipo\_ambiente>|

xml4QR-Code - 3.0
https://hom.sat.sef.sc.gov.br/nfce/consulta?p=42250859269654000672650000000001261376978478|3|2
https://hom.sat.sef.sc.gov.br/nfce/consulta
]]>

### Para a NFC-e emitida em contingência “off-line:

Composição = URL + Chave de acesso | Versão QR-Code | Tipo Ambiente | Dia data Emissão | Valor Total NFCe | Tipo ID Destinatário | ID Destinatário | Assinatura  
  
https:// endereco-consulta-QRCode?p=<chave\_acesso>|<versao\_qrcode>|<tpAmb>|<dia\_data\_emissao>|<vNF>|<tp\_idDest>|<idDest>|<assinatura>

xml4QR-Code - 3.0
https://hom.sat.sef.sc.gov.br/nfce/consulta?p=42250859269654000672650000000001259381321528|3|2|08|10.00|1|59269654000672|4d4467617356526a4b307a5642627851704a6b4d6c5459664535413d
https://hom.sat.sef.sc.gov.br/nfce/consulta
]]>

# 4. DANFE - NFC-e

A DANFE (Documento Auxiliar da Nota Fiscal Eletrônica) é uma representação simplificada da Nota Fiscal Eletrônica (NFC-e), que acompanha o consumidor durante a compra. Diferente da nota fiscal tradicional em papel, a NFC-e é um documento digital, e a DANFE funciona como um comprovante impresso que traz informações essenciais da operação e também o QR-Code.  
  
A DANFE NFC-eestá disponível para importação no [TOTVS compartilhamento.](https://tdn.totvs.com/display/LRM/TOTVS+Compartilhamento)  
  
Acesse Gestão | Totvs Compartilhamento  
Faça o Filtro por Relatório > Controle de Estoque  
  
Importar DANFE

Imagem

DANFE NFCe

Imagem
