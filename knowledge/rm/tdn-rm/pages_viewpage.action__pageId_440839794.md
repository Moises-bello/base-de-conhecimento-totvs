---
content_hash: a86a4fe80126c24bb6fa6dd76ec6e4e84b9d6dd11615dd1071014ac7f69fc4b2
fetched_at: '2026-06-29T00:09:53.502813+00:00'
page_id: '440839794'
product: rm
source: tdn-rm
title: Inclusão e Leitura de Lançamentos Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=440839794
version: 19
---

**Objetivo**

O objetivo deste guia é apresentar como expor o e utilizar os WebMethods do WebService utilizado para inclusão e leitura de lançamentos contábeis.

**Expondo e utilizando o DataServer do TOTVS Gestão Contábil via WebService**

1 - Para configurar o WebService no RM.Host.exe e/ou RM.Host.Service.exe seguir os passos dos documentos de referência a seguir:

a - <http://tdn.totvs.com/display/public/LRM/WebService+RM>

b - <http://tdn.totvs.com/pages/viewpage.action?pageId=89620766>.

Os documentos em questão mostram como expor os serviços do webservice RM. No caso o serviço que nos interessa está exposto no caminho a seguir com o título ***DataServer***: “<http://localhost:8051/wsDataServer/MEX?wsdl>”. Lembrando que localhost será a máquina onde se encontram os aplicativos RM.Host.exe e/ou RM.Host.Service.exe.

2 - O serviço DataServer possui diversos webmethods. Os principais, utilizados para leitura e inserção/alteração de registros, são:

2.1 - **ReadView** -> Responsável por retornar os registros com base no filtro passado. Esse webmethod retorna os dados das tabelas CLANCAMENTO e CPARTIDA. O xml abaixo faz com que o webservice retorne o lançamento e suas partidas da coligada 1 e lançamento 2897 utilizando o DataServer CtbLanData “<tot:DataServerName>CtbLanData</tot:DataServerName>”.

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">

   <soapenv:Header/>

   <soapenv:Body>

      <tot:ReadView>

         <tot:DataServerName>CtbLanData</tot:DataServerName>

         <tot:Filtro>clancamento.codcoligada=1 and clancamento.idlancamento=2897</tot:Filtro>

         <tot:Contexto>codcoligada=1;codusuario=mestre;codsistema=C</tot:Contexto>

      </tot:ReadView>

   </soapenv:Body>

</soapenv:Envelope>

2.2 - **ReadRecord** -> Responsável por retornar um registro de forma detalhada com base na chave passada “<tot:PrimaryKey>1;0;12</tot:PrimaryKey>” (CODCOLIGADA; CODLOTE; IDLANCAMENTO). Este webmethod retorna o lançamento, partida(s), rateio(s) e campo(s) complementares. O xml abaixo faz com que o webmethod retorne o lançamento e sua(s) partida(s), rateio(s) e campo(s) complementares da coligada 1, lote zero e lançamento 12 utilizando o DataServer CtbLanData “<tot:DataServerName>CtbLanData</tot:DataServerName>”.

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">

   <soapenv:Header/>

   <soapenv:Body>

      <tot:ReadRecord>

         <tot:DataServerName>CtbLanData</tot:DataServerName>

         <tot:PrimaryKey>1;0;12</tot:PrimaryKey>

 <tot:Contexto>codcoligada=1;codusuario=mestre;codsistema=C</tot:Contexto>

      </tot:ReadRecord>

   </soapenv:Body>

</soapenv:Envelope>

2.3 - **SaveRecord** -> Responsável por Salvar/Atualizar um registro. Este webmethod salva o lançamento contábil com sua(s) partida(s), rateio(s) e campo(s) complementares. Lembrando que só o lançamento e partida são obrigatórios para serem salvos. Abaixo o xml de exemplo mostrando como salvar um lançamento contábil que possui duas partidas, dois rateios (um para cada partida) e os campos complementares (um para cada partida). Rateios e campos complementares podem ser mais de um por partida.

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">

    <soapenv:Header/>

    <soapenv:Body>

        <tot:SaveRecord>

        <tot:DataServerName>CtbLanData</tot:DataServerName>

        <tot:XML>

        <![CDATA[

                                              <CtbLan>

                                               <CLANCAMENTO>

                                                               <CODCOLIGADA>1</CODCOLIGADA>

                                                               <CODLOTE>0</CODLOTE>

                                                               <IDLANCAMENTO>-1</IDLANCAMENTO>

                                                               <DESCRICAO>Lançamento da data 15/10/2010</DESCRICAO>

                                                               <DATA>2010-10-15T00:00:00</DATA>

                                                               <ORIGEM\_HISTORICO>0</ORIGEM\_HISTORICO>

                                                               <INTEGRAAPLICACAO>C</INTEGRAAPLICACAO>

                                               </CLANCAMENTO>

                                               <CPARTIDA>

                                                               <CODCOLIGADA>1</CODCOLIGADA>

                                                               <IDPARTIDA>-1</IDPARTIDA>

                                                               <LCTREF>-1</LCTREF>

                                                               <CODLOTE>0</CODLOTE>

                                                               <IDLANCAMENTO>-1</IDLANCAMENTO>

                                                               <CODLOTEORIGEM>30</CODLOTEORIGEM>

                                                               <CODFILIAL>1</CODFILIAL>

                                                               <DOCUMENTO>002349</DOCUMENTO>

                                                               <DATA>2010-10-15T00:00:00</DATA>

                                                               <CODCOLDEBITO>0</CODCOLDEBITO>

                                                               <DEBITO>1.1.1.1.361</DEBITO>

                                                               <CODCOLCREDITO>1</CODCOLCREDITO>

                                                               <CODCOLPARTIDA>1</CODCOLPARTIDA>

                                                               <VALOR>237300,00</VALOR>

                                                               <VALOR2>121692,3077</VALOR2>

                                                               <DATA2>2010-10-15T00:00:00</DATA2>

                                                               <USUARIO>charles</USUARIO>

                                                               <DATAINCLU>2010-10-15T00:00:00</DATAINCLU>

                                                               <USUARIOALTER>charles</USUARIOALTER>

                                                               <DATAALTER>2010-10-15T00:00:00</DATAALTER>

                                                               <USUARIOINTEGRACAO>Walquiria</USUARIOINTEGRACAO>

                                                               <DATAINTEGRACAO>2011-10-07T09:05:06.153</DATAINTEGRACAO>

                                                              <INTEGRAAPLICACAO>C</INTEGRAAPLICACAO>

                                                               <INTEGRACHAVE>2349</INTEGRACHAVE>

                                                               <EXIGERATEIODEBITO>0</EXIGERATEIODEBITO>

                                                               <ORIGINADONOVOMOD>1</ORIGINADONOVOMOD>

                                                               <TIPOAGRUP>0</TIPOAGRUP>

                                               </CPARTIDA>

                                               <CPARTIDA>

                                                               <CODCOLIGADA>1</CODCOLIGADA>

                                                               <IDPARTIDA>-2</IDPARTIDA>

                                                               <LCTREF>-2</LCTREF>

                                                               <CODLOTE>0</CODLOTE>

                                                               <IDLANCAMENTO>-1</IDLANCAMENTO>

                                                               <CODLOTEORIGEM>30</CODLOTEORIGEM>

                                                               <CODFILIAL>1</CODFILIAL>

                                                               <DOCUMENTO>002349</DOCUMENTO>

                                                               <DATA>2010-10-15T00:00:00</DATA>

                                                               <CODCOLDEBITO>1</CODCOLDEBITO>

                                                               <CODCOLCREDITO>1</CODCOLCREDITO>

                                                               <CREDITO>1.1.1.1.004</CREDITO>

                                                               <CODCOLPARTIDA>1</CODCOLPARTIDA>

                                                               <VALOR>237300,00</VALOR>

                                                               <VALOR2>121692,3077</VALOR2>

                                                               <DATA2>2010-10-15T00:00:00</DATA2>

                                                               <USUARIO>charles</USUARIO>

                                                               <DATAINCLU>2010-10-15T00:00:00</DATAINCLU>

                                                               <USUARIOALTER>charles</USUARIOALTER>

                                                               <DATAALTER>2010-10-15T00:00:00</DATAALTER>

                                                               <USUARIOINTEGRACAO>Walquiria</USUARIOINTEGRACAO>

                                                               <DATAINTEGRACAO>2011-10-07T09:05:06.153</DATAINTEGRACAO>

                                                               <INTEGRAAPLICACAO>C</INTEGRAAPLICACAO>

                                                               <INTEGRACHAVE>2349</INTEGRACHAVE>

                                                               <EXIGERATEIOCREDITO>0</EXIGERATEIOCREDITO>

                                                               <ORIGINADONOVOMOD>1</ORIGINADONOVOMOD>

                                                               <TIPOAGRUP>0</TIPOAGRUP>

                                               </CPARTIDA>

                                               <CRATEIOLCCREDITO>

                                                               <CODCOLIGADA>1</CODCOLIGADA>

                                                               <CODLOTE>0</CODLOTE>

                                                               <IDRATEIO>-1</IDRATEIO>

                                                               <IDPARTIDA>-2</IDPARTIDA>

                                                               <LCTREF>-2</LCTREF>

                                                               <CODCOLCONTA>1</CODCOLCONTA>

                                                               <CODCONTA>1.1.1.1.004</CODCONTA>

                                                               <CODCOLGERENCIAL>1</CODCOLGERENCIAL>

                                                               <CODGERENCIAL>1.01.01.3</CODGERENCIAL>

                                                               <DATA>2010-10-15</DATA>

                                                               <VLRCREDITO>237300,00</VLRCREDITO>

                                                               <PERCENTUAL>100,00</PERCENTUAL>

                                               </CRATEIOLCCREDITO>

                                               <CRATEIOLCDEBITO>

                                                               <CODCOLIGADA>1</CODCOLIGADA>

                                                               <CODLOTE>0</CODLOTE>

                                                               <IDRATEIO>-2</IDRATEIO>

                                                               <IDPARTIDA>-1</IDPARTIDA>

                                                               <LCTREF>-1</LCTREF>

                                                               <CODCOLCONTA>0</CODCOLCONTA>

                                                               <CODCONTA>1.1.1.1.361</CODCONTA>

                                                               <CODCOLGERENCIAL>1</CODCOLGERENCIAL>

                                                               <CODGERENCIAL>1.01.01.4</CODGERENCIAL>

                                                               <DATA>2010-10-15</DATA>

                                                               <VLRDEBITO>237300,00</VLRDEBITO>

                                                               <PERCENTUAL>100,00</PERCENTUAL>

                                               </CRATEIOLCDEBITO>

                                               <CLCOMPL>

                                                               <CODCOLIGADA>1</CODCOLIGADA>

                                                               <CODLOTE>0</CODLOTE>

                                                               <IDPARTIDA>-1</IDPARTIDA>

                                               </CLCOMPL>

                                               <CLCOMPL>

                                                               <CODCOLIGADA>1</CODCOLIGADA>

                                                               <CODLOTE>0</CODLOTE>

                                                               <IDPARTIDA>-2</IDPARTIDA>

                                               </CLCOMPL>

                                               </CtbLan>

        ]]>

        </tot:XML>

        <tot:Contexto>codcoligada=1;codusuario=mestre;codsistema=C</tot:Contexto>

    </tot:SaveRecord>

   </soapenv:Body>

</soapenv:Envelope>

**Observação**

As tags <IDLANCAMENTO>, <IDPARTIDA>, <LCTREF> e <IDRATEIO> quando inseridas com valores negativos ou valores que não existam na base de dados, estes irão gerar um novo lançamento contábil, desde que respeitando as FKs. Caso seja inserido um valor de um lançamento existente na base de dados, este será atualizado.

Verificar se a permissão do Perfil do Usuário (08 - Desconsiderar filtro do produto em WebService) esta Habilitada.

Caso esteja Habilitado, irar ignorar a necessidade de colocar contexto no XML e não irar passar pelo método de leitura com segurança, caso esteja desabilitado, não irar inserir os registros se não tiver dados corretos no contexto, pois irar cruzar os dados do contexto com os dados da base utilizando método de segurança.
