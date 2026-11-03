---
content_hash: 0eef213963b9d7b35e2818a7e5c1ab5762d5ddd9f1ba99387eca1bb3897f4429
fetched_at: '2026-06-29T00:08:09.348453+00:00'
page_id: '239034160'
product: rm
source: tdn-rm
title: Conexão a Banco de Dados Externo MySQL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=239034160
version: 14
---

# Índice:

---

.\*ndice:

# Objetivo

---

       O objetivo deste documento é demonstrar como configurar uma conexão em Banco de Dados Externo MySQL e como utilizá-lo em uma Consulta SQL.

# Introdução

---

          O RM permite a utilização de Banco de Dados Externo com o MySQL para execução de Consultas SQL. A configuração da Conexão de banco pode ser feita na própria tela de edição da Consulta, em qualquer módulo, menu '**Gestão | Visão de Dados**', ou no módulo '**Serviços Globais**'**,** menu'**Segurança | Conexões a banco de dados externos**'.

          Veja nos passos a seguir como deve ser feito o procedimento para utilização desse recurso.

falseDesenvolvimento/ProcedimentoPasso 1Passo 1Passo 1

 Crie a sentença SQL desejada, acessando o menu **'Gestão | Visões de Dados'** e clique no botão Incluir (Ctrl + Ins).

Em seguida, clique em Banco de Dados Externo, para vincular a Consulta ao banco **MySQL**.

Por essa tela também é possível gerenciar as conexões externas existentes em Consultas SQL, criar novas ou editar.

Passo 2Passo 2Passo 2

Para cadastrar uma nova conexão, após acessar a tela de Conexões a banco de dados externos, clique no botão Incluir (Ctrl + Ins) e preencha os principais campos, como demonstrado no exemplo abaixo:

Clique em "String de conexão", selecione o Data Source e Data Provider conforme seu ambiente. No exemplo a seguir, usaremos uma conexão MySQL.

Clique em "OK".

Passo 3Passo 3Passo 3

Clique em "Test Connection" para certificar que a base está acessível e a conexão está funcionando, como mostrado na imagem abaixo:

Passo 4Passo 4Passo 4

Se ao clicar no botão salvar, **o erro evidenciado abaixo¹** acontecer, algumas providências terão que ser tomadas para que a consulta possa ser devidamente executada. Essa não conformidade poderá ser apresentada, caso existam configurações incorretas.

**Imagem** – Não conformidade apresentada, caso existam configurações incorretas.

Observação

**Erro evidenciado¹:** A causa da mensagem de não conformidade evidenciada na **imagem** acima é porque a versão do arquivo **MySql.Data.dll** estava diferente da versão da entrada **“MySQL Data Provider”.**

**SOLUÇÃO**

Dentro da pasta **Config** **[C:\windows\Microsoft.NET\Framework\v4.0.30319\Config]²,** abra o arquivo chamado **Machine.Config**.

**Imagem** – Arquivo **machine.config**.

Observação

**Config** **[C:\windows\Microsoft.NET\Framework\v4.0.30319\Config]**²**:** A pasta **v4.0.30319** se refere a versão do **.NET framework** instalado na máquina, deve-se verificar na pasta do framework instalado na máquina, sendo ele versão 4, 4.5, 4.6, etc....

Ao abrir o arquivo machine.config, verifique se:

* A tag **<DbProviderFactories>** está presente nesse arquivo;
* A tag **<DbProviderFactories>** “fecha” corretamente, ou seja, se existe a diretiva **</ DbProviderFactories>**
* Alguma entrada filha dessa tag **<DbProviderFactories>** está vazia;
* A entrada filha cujo nome é **“MySQL Data Provider”** está presente.

**Imagem** – Tag **<DbProviderFactories>.**

Correções necessárias, caso algum dos casos acima aconteçam:

* Caso a tag **<DbProviderFactories>** não exista adicione-a como filha da tag **<System.Data>.**
* Caso a tag **<DbProviderFactories>** não feche corretamente, adicione a diretiva **</ DbProviderFactories>**
* Caso alguma entrada da tag **<DbProviderFactories>** estiver vazia, remova-a**.**
* Caso a entrada **“MySQL Data Provider”** não estiver presente adicioná-la**.**

1580836060781\_-201640808

| <add name="MySQL Data Provider" invariant="MySql.Data.MySqlClient" description=".Net Framework Data Provider for MySQL" type="MySql.Data.MySqlClient.MySqlClientFactory,   MySql.Data, Version=6.9.8.0, Culture=neutral, PublicKeyToken=c5687fc88969c44d" /> |
| --- |

Após verificar e/ou corrigir as inconsistências indicadas acima, é hora de comparar a versão entre a entrada evidenciada no quadro acima **“MySQL Data Provider”** e a versão do **MySql.Data.dll.**

**Imagem** – Versão da entrada **“MySQL Data Provider”.**

**Imagem** – Versão do arquivo **MySql.Data.dll.**

 

A versão tanto do arquivo **MySql.Data.dll**, quanto da entrada **“MySQL Data Provider”** deve ser a mesma**.**

O arquivo **MySql.Data.dll** se encontra na pasta **RM.Net **[C:\windows\totvs\CorporeRM\RM.Net]****, pasta padrão onde foi instalado a **biblioteca RM.**

**Imagem –** Localização do arquivo **MySql.Data.dll.**

Observação

**Atenção:** É recomendado que após a instalação e configuração dos providers net connector seja realizado a reinicialização do sistema operacional para efetivação das alterações.

Os componentes para conexão podem ser obtidos no site disponível para downloads do MySQL.

**1º MySQL Connector/Net  
<https://dev.mysql.com/downloads/connector/net/>**

**2º MySQL Workbench** (Obs.: Esse componente será necessário instalar, caso o acima sozinho não surta efeito, pois este aplicativo contem alguns outros componentes auxiliares na comunicação do MySQL com o .Net Framework)**.  
<https://www.mysql.com/products/workbench/>**

Passo 5Passo 5Passo 5

Caso os passos descritos até aqui tenham sido executados corretamente, a consulta SQL será executada com sucesso.

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX ou 12.01.XX

false

**Processo:** Banco de Dados Externo

false

**Subprocesso:** Conexão a Banco de Dados Externo MySQL

falsefalse

**Status:** Finalizado

false

**Data:** 26/07/2016

false

**Autores:**
