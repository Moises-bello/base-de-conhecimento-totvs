---
article_id: 360028943352
category: ADVPL - Web Service
content_hash: 49a4bf6b428570d7a54f7f92c3b64d60c51af3c229914c78cbdc36175c7c160f
fetched_at: '2026-06-28T22:40:10.291146+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - O que é SOAP
type: support-article
updated_at: '2022-03-09T19:17:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028943352-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-O-que-%C3%A9-SOAP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**O que é, pra que serve e como funciona a comunicação em um *web service* SOAP?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**SOAP (*Simple Object Access Protocol*) é um tipo de arquitetura de software que define um conjunto de restrições/regras a serem usados para a criação de serviços *web*.  
  
Pra que serve?  
Inicialmente quando escrevemos nossas aplicações elas estão isoladas, contudo, para que seja possível consumi-las em outras aplicações é necessário expô-las por algum método de comunicação.

Dentre diversos outros métodos, os *web services* SOAP são um deles.

**Exemplo**  
Tenho um sistema de vendas que armazena os dados de cada nota fiscal emitida.

Preciso acessar as informações da nota fiscal (quantidade, preço unitário, valor total, impostos), assim como preciso enviar estes dados para um outro sistema de contabilidade diariamente.

Estas informações precisam estar disponíveis tanto no meu sistema quanto no sistema de contabilidade da empresa.

A partir dessa necessidade, eu crio um *web service* SOAP e programo minhas aplicações (tanto a local quanto a da contabilidade) para realizar requisições para o mesmo (seja de inclusão ou visualização de notas).

Desta forma eu tenho um serviço único, que é consumido da mesma maneira (porém por métodos diferentes) e que mantém as informações disponíveis para diversas outras aplicações.  
  
**Comunicação**  
Na grande maioria dos casos, as comunicações em *web services* SOAP ocorrem sob o protocolo HTTP utilizando o padrão XML (Linguagem de Marcação Extensível), onde são utilizados métodos específicos para retorno das informações (criaNota(), visualizaNota(), todasNotas()).

**Exemplo**  
Preciso que seja possível visualizar os dados de um cliente com código, nome, tipo e endereço, como os dados poderão serão trazidos?

Eu irei realizar um consumo para um serviço chamado já criado através da URI (*Uniform Resource Identifier*) abaixo por meio de um WSDL:

```
{method} {schema}://{domain}{:port}/{patch}?{query}  
{SOAP} {https}://{mydomain.com.br:5090}/{soap/invoices}?{wsdl}
```

E quando eu fizer a requisição, me será retornado o XML abaixo:

```
<?xml version="1.0" encoding="utf-8"?>  
<soap:Envelope   
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"   
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"   
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">  
   
    <soap:Body>  
        <code>CLT018</code>  
        <name>IMPACTART DIGITAL</name>  
        <strategicCustomerType>F</strategicCustomerType>  
        <address>  
            <street>AVENIDA ALVES CARMO, 7811</street>  
            <city>JARDIM CARLOS MENDES</city>  
            <stateId>SP</stateId>  
        </address>  
    </soap:Body>  
</soap:Envelope>
```

**O que fazer com o XML?**  
Uma vez recebida a resposta do *web service*, apenas extraia apenas o corpo da resposta (<soap:Body>) e acesse as propriedades contidas nele para integrar ao seu sistema.

Exemplo em ADVPL

```
/** RESTANTE DA APLICAÇÃO **/  
  
cXML := "BODY_RESPOSTA_DO_WS_SOAP_AQUI"  
  
oXML := TXMLManager():New()  
oXML:Parse(cXML)  
  
// AQUI CONTÉM TODOS OS CAMPOS E CONTEÚDOS  
// (ex: aNodes[1][1] => "code" | aNodes[1][2] => "CLT018")  
aNodes := oXML:DOMGetAttArray()   
  
/** RESTANTE DA APLICAÇÃO **/
```

**Saiba mais**  
[Web service SOAP](http://tdn.totvs.com/pages/viewpage.action?pageId=274332818)  
[SOAP - Wikipedia](https://pt.wikipedia.org/wiki/SOAP)  
[XML - Wikipedia](https://pt.wikipedia.org/wiki/XML)  
[URI - Wikipedia](https://pt.wikipedia.org/wiki/URI)  
[WSDL - Wikipedia](https://pt.wikipedia.org/wiki/Web_Services_Description_Language)
