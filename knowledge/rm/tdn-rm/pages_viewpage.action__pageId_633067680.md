---
content_hash: 3623cf2c9655e52d7b85e097852f4d7bd1b10689c459f1212a054cf8dded5296
fetched_at: '2026-06-29T00:11:06.285308+00:00'
page_id: '633067680'
product: rm
source: tdn-rm
title: Criação de atendimento via webservice
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=633067680
version: 2
---

É possível criar ou alterar atendimentos usando WebService, para mais informações sobre configurar um WebService, ver o link abaixo:

<https://tdn.totvs.com/display/public/LRM/Configurar+Webservice>

Realizadas todas configurações do link, deve se criar um request de SaveRecord usando o DataServer CRMAtendimentoExtData.

Algumas considerações importantes:

 - Caso queira criar um novo atendimento, o campo CODATENDIMENTO sempre deve ser informado -1, dessa forma o sistema irá

gerar automaticamente o código de acordo com as regras do sistema, caso qualquer outro código for informado, o sistema entendera

que trata-se de uma alteração e irá retornar uma mensagem de erro caso o registro não exista.

 - Para os campos solicitação, discussão e solução deve-se usar respectivamente as TAGs TEXTOSOLICITACAO\_NOVO,

TEXTODISCUSSAO\_NOVO e TEXTOSOLUCAO\_NOVO

Segue abaixo um exemplo de requisição SOAP de uma inclusão de atendimento com os principais campos preenchidos:

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
<soapenv:Header/>  
<soapenv:Body>  
<tot:SaveRecord>  
<!--Optional:-->  
<tot:DataServerName>CRMAtendimentoExtData</tot:DataServerName>  
<!--Optional:-->  
<tot:XML><![CDATA[<CRMAtendimentoExt>  
<HAtendimentoBase>  
<CODCOLIGADA>1</CODCOLIGADA>  
<CODCOLIGPRD>1</CODCOLIGPRD>  
<CODATENDENTERESP>11</CODATENDENTERESP>  
<CODPRODUTO>1</CODPRODUTO>  
<CODITEMPRD>A4</CODITEMPRD>  
<CODLOCAL>1</CODLOCAL>  
<CODATENDIMENTO>-1</CODATENDIMENTO>  
<ABERTURA>2021-08-10T11:58:09</ABERTURA>  
<CODRPR>10</CODRPR>  
<CODATENDENTE>11</CODATENDENTE>  
<CODCLASSIFICACAO>00000</CODCLASSIFICACAO>  
<TIPOCONTATO>1</TIPOCONTATO>  
<ORIGEMCONTATO>3</ORIGEMCONTATO>  
<CAIXAPOSTAL>2</CAIXAPOSTAL>  
<SOLICITANTE>0</SOLICITANTE>  
<CODCOLIGADARPR>1</CODCOLIGADARPR>  
<CODSTATUS>A</CODSTATUS>  
<AGENDADOPARA>2021-08-10T12:02:00</AGENDADOPARA>  
<PRIORIDADE>100</PRIORIDADE>  
<NUMAGENDAMENTOS>0</NUMAGENDAMENTOS>  
<CODCATEGORIAGERAL>6</CODCATEGORIAGERAL>  
<TOTALCAIXAPOSTAL>0</TOTALCAIXAPOSTAL>  
<ASSUNTOOC>Assunto do atendimento</ASSUNTOOC>  
<ID>0</ID>  
<CODCOLIGADARESP>1</CODCOLIGADARESP>  
<PCTPRONTO>0</PCTPRONTO>  
<DATAFIMPREV>2021-08-10T12:02:00</DATAFIMPREV>  
<GRAUDIFICULDADE>100</GRAUDIFICULDADE>  
<NIVELACESSO>0</NIVELACESSO>  
<CODTIPOATENDIMENTO>1</CODTIPOATENDIMENTO>  
<CODGRUPOATENDIMENTO>20</CODGRUPOATENDIMENTO>  
<CODLOCALENTREGA>1</CODLOCALENTREGA>  
<CODCATEGORIA>11</CODCATEGORIA>  
<CODCOLIGADAATENDENTE>1</CODCOLIGADAATENDENTE>  
<TEXTOSOLICITACAO\_NOVO>  
Solicitação do atendimento</TEXTOSOLICITACAO\_NOVO>  
<TEXTODISCUSSAO\_NOVO>  
Discussão do atendimento  
</TEXTODISCUSSAO\_NOVO>  
<TEXTOSOLUCAO\_NOVO>  
Solução do atendimento</TEXTOSOLUCAO\_NOVO>  
<BLOQUEAREDICAOATENDIMENTO>0</BLOQUEAREDICAOATENDIMENTO>  
<CODCOLIGADACLI>0</CODCOLIGADACLI>  
<CODCFO>C27554</CODCFO>  
<TIPOCLIENTE>Cliente</TIPOCLIENTE>  
<TEMPLATE>false</TEMPLATE>  
<DESCSITUACAOATENDIMENTO>Em andamento</DESCSITUACAOATENDIMENTO>  
<PUBLICARDISCUSSAO>0</PUBLICARDISCUSSAO>  
<PUBLICARDISCUSSAOFORUM>0</PUBLICARDISCUSSAOFORUM>  
<GUIASINVISIVEIS>3;</GUIASINVISIVEIS>  
<CONSULTASQL>;;</CONSULTASQL>  
<ORIGEMSQL />  
<DESTINOSQL />  
</HAtendimentoBase>  
</CRMAtendimentoExt>]]></tot:XML>  
<!--Optional:-->  
<tot:Contexto>?</tot:Contexto>  
</tot:SaveRecord>  
</soapenv:Body>  
</soapenv:Envelope>
