---
content_hash: cc93799f079dbd1ca73f0b553d05cbcf461103ac2f016a61366727d371f3e9d2
fetched_at: '2026-07-02T19:24:25.871156+00:00'
page_id: '513432110'
product: protheus
source: tdn-tec
title: Migrador de Ambiente
type: documentation
url: https://tdn.totvs.com/display/tec/Migrador+de+Ambiente
version: 17
---

DBTools - Migrador de Ambientes

## Introdução

A funcionalidade Migrador de Ambiente do DBTools oferece uma forma eficiente e segura de copiar uma base de dados do **ERP TOTVS - Linha Protheus** entre dois bancos de dados quaisquer (consulte as versões  para o true).

Esta ferramenta permite o uso de modo interativo, onde você parametriza as conexões de origem e destino, além dos parâmetros de cópia pela interface. Há também o modo "batch", onde a ferramenta usa um arquivo de configuração que pode ser fornecido como parâmetro para obter os detalhes da operação de cópia a ser realizada, sem paradas ou iterações com o usuário, apenas mostrando as etapas de execução na tela em modo "corrido", gravando um log com mais detalhes das operações realizadas.

A ferramenta de migração não acessa diretamente os bancos de dados, mas usa o true para acessar os databases de origem e destino.

Logo, a topologia mínima necessária para uso do migrador é :

* Uma instância atualizada do true configurada para acessar os dois bancos de dados, origem e destino
* Executar o DBTools para fazer a migração na mesma máquina onde está o true

Outra topologia sugerida é configurar duas instâncias do true, preferencialmente um em cada servidor de cada banco de dados, e executar o DBTools para a migração em uma delas.  
*\* A execução pode ser no servidor de origem ou no servidor de destino, não há diferença de resultado.*

---

## Passo a Passo para utilização

A utilização da ferramenta de migração normalmente envolve as seguintes etapas:

* Instalar um true atualizado para a leitura dos dados do SGBD de origem
* Configurar a ODBC/OCI para conexão com o SGBD de origem
* Testar a conexão com o SGBD de origem
* Criação do SGBD de destino
* Instalar um true atualizado para a gravação dos dados do SGBD de destino (se  for o caso)
* Configurar a ODBC/OCI para conexão com o SGBD
* Testar a conexão com o SGBD de destino

**Requisitos:**

* O SGBD de destino deve ter tamanho pré-alocado ou *autogrowth* habilitado para suportar o volume de dados a ser inserido
* O SGBD de destino deve ter uma área de LOG configurada adequada aos tamanhos das tabelas, para comportar a criação dos índices
* O SGBD de origem não deve ser acessado ou atualizado enquanto os dados estiverem sendo lidos para a cópia
* Determinar a máscara de tabelas a serem ignoradas para cópia no SGBD de origem – Por default a aplicação ignora tabelas que terminem com "BKP" e "LOG", mas isto pode ser alterado para contemplar mais definições

  
Observação

Serão migradas apenas as tabelas que contenham os campos de controle do true.

---

## Primeira execução

A primeira execução do programa criará os arquivos:

| Arquivo | Descrição |
| --- | --- |
| **dbtools.ini** | Neste arquivo, serão inseridas todas as configurações possíveis de serem realizadas para o aplicativo com seus valores default |
| **dbools.log** | Neste arquivo serão armazenados os registros das operações realizadas |

Ambos os arquivos podem podem ser editados e visualizados através de um editor de textos simples (notepad, notepad++, vi, etc).

A seguir, com o intuito de trazer clareza aos procedimentos, veremos o exemplo do passo a passo de uma cópia de tabelas entre um MS-SQL Server e um PostgreSQL.

Neste exemplo, usaremos apenas uma instância do true para fazer a cópia dos dados, configurando as ODBCs desta mesma máquina para acessar ambos os bancos de dados.

Concluídas as configurações de acesso de ambos os bancos de dados no truee os respectivos testes de conexão, executaremos o migrador em modo interativo (execução direta do aplicativo **dbtools.exe**).

Vale ressaltar que para o teste, criamos um atalho do executável e determinamos que sua resolução de tela será de 80x25 (resolução mínima e necessária para a ferramenta).

Observações

A navegação entre as opções não é feita por mouse ou setas de direção, a opção desejada deve ser informada digitando o número correspondente e pressiondo ENTER para confirmar e continuar.

Para acessar o migrador, digitamos "1" e pressionamos ENTER.

---

## Menu de operações

Atualmente existem quatro operações disponíveis, normalmente executadas em sequência, para realizarmos a cópia das tabelas entre os bancos de dados.

1. Source Data Connection
2. Target Data Connection
3. Set migration parameters
4. Run data migration

Na parte superior da tela, é informado que ainda não conectamos com o true para a origem de dados, nem para o destino.

Vamos começar informando a origem dos dados e estabelecendo a conexão, executando a operação "1".

---

## Passo 01: Conexão de Origem dos dados

Ao acessarmos a definição da origem dos dados, devemos informar o servidor e a porta onde está o true que será usado para ler os dados do banco de origem, o tipo do banco, o nome do ALIAS / DSN do banco de dados e, caso este true possua um usuário de monitoramento para administração via true, devemos informar o usuário e a senha utilizadas.

Cada uma destas definições pode ser alterada ou configurada executando a opção de número correspondente, informando o valor da configuração e pressionando ENTER.

A tela de definição da conexão de destino é exatamente igual a exibida no print abaixo (pode haver variação no título da janela):

ATENÇÃO

O usuário e a senha solicitados nas configurações de conexão do DBTools **somente devem ser informados se** o true indicado para a conexão possuir um controle de acesso administrativo de monitoramento (o mesmo utilizado para acesso via true).

Se o true alvo desta conexão não exige ou não tem configuração de login para conexão administrativa de monitoramento, estas informações devem ser deixadas EM BRANCO.

Caso os dados de acesso informados estejam incorretos, ou sejam informados para um true que não tem controle de acesso de monitoramento, será retornado o erro de conexão **\*\*\* DBAccess SetAuthentication ERROR -33 \*\*\***

Após preencher os dados, estabelecemos a conexão de origem executando a opção **7 - Connect with DBMS**.

Veja abaixo o exemplo de uma conexão com o banco MS-SQL Server configurado:

---

## Passo 02: Conexão de Destino dos dados

Ao retornar para a tela anterior, usando a opção "0", acessamos a operação de **Target Data Connection** e informamos o nosso banco de dados de destino.

Para o nosso exemplo, as configurações ficaram assim:

Uma vez que as conexões estejam estabelecidas, elas são visíveis no true, veja o exemplo abaixo:

---

## Passo 03: Parâmetros de Cópia

Ao acessarmos a operação 3, são trazidos os parâmetros default para a cópia de dados. Você pode alterar estes parâmetros no momento da execução via interface, mas eles não serão salvos no arquivo de configuração "dbtools.ini".

Por outro lado, ao alterar os parâmetros deste arquivo usando um editor de texto, ao executar o programa DBTools, os valores especificados serão lidos e utilizados pela aplicação.

Veja abaixo os valores default da aplicação:

| Parâmetros | Default | Descrição |
| --- | --- | --- |
| **Number of threads** | 0 (zero) | Indica que o programa deve escalar os processos automaticamente. Qualquer numero maior que zero indica uma quantidade fixa de processos para cópia simultânea de tabelas – cada processo copia uma tabela. |
| **Overwrite tables** | Não | Permite especificar se o processo deve apagar e copiar por cima os dados de uma tabela do banco de dados de origem que já exista no banco de dados de destino. |
| **Copy deleted records** | Não | Permite especificar se o processo deve copiar do banco de dados de origem todos os registros das tabelas, mesmo que estejam marcados para serem deletados  – campo D\_E\_L\_E\_T\_ = ' \*' |
| **Copy empty tables** | Sim | Permite especificar se o processo criará (ou não) as tabelas vazias do banco de dados de origem no banco de dados de destino. |
| **Create indexes in target** | Sim | Permite especificar se o processo deve identificar os índices de dados e chave única existentes no banco de dados de origem para a tabela a ser copiada, e cria os índices imediatamente após o término da cópia dos dados de cada tabela |
| **Stop on error** | Sim | Permite especificar se toda a execução caso deve ser abortada caso um dos processos de cópia apresente um erro qualquer (leitura ou gravação de dados)  Caso mantenha o valor default, o processo de cópia desta tabela é finalizado com a ocorrência de erro e o aplicativo não copia mais nenhuma tabela da lista, mas aguarda os outros processos de cópia serem terminados.  Quando especificado o valor "NÃO", os processos continuam copiando as demais tabelas até que a lista esteja completa. Neste caso, o registro de log da ferramenta deve ser consultado para verificar se houve ocorrência de erro, quantas tabelas apresentaram erro e não foram copiadas, ou quantas tabelas foram copiadas parcialmente. |
| **Keep source RECNO** | Não | Por padrão este recurso está desligado e não é necessário. Contudo, caso ativado, mantém a mesma numeração de registros das tabelas de origem para todas as tabelas que não possuam controle de numeração automáticas pelo banco de dados.  Os registros das tabelas são lidos e inseridos por ordem crescente de RECNO, representando a ordem física de inserção.    Tabelas que possuem o recurso de RECNO Incremental **não** **mantém** a mesma numeração de registros das tabelas de origem. |
| **Tables to copy** | % | Este parâmetro respeita a sintaxe LIKE (SQL ANSI) para informar uma ou mais máscaras separadas por vírgula para limitar ou especificar as tabelas que devem ser copiadas.  Por default todas são (%).   DBAccess 22.1.1.2 A partir desta versão o DBTools conta com um novo recurso, a utilização de um arquivo contendo a lista de tabelas que devem ser migradas.  Quanto ao novo recurso:   * Suporta a leitura de um arquivo * Pode-se informar apenas o nome do arquivo (file.txt) desde que ele esteja no mesmo *path* do executável do DBTools * Pode-se utilizar *path* absoluto, desde que na mesma máquina, tanto para a versão Windows quanto para Linux Exemplo:    ```   windows - c:\tmp\tables.txt   linux - /tmp/tables.txt   ```   Quanto ao arquivo:   * Ele deve, obrigatoriamente, ter a extensão **.txt** * Não recomendamos que ele seja formatado com quebras de linhas (sejam CRLF ou LF), embora haja um tratamento básico para retirá-los * Caso haja quebra de linha, todo o conteúdo posterior a quebra será desconsiderado * Para distinguir as diferentes tabelas a serem migradas, deve-se utilizar a virgula (,) como separador * Foi mantido o suporte a sintaxe LIKE (SQL ANSI) |
| **Tables ignored** | %BKP,%LOG | Este parâmetro respeita a sintaxe LIKE (SQL ANSI) para informar quais arquivos não devem ser considerados para o processo de cópia, separados por vírgula.  Por default arquivos com o sufixo BKP e LOG são ignorados. |
| **Resume previous copy** | Não | Habilitar esta opção faz com que a ferramenta compare a quantidade de registros de tabelas já existentes no destino com a base de origem e caso a quantidade seja inferior, representando uma cópia parcial, a ferramenta inicia a copia dos demais registros que faltam.  Obs.: Este parâmetro atende à casos em que o processo de cópia estava em execução, mas foi interrompido antes de seu término. |
| **Use better estimative** | Não | Este parâmetro permite uma melhor estimativa de tamanho dos dados que serão migrados.  Obs.: O parâmetro está disponível a partir da versão **22.1.1.2** do true e tem efeito apenas para o SGBD **SQL Server** como SGBD de **origem**. |
| **Adjust (round) numbers** | Não | Ao habilitar esta opção, caso existam números com a parte decimal maior que a suportada e definida para o campo eles serão automaticamente arredondados.  Obs.: Este parâmetro está disponível a partir da versão **24.1.0.1** do true. |

---

## Passo 04: Executar a cópia

Confirmados os parâmetros, voltamos ao menu anterior e executamos a operação 4 – **Run data migration**.

Ao ser acionada, é exibido na tela um resumo dos parâmetros de cópia, a quantidade de tabelas que satisfazem os critérios de busca e exclusão de cópia, seguido do tamanho estimado dos dados de todas as tabelas a serem avaliadas.

Vejamos o print abaixo, que atende ao nosso exemplo:

 

Confirmados em tela os parâmetros e a quantidade estimada de tabelas e dados, podemos iniciar a operação, pressionando "Y" seguido de "ENTER".

Informações adicionais

* O tamanho estimado dos dados está sujeito a variações e pode ser maior que o reportado, pois o tamanho é obtido através de diferentes catálogos para cada banco de dados.
* As tabelas no banco de origem são ordenadas por tamanho e em ordem decrescente, para avaliar as tabelas maiores antes das menores.
* A leitura dos registros é feira pela ordem de inserção física do banco de dados de origem (com base no campo R\_E\_C\_N\_O\_ ).
* Os índices somente são criados no banco de destino após a cópia de cada tabela.
* Se a tabela já existir no SGBD de **destino** e a opção de **Sobrescrever tabelas** estiver **ligada**, será exibida uma mensagem de **warning** informando que a tabela já existe no destino e a tabela será apagada. Caso dê erro na remoção da tabela, será exibida uma mensagem de **erro**.
* Se a opção de **Continuar cópia anterior** estiver **ligada**, a tabela já existir no SGBD de **destino** e a **quantidade de registros** na **origem** e no **destino** são **iguais**, será exibida uma mensagem de **warning** informando que a tabela será ignorada, e **continuará** a migração.
* Se a opção de **Continuar cópia anterior** estiver **ligada**, a tabela já existir no SGBD de **destino** e a **quantidade de registros** na **origem** for **maior** que no **destino**, será exibida uma mensagem de **erro** informando que a tabela de origem não pode ser maior que a destino, e a migração será **encerrada**.
* Se a opção de **Continuar cópia anterior** estiver **desligada** e a tabela já existir no SGBD de **destino**, será exibida uma mensagem de **warning** informando que a tabela será ignorada, e **continuará** a migração.
* Se não for possível abrir uma tabela no SGBD de **origem**, a tabela será ignorada e **continuará** a migração.
* Se a tabela não tiver registros e a opção de **Copiar Tabelas Vazias** estiver **desligada**, será exibida uma mensagem de **warning** informando que a tabela será ignorada, e **continuará** a migração.

---

## Tamanho estimado dos Dados

O tamanho estimado dos dados está sujeito a variações e pode ser maior que o reportado, pois o tamanho é obtido através de diferentes catálogos para cada banco de dados. Contudo, esta variação afeta apenas o cálculo do tempo estimado de cópia.

Os números informados de volume e registros copiados são reais e incrementados ao longo da execução do processo.

Cada banco de dados definido como origem possui uma abordagem específica para obter estas informações dos catálogos do banco de forma rápida, sendo que o usuário usado na conexão do SGBD de origem precisa ter os privilégios de SELECT / QUERY nas seguintes views:

| SGBD | Views |
| --- | --- |
| MS-SQL Server | sys.tables, sys.index, sys.partitions |
| Oracle | dba\_segments |
| PostgreSQL | information\_schema.tables, pg\_relation\_size() |
| MySQL | information\_schema.tables |
| DB2 | syscat.tables |
| Informix | systables, sysmaster:sysptnhdr |

---

## Acompanhamento do processo de cópia

Durante o processo de cópia, uma interface de status mostra suas etapas sendo concluídas durante sua execução. Vejamos o exemplo abaixo: 

Informações adicionais

* O percentual de cópia concluído é baseado no tamanho dos dados já copiados por todos os processos até o momento atual e está diretamente relacionado a estimativa do tamanho total dos dados.
* O tempo estimado para término é atualizado durante a execução e é calculado levando em conta a média de bytes copiados por segundo nos últimos 20 segundos da operação de cópia.

---

## Informações adicionais da execução do processo

Na parte inferior da tela, as informações mostradas são:

| info | Descrição |
| --- | --- |
| Time (hh:mm:ss) | Tempo decorrido em horas, minutos e segundos desde o início do processo de cópia |
| Speed ( V1 / V2 / V3 ) | Três indicadores de desempenho de cópia em KB ou MB por segundo, onde:   * V1: indica o tempo apurado entre cada atualização (2,5 segundos) * V2: indica a média de tempo das últimas 10 tomadas de tempo (últimos 25 segundos) * V3: indica a velocidade média apurada considerando todo o volume copiado desde o início do processo |
| Processing <X>/<Y> | * X: indica o número de tabelas já avaliadas pelos processos de cópia * Y: indica o número total de tabelas      * A cópia de uma tabela requer a validação dos parâmetros do programa, ter dados, existir ou não na base de destino, etc. * Estas validações são realizadas durante o processo, onde cada tabela da lista é avaliada na origem e no destino. |
| n Recs | transf / estimado | * n: indica a quantidade de registros total copiados entre a origem e o destino * transf:  indica o volume de registros copiados em KB, MB ou GB * estimado: indica o tamanho total de todas as tabelas levantados no início do processo |

---

## Consumo de recursos durante a cópia

Quando iniciamos com o número de processos "0" (zero), o migrador sobe o primeiro processo dedicado de cópia e 90 segundos depois guarda o desempenho médio de cópia. Em seguida, um novo processo para copiar tabelas simultaneamente é iniciado.  
A cada 90 segundos o migrador avalia o desempenho antes de subir o último processo, comparando com o desempenho atual. Caso haja aumento do desempenho, ele sobe mais um processo e guarda o desempenho atual para a próxima comparação.  
  
Dessa forma, ele somente vai parar de subir novos processos, quando for detectado que ao subir um novo processo não houve aumentou no desempenho total do processo em volume de cópia.  
  
Normalmente este patamar é atingido quando o limite de banda de rede, ou de *throughput*de leitura ou gravação foram atingidos. Assim, é esperado que o consumo de recursos durante a cópia seja a capacidade computacional total do ambiente envolvido.  
Caso seja especificado um valor fixo de processos, maior que zero, a ferramenta logo de início sobe os processos de cópia informados e somente finaliza estes processos quando não houverem mais tabelas na fila de cópia.  
  
Durante o processo de cópia, é possível visualizar e monitorar as conexões nos true envolvidos no processo usando o true.  
Vejamos o exemplo abaixo:

---

## Passo 05: Conclusão do processo

Concluída a cópia, uma tela final é exibida com algumas estatística. Vejamos o exemplo abaixo:

O registro de LOG da operação completa neste exemplo foi salvo no arquivo **dbtools.log** e contém muito mais detalhes das operações realizadas, como por exemplo:

* todas as configurações e informações dos bancos de dados de origem e destino
* a estrutura de cada tabela envolvida na cópia
* os índices identificados e criados no destino
* o tamanho de dados real de cada tabela determinados durante a cópia, entre outras informações

Para sair do programa após a cópia, basta retornar ao menu principal através da opção "0" (zero).

Como as conexões de origem e destino ainda estão estabelecidas, a aplicação apenas pede para você confirmar a saída. 

---

## Retomada de processo de cópia interrompido

Somente é possível continuar novamente uma cópia interrompida nos seguintes casos:

* Ninguém mexeu no banco de origem e no banco de destino após a cópia ter sido interrompida. A ferramenta de cópia não tem como verificar isso.
* A cópia estava sendo feita para um banco de dados vazio.
* Os parâmetros de cópia devem ser os mesmos da cópia original, não se pode mudar parâmetros como “Copiar registros deletados” e/ou “Manter RECNO de origem.

Ao reiniciar a cópia com a configuração de continuação / recuperação (resume), caso uma tabela já exista no ambiente de destino, a ferramenta fará uma contagem dos registros em ambos os bancos e copiará apenas os registros que faltam – a partir do último registro previamente copiado.

Não há comparação dos dados, apenas a contagem de linhas da tabela!

---

## Execução em modo BATCH

Partindo do arquivo de configuração default criado pela ferramenta (dbtools.ini), podemos alterá-lo com um editor de texto de arquivos ASCII e preencher as chaves com as informações de cópia.

Para executar o migrador utilizando este arquivo, via linha de comando utilizamos o parâmetro "/batch", onde o processo será executado automaticamente usando a interface apenas para mostrar o echo das etapas de execução do processo.

Neste exemplo, onde as configurações default foram mantidas e apenas informamos os bancos de dados de origem e destino, o arquivo **dbtools.ini** ficaria assim:

Exemplo de execução:

dbtools.exe /batch]]>

---

## Parâmetros de linha de comando

Existem outros parâmetros que permitem especificar o nome de um arquivo diferenciado de configuração, um arquivo diferenciado de log a ser gerado, entre outros.

Para a lista completa de parâmetros, execute **dbtools /help**:

 Log file (default=dbtools.log).
/config  Configuration file (default=dbtools.ini).
/batch Run in BATCH mode.
/quiet Turn off echo of the messages in BATCH mode.
 ]]>
