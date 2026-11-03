---
content_hash: 5caef80ccfbc70c4cd82eef914af4783b6d922b08d809cc304caa8b21766e1df
fetched_at: '2026-06-29T00:05:51.739671+00:00'
page_id: '1054135207'
product: rm
source: tdn-rm
title: Geração de QRCode PIX de boleto já existente na base
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1054135207
version: 2
---

## **Exemplo do xml de geração de QRCode PIX de boleto já existente na base.**

## **(http://localhost:8051/wsProcess/IwsProcess)**

Observação: Método utilizado ExecuteWithParams

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
    <soapenv:Header/>  
    <soapenv:Body>  
        <tot:ExecuteWithParams>  
            <!--Optional:-->  
            <tot:ProcessServerName>FinPaymentHubGeraQRCodeProcess</tot:ProcessServerName>  
            <!--Optional:-->  
            <tot:strXmlParams><![CDATA[  
<FinPaymentHubGeraQRCodeParamsProc>  
<Context>  
    <CODCOLIGADA>1</CODCOLIGADA>  
    <CODUSUARIO>mestre</CODUSUARIO>  
    <CODSISTEMA>F</CODSISTEMA>  
</Context>  
    <QRCodePixInfoList>  
        <FinInfoGeracaoQRCodePix>  
            <Registros>  
                    <FinKeyBoleto>  
                    <CodColigada>1</CodColigada>  
                    <CodFilial>1</CodFilial>  
                    <IdBoleto>123456</IdBoleto>  
                </FinKeyBoleto>  
            </Registros>  
        </FinInfoGeracaoQRCodePix>  
    </QRCodePixInfoList>  
</FinPaymentHubGeraQRCodeParamsProc>  
]]></tot:strXmlParams>  
        </tot:ExecuteWithParams>  
    </soapenv:Body>  
</soapenv:Envelope>
