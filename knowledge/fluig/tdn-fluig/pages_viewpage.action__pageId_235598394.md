---
content_hash: 3662e76eec39c4a3f170da257a1f7ac2d73fda8a705ab644d2d1ae1c23cc20c6
fetched_at: '2026-06-28T21:35:22.436077+00:00'
page_id: '235598394'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Datasets
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235598394
version: 83
---

.\*ndice

# Falando de *datasets*...

---

*Datasets* são componentes que permitem padronizar o acesso às informações provenientes de locais externos à plataforma, tais como aplicativos e banco de dados. Os *datasets* de alta performance possuem um cache de armazenamento de dados obtidos externamente, que tem como objetivo reduzir o número de acessos aos serviços de dados externos, ou seja, cria uma cópia da estrutura dos dados dentro da plataforma para consulta, aprimorando a performance dos *datasets* desenvolvidos sobre a plataforma. Desta forma, os dados são consultados na própria plataforma, evitando acessar os dados no sistema provedor externo a cada requisição.

Esse recurso permite criar *datasets* e definir quais serão *offline* em dispositivos móveis, quais devem ser sincronizados com o provedor externo de dados, a frequência de sincronização, inativar aqueles que não estiverem mais em uso, entre outras opções.

Os *datasets* ativos são apresentados com uma cor de fonte mais forte, para se destacarem em relação aos *datasets* que não estão mais sendo utilizados.

Dica!

Saiba mais sobre o desenvolvimento de datasets acessando a .

## Ver *datasets*

---

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Desenvolvimento**.

**03**. Clique em  ***Datasets***.

**04**. Veja os *datasets* existentes.

#f2f2f2#f2f2f2

É possível pesquisar um *dataset* específico por meio do campo **Buscar**, localizado no canto superior direito da janela, ou utilizar o botão **Filtrar**, para escolher os *datasets* que serão retornados.

## Filtrar *dataset*

---

**01**. Clique em **Filtrar**, localizado na parte superior direita da tela.

**02**. Selecione os *datasets* que deseja ver. É possível filtrar por situação (ativos, inativos e/ou em edição) e também por tipo (internos, simples e/ou avançados).

**03**. Os *datasets* dos tipos escolhidos serão listados.

novo

## Adicionar *dataset* simples

---

https://www.youtube.com/watch?v=GEpWD61D4wwtruevideo-filledAssista ao vídeo#0897E9INLINE

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Desenvolvimento**.

**03**. Clique em  ***Datasets***.

**04**. Clique em **Novo *dataset*** e selecione a opção **Simples**.

**05**. No campo **Código**, insira um código para o *dataset.*

**06**. No campo **Descrição**, insira uma descrição para o *dataset.*

#f2f2f2#f2f2f2

Para evitar inconsistências, o código e a descrição do *dataset* não devem conter caracteres especiais (com exceção de "\_" e "-").

**07**. No campo **Serviço**, selecione um serviço para o *dataset*.

#f2f2f2#f2f2f2

Caso não possua nenhum serviço cadastrado, inclua um serviço conforme as orientações contidas .

**08**. O serviço selecionado pode ser do tipo: **SOAP**, **REST** ou **JDBC.** As opções de preenchimento aparecerão de forma diferente de um para o outro. Preencha os campos de acordo com o serviço selecionado.

#f2f2f2#f2f2f2false1soapSOAP

Ao selecionar o tipo de serviço **SOAP**, preencha os seguintes campos:

**Operação**Ao selecionar o ícone de lupa, permitirá selecionar uma das operações disponíveis. As operações estarão listadas por Nome e *PortType* (ColleagueService).

**Configurar**  
Nas configurações da operação selecionada, podem ser configuradas as Propriedades, Chaves do *Dataset*, SOAP *Headers* e Tratamento retorno.

**Propriedades**

* + Autenticação Básica - selecionar se a autenticação for necessária, nesse caso será requisitado usuário e senha.
  + SSL - habilitar quando o serviço SOAP exigir utilização de SSL (camada extra de segurança).
  + Desabilitar *Chunking* - desabilitar o envio do envelope SOAP inteiro.
  + Listar mensagens SOAP - habilitar para mostrar as mensagens de envio e recebimento no log.
  + Tempo de resposta - habilitar para mostrar o tempo que a requisição aguarda pela resposta.

**Chaves do *Dataset***

Permite definir as chaves que serão utilizadas no momento da sincronização *offline*, para evitar duplicação de registros a cada sincronização.

**SOAP *Headers***Permite adicionar um *header* (cabeçalho).

**Tratamento Retorno**

* + Extrair resultado - permite selecionar esta opção para extrair um relatório em formato XML e incluir uma tag.

Acionar **Salvar** para concluir a configuração.

**Parâmetros**Preencha os parâmetros de acordo com o solicitado:

**Atribuição**-Nulo, Valor ou Variável (Ao selecionar Nulo, o campo Valor é automaticamente dispensado)

**Valor**-WKCompany ou WKUser (Será visualizado quando o campo de atribuição for selecionado como Variável).

restREST

Ao selecionar o tipo de serviço **REST**, preencha os seguintes campos:

**Operação**Ao selecionar o ícone de lupa, permitirá selecionar uma das operações disponíveis. As operações estarão listadas por Nome, Método(GET) e API.

**Configurar**Nas configurações da operação selecionada, podem ser configuradas as Propriedades, Chaves do *Dataset,* *Headers* e Tratamento retorno.

**Propriedades**

* + SSL - habilitar quando o serviço exigir utilização de SSL (camada extra de segurança).
  + Listar mensagens - habilitar para mostrar as mensagens de envio e recebimento no log.
  + Tempo de resposta - habilitar para mostrar o tempo que a requisição aguarda pela resposta.

**Chaves do *Dataset***

Permite definir as chaves que serão utilizadas no momento da sincronização *offline*, para evitar duplicação de registros a cada sincronização.

***Headers***

Permite adicionar um *header* (cabeçalho).

**Tratamento Retorno**

* + Extrair resultado: Permite selecionar esta opção para extrair um relatório em formato JSON e incluir um caminho.

Acionar **Salvar** para concluir a configuração.

**Parâmetros**Preencha os parâmetros de acordo com o solicitado:

**Atribuição**-Nulo, Valor ou Variável (Ao selecionar Nulo, o campo Valor é automaticamente dispensado)

**Valor**-WKCompany ou WKUser (Será visualizado quando o campo de atribuição for selecionado como Variável).

jdbcJDBC

Ao selecionar o tipo de serviço **JDBC**, preencha os seguintes campos:

**Tabela**Ao selecionar o ícone de lupa, permitirá selecionar uma das tabelas disponíveis. As operações estarão listadas por Nome e Tipo (*Table*, *View* ou *Synonym*).

**Configurar**Nas configurações da tabela selecionada, podem ser configuradas algumas propriedades como:

* Limitar Resultado - habilitar para limitar o número de registros retornados.
* Campo chave para a tabela - Permite selecionar um campo chave para a tabela, podendo ser: *limit* ou *offset*.

Acionar **Salvar** para concluir a criação.

**Campos**Preencha os campos de acordo com o solicitado:

* **Filtros** - Permite adicionar filtros para os campos.  

  Para criar filtros, é necessário configurar algumas informações. São elas:

  **Operação**Permite selecionar uma das operações disponíveis: AND, OR ou NOT.

  **Valor inicial**Definir um valor inicial. Ex: 1

  **Valor final**Definir um valor final. Ex: 3

  **Utilizar Like**Buscar pelo conteúdo, não exato, mas que contenha parte do valor informado. Basta selecionar Sim ou Não.

* **Retornar** - Se necessário, marcar Sim para retornar um valor.

* **Ordenar** - Permite ordenar os campos em ordem crescente ou decrescente.

**09**. Clique em **Salvar**.

avançado

## Adicionar *dataset* avançado

---

https://www.youtube.com/watch?v=GEpWD61D4wwtruevideo-filledAssista ao vídeo#0897E9INLINE

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Desenvolvimento**.

**03**. Clique em  ***Datasets***.

**04**. Clique em **Novo *dataset***e selecione a opção**Avançado**.

**05**. No campo **Código**, insira um código para o *dataset.*

**06**. No campo **Descrição**, insira uma descrição para o *dataset.*

#f2f2f2#f2f2f2

Para evitar inconsistências, o código e a descrição do *dataset* não devem conter caracteres especiais (com exceção de "\_" e "-").

**07.** Clique em **Próximo**.

#f2f2f2#f2f2f2

Com isso, será incluído um novo registro de *dataset* avançado, e será aberta a tela para edição do código-fonte do *dataset*. O código-fonte será mantido como rascunho enquanto o usuário autenticado acionar a opção **Salvar**. As alterações de código-fonte só serão aplicadas ao *dataset* no momento em que o usuário tiver concluído as alterações, acionando o botão **Publicar**.

Saiba mais sobre a construção de um *dataset* avançado acessando a nossa documentação técnica disponível .

## Habilitar *dataset offline* no *mobile*

---

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Desenvolvimento**.

**03**. Clique em  ***Datasets***.

**04.** Localize o *dataset* que será habilitado *offline* no *mobile*.

**05.** Abra a tela **Comportamento *mobile*** clicando no *link* da coluna ***Offline mobile***.

**06.** Na janela apresentada, defina as informações solicitadas.

#f2f2f2#f2f2f2

A configuração padrão é Não (Off).

As informações solicitadas são:

**Utilizar cache em dispositivos móveis?**Quando habilitado, determina que os dados do *dataset* serão armazenados no cache quando ele é utilizado em dispositivos móveis. Nesse caso, o botão é apresentado com o indicativo **ON** (sim), informando que o recurso está ativo. Quando acionado para desabilitar o recurso, o botão é apresentado com o indicativo **OFF** (não), informando que o recurso está desabilitado.

**Tempo de expiração do *cache mobile***Tempo no qual os dados armazenados são considerados válidos e permanecem no *cache* de dispositivos móveis antes de serem atualizados novamente.

**Não utilizar *cache* quando o dispositivo *mobile* estiver *online*?**Quando habilitado, determina que não serão consultados os dados em *cache* quando o dispositivo móvel estiver *online*, ou seja, serão requisitados do sistema externo.

**03.** Acionar **Salvar**.

#f2f2f2#f2f2f2Importante!

Novos dados criados em dispositivos móveis, quando utilizando o modo *offline*, só estarão disponíveis para consulta em outros formulários depois que o aplicativo móvel passar por um processo de sincronização com o servidor. Para entender mais sobre este processo, acesse a página de .

Para alguns *Datasets* do tipo **Interno** este recursonão é disponibilizado.

Acesse nossa documentação e confira como [carregar dados do dataset em modo offline.](https://tdn.totvs.com/pages/viewpage.action?pageId=146181573#1--1353119673)

## Importar *dataset*

---

**01.** Acionar o botão **Importar**.

**02.**Selecionar o servidor para o qual o *dataset* será importado.

#f2f2f2#f2f2f2

O servidor deve estar corretamente cadastrado, conforme as instruções do item . A importação só irá funcionar se, no servidor selecionado, a plataforma estiver em uma atualização 1.6.5 (Liquid) ou superior.

Caso já exista um *dataset* com o mesmo código do *dataset* importado de outro servidor, a plataforma irá emitir uma  e, caso o usuário confirme a ação, será criada uma nova versão com a implementação do *dataset* importado.

**03.** Acionar**Importar.**

## Exportar *dataset*

---

**01.** Selecionar na listagem o(s) *dataset(s)* que deve(m) ser exportado(s).

**02.** Acionar o botão **Exportar**.

**03.**Selecionar o servidor para o qual o *dataset* será exportado.

#f2f2f2#f2f2f2

O servidor deve estar corretamente cadastrado, conforme as instruções do item . A importação só irá funcionar se, no servidor selecionado, a plataforma estiver em uma atualização 1.6.5 (Liquid) ou superior.

**04.** Acionar**Exportar.**

## Configurar permissão de acesso no *dataset*

---

Por meio do recurso de  do Painel de controle, é possível definir os usuários, papéis ou grupos que terão acesso ao datasets do tipo Interno. Confira mais detalhes em .

## Sincronizar *datasets*

---

Os recursos de sincronização se encontram em uma tela específica, que pode ser acessada acionando o link da coluna **Sincronização**. Para saber mais sobre esse recurso, acesse a página de .

## Mais ações do *dataset*

---

Os *datasets* apresentam diversas ações específicas, que podem ser conferidas acionando o ícone , localizado na coluna **Mais ações**. Para saber mais sobre esses recursos, acesse a página .

Fique atento!

Esta documentação é válida a partir da atualização **Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.

$("b:contains('oculto')").parent().parent().hide();
]]>
