---
content_hash: a708c8b270a478cf4cdfd21cfa6dee489327a10e4ab6e991d823ba7ced091966
fetched_at: '2026-06-28T21:35:30.207130+00:00'
page_id: '817650828'
product: fluig
source: tdn-fluig
title: Métodos de contorno de lentidão na plataforma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=817650828
version: 120
---

Fique atento!

Esta página é válida a partir da atualização **Voyager (2.0)** do TOTVS Fluig.

Se você utiliza uma atualização anterior, acesse Métodos de contorno de lentidão da plataforma da atualização **1.6 até 1.8.2**.

Índicetoc-item-body

# Objetivo

---

Problemas de lentidão no TOTVS Fluig podem acontecer por diversos motivos, por isso, reunimos alguns métodos e ações que podem auxiliar o administrador do ambiente a reduzir ou sanar a lentidão.

Plataforma TOTVS Fluig em Cloud

Clientes Cloud precisam entrar em contato com o time de Cloud para que os procedimentos sejam realizados.

# Pré-requisitos

---

* Servidores respeitando o .
* Plataforma de acordo com os padrões da .
* Ambiente em conformidade com os ciclos de .
* Conferir outras  necessárias.
* Conhecimento prévio referente às documentações  e .

# Limpeza de arquivos temporários e pastas *keys*

---

Realizar a limpeza dos arquivos temporários e pastas *keys*, conforme o passo a passo abaixo:

**01.** Parar a execução dos serviços do Fluig: (1) fluig, (2) fluig\_Indexer e (3) fluig\_RealTime.

**02.** Acessar o diretório: <**diretório de instalação do Fluig>\appserver\standalone**.

**03.** Eliminar as pastas: **data, log, servers** e **tmp**.

Atenção!

Nesse diretório existe a pasta **configuration**, que**não deve ser excluída**, pois se trata de uma pasta fundamental para o funcionamento da plataforma. As demais pastas são todas temporárias. Caso a plataforma não as encontre, ela automaticamente recria as pastas.

Nota:

Esse procedimento reiniciará a plataforma e limpará os arquivos de *log* do ambiente.

**04.** Apagar as pastas *keys* disponíveis nos caminhos:

* **<diretório de instalação do Fluig>\repository\wcmdir**
* **<volume do Fluig>\keys**

**05.** Verificar se existem arquivos que **NÃO** estejam nos formatos **.war**, **.ear** ou **.jar** dentro das pastas **apps**, **core** e **system**. Caso existam, é necessário remover esses arquivos **fora do formato** das pastas:

* **<diretório de instalação do Fluig>\appserver\apps**
* **<diretório de instalação do Fluig>\appserver\core**
* **<diretório de instalação do Fluig>\appserver\system**

Importante!

Os arquivos temporários gerados nestas pastas são excluídos no momento da finalização dos serviços, porém, em casos de desligamentos forçados do ambiente estes arquivos podem não ser excluídos automaticamente. Assim, é necessário fazer a exclusão manualmente. Geralmente, **os arquivos temporários estão no formato .tmp ou são diretórios como o mesmo nome**.

**06.** Iniciar novamente os serviços do Fluig: (1) fluig\_Indexer, (2) fluig\_RealTime e (3) fluig.

# Utilização do Agendador de tarefas

---

**01.** Recomendamos a configuração da**limpeza de notificações** e da **limpeza de arquivos temporários de documentos**por meio do Agendador de tarefas do Fluig. Saiba mais em .

**02.** Em casos **extremos** de lentidão, é possível reduzir o tamanho das tabelas de alerta no banco de dados através da instrução **DELETE** ou **TRUNCATE**. No entanto, **NÃO** recomendamos a manipulação recorrente do banco, o correto é a ativação do Agendador de tarefas.

**a)** **Instrução DELETE:** é usada para excluir as linhas de uma tabela, porém, não libera o espaço ocupado por essas linhas.

sql

**b) Instrução TRUNCATE:** é usada para excluir as linhas de uma tabela e liberar o espaço ocupado por essas linhas.

sql

# *Datasets* utilizando *datasources* nativos do Fluig

---

**01.** Executar as consultas abaixo no banco de dados e enviar os resultados em *prints* ou formato **.csv** para a equipe de Suporte Fluig. Para isso, é necessária abrir um *ticket* na [Central do cliente](https://suporte.totvs.com), a partir da opção **Abrir *ticket***.

sql

## O que o resultado das consultas dizem?

---

→ Se as *queries* retornarem vazias, sem nenhum resultado, significa que as práticas de desenvolvimento do seu ambiente estão corretas e não necessitam de ajustes.

→ Caso alguma *query* retorne resultados, é sinal que existem *datasets* personalizados utilizando os*datasources* nativos da plataforma **FluigDS** e **FluigDSRO**. No exemplo abaixo, uma das queries retornou 36 resultados:

→ Essa prática de desenvolvimento **não é recomendada**, pois o Fluig disputa o *pool* de conexões no banco de dados com os *datasets* que utilizam os *datasources* nativos. O resultado disso é lentidão, queda e/ou indisponibilidade do ambiente, até que este, seja reinicializado ou ocorra a liberação da conexão com o banco novamente.

→ A partir da atualização 1.6.5-190514, sempre que realizar um desenvolvimento usando o *datasource* da plataforma, é **indispensável** utilizar o **AppDS**.

→ Verificar cada *dataset* retornado pelas *queries* e realizar o **ajuste no desenvolvimento** para que utilize o **AppDS**, conforme documentação: [*Datasets* acessando banco de dados externo](https://tdn.totvs.com/display/public/fluig/Datasets+acessando+banco+de+dados+externo).

# Arquivos de instalação relacionados à lentidão

---

Os arquivos de instalação abaixo são os mais solicitados pela equipe de Suporte Fluig. Caso necessário, abra um *ticket* na [Central do cliente](https://suporte.totvs.com), a partir da opção **Abrir *ticket****,*e anexe esses arquivos ao chamado. Essa ação agilizará todo o processo de atendimento:

* **<diretório de instalação do Fluig>\appserver\standalone\configuration\standalone.xml**
* **<diretório de instalação do Fluig>\appserver\bin\standalone.conf (Linux)**
* **<diretório de instalação do Fluig>\appserver\bin\standalone.conf.bat (Windows)**
* **<diretório de instalação do Fluig>\appserver\standalone\log\server.log**
* **<diretório de instalação do Fluig>\node\fluig.rt\package.json**
* **<diretório de instalação do Fluig>\node\fluig.rt\logs**
* **<fluig.conf> (Arquivo que fica dentro do servidor do *Proxy* reverso)**

No entanto, recomendamos que nossos usuários tenham autonomia para detectar as causas de lentidão do seu ambiente. Assim, disponibilizamos uma série de achados nos arquivos de instalação e que podem ocasionar lentidão.

## server.log

---

**01.** O server.log pode ser consultado em: **<diretório de instalação do Fluig>\appserver\standalone\log\server.log**.

**02.** Geralmente, o server.log é um arquivo extenso e sugerimos que consulte [Ferramentas de Análise de Log | Ferramentas indicadas | glogg](https://tdn.totvs.com/pages/viewpage.action?pageId=235336390#FerramentasdeAn%C3%A1lisedeLog-glogg).

**03.** Termos de buscas mais comuns no **glogg:**

* *ERROR;*
* *ja esta sendo executado por;*
* *executou por;*
* *invokeFunction.servicetask64;*
* *invokeFunction.createDataset;*
* Thread em execução (ex.: *default task-39*).

**04.** Principais achados no **server.log:**

**a)** Sincronização de *d**atasets* levando mais tempo que o tolerável para finalizar as sincronizações. No exemplo, os *datasets* estão sincronizando por mais de **2500 segundos**:

javaserver.log

**b)** Execução de *datasets* personalizados com tempo maior que **5 segundos**. Normalmente, essa situação está relacionada com a utilização dos *datasources* nativos do Fluig nesses desenvolvimentos. Exemplos:

javaserver.log

**c)** Os termos ***"*invokeFunction.servicetask64"**e **"****invokeFunction.createDataset"**,geralmente, possuem relação com *datasets* de ***Workflow* (Processos)**:

javaserver.log

**d****)** Busca pela *thread* em execução **(****default task-39)***:*

javaserver.log

## standalone.xml

---

**01.** O standalone.xml pode ser consultado em: **<diretório de instalação do Fluig>\appserver\standalone\configuration\standalone.xml.**

**02.** O **<max-pool-size>** pode ser ajustado entre **50-200** nos *datasources*. É possível utilizar um **<max-pool-size>** menor, quando houver mais de um banco de dados no mesmo servidor.

xmlstandalone.xml

jdbc:mysql://localhost:3306/fluig\_mysql?useSSL=false&nullDatabaseMeansCurrent=true
mysqlDriver
TRANSACTION\_READ\_COMMITTED

10
100

admin
admin


true
false

false

jdbc:mysql://localhost:3306/fluig\_mysql?useSSL=false&nullDatabaseMeansCurrent=true
mysqlDriver
TRANSACTION\_READ\_COMMITTED

5
50

admin
admin


true
false

30000

false

jdbc:mysql://localhost:3306/fluig\_mysql?useSSL=false&nullDatabaseMeansCurrent=true
mysqlDriver
TRANSACTION\_READ\_COMMITTED

5
150

admin
admin


true
false

30000

false


com.mysql.jdbc.Driver
]]>

## standalone.conf (Linux)

---

**01.** O standalone.conf pode ser consultado em: **<diretório de instalação do Fluig>\appserver\bin\standalone.conf.**

**02.** Por padrão. o tamanho de memória que o servidor consome vem ajustado em: **-Xmx4g**e **-Xms2g**, porém, é possível alterar esses valores:

bashstandalone.conf

**03.** O Fluig suporta **até 16 GB de memória**, sendo essa, uma limitação do JBoss. Caso o seu servidor de aplicação tenha mais de 16 GB de memória, recomendamos o uso de um **cluster** para distribuir os recursos. Saiba mais em

**04.** Não é preciso alterar a quantidade inicial (mínima) de memória alocada **(-Xms2g)**, pois a plataforma alocará memória de acordo com a necessidade. Saiba mais em .

## standalone.conf.bat (Windows)

---

**01.** O standalone.conf.bat pode ser consultado em: **<diretório de instalação do Fluig>\appserver\bin\standalone.conf.bat.**

**02.** Por padrão. o tamanho de memória que o servidor consome vem ajustado em: **-Xmx4g**e **-Xms2g**, porém, é possível alterar esses valores:

bashstandalone.conf.bat

**03.** O Fluig suporta **até 16 GB de memória**, sendo essa, uma limitação do JBoss. Caso o seu servidor de aplicação tenha mais de 16 GB de memória, recomendamos o uso de um **cluster** para distribuir os recursos. Saiba mais em

**04.** Não é preciso alterar a quantidade inicial (mínima) de memória alocada **(-Xms2g)**, pois a plataforma alocará memória de acordo com a necessidade. Saiba mais em .

# Outros interferentes no desempenho da plataforma

---

**01.** Execução de *backups* da aplicação e/ou banco de dados em horários de maior utilização da plataforma.

**02.** Personalizações onerosas no diretório: **<diretório de instalação do Fluig>\appserver\apps**.

**03.** Plataforma desatualizada.

**04.** Problemas na .

**05.** Problemas no *Proxy* reverso.

**06.** Excesso de consultas em *datasets*, pois podem gerar estresse desnecessário ao banco de dados.
