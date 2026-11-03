---
content_hash: f07d5cc27af93bb84a26373848a3c023b43a1418773b74de00d844d681d159e2
fetched_at: '2026-06-29T00:12:14.665211+00:00'
page_id: '969973276'
product: rm
source: tdn-rm
title: Migração dos tipos de dados TEXT,NTEXT e IMAGE nas colunas em SQL Server
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=969973276
version: 50
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Detalhamento da migração**
3. **Tela RM Atualizador**
4. **Regra de Tempo Limite para Migração**
5. **Listagem de tabelas migradas**
6. **Uso do modelo de recuperação Full**

## **01. VISÃO GERAL**

Este documento apresenta como será realizada a migração dos tipos de dados **text**, **ntext** e **image** nas colunas do banco de dados. Esses tipos foram marcados pela Microsoft como obsoletos e estão em processo de descontinuação, com remoção prevista em versões futuras do SQL Server. Para apoiar esse processo, a Microsoft já disponibiliza diretrizes oficiais que recomendam a substituição por tipos mais modernos e compatíveis, como **varchar(max)**, **nvarchar(max)** e **varbinary(max)**, assegurando melhor desempenho, suporte contínuo e maior compatibilidade futura.

Mais informações técnicas a respeito destes tipos de dados descontinuados no site do fabricante:  <https://learn.microsoft.com/pt-br/sql/t-sql/data-types/ntext-text-and-image-transact-sql?view=sql-server-ver16>

Com o objetivo de apoiar o processo de atualização do cliente, nossa ferramenta apresentará uma etapa dedicada à migração automática de **todas as colunas de negócio existentes no banco de dados da linha RM** que ainda utilizam os datatypes legados.  
Essa etapa foi planejada para reduzir riscos e acelerar a adequação da estrutura, alinhando-se às melhores práticas já recomendadas pela Microsoft.

## Benefícios da migração

* + **Compatibilidade futura**: uso de datatypes plenamente suportados nas versões mais recentes do SQL Server.
  + **Melhoria de performance**: consultas e operações passam a ter ganhos de desempenho em cenários de leitura e escrita.
  + **Facilidade de manutenção**: uso de tipos modernos simplifica scripts, integrações e ajustes futuros.
  + **Confiabilidade**: elimina riscos relacionados ao uso de tipos obsoletos, que podem deixar de ser suportados em releases futuras.

## **02. DETALHAMENTO DA MIGRAÇÃO**

A migração será realizada por meio de um item disponível na última etapa do processo de execução do RM Atualizador, conforme ilustrado abaixo:

Tabela com log detalhado

Durante a atualização, será gerado um log em uma tabela interna do sistema (**GUPGLOGMIGRACAODATATYPESIMAGETEXT**), registrando o processo de conversão dos tipos de dados e, em caso de falhas, detalhando o respectivo motivo.

### 02.1. Migração datatypes (tratamento locks) - Com uso de triggers

Durante a migração será criada uma trigger na base de dados para impedir alterações concorrentes na coluna em migração, a tabela ficará bloqueada durante este processo de migração. A trigger é criada de forma temporária e removida ao final do processo de migração do dados.

Toda esta operação de criação e remoção da trigger também pode ser visualizada na tabela de log (GUPGLOGMIGRACAODATATYPESIMAGETEXT) de migração dos dados

Caso ocorra falhas durante a atualização de um base de dados, como por exemplo queda de comunicação com o Host do RM, a base poderá conter objetos que são utilizados durante a migração de datatypes. Não se preocupe quanto aos objetos existentes, nas próximas execuções o processo irá ajustar a estrutura da tabela de maneira resiliente sem gerar efeitos colaterais no uso do sistema.

Os objetos usados na migração são:

* + Trigger **MigraDatatypes\_Bloquear**
  + Coluna temporária: **NOVOTYPEPARAMIGRACAOIMAGETEXT**
  + Indice de contador linhas: **IDX\_CONTADORLINHAS**
  + Coluna Contador Linhas: **CONTADORLINHAS**

## **03. TELA RM ATUALIZADOR**

No RM Atualizador haverá uma etapa dedicada a apresentar ao usuário as tabelas envolvidas na migração, organizadas conforme o tamanho em disco.

O objetivo é incentivar a análise da possibilidade de reduzir o conteúdo dessas tabelas antes de submetê-las à migração, o que pode, consequentemente, diminuir o tempo necessário para a atualização da base de dados.

*Para mais orientações sobre como reduzir o conteúdo da tabela, consulte o quadro de dicas no Tópico 5 deste documento.*

Em seguida, é apresentada a lista de versões, juntamente com o item responsável pela migração, conforme ilustrado:

No momento da Migração dos Tipos de dados  SQL Server, o sistema apresenta qual tabela está em processo de migração:

## **04.** **REGRA DE TEMPO LIMITE PARA MIGRAÇÃO**

### Visão Geral

Durante o processo de **migração de datatypes** do sistema o tempo limite de processamento varia de acordo com o **tipo de entrega** (*Release* ou *Patch*).  
O sistema possui valores mínimos padronizados de acordo com cada tipo de instalação, veja o exemplo abaixo:

* + Tempo mínimo para **release** de 60 minutos
  + Tempo mínimo para **patch** de 15 minutos
* Após a execução dos scripts, será iniciada a migração dos tipos. O tempo definido acima se aplica exclusivamente a essa etapa e será somado ao tempo habitual de conversão da sua base de dados.

### Regras de Configuração

* Sem Limite de tempo - O processo irá executar a migração de todas as colunas das tabelas até sua totalidade.
* Limitar o tempo de execução em N minutos - A migração ocorrerá dentro do tempo estipulado. Caso o limite seja atingido, a conversão da coluna atual será interrompida com segurança e o motivo registrado no log, deixando a tabela pronta para reiniciar a migração na próxima oportunidade.

Uso do Parametro pela API

Para alterar o tempo limite padrão (em minutos) durante a conversão da base via API (`ExecuteUpgrade`), utilize o parâmetro **tempoLimiteRelease= N**, substituindo o '**N**' por um número inteiro.

## **05. LISTAGEM DAS TABELAS MIGRADAS**

Para visualizar as tabelas migradas por versão clique nos links abaixo:

* [Versão 12.1.2606](https://tdn.totvs.com/x/-yTuPQ)

### Ordem de Migração dos dados

A migração das colunas será feita de forma diferente para release e patch, sempre respeitando o tempo definido pelo usuário conforme descrito acima.

* + **Release:** a migração das colunas começa pelas maiores tabelas e segue até as menores.
  + **Patch:** a migração das colunas começa pelas menores tabelas e segue até as maiores.

Redução de dados nas tabelas

Para potencializar os benefícios, reforçamos a importância de **reduzir o conteúdo das principais tabelas mais volumosas** antes da execução do processo de migração.  
Ao diminuir a quantidade de dados armazenados, o tempo necessário para converter os datatypes pode ser significativamente reduzido, resultando também em menor tempo destinado à atualização da base de dados como um todo.

 Foi criado um requisito que identifica bases contendo tabelas com grandes volumes de dados, as quais podem ocasionar demora na migração dos tipos de dados em suas colunas. Caso o RM.Atualizador sinalize este requisito, significa que uma ou mais tabelas do seu banco de dados podem gerar lentidão durante a etapa de atualização. Abaixo disponibilizamos um modelo de consulta SQL para auxiliá-lo na identificação das tabelas que necessitam ser saneadas:

sqlDJangoConsulta tabelas tamanhostruetrue

Nossa ferramenta já disponibiliza documentações de apoio para auxiliar na redução do conteúdo das tabelas e otimizar o processo. Recomendamos que o cliente utilize essas orientações previamente, de forma a garantir que a migração seja mais ágil, segura e com menor impacto para os usuários:

**Segue o link com documentação para auxiliar na redução de dados nas principais tabelas do produto:** <https://tdn.totvs.com/x/KmTeO>

## **06. USO DO MODELO DE RECUPERAÇÃO FULL**

Este processo utiliza transações atômicas para transferir os valores entre as colunas, garantindo o menor risco possível aos dados. No entanto, bancos de dados com o modelo de recuperação *Full* terão um alto consumo do log de transações. Para assegurar a conclusão do RM Atualizador e a operação normal do produto, alinhe com o seu DBA as seguintes medidas preventivas: garantir espaço em disco suficiente e aumentar a frequência dos backups de log.

**Observação**: Durante a migração, o RM.Atualizador avalia o espaço disponível no log de transação. Se não houver capacidade suficiente, a conversão da coluna é interrompida por segurança, evitando que a base de dados fique inacessível.
