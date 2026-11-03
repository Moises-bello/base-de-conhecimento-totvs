---
content_hash: f9a63470ef1c82512a239c0ade5abb0dd1d3a4818c0042ff47fd996990a175fe
fetched_at: '2026-06-29T00:08:48.026353+00:00'
page_id: '322148630'
product: rm
source: tdn-rm
title: WebService - Inscrição de Candidatos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=322148630
version: 9
---

Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Educacional |
| **Versões:** | 12.1.17 |
| **Pre-****requisitos** | Para utilização da Funcionalidade é necessário que já existe a pessoa cadastrada na base de dados, para criação da pessoa, utilizar o Dataserver RHUPESSOADATA |

Como configura o WebService e Obter as chaves primarias.

[Como Expor os Web Services do RM através do Host (recomendado)](http://tdn.totvs.com/pages/viewpage.action?pageId=89620766)

[Utilizando o TOTVS WS Client - Ferramenta para auxiliar a utilização dos Web Services providos pelo TBC](http://tdn.totvs.com/pages/viewpage.action?pageId=189307798)

**Informações de criação do Projeto e Autenticação no link abaixo.**

[Criação do Projeto e Autenticação.](http://tdn.totvs.com/pages/viewpage.action?pageId=322149560)

**Criando XML base para cadastro de candidatos**

Acesse o aplicativo SoapUi (Disponível na web gratuitamente <http://www.soapui.org/>)

Solicite um novo projeto e informe:

- O nome do projeto

- O link WSDL copiado anteriormente na configuração do WS RM

Será criado um projeto com as opções do print abaixo, onde deverão ser definidas as propriedades listadas:

- Name = Nome da Janela/página do ReadRecord para o projeto

- Encoding = UTF-8

- **Username** = Usuário do sistema RM

- **Password** = Senha do usuário do sistema RM

Localizar o Projeto Criado "Inscrição Processo Seletivo"

RM\_IwsSataServer

Localizar

ReadRecord - Request 1

Clicar com Botão direito Rename

Clicar duas vezes no Item criado.e a tela abaixo será exibida

Dê um duplo clique em Inscrição Candidato, em seguida será aberto uma janela. Informe nas tags abaixo, os valores:

**É de suma importância que todas as tags abaixo estejam corretamente configuradas.**

- “*<tot:DataServerName>*”  EduPSInscricaoAreaOfertadaData

- ***“**<tot:PrimaryKey>*”  COLIGADA;IDPS;NUMEROINSCRICAO (ex.: 1;173;1)

- “*<tot:Contexto>*”  CODCOLIGADA=1,CODFILIAL=1,CODUSUARIO=mestre,CODSISTEMA=S (dados do contexto)

Clique no ícone “Submit” (Play) conforme demonstra o print acima. Neste momento, o sistema irá gerar o XML do candidato pesquisado, sendo este a base para a criação de novos XML’s de Cadastro de candidato via SoapUI ou WebService.

Obs.: O Arquivo tem início no marcador “<![CDATA[” e final no marcador “]]>”. Entre estes marcadores está o XML do candidato pesquisado, que servirá como base para os candidatos que serão incluídos a partir do WebService.

Exemplo

XML gerado.

<![CDATA[<EduPSInscricaoAreaOfertada>  
 <SPSInscricaoAreaOfertada>  
 <CODCOLIGADA>1</CODCOLIGADA>  
 <IDPS>173</IDPS>  
 <CODPESSOA>12936</CODPESSOA>  
 <NUMEROINSCRICAO>1</NUMEROINSCRICAO>  
 <IDFORMAINSCRICAO>159</IDFORMAINSCRICAO>  
 <DATAINSCRICAO>2017-12-19T11:21:38</DATAINSCRICAO>  
 <VALORINSCRICAO>0.0000</VALORINSCRICAO>  
 <VALORDESCONTO>0.0000</VALORDESCONTO>  
 <UTILIZANOTAENEM>F</UTILIZANOTAENEM>  
 <NUMEROCARTAORESPOSTA>1</NUMEROCARTAORESPOSTA>  
 <CODMUNICIPIO>06200</CODMUNICIPIO>  
 <CODETDMUNICIPIO>MG</CODETDMUNICIPIO>  
 <ENEMNUMINSCRICAO />  
 <STATUS>1</STATUS>  
 <TREINEIRO>F</TREINEIRO>  
 <DEFAUDITIVA>F</DEFAUDITIVA>  
 <DEFVISUAL>F</DEFVISUAL>  
 <DEFFISICA>F</DEFFISICA>  
 <DEFMULTIPLA>F</DEFMULTIPLA>  
 <DEFOUTRAS>F</DEFOUTRAS>  
 <DEFMOTIVOOUTRAS />  
 <CODCOLIGADAQS>0</CODCOLIGADAQS>  
 <CODPROVAQS />  
 <IDQS>0</IDQS>  
 <CANHOTO>F</CANHOTO>  
 <SENHA>01r0tN2N1y</SENHA>  
 <NOMECANDIDATO>Candidato Processo Seletivo</NOMECANDIDATO>  
 <STATUSLAN>10</STATUSLAN>  
 <IDCAMPUS>2</IDCAMPUS>  
 <COTAFEDERAL>F</COTAFEDERAL>  
 <COTAFEDERALENSINOPUBLICO>F</COTAFEDERALENSINOPUBLICO>  
 <COTAFEDERALRENDA>F</COTAFEDERALRENDA>  
 <COTAFEDERALCORACA>F</COTAFEDERALCORACA>  
 <USANOVOPORTAL>F</USANOVOPORTAL>  
 <IDCAMPUS1>2</IDCAMPUS1>  
 <CODFILIAL>1</CODFILIAL>  
 <IDBOLETO />  
 </SPSInscricaoAreaOfertada>  
 <SPSOpcaoInscrito>  
 <CODCOLIGADA>1</CODCOLIGADA>  
 <IDPS>173</IDPS>  
 <CODPESSOA>12936</CODPESSOA>  
 <NUMEROINSCRICAO>1</NUMEROINSCRICAO>  
 <IDAREAINTERESSE>33</IDAREAINTERESSE>  
 <NUMEROOPCAO>1</NUMEROOPCAO>  
 <NOME>Tecnologia em Redes</NOME>  
 <STATUS>0</STATUS>  
 <NUMEROVAGAS>10</NUMEROVAGAS>  
 </SPSOpcaoInscrito>  
 <SPSIdiomaInscrito>  
 <CODCOLIGADA>1</CODCOLIGADA>  
 <IDPS>173</IDPS>  
 <CODPESSOA>12936</CODPESSOA>  
 <NUMEROINSCRICAO>1</NUMEROINSCRICAO>  
 <IDAREAINTERESSE>33</IDAREAINTERESSE>  
 <CODIDIOMA>1</CODIDIOMA>  
 <NOME>Português</NOME>  
 </SPSIdiomaInscrito>  
 <SPSInscAreaOfertaCompl>  
 <CODCOLIGADA>1</CODCOLIGADA>  
 <IDPS>173</IDPS>  
 <NUMEROINSCRICAO>1</NUMEROINSCRICAO>  
 <CODPESSOA>12936</CODPESSOA>  
 <VICTOR>F</VICTOR>  
 <CC>T</CC>  
 <DD>T</DD>  
 </SPSInscAreaOfertaCompl>  
</EduPSInscricaoAreaOfertada>]]>

**Alterar o XML para o cadastro do novo usuário**

Selecione o conteúdo do XML

Copie para algum editor de texto (Notepad, Notepad++, etc).

Em seguida altere os dados para o cadastro do novo Candidato.

**Obs.:**Devemos nos atentar aos seguintes pontos:

1. O campo <CODPESSOA> deverão ser preenchidos com o valor recuperado da tabela PPESSOA, para realizar a inscrição é necessario que já existe pessoas cadastradas ba base.
2. Todos os campos <NUMEROINSCRICAO> deverão ser preenchidos com o valor "-1" para que o sistema dê sequência as inscrições que já estão cadastradas.
3. O campo <NUMEROCARTAORESPOSTA> não deve conter nenhum valor, para que o sistema dê sequência as inscrições que já estão cadastradas.
4. Os campos <CODMUNICIPIO> e <CODETDMUNICIPIO> são de preenchimento obrigatório, no entanto, se os mesmos não estiverem presentes no XML o candidato não será inscrito..

Lembre-se!

Na versão 12.1.10 todos os campos <NUMEROINSCRICAO> deveram conter valor -1 e o campo <NUMEROCARTAORESPOSTA> não deve conter valores.

Depois de alterado os dados acesse o SaveRecord e abra o Request 1 (Salvar Inscrição Candidato). Lembra de Autenticar o usuario no Auth

Informe novamente nas Tags os valores abaixo:

- “*<tot:DataServerName>*” EduPSInscricaoAreaOfertadaData

- ***“**<tot:PrimaryKey>*” Informar o XML com os dados do novo candidato

- “*<tot:Contexto>*” CODCOLIGADA=1,CODFILIAL=1,CODUSUARIO=mestre,CODSISTEMA=S (dados do contexto)

Clique no ícone “Submit” (Play) para que o candidato seja cadastrado com Sucesso.

Candidato Cadastrado.
