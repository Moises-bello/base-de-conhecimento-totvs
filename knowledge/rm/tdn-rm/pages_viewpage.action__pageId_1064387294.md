---
content_hash: 848b7b1de15edb8e613a085ff0ae56cd3cc7eee3098a006d37432ef0e31db781
fetched_at: '2026-06-29T00:05:53.050650+00:00'
page_id: '1064387294'
product: rm
source: tdn-rm
title: DT - Informe de Rendimentos - Geração via WEBSERVICE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1064387294
version: 13
---

## **1. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Informe de Rendimentos - Geração via WEBSERVICE |
| País: | Brasil |
| Issue: | [DRHROTRM-18181](https://jiraproducao.totvs.com.br/browse/DRHROTRM-18181) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2506.297
* 12.1.2510.223
* 12.1.2602.141 e superiores

## **03. SITUAÇÃO/REQUISITO**

Ao gerar o Informe de Rendimentos por meio do Web Service **FOPDIRFDATA**, o sistema deve passar a considerar o leiaute mais recente do informe, evitando divergências nas informações apresentadas.

## **04. SOLUÇÃO**

Devido a descontinuação do layout apresentado, foi realizada a melhoria no produto TOTVS Folha de Pagamento para a geração do Informe de Rendimentos via webservice. Este passa a ser gerado no novo modelo disponível no TOTVS Compartilhamento.

Para o correto funcionamento após alteração, será necessário associar o novo modelo do relatório **FOPREL0008.01 - Informe de Rendimentos - NOVO MODELO.TotvsReport** no grupo de portal em Configurações | Parametrizador | RM Portal | Seleção do Grupo de Acesso | Informe de Rendimentos.

Por obrigatoriedade será necessário repassar a chapa do funcionário e informada na tag primaryKey no contexto do XML, conforme  destaque em vermelho no exemplo abaixo:

#### **Exemplo de XML no ReadRecord:**

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
   <soapenv:Header/>  
   <soapenv:Body>  
      <tot:ReadRecord>  
         <!--Optional:-->  
         <tot:DataServerName>FopDirfData</tot:DataServerName>  
         <!--Optional:-->  
         <tot:PrimaryKey>1;**956590**;2025</tot:PrimaryKey>  
         <!--Optional:-->  
         <tot:Contexto>CodColigada=1;CodAplicacao=P;CodUsuario=mestre;**chapafuncionario=956590**</tot:Contexto>  
      </tot:ReadRecord>  
   </soapenv:Body>  
</soapenv:Envelope>

Informe de Rendimentos gerado a partir da tag **<ARQUIVO>** no resultado do **ReadRecord**.

## **05. DEMAIS INFORMAÇÕES**

* [Informe de Rendimentos e DIRF 2026](https://tdn.totvs.com/display/LRM/Informe+de+Rendimentos+e+DIRF+2026)
