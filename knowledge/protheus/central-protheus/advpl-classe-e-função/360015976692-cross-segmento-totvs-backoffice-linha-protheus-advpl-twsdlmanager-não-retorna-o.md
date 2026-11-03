---
article_id: 360015976692
category: ADVPL - Classe e Função
content_hash: dc8b4b00424df9409a1a42b445af51ea3cd7ebe4d8e57f35734c3b4cfa3dfbdb
fetched_at: '2026-06-28T22:40:18.150286+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - TWsdlManager não
  retorna o xml com as tags completas
type: support-article
updated_at: '2022-06-14T17:39:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015976692-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-TWsdlManager-n%C3%A3o-retorna-o-xml-com-as-tags-completas
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min****Ocorrência**A Classe TWSDLMANAGER com SimpleInput e o retorno GetSoapMsg não retorna o Xml completo conforme abaixo.  
Segue fonte e evidencia para auxilio e entendimento:

```
<?xml version="1.0" encoding="UTF-8"?>  
<SOAP-ENV:Envelope xmlns:SOAP-ENV="Http://www.w3.org/2001/XMLSchema-instance">  
  <SOAP-ENV:Body>  
     <pesquisaProtocoloRequest xmlns="https://webservices.com.br/atendimento">  
        <statusProtocolo>ABERTO</statusProtocolo>  
        <usuario />  
     </pesquisaProtocoloRequest>  
  </SOAP-ENV:Body>  
</SOAP-ENV:Envelope>
```

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Causa**As Tags vem incompleta pois tem tipos complexos utilizados na mensagem  
  
**Solução**Neste caso deve-se utilizar o método oWsdl:ComplexInput() antes do simplesinput() onde os tipos complexos utilizados na mensagem do tipo input possuem número variável de ocorrências.

```
oWsdl:lUseNSPrefix := .T.  
//  
aComplex := oWsdl:ComplexInput()  
oWsdl:SetComplexOccurs( aComplex[1][1],1 )  
aSimple := oWsdl:simpleInput()
```

Para auxilio no desenvolvimento segue a documentação da Classe.  
  
**Saiba mais**  
[Classe TWsdlManager](http://tdn.totvs.com/display/tec/Classe+TWsdlManager)  
[TWsdlManager:lUseNSPrefix](http://tdn.totvs.com/display/tec/TWsdlManager%3AlUseNSPrefix)
