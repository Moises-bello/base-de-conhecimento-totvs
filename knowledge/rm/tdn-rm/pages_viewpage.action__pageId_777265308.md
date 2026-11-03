---
content_hash: 2161f32c9c2503664648d4f6bddd191e303f782c1fca0ece78571fc89bd518b3
fetched_at: '2026-06-29T00:11:37.378875+00:00'
page_id: '777265308'
product: rm
source: tdn-rm
title: Cópia de RMEDU00001_Automação via Web Services ( Processos )
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=777265308
version: 1
---

# **AUTOMAÇÃO DE WEB SERVICE**

**Sobre a ferramente SoapUI :**

SoapUI é uma ferramenta open source escrita em Java cuja principal função é consumir e testar Web Services. Web Service é uma tecnologia baseada em [XML](http://www.devmedia.com.br/xml-e-seu-armazenamento-em-bancos-de-dados/28744) e HTTP cuja principal função é disponibilizar serviços interativos na WEB que podem ser acessados (ou consumidos) por qualquer outra aplicação independente da linguagem ou plataforma em que a aplicação foi construída. O SOAP (Simple Object Access Protocol) é o padrão universal utilizado para a troca de mensagens entre as aplicações consumidoras e o Web Service. O Web Service expõe as suas operações por meio de um tipo de esquema XML chamado WSDL (Web Service Description Language). Neste contexto, o SoapUI facilita todo o processo de criação e depuração dos testes por meio de uma interface gráfica visual e intuitiva. Dentre as suas principais características, podemos destacar as seguintes:

* Importação e geração automática das requisições descritas no WSDL;
* Capacidade de gerenciar um número ilimitado de requisições para cada operação;
* Gerenciamento de múltiplo endpoints para cada Web Service;
* Validação das requisições e respostas contra as suas definições no WSDL;
* [Testes funcionais](http://www.devmedia.com.br/automacao-de-testes-funcionais-em-sistema-embarcados/33993), carga e stress;
* Execução de diversos testes em paralelo;

**Baixar a ferramenta SoaupUI** : <https://www.soapui.org/downloads/latest-release.html>

# WEB SERVICE

**Como subir o serviço de Web Service:**Clique no Link ao lado :  

Web Service é uma solução que permite integrar aplicações web independente de plataforma ou linguagem que foram escritas proporcionando agilidade e eficiência na troca de informações. Através de uma “linguagem universal”, no caso a XML, um Web Service poderá receber dados e processá-los em sua linguagem de origem e em seguida disponibilizar a informação ou serviço para o qual foi projetado para a aplicação que o invocou. Um Web Service é descrito e definido usando XML (eXtensible Markup Language) e são identificados por uma URI (Unique Resource Identifier). Uma das grandes motivações para a utilização de Web Services é a possibilidade de diferentes aplicações comunicarem entre si utilizando recursos diferentes. Em outras palavras, o Web Service permite que qualquer aplicação possa utilizá-lo extraindo e operando informações disponibilizadas por estes. Os Web Services fazem uso de algumas tecnologias como XML, WSDL, SOAP e UDDI

# 1º ) Levantar o WebService RM

http://( IP DA MÁQUINA ):8051/wsProcess/MEX?wsdl

* Clicar no Processo  ( wsProcess ) para obter o WebService ( Processos )
* Se for um Crud ( DataServer )

# 2º Fazer todo processo na Base Resultado **( Processo que deseja resultado final na Base Modelo )**

Acessar o  RM ( Executar | Pesquisar por : JOB )

Clicar em : XML de Parâmetros de Job..

Localizar o JOB desejado ( Editar ) Exemplo : EduTransferenciaInternaData

Copiar todo comando XML .

# 3º ) Abrir o SoapUI

File | New SOAP Project

Project Name : Inserir  Nome do Projeto Desejado

Initial WSDL : ( Inserir o WebService ) Processo que foi informando no primeiro passo.

Expandir o Processo : Localizar ( ExecuteWithParams )

Sobre o Método :

* "ExecuteWithXmlParams" é o mais indicado para criação de processos.

Request1 ( Editar )

Informar o nome do Processo

Exemplo : EduMudancaTurmaData

Dentro de : <tot:strXmlParams>?</tot:strXmlParams>

Informar o XML ( Parâmetros do JOB – Gerado no RM )

`OBS :` Antes do XML – Não esquecendo de iniciar com ***<![CDATA[    e***Terminar com ***]]>  - Como é visualizado nos Prints Abaixo.***

Autenticar .

Selecionar Type : Basic

Username : mestre

Password : totvs

Pre-emptive auth ( Authenticate pre-emptively )

 Importante executar o Web Sevice na base Modelo para verificar se todo cenário encontra-se idêntico ao da Base Resultado antes de executar o processo como exemplo:

* Codigo de Curso se é o mesmo.
* Código de Turma.
* Código de Contrato.
* Etc..

# 4º) Acessar Teste Flow

<http://bh-testflow/testflow/dashboard>

Testando WebService ( via Teste Flow )

Criando a tarefa do WebService

Cadastros | Atividades | Serviços | Web Service

Nome : Inserir Nome do Projeto de Web Services

Descrição : Inserir Descrição

URI ( WSDL ) Informar o Web Service  ( Informar o IP o Nome da máquina na qual o usuário deseja fazer a validação )

Em Propriedades :

Inserir usuário e senha para autenticação do Web Service

* Se for a base modelo o teste Web Service, é necessário lembrar de apagar os registros da base para quando a automação for executada não encontrar duplicidades.

Em Operações :

Clicar em RM\_IwsProcess

Selecionar o Processo :

Neste exemplo : ExecuteWhitXmlParams:string

* ***Copiar o XML que foi validado no SOAPUI***

Clicar em : Validar

Web Service – Validado

Criando o Projeto de Teste

Clicar em Novo

**1º Processo ( Restaurar Base Modelo )**

**Obs:** verificar caminho onde vai obter o BKP .. versão

**2º Alias** – Inserir o Alias para o processo

Alterar o Alias no Host .. Para a Base Modelo

# 3º ) Iniciar RM.Host.exe

# 4º ) Iniciando processo de Web Service

# 5º ) Comparação de banco

Comparando Transferência

Comparando contrato

Inserir os Dois Scripts no Projeto de Teste

Processo de Falha ( Finalizar – Apagar ) Marcar para Ignorar Resultado

Selecionar todas as Atividades que necessitam de um Recurso e vincular .

Exemplo de um Projeto de teste WS pronto

* Restaurar Base Modelo
* Subir o Alias
* Iniciar o Host
* Executar o Web Services
* Comparar o Banco

Incluir os processos para Apagar Alias, Banco , Finalizar processo e Sleep

Feito o Projeto ( Versionar o mesmo em Agendamento )

Execução de Testes | Agendamentos

* Informar a Versão
* Grupo de servidores
* Projeto de teste
* Produto  ( EDU )

Selecionar a Versão Desejada | Servidor  e Executar o processo .

**Obs: Lembrar de apagar o Alias do Alias.Dat ( RM ) para base Modelo antes de executar o processo**

**Lembrar também de : O TOTVERS que fizerem a Automação , fazer sempre o backup da base modelo no servidor de automação, para que possa pegar todo cenário construído .**
