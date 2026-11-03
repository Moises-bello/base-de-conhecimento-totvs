---
article_id: 31120681945879
category: Integrações - Conceito e WebService
content_hash: 7fba9b571977b0fbb41dc7a3eb34d34bacd169a9f33af21d89f881b888382fe7
fetched_at: '2026-06-28T22:46:44.898273+00:00'
product: rm
section_id: 1500000834721
source: central-rm
title: RH - RM - FOP - Cadastro de Funcionário via WebService/API utilizando o DataServer
  FopFuncData
type: support-article
updated_at: '2026-01-09T20:40:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31120681945879-RH-RM-FOP-Cadastro-de-Funcion%C3%A1rio-via-WebService-API-utilizando-o-DataServer-FopFuncData
---

**Dúvida**Como
cadastrar um funcionário pelo DataServer FopFuncData, através de API / Web
Service via SoapUI ou Postman    
  
**Ambiente**

* TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**

Para cadastrar um funcionário no RM via WebService/API, utiliza-se o
**DataServer FopFuncData**.
Para mais detalhes sobre esse DataServer, consulte a documentação oficial:

🔗 [**FopFuncData - Documentação Oficial**](https://apitotvslegado.z15.web.core.windows.net/FopFuncData.html?Objeto=FopFuncData)  
🔗 **[FopFuncData - Lista das campos obrigatórios](https://tdn.totvs.com/pages/releaseview.action?pageId=859578298)**

Antes de cadastrar um novo funcionário, recomenda-se
**consultar os dados de um funcionário já existente**.
Isso retorna um XML ou JSON pronto, que pode ser utilizado como base para
o cadastro de um novo.

Abaixo, exemplificamos esse processo utilizando as ferramentas
**SoapUI** e
**Postman**:

[1- Consulta e cadastro via SoapUI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31120681945879-RH-RM-FOP-Cadastro-de-Funcion%C3%A1rio-via-WebService-API-utilizando-o-DataServer-FopFuncData#soap)

[2- Consulta e cadastro via Postman](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31120681945879-RH-RM-FOP-Cadastro-de-Funcion%C3%A1rio-via-WebService-API-utilizando-o-DataServer-FopFuncData#post)

  
 Processo via
**SoapUI**

1. Para realizar o consumo dos dados, é necessário, primeiramente, executar
   um **ReadRecord** para
   obter as informações base.

   Para isso, devem ser fornecidas as chaves primárias:

   * **CODCOLIGADA**
     (código da coligada do funcionário)
   * **CHAPA** (chapa
     do funcionário em questão)

   Além das chaves primárias, é imprescindível informar o nome do
   **DataServer** correspondente,
   que, neste caso, é o
   **FopFuncData**.

   Por fim, deve-se especificar o contexto do consumo, fornecendo os
   seguintes parâmetros:

   * **CODCOLIGADA**
   * **CODUSUARIO**
   * **CODSISTEMA**

   Abaixo, segue um exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31120707473303)

OBS: Lembre-se de colocar a autenticação (basic), no canto inferior esquerdo

        2. Em seguida, será necessário obter o
**XML** gerado após o consumo
do **DataServer**. Para isso,
deve-se acessar a aba **XML**
e extrair as informações disponíveis na tag
**"ReadRecordResult"**, a partir
da tag  "<![CDATA[", conforme o exemplo abaixo:

![Gravar_2025_08_19_09_54_39_453-ezgif.com-video-to-gif-converter.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/34287325601303)

       3. Após copiar o XML, vamos acessar o método SaveRecord
e informar o DataServer em questão (FopFuncData), o XML que copiamos e também
o contexto da mesma forma que fizemos no ReadRecord, conforme o exemplo a
baixo:

![Gravar_2025_03_31_11_30_01_916-ezgif.com-video-to-gif-converter.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/31120681925655)

      4. Em quarto passo você deve alterar as informações
base para as informações do novo funcionário que será cadastrado, se atente
ao formato que as tags pedem para serem inseridas, conforme está na documentação
do DataServer.

***Clique aqui para ver o conteúdo de um XML pronto de exemplo !***

```
<![CDATA[  
<FopFunc>
  <PFunc>
    <CODCOLIGADA>1</CODCOLIGADA>
    <CHAPA>11111</CHAPA>
    <NROFICHAREG>11111</NROFICHAREG>
    <CODRECEBIMENTO>M</CODRECEBIMENTO>
    <CODSITUACAO>A</CODSITUACAO>
    <CODTIPO>N</CODTIPO>
    <CODSECAO>01.01</CODSECAO>
    <CODFUNCAO>00005</CODFUNCAO>
    <CODSINDICATO>0001</CODSINDICATO>
    <JORNADA>220.00</JORNADA>
    <CODHORARIO>0002</CODHORARIO>
    <NRODEPIRRF>0</NRODEPIRRF>
    <NRODEPSALFAM>0</NRODEPSALFAM>
    <DTBASE>1998-12-02T00:00:00</DTBASE>
    <SALARIO>2660.67</SALARIO>
    <SITUACAOFGTS>1</SITUACAOFGTS>
    <DTOPCAOFGTS>1998-12-02T00:00:00</DTOPCAOFGTS>
    <CONTAFGTS>311-82</CONTAFGTS>
    <SALDOFGTS>497.00</SALDOFGTS>
    <CONTRIBSINDICAL>J</CONTRIBSINDICAL>
    <APOSENTADO>0</APOSENTADO>
    <TEMMAIS65ANOS>0</TEMMAIS65ANOS>
    <PERCENTADIANT>40.00</PERCENTADIANT>
    <DATAADMISSAO>1998-12-02T00:00:00</DATAADMISSAO>
    <TIPOADMISSAO>P</TIPOADMISSAO>
    <MOTIVOADMISSAO>01</MOTIVOADMISSAO>
    <TEMPRAZOCONTR>0</TEMPRAZOCONTR>
    <TEMAVISOPREVIO>0</TEMAVISOPREVIO>
    <DTVENCFERIAS>2024-12-02T00:00:00</DTVENCFERIAS>
    <QUERABONO>0</QUERABONO>
    <QUER1APARC13O>1</QUER1APARC13O>
    <FERIASCOLETIVAS>0</FERIASCOLETIVAS>
    <NRODIASABONO>0</NRODIASABONO>
    <SALDOFERIAS>0</SALDOFERIAS>
    <NDIASLICREM1>0</NDIASLICREM1>
    <NDIASLICREM2>0</NDIASLICREM2>
    <SITUACAORAIS>1</SITUACAORAIS>
    <CONTAPAGAMENTO>2111-5</CONTAPAGAMENTO>
    <MEMBROSINDICAL>0</MEMBROSINDICAL>
    <VINCULORAIS>1</VINCULORAIS>
    <DIASUTEISMES>0</DIASUTEISMES>
    <DIASUTPROXMES>0</DIASUTPROXMES>
    <MUDOUENDERECO>0</MUDOUENDERECO>
    <MUDOUCARTTRAB>0</MUDOUCARTTRAB>
    <MUDOUNOME>0</MUDOUNOME>
    <MUDOUPIS>0</MUDOUPIS>
    <ANTIGOPIS></ANTIGOPIS>
    <MUDOUCHAPA>0</MUDOUCHAPA>
    <MUDOUADMISSAO>0</MUDOUADMISSAO>
    <ANTIGADTADM></ANTIGADTADM>
    <ANTIGOTIPOFUNC></ANTIGOTIPOFUNC>
    <ANTIGOTIPOADM></ANTIGOTIPOADM>
    <MUDOUDTOPCAO>0</MUDOUDTOPCAO>
    <ANTIGADTOPCAO></ANTIGADTOPCAO>
    <MUDOUSECAO>0</MUDOUSECAO>
    <MUDOUDTNASCIM>0</MUDOUDTNASCIM>
    <FALTAALTERFGTS>0</FALTAALTERFGTS>
    <DEDUZIRRF65>0</DEDUZIRRF65>
    <PISPARAFGTS>0</PISPARAFGTS>
    <ULTIMORECALCULODATA></ULTIMORECALCULODATA>
    <ULTIMORECALCULOHORA></ULTIMORECALCULOHORA>
    <DESCONTAAVISOPREVIO>0</DESCONTAAVISOPREVIO>
    <CODFILIAL>1</CODFILIAL>
    <NOME></NOME>
    <INDINICIOHOR>0</INDINICIOHOR>
    <PISPASEP></PISPASEP>
    <DTCADASTROPIS></DTCADASTROPIS>
    <CODPESSOA></CODPESSOA>
    <CODBANCOFGTS></CODBANCOFGTS>
    <CODBANCOPAGTO></CODBANCOPAGTO>
    <CODAGENCIAPAGTO></CODAGENCIAPAGTO>
    <CODBANCOPIS></CODBANCOPIS>
    <RESCISAOCALCULADA>0</RESCISAOCALCULADA>
    <MEMBROCIPA>0</MEMBROCIPA>
    <USASALCOMPOSTO>0</USASALCOMPOSTO>
    <REGATUAL></REGATUAL>
    <GRUPOSALARIAL></GRUPOSALARIAL>
    <JORNADAMENSAL>0.00</JORNADAMENSAL>
    <PREVDISP>0</PREVDISP>
    <CODOCORRENCIA></CODOCORRENCIA>
    <CODCATEGORIA></CODCATEGORIA>
    <ESUPERVISOR>0</ESUPERVISOR>
    <INTEGRCONTABIL>0</INTEGRCONTABIL>
    <USACONTROLEDESALDO>0</USACONTROLEDESALDO>
    <MUDOUCI>0</MUDOUCI>
    <PERIODORESCISAO>0</PERIODORESCISAO>
    <CODGRPQUIOSQUE></CODGRPQUIOSQUE>
    <FGTSMESANTRECOLGRFP>0</FGTSMESANTRECOLGRFP>
    <CODNIVELSAL></CODNIVELSAL>
    <TRABALHOUNADEMISSAO>0</TRABALHOUNADEMISSAO>
    <NRODIASFERIASJORNRED>0</NRODIASFERIASJORNRED>
    <POSSUIALVARAMENOR16>0</POSSUIALVARAMENOR16>
    <SITUACAOINSS>1</SITUACAOINSS>
    <CODTABELASALARIAL></CODTABELASALARIAL>
    <TEMDEDUCAOCPMF>0</TEMDEDUCAOCPMF>
    <NRODIASFERIASCORRIDOS>0</NRODIASFERIASCORRIDOS>
    <NRODIASABONOCORRIDOS>0</NRODIASABONOCORRIDOS>
    <POSICAOABONO>0</POSICAOABONO>
    <QUERADIANTAMENTO>0</QUERADIANTAMENTO>
    <SEXO>M</SEXO>
    <NACIONALIDADE>10</NACIONALIDADE>
    <GRAUINSTRUCAO>06</GRAUINSTRUCAO>
    <NATURALIDADE></NATURALIDADE>
    <APELIDO></APELIDO>
    <EMAIL></EMAIL>
    <DTNASCIMENTO>1980-01-01T00:00:00</DTNASCIMENTO>
    <CARTIDENTIDADE></CARTIDENTIDADE>
    <ORGEMISSORIDENT></ORGEMISSORIDENT>
    <DTEMISSAOIDENT></DTEMISSAOIDENT>
    <UFCARTIDENT></UFCARTIDENT>
    <CARTEIRATRAB></CARTEIRATRAB>
    <DTCARTTRAB></DTCARTTRAB>
    <SERIECARTTRAB></SERIECARTTRAB>
    <UFCARTTRAB></UFCARTTRAB>
    <NIT></NIT>
    <TITULOELEITOR></TITULOELEITOR>
    <SECAOTITELEITOR></SECAOTITELEITOR>
    <ZONATITELEITOR></ZONATITELEITOR>
    <CERTIFRESERV></CERTIFRESERV>
    <CATEGMILITAR></CATEGMILITAR>
    <CPF></CPF>
    <RUA></RUA>
    <NUMERO></NUMERO>
    <COMPLEMENTO></COMPLEMENTO>
    <BAIRRO></BAIRRO>
    <CIDADE></CIDADE>
    <ESTADO></ESTADO>
    <PAIS></PAIS>
    <CEP></CEP>
    <TELEFONE1></TELEFONE1>
    <NOMEBANCOPGTO></NOMEBANCOPGTO>
    <NOMEAGENCIAPGTO></NOMEAGENCIAPGTO>
    <NOMEPAI></NOMEPAI>
    <NOMEMAE></NOMEMAE>
    <CODIGO></CODIGO>
    <Jornada_Mensal>0.00</Jornada_Mensal>
    <Hora>00:00:00</Hora>
    <DEFICIENTEFISICO>0</DEFICIENTEFISICO>
    <DEFICIENTEAUDITIVO>0</DEFICIENTEAUDITIVO>
    <DEFICIENTEFALA>0</DEFICIENTEFALA>
    <DEFICIENTEVISUAL>0</DEFICIENTEVISUAL>
    <DEFICIENTEMENTAL>0</DEFICIENTEMENTAL>
    <BRPDH>0</BRPDH>
    <HSTAFT_ESTTEMPOSERVICO></HSTAFT_ESTTEMPOSERVICO>
    <IDIMAGEM></IDIMAGEM>
    <NOMEFUNC></NOMEFUNC>
    <CORRACA></CORRACA>
    <DTMUDANCASALARIO></DTMUDANCASALARIO>
    <DTMUDANCAFUNCAO></DTMUDANCAFUNCAO>
    <HSTSIT_DATAMUDANCA></HSTSIT_DATAMUDANCA>
    <HSTSIT_MOTIVO></HSTSIT_MOTIVO>
    <DTMUDANCASECAO></DTMUDANCASECAO>
    <DTMUDANCACONTRIBSINDICAL></DTMUDANCACONTRIBSINDICAL>
    <HSTSEFIP_DTMUDANCA></HSTSEFIP_DTMUDANCA>
    <DTMUDANCAHORARIO></DTMUDANCAHORARIO>
    <HSTBANCO_DTMUDANCA></HSTBANCO_DTMUDANCA>
    <MOTMUDANCASALARIO></MOTMUDANCASALARIO>
    <MOTMUDANCAFUNCAO></MOTMUDANCAFUNCAO>
    <MOTMUDANCASECAO></MOTMUDANCASECAO>
    <CODUSUARIO></CODUSUARIO>
    <ESTADOCIVIL></ESTADOCIVIL>
    <ESTADONATAL></ESTADONATAL>
    <CANDIDATO>0</CANDIDATO>
    <CODCOLIGADAORIGEM></CODCOLIGADAORIGEM>
    <CHAPAORIGEM></CHAPAORIGEM>
    <DEFICIENTEINTELECTUAL>0</DEFICIENTEINTELECTUAL>
    <CODMUNICIPIO></CODMUNICIPIO>
    <SITUACAOIRRF>1</SITUACAOIRRF>
    <NROFILHOSBRASIL>0</NROFILHOSBRASIL>
    <CODIGORECEITA3533></CODIGORECEITA3533>
    <IDADE>0</IDADE>
    <CODCATEGORIAESOCIAL></CODCATEGORIAESOCIAL>
    <ESOCIALNATATIVIDADE></ESOCIALNATATIVIDADE>
    <REFERENCIA_MENSAL></REFERENCIA_MENSAL>
    <ENVIORESCISAOCONSIGNADO>0</ENVIORESCISAOCONSIGNADO>
    <FUNCAOACUMULAVEL>0</FUNCAOACUMULAVEL>
    <FUMANTE>0</FUMANTE>
    <IMAGEM></IMAGEM>
    <DEFICIENTEMOBREDUZIDA>0</DEFICIENTEMOBREDUZIDA>
    <Periodo_Aquisitivo></Periodo_Aquisitivo>
    <Limite_Ferias_Dobro>0</Limite_Ferias_Dobro>
    <DiasFaltasFeriasNormais>0</DiasFaltasFeriasNormais>
    <CONJUGEBRASIL>0</CONJUGEBRASIL>
    <NATURALIZADO>0</NATURALIZADO>
    <FILHOSBRASIL>0</FILHOSBRASIL>
    <INVESTTREINANT>0</INVESTTREINANT>
    <AJUSTATAMANHOFOTO>0</AJUSTATAMANHOFOTO>
    <DATAAPROVACAOCURR></DATAAPROVACAOCURR>
    <ESTADOROW></ESTADOROW>
    <ROWVALIDA></ROWVALIDA>
    <ALUNO>0</ALUNO>
    <PROFESSOR>0</PROFESSOR>
    <USUARIOBIBLIOS>0</USUARIOBIBLIOS>
    <FUNCIONARIO>1</FUNCIONARIO>
    <EXFUNCIONARIO>0</EXFUNCIONARIO>
    <CODNATURALIDADE></CODNATURALIDADE>
    <FALECIDO>0</FALECIDO>
    <TIPOPRAZORESIDENCIA></TIPOPRAZORESIDENCIA>
  </PFunc>
</FopFunc>]]>
```

**Processo via **Postman****

1. Assim como no **SOAP**, o primeiro passo é obter as
   informações do **JSON** base para realizar o envio.
   Para isso, deve-se utilizar a **URL** do exemplo abaixo
   e informar o **DataServer** correspondente no método
   **GET**.

   Além disso, é necessário aplicar um filtro por **ID**,
   pois, caso o **GET** seja executado sem filtros, todos
   os funcionários serão retornados por padrão. Isso pode impactar o
   desempenho e resultar em alguns campos sendo carregados como
   **nulos**. Portanto, a aplicação de um
   **filtro por ID** é essencial para garantir que todos
   os campos sejam retornados corretamente, com as informações completas
   para nossa base.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31120707478679)

          2. Após essa etapa, copie apenas as informações
que antecedem a chave **"{"** da tag **"id"** e
finalize a cópia ao final dessa chave. É importante extrair apenas os dados
da **pfunc**, sem incluir outras tabelas, como
**VLCOMPL** ou **PFCOMPL**, pois essas não precisam
ser copiadas.

![Gravar_2025_03_31_11_47_58_331-ezgif.com-video-to-gif-converter.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/31120707478935)

         3. Após copiar os dados base utilizando
o método **GET**, é necessário alterar o método para
**POST** e informar no **body** o
**JSON** base copiado.

Diferente do **GET**, no **POST**
**não** é necessário informar o **ID** nem aplicar
um **filtro**.

Ao finalizar a estrutura do **JSON**, certifique-se de incluir
a chave de fechamento corretamente e garantir que não haja uma vírgula antes
dessa chave, evitando erros de formatação.

Segue um exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31120707480215)

         4. Em quarto passo você deve alterar as
informações base para as informações do novo funcionário que será cadastrado,
se atente ao formato que as tags pedem para serem inseridas, por isso tomamos
como base o Json de outro funcionário. Feito as alterações pode consumir
normalmente.

***Clique aqui para ver o conteúdo de um JSON pronto de exemplo !***

```
      {
  "CHAPA": "03333",
  "CODPESSOA": "100",
  "NROFICHAREG": "03333",
  "NOME": "ANA CHRIS",
  "DTNASCIMENTO": "2001-07-17T00:00:00",
  "CPF": "14153407658",
  "BAIRRO": "MARACANAZINHO",
  "CODIGO": "100",
  "CODCOLIGADA": "1",
  "CODFILIAL": "1",
  "CODRECEBIMENTO": "M",
  "CODTIPO": "N",
  "SEXO": "M",
  "CARTIDENTIDADE": "0010101010",
  "CEP": "78205585",
  "CIDADE": "CACERES",
  "CODCCUSTO": "02.1",
  "ESTADO": "MT",
  "ESTADOCIVIL": "C",
  "ORGEMISSORIDENT": "SSP/MT",
  "RUA": "RUA PADRE CASSEMIRO",
  "NUMERO": "2050",
  "CODCATEGORIA": "01",
  "CODCATEGORIAESOCIAL": "101",
  "CODSITUACAO": "A",
  "GRAUINSTRUCAO": "7",
  "Jornada_Mensal": "220:00",
  "JORNADAMENSAL": "13200",
  "CONTRIBSINDICAL": "N",
  "FUNCIONARIO": "1",
  "INDINICIOHOR": "1",
  "MOTIVOADMISSAO": "01",
  "SITUACAOFGTS": "1",
  "CODBANCOFGTS": "104",
  "SITUACAOINSS": "1",
  "SITUACAOIRRF": "1",
  "SITUACAORAIS": "1",
  "TIPOADMISSAO": "R",
  "VINCULORAIS": "1",
  "NACIONALIDADE": "10",
  "CODGRPQUIOSQUE": "LOCAL",
  "TEMPOPARCIAL": "0",
  "TIPOREGIMEJORNADA": "1",
  "TPREGIMEPREV": "1",
  "ESTADONATAL": "MT",
  "PAIS": "Brasil",
  "CODSINDICATO": "0001",
  "CODFUNCAO": "00004",
  "CODHORARIO": "0010",
  "CODSECAO": "01.01",
  "SALARIO": "17600.00",
  "DATAADMISSAO": "2025-04-28T00:00:00",
  "DTBASE": "2025-04-28T00:00:00",
  "DTOPCAOFGTS": "2025-04-28T00:00:00",
  "DTCARTTRAB": "2025-04-28T00:00:00",
  "DTMUDANCACONTRIBSINDICAL": "2025-04-28T00:00:00",
  "DTMUDANCAFUNCAO": "2025-04-28T00:00:00",
  "DTMUDANCAHORARIO": "2025-04-28T00:00:00",
  "DTMUDANCASALARIO": "2025-04-28T00:00:00",
  "DTMUDANCASECAO": "2025-04-28T00:00:00",
  "HSTSIT_DATAMUDANCA": "2020-12-02T00:00:00",
  "HSTSEFIP_DTMUDANCA": "2020-12-02T00:00:00",
  "MOTMUDANCASALARIO": "01",
  "HSTSIT_MOTIVO": "1",
  "MOTMUDANCASECAO": "01",
  "MOTMUDANCAFUNCAO": "01"
}
```

**Saiba mais**

[Cross Segmentos - Backoffice RM - Integração - WebServices - Lista de DataServers Web Services](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5275823964567-Cross-Segmentos-Backoffice-RM-Integra%C3%A7%C3%A3o-WebServices-Lista-de-DataServers-Web-Services)

[Cross Segmentos - Backoffice RM - Integração - WebServices - Utilizando o SoapUI para consumir DataServers RM via WebServices](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007851192-Cross-Segmentos-Backoffice-RM-Integra%C3%A7%C3%A3o-WebServices-Utilizando-o-SoapUI-para-consumir-DataServers-RM-via-WebServices)
