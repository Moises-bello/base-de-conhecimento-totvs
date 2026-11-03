---
content_hash: aec089dbb63bbdca27409559519319914de29bc57f3467697fddb6986dc01581
fetched_at: '2026-07-02T19:24:26.576192+00:00'
page_id: '520679004'
product: protheus
source: tdn-tec
title: SQLite - Corrompimento de arquivos
type: documentation
url: https://tdn.totvs.com/display/tec/SQLite+-+Corrompimento+de+arquivos
version: 3
---

Embora o SQLITE utilize um arquivo de log transacional interno ( WAL - Write Ahead Log ) e tenha as proteções pertinentes, existem eventos que podem causar corrompimento de partes dos dados (tabelas e índices) gravados em um Database SQLITE, em especial caso ocorram em um momento onde a aplicação está escrevendo/atualizando informações no Database, como por exemplo:

* Finalização forçada do serviço do TOTVS Application Server.
* CRASH / Access Violation / Segment Fault no Application Server.
* Queda de energia do equipamento.
* Queda / CRASH do sistema operacional

Quando uma parte dos dados do Database SQLITE apresentar inconsistência de registro, a instrução executada para recuperar ou manipular os dados retorna um erro de falha na imagem de disco, vide exemplo abaixo:

**SL1010: SQLite Error (11) database disk image is malformed on MSUNLOCK(APLIB060.PRW) 16/09/2019 15:15:55 line : 829**

## Utilitário de linha de comando SQLITE3.EXE

Existem algumas formas de recuperar os dados íntegros de um Database SQLITE. Ambas as formas descritas neste documento utilizam o utilitário de linha de comando oficial do SQLITE – chamado *sqlite3.exe* – que está disponível para download no site oficial do SQLITE ( <https://www.sqlite.org/download.html> ) , basta procurar o tópico **"Precompiled Binaries for Windows"**, e localizar o arquivo **"sqlite-tools-win%.zip"** – ele contém o utilitário de linha de comando interativo SQLITE3.EXE. Este utilitário também possui build  pré-compilada para Linux, também disponível para download nesta página. Você pode baixar o ZIP contendo as ferramentas e descompactar apenas o "sqlite3" na pasta onde está o Database SQLITE a ser manipulado.

### Verificação de integridade do Database

Abra um prompt de comando do Windows ( Iniciar + R → CMD ), entre no diretório / pasta onde está o arquivo a ser verificado e o utilitário sqlite3.exe, e use o seguinte comando:

```
echo PRAGMA integrity_check; | sqlite3 SYSTEM.db  
OK
```

Caso a verificação de integridade seja executada com sucesso, será mostrada uma mensagem "ok" na tela. Esta verificação tende a demorar proporcionalmente em razão do tamanho do arquivo.

Caso seja detectada alguma anormalidade / corrompimento, serão mostradas mensagens com detalhes técnicos dos erros encontrados, vide exemplo abaixo:

```
echo PRAGMA integrity_check; | sqlite3 SYSTEM_DAMAGED.db  
*** in database main ***  
On page 827 at right child: Bad ptr map entry key=77441 expected=(5,827) got=(5,68884)  
Page 77441: btreeInitPage() returns error code 11  
On page 1127 at right child: Bad ptr map entry key=77440 expected=(5,1127) got=(5,76446)  
Page 77440: btreeInitPage() returns error code 11  
Error: near line 1: database disk image is malformed
```

### Recuperação do Database - Exemplo na plataforma WINDOWS

* Baixe o serviço e/ou feche o TOTVS | Application Server que acessa este Database SQLITE.
* Siga as instruções de abertura de prompt de comando do tópico "Verificação de Integridade do Database"
* Renomeie o SYSTEM.db corrompido para, por exemplo, SYSTEM\_DAMAGED.db
* A partir deste ponto, existem duas formas de recuperação do SYSTEM.db

**Alternativa 1:**

Execute o comando abaixo do SQLITE. Ele vai criar um clone do Database, criando um novo SYSTEM.db, partindo dos dados que ele conseguir ler do arquivo corrompido SYSTEM\_DAMAGED.db:

```
echo .clone SYSTEM.DB | sqlite3 SYSTEM_DAMAGED.db
```

Será mostrado na tela o progresso e os objetos lidos e clonados no novo database. Ao final do processo, o novo arquivo SYSTEM.DB estará totalmente íntegro.

**Alternativa 2:**

Execute o comando abaixo, ele vai criar um script SQL ( para o SQLLITE ) contendo a criação e alimentação de todos os dados e objetos do banco corrpompido SYSTEM\_DAMAGED.db e criar o arquivo "SYSTEM\_RECOVER.sql"

```
echo .recover | sqlite3 SYSTEM_DAMAGED.db > SYSTEM_RECOVER.sql
```

Feito isso, agora executamos o comando abaixo, que vai criar um novo database SYSTEM.db, e alimentá-lo com os dados e objetos usando o script do arquivo SYSTEM\_RECOVER.sql

```
echo. | sqlite3 SYSTEM.db -init SYSTEM_RECOVER.sql
```
