---
content_hash: 05a79effd23d7e5098855ce955ff86a6d5f3423f7f09944f2f20e78b7d870d7f
fetched_at: '2026-06-29T00:08:33.918991+00:00'
page_id: '274629504'
product: rm
source: tdn-rm
title: RMEDU00002_Utilizando Dataserver para leitura de Alunos
type: documentation
url: https://tdn.totvs.com/display/LRM/RMEDU00002_Utilizando+Dataserver+para+leitura+de+Alunos
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Educacional |
| **Versões:** | 12.1.16 |
| **Observações:** | WebService |

Após configurar o ambiente acessar o link abaixo e validar a conexão

<http://localhost:8051/wsPageIndex/>

Onde Localhost deve ser o nome ou IP servidor onde o WebService foi exposto

Ao clicar no link indicado a pagina abaixo deve ser exibida

Como vamos validar cadastros de alunos precisamos clicar na primeira opção "[wsDataServer/MEX?wsdl](http://localhost:8051/wsDataServer/MEX?wsdl)" a tela abaixo deve ser exibida

**Para consumir os WebServices, utilize um aplicativo que faça uso do protocolo Soap nas chamadas. Indicamos o SoapUI.**

****Para baixar o software, [Clica aqui para Download](https://www.soapui.org/downloads/soapui.html)****

Nomear o Novo Projeto e inserir o Link recuperado

<http://localhost:8051/wsDataServer/MEX?wsdl>

Apos criar o Projeto a tela abaixo será exibida

Com vamos Ler os dados é necessário clicar na Opção "ReadRecord" e clicar na opção "Request 1" duas vezes a tela abaixo será exibida

Na opção DataServerName inserir o DataServer a ser utilizado, neste caso vamos utilizar o de Alunos "EduAlunoData"

Na Opção PrimaryKey devem ser inseridas a chave primaria da tabela CODCOLIGADA e RA.

Na Opção Contexto devem ser inseridos os campos CODCOLIGADA: Código da Coligada, CODFILIAL: Código da Filial, CODTIPOCURSO: Código referente ao nível de ensino

Obs. Todos os campos devem ser separados por ; (Ponto e virgula)

Exemplo:

Para leitura das informações é necessário a autenticação com um usuário com acesso ao sistema.

neste caso informamos o usuário e a senha do mestre.

Clicar no Ícone Verde marcado de amarelo.

Apos clicar no Play tela abaixo será exibida com o XML de leitura dos dados do cadastro do Aluno.

XML extraido com informações do cadastro do Aluno

<s:Envelope xmlns:s="<http://schemas.xmlsoap.org/soap/envelope/>">  
 <s:Body>  
 <ReadRecordResponse xmlns="<http://www.totvs.com/>">  
 <ReadRecordResult><![CDATA[<EduAluno>  
 <SAluno>  
 <CODCOLIGADA>1</CODCOLIGADA>  
 <RA>ES-00181</RA>  
 <CODTIPOALUNO>4</CODTIPOALUNO>  
 <CODPESSOA>12649</CODPESSOA>  
 <CODTIPOCURSO>1</CODTIPOCURSO>  
 <CODIGO>12649</CODIGO>  
 <DESCTIPOALUNO>Veterano</DESCTIPOALUNO>  
 <SEXO>M</SEXO>  
 <NOME>Teste Cadastro Aluno WebService</NOME>  
 <CPF>23146829479</CPF>  
 <SOBRENOME>WebService</SOBRENOME>  
 <DTNASCIMENTO>1978-03-02T00:00:00</DTNASCIMENTO>  
 <ESTADOCIVIL>S</ESTADOCIVIL>  
 <EMAIL>testecadastroalunowebservice@[totvs.com.br](http://totvs.com.br)</EMAIL>  
 <NACIONALIDADE>10</NACIONALIDADE>  
 <ESTADONATAL>MG</ESTADONATAL>  
 <NATURALIDADE>Belo Horizonte</NATURALIDADE>  
 <CODUSUARIO>ES-00181</CODUSUARIO>  
 <DEFICIENTEFISICO>0</DEFICIENTEFISICO>  
 <DEFICIENTEFALA>0</DEFICIENTEFALA>  
 <DEFICIENTEMENTAL>0</DEFICIENTEMENTAL>  
 <DEFICIENTEVISUAL>0</DEFICIENTEVISUAL>  
 <DEFICIENTEAUDITIVO>0</DEFICIENTEAUDITIVO>  
 <RUA>RUA CAMPESTRE</RUA>  
 <NUMERO>626</NUMERO>  
 <COMPLEMENTO>CASA</COMPLEMENTO>  
 <BAIRRO>DOM BOSCO</BAIRRO>  
 <PAIS>BRASIL</PAIS>  
 <ESTADO>MG</ESTADO>  
 <CIDADE>Betim</CIDADE>  
 <TELEFONE1>3121229733</TELEFONE1>  
 <TELEFONE2>3199999733</TELEFONE2>  
 <TELEFONE3>3121229733</TELEFONE3>  
 <FAX>3121229733</FAX>  
 <CEP>30000000</CEP>  
 <NIT>0</NIT>  
 <NROFILHOSBRASIL>0</NROFILHOSBRASIL>  
 <CONJUGEBRASIL>0</CONJUGEBRASIL>  
 <NATURALIZADO>0</NATURALIZADO>  
 <FILHOSBRASIL>0</FILHOSBRASIL>  
 <INDATENDESPECIALIZADO>00</INDATENDESPECIALIZADO>  
 <INDATENDESPECIFICO>00</INDATENDESPECIFICO>  
 <INDICADORDERECURSOS>00</INDICADORDERECURSOS>  
 <CANHOTO>F</CANHOTO>  
 <USERID>ES-00181</USERID>  
 <BRPDH>0</BRPDH>  
 <INVESTTREINANT>0.00</INVESTTREINANT>  
 <ESTADOROW>0</ESTADOROW>  
 <ROWVALIDA>0</ROWVALIDA>  
 <ALUNO>1</ALUNO>  
 <PROFESSOR>0</PROFESSOR>  
 <CANDIDATO>0</CANDIDATO>  
 <USUARIOBIBLIOS>1</USUARIOBIBLIOS>  
 <FUNCIONARIO>0</FUNCIONARIO>  
 <EXFUNCIONARIO>0</EXFUNCIONARIO>  
 <CODTIPOBAIRRO>1</CODTIPOBAIRRO>  
 <CODTIPORUA>1</CODTIPORUA>  
 <DEFICIENTEINTELECTUAL>0</DEFICIENTEINTELECTUAL>  
 <FALECIDO>0</FALECIDO>  
 <CODSTATUS>-1</CODSTATUS>  
 <FIADOR\_SGI>0</FIADOR\_SGI>  
 <CONJUGE\_SGI>0</CONJUGE\_SGI>  
 <RECCREATEDBY>mestre</RECCREATEDBY>  
 <RECCREATEDON>2017-05-19T12:12:46</RECCREATEDON>  
 <RECMODIFIEDBY>mestre</RECMODIFIEDBY>  
 <RECMODIFIEDON>2017-05-19T14:01:57</RECMODIFIEDON>  
 <CODIGO1>12649</CODIGO1>  
 </SAluno>  
 <SAlunoCompl>  
 <CODCOLIGADA>1</CODCOLIGADA>  
 <RA>ES-00181</RA>  
 <RECCREATEDBY>mestre</RECCREATEDBY>  
 <RECCREATEDON>2013-01-08T08:23:18</RECCREATEDON>  
 <RECMODIFIEDBY>mestre</RECMODIFIEDBY>  
 <RECMODIFIEDON>2017-05-19T14:02:00</RECMODIFIEDON>  
 </SAlunoCompl>  
 <SAlunoMEC>  
 <CODCOLIGADA>1</CODCOLIGADA>  
 <RA>ES-00181</RA>  
 <NACIONALIDADE>1</NACIONALIDADE>  
 <TRANSPORTEPUB>0</TRANSPORTEPUB>  
 <ZONARESIDENCIA>1</ZONARESIDENCIA>  
 <EDUEMOUTROESPACO>3</EDUEMOUTROESPACO>  
 <NECESSIDADEESPEC>0</NECESSIDADEESPEC>  
 <DEFAUDITIVA>0</DEFAUDITIVA>  
 <DEFFISICA>0</DEFFISICA>  
 <DEFMENTAL>0</DEFMENTAL>  
 <RALIMPO>ES00181</RALIMPO>  
 <TRPRODVAN>0</TRPRODVAN>  
 <TRPRODMICROBUS>0</TRPRODMICROBUS>  
 <TRPRODBUS>0</TRPRODBUS>  
 <TRPRODBICICLO>0</TRPRODBICICLO>  
 <TRPRODANIMAL>0</TRPRODANIMAL>  
 <TRPRODOUTRO>0</TRPRODOUTRO>  
 <TRPBARCOATE5>0</TRPBARCOATE5>  
 <TRPBARCOATE15>0</TRPBARCOATE15>  
 <TRPBARCOATE35>0</TRPBARCOATE35>  
 <TRPBARCOMAIS35>0</TRPBARCOMAIS35>  
 <TRPFERROVIARIO>0</TRPFERROVIARIO>  
 </SAlunoMEC>  
</EduAluno>]]></ReadRecordResult>  
 </ReadRecordResponse>  
 </s:Body>  
</s:Envelope>
