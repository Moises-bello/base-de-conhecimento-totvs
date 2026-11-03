---
content_hash: 51857fff6308e320e2971aa449264c512c20a638fc2f7c13c47e340ab500ad3c
fetched_at: '2026-06-28T21:35:28.344609+00:00'
page_id: '661871105'
product: fluig
source: tdn-fluig
title: Migração e Conversão do Oracle ECM para plataforma TOTVS Fluig
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=661871105
version: 24
---

# Índice

true.\*ndicenone

oculto

**Obs**: Liberar essa documentação após a liberação do oracle 19 e da issue FFDN-6298

# Objetivo

---

O objetivo deste guia é indicar um método de migração dos dados de uma base do TOTVS ECM 3.00 para o Fluig Plataforma. Utilizando conjunto de caracteres padrão para base através do NLS\_CHARACTERSET =  AL32UTF8, eliminando assim a necessidade de converter tabela por tabela.

# Pré-requisitos

---

* Conhecimento em administração de banco de dados Oracle;
* Conhecimento em ferramentas de UI/CLI Oracle.

# Ferramentas Utilizadas

---

* Oracle Database 19C XE
* SQL Plus
* SQL Developer

# Procedimento de Migração e Conversão de Dados

---

Atenção!

Esta operação deve ocorrer antes da conversão de uma base TOTVS ECM para TOTVS Fluig Plataforma. Mesmo com a alteração do agrupamento padrão, os campos existentes permanecem incorretos, podendo assim, causar comportamentos inesperados na utilização da plataforma.

Acompanhe a seguir o checklist para a conversão.

false1true1Passo 01

* Gere um **DUMP** desta base de dados do **TOTVS ECM 3.00**, com toda estrutura de tabelas, campos e dados.
* É necessário realizar alguns processos para que a exportação ocorra com sucesso, portanto, utilize o procedimento a seguir:

**1)** Criar um diretório no sistema operacional para armazenar os arquivos exportados (Dumps), conforme exemplo abaixo: 

**2)** Logo em seguida, acesse a ferramenta **sqlplus**, com o seguinte comando: 

**3)** Execute a instrução SQL abaixo, passando o caminho da pasta que você criou anteriormente:

 CREATE OR REPLACE DIRECTORY exp\_dumps AS ‘/home/oracle/dumps/exp\_dump’;]]>

**4)** Agora é necessário setar permissão para o usuário que vai realizar a exportação dos dados, para isso, utilize o comando abaixo:

 GRANT READ, WRITE on directory exp\_dumps TO seu\_usuario;]]>

**5)** Após setar as permissões, saia do SQL Plus com o comando “**exit**” e abra o SQL Developer, para realizarmos a exportação da base;

**6)** Com o banco na ferramenta instalado e uma conexão já configurada, clique no menu **Exibir > DBA** e **selecione** sua conexão. Caso a conexão não apareça, clique no ícone “**+**” para selecionar uma nova:

Veja a imagem

**7)** Em seguida, vá até a opção **Data Pump** > **Jobs de Exportação** > clique no botão**Ações** > **Assistente de Exportação do Data:**

Veja a imagem

**8)** Após realizar os procedimentos mencionados até aqui e com a tela do **Assistente de Exportação do Data** aberta**,**basta seguir os passos abaixo em cada tópico:

* **Origem**

*-Dados ou DDL:* Dados e DDL   
*-Tipos a serem exportados no Data Pump:* Tabelas

Veja a imagem

* **Tabelas**

-Selecione o esquema  
-Selecione todas as tabelas

Veja a imagem

* **Dados da tabela**

-Selecione todas as tabelas e campos

Veja a imagem

* **Opções**

-**Ative o log** e selecione a pasta de **exportação de dumps** criada anteriormente

Veja a imagem

* **Arquivos de Saída**

-Selecione o diretório de exportação criado anteriormente;  
-Defina o nome do arquivo, recomendado usar o nome do schema;  
-Deixe marcado as opções: *Anexar Timestamp a nomes de Dump, Log e Job; Compactação; Ir para resumo.*

Veja a imagem

* Confira o resumo e clique em **finalizar** para gerar o Dump

  Veja a imagem

2Passo 02

* Agora vamos configurar o banco de dados que irá receber os dados e a instalação do Fluig Plataforma.

         Primeiramente, acesse a documentação de [configuração do banco de dados Oracle](https://tdn.totvs.com/x/uAVbDw) disponível no TDN , crie o usuário/schema + tablespace e realize as configurações necessárias para funcionamento da plataforma.

3Passo 03

* Após realizar as configurações indicadas no passo 2, crie uma conexão no SQL Developer para essa nova base, e acesse o Assistente de Importação do Data Pump na palheta **DBA** > **Data Pump** > **Jobs de Importação** > clique no botão **Ações** > **Assistente de Importação:**

* **Tipo**

-Dados e DDL  
-Tipo de importação: Tabelas  
-Escolha o diretório IMP\_DUMPS criado anteriormente e insira o nome do arquivo de dump gerado.

Veja a imagem

* **Filtrar**

-Selecione todas as tabelas do schema desejado

Veja a imagem

* **Remapeamento**

-**Remapear Esquemas***Origem:* Schema da base original  
*Destino:* Novo Schema

-**Remapear Tablespaces**Mesma lógica dos esquemas

Veja a imagem

* **Opções**

-Clicar na opção **Ativar Log**-Selecione o diretório de importação e defina o nome do arquivo de log  
-Clicar em **Anexar Timestamp a nomes de Log e Job** e ****Ir para resumo.****

Veja a imagem

* **Resumo**

-Confira os dados e clique em **finalizar** para executar o Job

Veja a imagem4Passo 04

* Instalar a versão **1.5.13** (Última EP) do Fluig e apontar a configuração para esta base de dados (fluig).
5Passo 05

* Inicializar o serviço Fluig, e acompanhar o LOG, para se certificar de que toda a inicialização foi bem sucedida. Caso apresente alguma inconsistência, como por exemplo, falha na conexão com a base de dados, basta seguir o passo 6.
6Passo 06

* Retornar ao processo de [c](https://tdn.totvs.com/x/qANbDw)[onversão TOTVS ECM para plataforma TOTVS Fluig](https://tdn.totvs.com/x/qANbDw) se for este o caso, ou então, realizar as validações desejadas e uso da nova instalação.

$("b:contains('oculto')").parent().parent().hide();
]]>
