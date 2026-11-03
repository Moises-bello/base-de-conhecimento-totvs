---
content_hash: 2de0892bf7768e91c33030e2465eb9b7480c98ce68b05e09328c90676ffc8dc9
fetched_at: '2026-06-29T00:06:28.195086+00:00'
page_id: '233750668'
product: rm
source: tdn-rm
title: TUKHW6_DT_EduNotaEtapaData_WebService
type: documentation
url: https://tdn.totvs.com/display/LRM/TUKHW6_DT_EduNotaEtapaData_WebService
version: 119
---

# DataServer EduNotaEtapaData

|  |  |
| --- | --- |
| **Linha do Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Classis.NET/Conector* |
| **Função:** | *DataServer EduNotaEtapaData.* |
| **Situação/Requisito:** | **Utilização do DataServer EduNotaEtapaData através do TBC*.* |
| **Solução/Implementação:** | *Foi realizado uma alteração no DataServer EduNotaEtapaData para possibilitar o uso deste dataServer através do webservice "wsDataServer" do TBC.*  *Desta forma, será possível utilizar os métodos DoReadView, DoReadRecord e DoSaveRecord deste data server para manipular os registros da tabela SNOTAETAPA.*  *Segue abaixo alguns exemplos de utilização:*    **ReadView:**    Conteúdo dos parâmetros para a chamada do ReadViewAuth.   <soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:br="<http://www.totvs.com.br/br/>">  <soapenv:Header/>  <soapenv:Body>  <br:ReadViewAuth>  <!--Optional:-->  <br:DataServerName>EduNotaEtapaData</br:DataServerName>  <!--Optional:-->  <br:Filtro>SMATRICULA.CODCOLIGADA=1 AND SMATRICULA.RA='1728590'</br:Filtro>  <!--Optional:-->  <br:Contexto>CODCOLIGADA=1</br:Contexto>  <!--Optional:-->  <br:Usuario>mestre</br:Usuario>  <!--Optional:-->  <br:Senha>totvs</br:Senha>  </br:ReadViewAuth>  </soapenv:Body> </soapenv:Envelope>  **ReadRecord:**    Conteúdo dos parâmetros para a chamada do ReadRecordAuth.  <soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:br="<http://www.totvs.com.br/br/>">  <soapenv:Header/>  <soapenv:Body>  <br:ReadRecordAuth>  <!--Optional:-->  <br:DataServerName>EduNotaEtapaData</br:DataServerName>  <!--Optional:-->       <br:PrimaryKey>1;7;N;1728590;1231747</br:PrimaryKey>       <!--Optional:-->  <br:Contexto>CODCOLIGADA=1</br:Contexto>  <!--Optional:-->  <br:Usuario>mestre</br:Usuario>  <!--Optional:-->  <br:Senha>totvs</br:Senha>  </br:ReadRecordAuth>  </soapenv:Body> </soapenv:Envelope>    **SaveRecord:**      <soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:br="<http://www.totvs.com.br/br/>">  <soapenv:Header/>  <soapenv:Body>  <br:SaveRecordAuth>  <!--Optional:-->  <br:DataServerName>EduNotaEtapaData</br:DataServerName>  <!--Optional:-->  <br:XML><![CDATA[<EduNotaEtapa>  <SNotaEtapa>  <CODCOLIGADA>1</CODCOLIGADA>  <CODETAPA>7</CODETAPA>  <TIPOETAPA>N</TIPOETAPA>  <IDTURMADISC>590976</IDTURMADISC>  <RA>1231747</RA>  <NOTAFALTA>3,1000</NOTAFALTA>  </SNotaEtapa>  </EduNotaEtapa>]]></br:XML>  <!--Optional:-->  <br:Contexto>CODCOLIGADA=1</br:Contexto>  <!--Optional:-->  <br:Usuario>mestre</br:Usuario>  <!--Optional:-->  <br:Senha>totvs</br:Senha>  </br:SaveRecordAuth>  </soapenv:Body> </soapenv:Envelope> |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados vinculados:** | *N/A* |
| **Requisito:** | *N/A* |

divs
