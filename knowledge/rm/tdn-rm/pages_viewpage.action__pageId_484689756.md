---
content_hash: 79e6d2d2a585daf27a41cecf964b411f5944f36a03e16992cb71bb92e7511992
fetched_at: '2026-06-29T00:10:19.983142+00:00'
page_id: '484689756'
product: rm
source: tdn-rm
title: Consulta integração via Webservice
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=484689756
version: 14
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | RH |
| Módulo: | Folha de Pagamento |
| Função: | Implementação de CRUD no DATASERVER FopLancExternoData |
| Requisito/Story/Issue | [FOPCALCULO01-6530](http://jiraproducao.totvs.com.br/browse/FOPCALCULO01-6530) |

## **02. SITUAÇÃO/REQUISITO**

Adaptação do DATASERVER “FopLancExternoData” para permitir inclusão/edição de dados, possibilitando inclusões, exclusões e edições externamente (via webservice) e permitindo também segurança via “Perfil de acesso” do sistema.

## **03. SOLUÇÃO**

Foi implementada a permissão para a inclusão/ edição e Exclusão de eventos utilizando o DATASERVER “FopLancExternoData” via webservice.

E para melhor visualização da integração dos eventos importados foi criado a Origem de Evento 7 ( Sistemas Externos ).

## **04. DEMAIS INFORMAÇÕES**

          Para o lançamento dos eventos importados via webservice em folha, deverá utilizar o tipo de lançamento conforme abaixo:

         

         Veja exemplos de utilização e formato do XML:

1

**Executando via SoapUi em base Exemplo (fictícia):**

1INCLUSÃO - SaveRecord

Não havendo nenhuma informação na consulta do movimento da integração foi importado via WebService

<tot:XML><![CDATA[<FopLancExterno >  
  <PFMOVTEMP>  
    <CODCOLIGADA>1</CODCOLIGADA>  
    <CHAPA>00001</CHAPA>  
    <ANOCOMP>2023</ANOCOMP>  
    <MESCOMP>10</MESCOMP>  
    <CODEVENTO>0082</CODEVENTO>  
    <IDMOVTEMP>1</IDMOVTEMP>  
    <HORA>120</HORA>  
    <REF>2</REF>  
    <VALOR>0.00</VALOR>  
    <VALORFORCADO>0</VALORFORCADO>  
    <ORIGEMEVENTO>7</ORIGEMEVENTO>  
    <DATAINCLUSAO>2023-11-08T11:33:40</DATAINCLUSAO>  
    <CODUSUARIO>mestre</CODUSUARIO>  
    <TIPOLANCAMENTO>1</TIPOLANCAMENTO>  
    <HORAFORMATADA>002:00</HORAFORMATADA>  
  </PFMOVTEMP>  
</FopLancExterno>]]></tot:XML>

2ALTERAÇÃO - SaveRecord

Alterando a  informação na consulta do movimento da integração foi importado via WebService

Hora de 120 para 180

Ref de 2 para 3

<tot:XML><![CDATA[<FopLancExterno >  
  <PFMOVTEMP>  
    <CODCOLIGADA>1</CODCOLIGADA>  
    <CHAPA>00001</CHAPA>  
    <ANOCOMP>2023</ANOCOMP>  
    <MESCOMP>10</MESCOMP>  
    <CODEVENTO>0082</CODEVENTO>  
    <IDMOVTEMP>1</IDMOVTEMP>  
    <HORA>180</HORA>  
    <REF>3</REF>  
    <VALOR>0.00</VALOR>  
    <VALORFORCADO>0</VALORFORCADO>  
    <ORIGEMEVENTO>7</ORIGEMEVENTO>  
    <DATAINCLUSAO>2023-11-08T11:33:40</DATAINCLUSAO>  
    <CODUSUARIO>mestre</CODUSUARIO>  
    <TIPOLANCAMENTO>1</TIPOLANCAMENTO>  
    <HORAFORMATADA>002:00</HORAFORMATADA>  
  </PFMOVTEMP>  
</FopLancExterno>]]></tot:XML>

3EXCLUSÃO - DeleteRecord

Excluindo a  informação na consulta do movimento da integração foi importado via WebService

<![CDATA[<FopLancExterno >  
  <PFMOVTEMP>  
    <CODCOLIGADA>1</CODCOLIGADA>  
    <CHAPA>00001</CHAPA>  
    <ANOCOMP>2023</ANOCOMP>  
    <MESCOMP>10</MESCOMP>  
    <CODEVENTO>0082</CODEVENTO>  
    <IDMOVTEMP>1</IDMOVTEMP>  
  </PFMOVTEMP>  
</FopLancExterno>]]>

FOI EXCLUIDO COM SUCESSO
