---
content_hash: 4adf3807c0ce5aa46d27a5ece37d14995da94c175a555585199d7e7a66c1def3
fetched_at: '2026-06-29T00:12:15.145824+00:00'
page_id: '971938059'
product: rm
source: tdn-rm
title: FISCAL01-26304 - NT_2025.001- QR-Code versão 3.0
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=971938059
version: 3
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão de Estoque, Compras e Faturamento |
| Função: | Envio NF-e / NFC-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-26304 |

## **02. SITUAÇÃO/REQUISITO**

Nesta NT está definido o novo leiaute do QR-Code da NFC-e (versão 3). Nesta nova versão, o controle sobre a autenticidade do conteúdo do QR-Code impresso no DANFE NFC-e será feito pela assinatura de campos específicos do QR-Code. Esse controle será feito unicamente para as NFC-e emitidas em Contingência, com a inclusão do resultado da assinatura no próprio QR-Code.  
Neste novo modelo, não será mais necessário o controle do CSC-Código de Segurança do Contribuinte pelas empresas.

## **03. SOLUÇÃO**

Em ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por filial, Edite a Filial:

Na etapa Ambiente NFC-e quando preenchido as informações de Código de segurança e ID do Código de Segurança estiverem preenchidos, o QR- Code será gerado na versão 2.0. Quando ambos os campos estiverem vazios, o QR-Code será gerado na versão 3.0.

Layout da versão 3.0.

• Para NFC-e emitida “on-line”: https://endereco-consulta-QRCode?p=<chave\_acesso>|<versao\_qrcode>|<tpAmb>  
• Para NFC-e emitida em contingência “off-line”: https:// endereco-consulta-QRCode?p=<chave\_acesso>|<versao\_qrcode>|<tpAmb>|<dia\_data\_emissao>|<vNF>|<tp\_idDest>|<idDest>|<assinatura>
