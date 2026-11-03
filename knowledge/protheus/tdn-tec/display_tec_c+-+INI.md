---
content_hash: 57695171bd565f52cab178a653e95481567527cd4a6610669ac11cbe67418497
fetched_at: '2026-07-02T19:24:27.636917+00:00'
page_id: '658744528'
product: protheus
source: tdn-tec
title: c - INI
type: documentation
url: https://tdn.totvs.com/display/tec/c+-+INI
version: 9
---

## Exemplo: appserver.ini

```
[PROBAT]
DEVTLPP=0  
LOG_VERBOSE=0  
LOG_INFO=1  
LOG_WARN=0  
LOG_DEBUG=0  
LOG_ERROR=0  
THREADS_MEMORY=1
SOURCE_DISCOVERY_MODE=0
SOURCE_PATH=C:/my_project/src/
SOURCE_SKIPPED_PATH=subfolder_1,subfolder_3
TESTS_DISCOVERY_MODE=0
TESTS_DISCOVERY_TIME_INTERVAL=3600
CROSS_VALIDATION=u_minha_funcao_cross
CODECOVERAGE=1
CODECOVERAGE_EXPORT_JSON=1
CODECOVERAGE_PERCENT=80
CODECOVERAGE_EXPORT_TFS=1
CODECOVERAGE_FILTER_SRC=subfolder_2,subfolder_4
EXPORT_FILE_NAME=test_results
EXPORT_AFTER_RUN=1
EXPORT_FORMAT=JUnit
BLOCKED_WORDS=palavra_bloqueada_1,palavra_bloqueada_2
ShutDown=0
```

## Descrição das chaves

Para descrever as chaves, iremos juntar em grupos conforme suas finalidades, conforme abaixo:

#### GENERAL

Configurações genéricas.

---

```
DEVTLPP=0
```

**ATENÇÃO**  
Essa chave deve sempre estar com o valor 0 (zero), pois 1 (um) é de uso exclusivo da equipe de desenvolvimento do tlppCore e ativar essas particularidades pode causar comportamentos inesperados em seu projeto.

---

```
ShutDown=0
```

Determina se ao final da execução dos testes o appserver será finalizado automaticamente ou permanece no ar.

0 = Mantém no ar o appserver.  
1 = Finaliza appserver

​

```
THREADS_MEMORY=1
```

Ao ligar essa chave indicamos ao mecanismo de coleta de memória de início e fim das execuções para coletar a memória de cada Thread separadamente. A única exceção é para a Thread principal que sempre irá coletar a memória do appserver.

0 = Coleta informações de memória sempre do appserver, inclusive para as Threads. 1 = Coleta informações de memória de cada Thread separadamente.

#### LOGS

Configurações para níveis diferentes de logs do PROBAT.

​​

```
LOG_VERBOSE=0
```

Torna os logs impressos pelo PROBAT em modo "verboso", ou seja, são adicionados informações além da mensagem original.

* 0 = Desligado.
* 1 = Ligado.

​​

```
LOG_INFO=0
```

Imprime os logs de Informações básicas do PROBAT.

* 0 = Desligado.
* 1 = Ligado.

​​

```
LOG_WARN=0
```

Imprime os logs de Avisos do PROBAT.

* 0 = Desligado.
* 1 = Ligado.

​​

```
LOG_DEBUG=0
```

Imprime os logs de Debug do PROBAT, com detalhes das execuções.

* 0 = Desligado.
* 1 = Ligado.

​​

```
LOG_ERROR=0
```

Imprime os logs de Erro do PROBAT.

* 0 = Desligado.
* 1 = Ligado.

#### SOURCE

Configurações referentes aos arquivos fontes oficiais do projeto.

---

```
SOURCE_DISCOVERY_MODE=0
```

Informa o modo de encontrar os arquivos fontes oficiais de seu projeto.

* 0 = Hierarquia de diretórios
* 1 = Annotation.

Veja a documentação completa sobre esse recurso em:  
[Encontrando fontes oficiais](https://tdn.totvs.com/display/tec/b+-+Encontrando+fontes+oficiais)

---

```
SOURCE_PATH=d:\tlppCore\src
```

Indica qual o diretório onde se encontram os arquivos fontes oficiais quando informado 0 (zero) em [SOURCE\_DISCOVERY\_MODE].

Veja a documentação completa sobre esse recurso em:  
[Encontrando fontes oficiais](https://tdn.totvs.com/display/tec/b+-+Encontrando+fontes+oficiais)

---

```
SOURCE_SKIPPED_PATH=subfolder_1,subfolder_3
```

Indica qual subdiretórios serão ignorados na busca pelos fontes oficiais para registrar no SQLite quando informado 0 (zero) em [SOURCE\_DISCOVERY\_MODE].

Caso nada seja informado, nenhum subdiretório seja ignorado, e caso precise de mais de um subdiretório separe por vírgula ",".

#### TESTS

Configurações referentes aos fontes de Testes do projeto.

---

```
TESTS_DISCOVERY_MODE=0
```

Informa o modo de descoberta dos fontes de testes, sendo:

* 0 - Por Solicitação
* 1 - Na Execução

Para saber mais sobre esse recurso, visite:  
[Discovery - Encontrando os Testes no RPO](https://tdn.totvs.com/display/tec/a+-+Discovery+-+Encontrando+os+Testes+no+RPO)

---

```
TESTS_DISCOVERY_TIME_INTERVAL=3600
```

Indica o intervalo em segundos que o **PROBAT** faz buscas novamente dos fontes de testes compilados no RPO.

Para saber mais sobre esse recurso, visite:  
[Discovery - Encontrando os Testes no RPO](https://tdn.totvs.com/display/tec/a+-+Discovery+-+Encontrando+os+Testes+no+RPO)

#### CODE COVERAGE

Configurações referentes à Cobertura de Código.

---

```
CODECOVERAGE=1
```

Indica que deseja ligar/desligar a cobertura de código na execução dos testes.

* 0 = Desligado
* 1 = Ligado

Saiba mais em:  
[Cobertura de Código](https://tdn.totvs.com/pages/viewpage.action?pageId=655633518)

---

```
CODECOVERAGE_PERCENT=80
```

Indica o percentual mínimo de cobertura aceito sobre os fontes oficiais.

Saiba mais em:  
[Cobertura de Código](https://tdn.totvs.com/pages/viewpage.action?pageId=655633518)

---

```
CODECOVERAGE_EXPORT_JSON=1
```

Indica que deseja exportar em formato JSON os resultados de cobertura de código.

Saiba mais em:  
[Cobertura de Código](https://tdn.totvs.com/pages/viewpage.action?pageId=655633518)

---

```
CODECOVERAGE_EXPORT_TFS=1
```

Indica que deseja exportar em formato COBERTURA (XML) os resultados de cobertura de código.

Saiba mais em:  
[Cobertura de Código](https://tdn.totvs.com/pages/viewpage.action?pageId=655633518)

---

```
CODECOVERAGE_FILTER_SRC=subfolder_2,subfolder_4
```

Indica quais subdiretórios do seu projeto serão considerados na validação no processo de cobertura de código.

Saiba mais em:  
[Cobertura de Código](https://tdn.totvs.com/pages/viewpage.action?pageId=655633518)

#### EXPORT

Configurações referentes à exportação dos resultados dos testes.

---

```
EXPORT_FILE_NAME=test_results
```

Informa o nome do arquivo de exportação dos resultados.

Saiba mais em:  
[Exportando Resultados](https://tdn.totvs.com/display/tec/a+-+Exportando+Resultados)

---

```
EXPORT_AFTER_RUN=1
```

Indica se deseja que gere os resultados logo após a execução dos testes.

0 = Não gera arquivo.  
1 = Gera arquivo com resultado, baseado em EXPORT\_FILE\_NAME e EXPORT\_FORMAT.

Saiba mais em:  
[Exportando Resultados](https://tdn.totvs.com/display/tec/a+-+Exportando+Resultados)

---

```
EXPORT_FORMAT=JUnit
```

Formato do arquivo com resultado dos testes.

Saiba mais em:  
[Exportando Resultados](https://tdn.totvs.com/display/tec/a+-+Exportando+Resultados)

#### VALIDATION

Configurações referentes à validações adicionais.

---

```
CROSS_VALIDATION=u_minha_funcao_cross
```

Ativa o Cross Validation informando a função de usuário que retornará a lista de "alvos".

Veja mais detalhes sobre esse recurso em: [e-8 - Cross Validation](https://tdn.totvs.com/display/tec/e-8+-+Cross+Validation)

Ao não informar nenhuma função para essa chave, essa validação é desativada.

---

```
BLOCKED_WORDS=palavra_bloqueada_1,palavra_bloqueada_2
```

Determina uma lista de palavras que serão bloqueadas no uso das descrições dos testes, assim poder-se-á impedir o uso de palavras que sejam consideradas inadequadas.

As palavras devem ser separada por vírgula "," quando houver mais de 1 (uma) palavra.

Ao não informar nenhuma palavra para essa chave, essa validação é desativada.
