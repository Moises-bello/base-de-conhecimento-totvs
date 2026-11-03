---
content_hash: b0629fbf066487db9393fa12726f03663b7494d0637b5e494eee0955a78acf92
fetched_at: '2026-06-29T00:09:07.659709+00:00'
page_id: '384586115'
product: rm
source: tdn-rm
title: 3348251 MATESTCNTFTOF01-2939 DT Inserção de Inventário via WebService
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=384586115
version: 7
---

# MANUTENÇÃO DE INVENTÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Manutenção de Inventário. |
| **Situação/Requisito:** | Ao tentar consultar o schema ou criar um Inventário através do WebService é apresentado o erro de "Não há linha na posição 0.". |
| **Solução/Implementação:** | Realizado ajuste no dataServer de Inventário **EstMntInventarioData** para que ao realizar a consulta de GetSchema não seja apresentado a mensagem citada. |
| **Procedimento para utilização** | **Inclusão de Inventário via webservice** Como a inclusão de inventário é realizada via wizard de processo, para realizar a inclusão de um inventário via webService deve-se utilizar o processo **EstAssistenteInventarioProcData**.  Para obter o xml esperado na inclusão deste processo faça um requisição via GetSchema ([http://servidor.com:8051/wsProcess/IwsProcess](http://bhn050102754.bh01.local:8051/wsProcess/IwsProcess)) utilizando o nome do processo EstAssistenteInventarioProcData  ***Exemplo de GetSchema via SoapUI:***  <soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  <soapenv:Header/>  <soapenv:Body>  <tot:GetSchema>  <!--Optional:-->  <tot:ProcessServerName>EstAssistenteInventarioProcData</tot:ProcessServerName>  </tot:GetSchema>  </soapenv:Body> </soapenv:Envelope>    ***Exemplo de xml para Inclusão de Inventário via SoapUI:***  **250** **Alteração de Inventário via webservice** Para realizar a alteração de Inventário via webService deve-se utilizar o dataserver **EstMntInventarioData.**  **Atenção:** sempre que enviar uma alteração do inventário via webService, deve-se passar a lista de todos os itens que compõem o Inventário (realize um ReadRecord para recuperar os dados do inventário que será alterado - [http://servidor.com:8051/wsDataServer/IwsDataServer](http://bhn050102754.bh01.local:8051/wsDataServer/IwsDataServer)/[ReadRecord](http://bhn050102754.bh01.local:8051/wsDataServer/IwsDataServer)) e para incluir novos itens a tag ***IDITMINVENTARIO*** deve ser passada com valor -1.  ***Exemplo de XML para Alteração de Inventário.***  Neste exemplo, o inventário de código 201801 foi criado sem itens e será incluído o produto de IdPrd 8. Como ele é um novo produto a tag IDITMINVENTARIO deve possuir valor -1  250 **Exclusão de Inventário via webservice** A exclusão de Inventário deve ser realizada utilizando o DataServerName EstMntInventarioData passando a chave primária do registro. Utilizar [htttp://servidor.com:8051/wsDataServer/IwsDataServer](http://bhn050102754.bh01.local:8051/wsDataServer/IwsDataServer)/[DeleteRecord](http://bhn050102754.bh01.local:8051/wsDataServer/IwsDataServer)  ***Exemplo de Exclusão via SoapUI***  250 |
| **Tickets relacionados:** | Não se aplica. |
| **Requisito:** | Inventário (EstMntInventarioAction). |
| **Documento de Referência:** | <http://wikihelp.totvs.com.br/WikiHelp/EST/EST.Inventario.aspx>. |
