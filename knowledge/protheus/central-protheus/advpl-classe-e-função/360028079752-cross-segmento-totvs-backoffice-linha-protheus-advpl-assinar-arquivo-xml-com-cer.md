---
article_id: 360028079752
category: ADVPL - Classe e Função
content_hash: fcbf2993971d725c85ab6fb400c59b06ef6a68b9699dcec911482e47dea7a2c6
fetched_at: '2026-06-28T22:40:14.460663+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Assinar arquivo
  xml com certificado digital
type: support-article
updated_at: '2022-01-03T21:39:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028079752-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Assinar-arquivo-xml-com-certificado-digital
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**É possível assinar um arquivo .XML por meio de assinatura digital utilizando um arquivo .PFX?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Sim, e para esta tratativa será necessário o uso das funções:

* EVPPrivSign()
* EVPDigest()

**Pré-requisitos**  
Para uso do exemplo abaixo são necessárias as seguintes premissas:

* Ambiente em servidor *Windows* (pois todos os caminhos [*paths*] estão com as barras formatadas para ambientes *Windows*);
* Criar abaixo do ROOTPATH as pastas DIRDOC e CERTIFICATE (pois no fonte, a leitura do .XML está sendo realizado com base na pasta DIRDOC e o arquivo .PFX está contido na pasta CERTIFICATE);
* Ter posse da senha do arquivo .PFX para inserir na variável cPassword;
* Ajustar a função RPCSetEnv() para o seu ambiente;
* Estrutura do .XML armazenado em DIRDOC ser similar a do exemplo abaixo.

**Exemplo**

Fonte

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
  
//--------------------------------------------------  
// ASSINA UM ARQUIVO XML DIGITALMENTE  
//--------------------------------------------------  
User Function T206SIGN()  
    Local cXML       As Character // CONTEÚDO XML  
    Local cDigest    As Character // VALOR DE RESUMO DO ARQUIVO  
    Local cSignInfo  As Character // CORPO DE INFORMAÇÕES DE ASSINATURA  
    Local cPassword  As Character // SENHA PARA LEITURA DO CERTIFICADO  
    Local cSignature As Character // CORPO DA ASSINATURA E CERTIFICADO  
    Local aCertific  As Array     // VETOR DE CERTIFICADOS  
  
    // PREPARAÇÃO DE AMBIENTE EM CASO DE ESTADO DE JOB  
    If (!IsBlind())  
        RPCSetEnv("99", "01")  
    EndIf  
  
    // INICIALIZAÇÃO DE VARIÁVEIS  
    cPassword  := "SUA_SENHA_AQUI"  
    cXML       := GetXMLFile("dirdoc", "SEU_XML_AQUI.xml")  
    cDigest    := GetDigest(cXML)  
    aCertific  := GetCertificate("\certificate", "NOME_ARQUIVO_PFX", cPassword)  
    cSignInfo  := GetSignInfo(Space(0), cDigest)  
    cSignature := GetSignature(aCertific, cSignInfo, cPassword)  
  
    // MONTA O XML COMPLETO  
    cXML := BuildXML(cXML, cSignature)  
  
    // SALVA O .XML COMPLETO NO CTRL+C  
    CopyToClipboard(cXML)  
  
    // ENCERRAMENTO DE AMBIENTE EM CASO DE ESTADO DE JOB  
    If (!IsBlind())  
        RPCClearEnv()  
    EndIf  
Return(NIL)  
  
//--------------------------------------------------  
// RETORNA O XML A SER ASSINADO  
//--------------------------------------------------  
Static Function GetXMLFile(cPath As Character, cFile As Character)  
    Local oFile As Object    // OBJETO DE ACESSO AO ARQUIVO .XML  
    Local cXML  As Character // CONTEÚDO DO ARQUIVO .XML  
  
    // INICIALIZAÇÃO DE VARIÁVEIS  
    cXML  := Space(0)  
    oFile := FwFileReader():New(cPath + "/" + cFile) // CAMINHO ABAIXO DO ROOTPATH  
  
    // SE FOR POSSÍVEL ABRIR O ARQUIVO, LEIA-O  
    // SE NÃO, EXIBA O ERRO DE ABERTURA  
    If (oFile:Open())  
        cXML := oFile:FullRead() // EFETUA A LEITURA DO ARQUIVO  
    Else  
        Final("Couldn't find/open file: " + cPath + "/" + cFile)  
    EndIf  
  
    // NORMALIZA O XML DA ASSINATURA  
    cXML := XMLSerialize(cXML)  
Return (cXML)  
  
//--------------------------------------------------  
// CALCULA O VALOR DO DIGEST  
//--------------------------------------------------  
Static Function GetDigest(cXML As Character)  
    Local cDigest As Character // VALOR DE RESUMO DO ARQUIVO  
  
    // INICIALIZAÇÃO DE VARIÁVEIS  
    cDigest := Space(0)  
  
    // CANONIZA O XML E CALCULA O DIGEST  
    cXML    := XMLSerialize(cXML)  
    cDigest := Encode64(EVPDigest(cXML, 3))  
Return (cDigest)  
  
//--------------------------------------------------  
// RETORNA O CAMINHO PARA OS ARQUIVOS (*CA.PEM,  
// *KEY.PEM E *CERT.PEM)  
//--------------------------------------------------  
Static Function GetCertificate(cCertPath As Character, cFileName As Character, cPassword As Character)  
    Local aCertific As Array     // VETOR DE CERTIFICADOS  
    Local cFullPath As Character // CAMINHO RELATIVO COMPLETO  
    Local cError    As Character // ERROS DE GERAÇÃO DE CERTIFICADO  
    Local lFind     As Logical   // VALIDADOR DE EXTRAÇÃO DE CERTIFICADO  
  
    // INICIALIZAÇÃO DE VARIÁVEIS  
    lFind     := .F.  
    aCertific := {}  
    cCertPath := cCertPath + "\"  
    cFullPath := Space(0)  
    cError    := Space(0)  
  
    // PROPRIEDADES PARA ARQUIVO *.CA  
    cError    := Space(0)  
    cFullPath := cCertPath + cFileName + "_ca.pem"  
    lFind     := File(cFullPath)  
  
    // VERIFICA SE O ARQUIVO JÁ EXISTE,  
    // CASO NÃO EFETUA A CRIAÇÃO  
    If (!lFind)  
        If (PFXCA2PEM(cCertPath + cFileName + ".pfx", cFullPath, @cError, cPassword))  
            ConOut(Repl("-", 80))  
            ConOut(MemoRead(cFullPath))  
            ConOut(Repl("-", 80))  
        Else  
            ConOut(Repl("-", 80))  
            ConOut(PadC("ERROR: Couldn't extract *_CA certificate", 80))  
            ConOut(Repl("-", 80))  
        EndIf  
    EndIf  
  
    // ADICIONA O CAMINHO NO RETORNO  
    AAdd(aCertific, {"CA", cFullPath, lFind})  
  
    // PROPRIEDADES PARA ARQUIVO *.KEY  
    cError    := Space(0)  
    cFullPath := cCertPath + cFileName + "_key.pem"  
    lFind     := File(cFullPath)  
  
    // VERIFICA SE O ARQUIVO JÁ EXISTE,  
    // CASO NÃO EFETUA A CRIAÇÃO  
    If (!lFind)  
        If (PFXKey2PEM(cCertPath + cFileName + ".pfx", cFullPath, @cError, cPassword))  
            ConOut(Repl("-", 80))  
            ConOut(MemoRead(cFullPath))  
            ConOut(Repl("-", 80))  
        Else  
            ConOut(Repl("-", 80))  
            ConOut(PadC("ERROR: Couldn't extract *_KEY certificate", 80))  
            ConOut(Repl("-", 80))  
        EndIf  
    EndIf  
  
    // ADICIONA O CAMINHO NO RETORNO  
    AAdd(aCertific, {"KEY", cFullPath, lFind})  
  
    // PROPRIEDADES PARA ARQUIVO *.CERT  
    cError    := Space(0)  
    cFullPath := cCertPath + cFileName + "_cert.pem"  
    lFind     := File(cFullPath)  
  
    // VERIFICA SE O ARQUIVO *.CERT JÁ EXISTE,  
    // CASO NÃO EFETUA A CRIAÇÃO  
    If (!lFind)  
        If (PFXCert2PEM(cCertPath + cFileName + ".pfx", cFullPath, @cError, cPassword))  
            ConOut(Repl("-", 80))  
            ConOut(MemoRead(cFullPath))  
            ConOut(Repl("-", 80))  
        Else  
            ConOut(Repl("-", 80))  
            ConOut(PadC("ERROR: Couldn't extract *_CERT certificate", 80))  
            ConOut(Repl("-", 80))  
        EndIf  
    EndIf  
  
    // ADICIONA O CAMINHO NO RETORNO  
    AAdd(aCertific, {"CERT", cFullPath, lFind})  
  
    // VERIFICA SE OS CERTIFICADOS BÁSICOS FORAM EXTRAÍDOS  
    If (!aCertific[2][3] .And. !aCertific[3][3])  
        Final("ERROR: Couldn't extract any certificate")  
    EndIf  
Return (aCertific)  
  
//--------------------------------------------------  
// CALCULA O SIGNEDINFO DA ASSINATURA  
//--------------------------------------------------  
Static Function GetSignInfo(cURI As Character, cDigest As Character)  
    Local cSignInfo As Character // CORPO DO SIGNEDINFO  
  
    // INICIALIZAÇÃO DE VARIÁVEIS  
    cSignInfo := Space(0)  
  
    // MONTAGEM DO SIGNEDINFO  
    cSignInfo += '<SignedInfo xmlns="http://www.w3.org/2000/09/xmldsig#">'  
    cSignInfo += '<CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/>'  
    cSignInfo += '<SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/>'  
    cSignInfo += '<Reference URI="' + cURI + '">'  
    cSignInfo += '<Transforms>'  
    cSignInfo += '<Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>'  
    cSignInfo += '</Transforms>'  
    cSignInfo += '<DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>'  
    cSignInfo += '<DigestValue>' + cDigest + '</DigestValue>  
    cSignInfo += '</Reference>'  
    cSignInfo += '</SignedInfo>'  
  
    // NORMALIZA O XML DA ASSINATURA  
    cSignInfo := XMLSerialize(cSignInfo)  
Return(cSignInfo)  
  
//--------------------------------------------------  
// GERA O CORPO DA ASSINATURA  
//--------------------------------------------------  
Static Function GetSignature(aCertific As Array, cSignInfo As Character, cPassword As Character)  
    Local oFile      As Object    // OBJETO DE ACESSO AO CERTIFICADO  
    Local cFile      As Character // CONTEÚDO DO CERTIFICADO  
    Local cError     As Character // ERROS DURANTE A CONVERSÃO  
    Local cXMLSign   As Character // CORPO .XML DA ASSINATURA  
    Local cSignature As Character // ASSINATURA  
  
    // INICIALIZAÇÃO DE VARIÁVEIS  
    cFile      := Space(0)  
    cError     := Space(0)  
    cXMLSign   := Space(0)  
    cSignature := Encode64(EVPPrivSign(aCertific[AScan(aCertific, {|aCert|aCert[1] == "KEY"})][2], cSignInfo, 3, cPassword, @cError))  
    oFile      := FwFileReader():New(aCertific[AScan(aCertific, {|aCert|aCert[1] == "CERT"})][2])  
  
    // SE FOR POSSÍVEL ABRIR O ARQUIVO, LEIA-O  
    // SE NÃO, EXIBA O ERRO DE ABERTURA  
    If (oFile:Open())  
        cFile := oFile:FullRead() // EFETUA A LEITURA DO ARQUIVO  
    Else  
        Final("Couldn't find/open file: " + cCertPath)  
    EndIf  
  
    // REMOVE A LINHA "BEGIN CERTIFICATE" E "END CERTIFICATE"  
    cFile := SubStr(cFile, At("BEGIN CERTIFICATE", cFile) + 22)  
    cFile := SubStr(cFile, 1, At("END CERTIFICATE", cFile) - 6)  
  
    // GERA A ESTRUTURA DE ASSINATURA DO .XML  
    cXMLSign += '<Signature xmlns="http://www.w3.org/2000/09/xmldsig#">'  
    cXMLSign += cSignInfo  
    cXMLSign += '<SignatureValue>' + cSignature + '</SignatureValue>'  
    cXMLSign += '<KeyInfo>'  
    cXMLSign += '<X509Data>'  
    cXMLSign += '<X509Certificate>' + cFile + '</X509Certificate>'  
    cXMLSign += '</X509Data>'  
    cXMLSign += '</KeyInfo>'  
    cXMLSign += '</Signature>'  
  
    // NORMALIZA O XML DA ASSINATURA  
    cXMLSign := XMLSerialize(cXMLSign)  
Return (cXMLSign)  
  
//--------------------------------------------------  
// SERIALIZA O XML NORMALIZANDO-O  
//--------------------------------------------------  
Static Function XMLSerialize(cXML)  
    Local cError   As Character // ERROS DURANTE A CONVERSÃO  
    Local cWarning As Character // AVISOS DURANTE A CONVERSÃO  
  
    // INICIALIZAÇÃO DE VARIÁVEIS  
    cError   := Space(0)  
    cWarning := Space(0)  
  
    // REMOVE SALTOS DE LINHA  
    cXML := StrTran(cXML, Chr(10), Space(0))  
    cXML := StrTran(cXML, Chr(13), Space(0))  
  
    // REMOVE ESPAÇOS EM BRANCO  
    While (At("> ", cXML) > 0)  
        cXML := StrTran(cXML, "> ", ">")  
    End  
  
    While (At(" <", cXML) > 0)  
        cXML := StrTran(cXML, " <", "<")  
    End  
  
    While (At(" </", cXML) > 0)  
        cXML := StrTran(cXML, " </", "</")  
    End  
  
    // CANONIZA O XML  
    cXML := XMLC14N(cXML, Space(0), @cError, @cWarning)  
Return (cXML)  
  
//--------------------------------------------------  
// MONTA O ARQUIVO .XML  
//--------------------------------------------------  
Static Function BuildXML(cXML As Character, cSignature As Character)  
    Local cTag     As Character // TAG DO CORPO  
    Local cNode    As Character // TAG A SER REMOVIDA  
    Local cFullXML As Character // XML COMPLETO  
  
    // INICIALIZAÇÃO DE VARIÁVEIS  
    cTag     := "nfd"  
    cNode    := Space(0)  
    cFullXML := Space(0)  
  
    // REMOVE A ÚLTIMA TAG  
    cNode := SubStr(cXML, At("</" + cTag + ">", cXML) + Len(cTag) + 3)  
    cXML := SubStr(cXML, 1, At("</" + cTag + ">", cXML) + Len(cTag) + 2)  
  
    // NORMALIZA O XML DA ASSINATURA  
    cFullXML := XMLSerialize(cXML + cSignature + cNode)  
Return (cFullXML)
```

  
ARQUIVO XML

```
<tbnfd>  
    <nfd>  
        <numeronfd>5123</numeronfd>  
        <codseriedocumento>2</codseriedocumento>  
        <codnaturezaoperacao>102</codnaturezaoperacao>  
        <codigocidade>3</codigocidade>  
        <inscricaomunicipalemissor>7540</inscricaomunicipalemissor>  
        <dataemissao>09/05/2019</dataemissao>  
        <razaotomador>SPORTECH AÇÕES DIGITAIS</razaotomador>  
        <nomefantasiatomador/>  
        <enderecotomador>AV. GUSTAVO GUSMÃO TAHIDE</enderecotomador>  
        <cidadetomador>SÃO PAULO</cidadetomador>  
        <estadotomador>SP</estadotomador>  
        <paistomador>BRASIL</paistomador>  
        <fonetomador/>  
        <faxtomador/>  
        <ceptomador>06783568</ceptomador>  
        <bairrotomador>ALPHAVILLE</bairrotomador>  
        <emailtomador>gustavo@sportech.com.br</emailtomador>  
        <cpfcnpjtomador>119210451000198</cpfcnpjtomador>  
        <inscricaoestadualtomador/>  
        <inscricaomunicipaltomador/>  
        <tbservico>  
            <servico>  
                <quantidade>1</quantidade>  
                <descricao>87990023</descricao>  
                <codatividade>15.21</codatividade>  
                <valorunitario>275.5</valorunitario>  
                <aliquota>3</aliquota>  
                <impostoretido>true</impostoretido>  
            </servico>  
        </tbservico>  
        <observacao/>  
        <razaotransportadora/>  
        <cpfcnpjtransportadora/>  
        <enderecotransportadora/>  
        <tipofrete>0</tipofrete>  
        <quantidade>0</quantidade>  
        <especie/>  
        <pesoliquido>0</pesoliquido>  
        <pesobruto>0</pesobruto>  
        <Pis>0</Pis>  
        <Cofins>0</Cofins>  
        <Csll>0</Csll>  
        <Irrf>0</Irrf>  
        <Inss>0</Inss>  
        <descdeducoesconstrucao/>  
        <totaldeducoesconstrucao/>  
        <tributadonomunicipio>true</tributadonomunicipio>  
        <numerort/>  
        <codigoseriert/>  
        <dataemissaort/>  
    </nfd>  
</tbnfd>
```

**Observações**  
O exemplo acima tem como finalidade ser apenas uma base para compreensão de como realizar a montagem da estrutura de um arquivo .XML assinado.  
Alterações serão necessárias para deixar o exemplo acima compatível com o ambiente cliente, e essa tratativa deve ser realizada pelo mesmo.  
  
**Saiba mais**  
[XMLC14N - APLICA O ALGORITMO CANONICALIZATION C14N](http://tdn.totvs.com/display/tec/XmlC14N)  
[FWFILEREADER - REALIZA LEITURA DE ARQUIVOS](http://tdn.totvs.com/display/framework/FWFileReader)  
[EVPPRIVSIGN - ASSINA USANDO ALGORITMO DIGEST](http://tdn.totvs.com/display/tec/EVPPrivSign)  
[PFXKEY2PEM - EXTRAI A CHAVE PRIVADA DE UM ARQUIVO COM EXTENSÃO .PFX](http://tdn.totvs.com/display/tec/PFXCA2PEM)  
[PFXCA2PEM - EXTRAI O CERTIFICADO DE AUTORIZAÇÃO DE UM ARQUIVO COM EXTENSÃO .PFX](http://tdn.totvs.com/display/tec/PFXCA2PEM)  
[PFXCERT2PEM - EXTRAI O CERTIFICADO DE CLIENTE DE UM ARQUIVO COM EXTENSÃO .PFX](http://tdn.totvs.com/display/tec/PFXCert2PEM)  
[EVPDIGEST - CALCULA O VALOR DO DIGEST](http://tdn.totvs.com/display/tec/EVPDigest)  
[ENCODE64 - GERA STRING CODIFICADA SEGUNDO O PADRÃO BASE64](http://tdn.totvs.com/display/tec/Encode64)
