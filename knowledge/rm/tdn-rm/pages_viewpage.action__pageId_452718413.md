---
content_hash: 48e2bf5b0a88494732838df723354a9557ddb56ae7a698a0fbf1220ebd77909c
fetched_at: '2026-06-29T00:09:59.837591+00:00'
page_id: '452718413'
product: rm
source: tdn-rm
title: Importação de RNT - Exemplo Arquivo XSD
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718413
version: 1
---

**Importação de RNT - Exemplo Arquivo XSD**   
**Exemplo Arquivo XSD:**  
<?xml version="1.0" encoding="utf-8"?> <xs:schema id="arquivo" xmlns="" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">   <xs:element name="arquivo" msdata:IsDataSet="true" msdata:Locale="en-US">     <xs:complexType>       <xs:choice minOccurs="0" maxOccurs="unbounded">         <xs:element name="rnt">           <xs:complexType>             <xs:sequence>               <xs:element name="codcoligada" type="xs:string" minOccurs="0" />               <xs:element name="codpessoa" type="xs:string" minOccurs="0" />               <xs:element name="data" type="xs:string" minOccurs="0" />               <xs:element name="codhabil" type="xs:string" minOccurs="0" />               <xs:element name="nivelhabil" type="xs:string" minOccurs="0" />               <xs:element name="pessoademanda" type="xs:string" minOccurs="0" />               <xs:element name="tipornt" type="xs:string" minOccurs="0" />             </xs:sequence>           </xs:complexType>         </xs:element>       </xs:choice>     </xs:complexType>   </xs:element> </xs:schema>
