---
content_hash: 9ddd3a8da29dbdde119aa34be262d2cbfa190eee6e93e4a2bbc3fa5ea5e9470f
fetched_at: '2026-06-29T00:08:55.491964+00:00'
page_id: '349184874'
product: rm
source: tdn-rm
title: Cache Centralizado - Guia de Utilização (DEV)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=349184874
version: 30
---

# Sumário

---

Sumário|Revisão|Download dos arquivos

# Revisão

---

|  |  |  |
| --- | --- | --- |
| Versão do Documento | Modificação | Autor / Revisor |
| 1.0 - 28/03/2018 | Criação do documento | Carlos Garcia / Carlos Garcia |

.panelContent, .panelContent p, .panelContent p span{
color: white !important;
background: #202020 !important;
}
]]>

# 1 Introdução

---

          O gargalo de performance em muitos sistemas frequentemente está relacionado a existência de um único servidor de armazenamento de dados, seja este, um banco de dados relacional ou um disco. Para aumentar o throughput nesses sistemas geralmente é necessário a substituição da máquina por uma de maior poder de processamento ou armazenamento, o que incorre em investimento em hardware. Outra forma é aumentar o número de clusters, o que pode se tornar muito complexo e também dispendioso [1].

          Atualmente, em aplicações escaláveis de alta performance e intensivo acesso a dados, bancos de dados NoSql do tipo key-Value (KV) tem recebido especial atenção nos meios acadêmico e corporativo. Além de serem utilizados como banco, KV storages são comumente utilizados como uma camada de cache, mantendo temporariamente informações rapidamente acessíveis cujo esforço de recuperação no banco de dados principal é alto, trazendo também neste contexto melhoria de performance [2,3]. Em aplicações em cloud onde já é utilizado cache em memória RAM, o uso de KV storages pode ser utilizado como meio para racionalizar este recurso removendo as cópias de objetos idênticos alocados por vários processos em diversas máquinas [4].

          Diante disso, o uso de KV storages pode trazer melhoria de performance e economia de recursos diminuindo os custos de uma aplicação. Por isso, o esforço para que este tipo de storage seja suportado deve ser avaliado pelos times de framework e de produto.

          Este documento é um guia de utilização da camada de serviço de cache centralizado desenvolvida pelo time de framework denominado de KVSCache.

# 2 Instalação e Configuração

---

          O documento “Totvs RM - Serviço de Cache - Instalação e Configuração.doc” contém as instruções para instalar e configurar o serviço de cache centralizado. Consulte-o para sanar quaisquer dúvidas referentes a este assunto.

# 3 CacheService - Utilização básica

          A classe RM.Lib.Cache.CacheService centraliza todas as funções de Cache da Lib. Ela deverá ser utilizada para criar as variáveis de cache por todo o sistema.

## 3.1.  Utilizando o cache

---

          Para criação de um novo cache, o desenvolvedor deverá declarar uma variável estática do tipo IRMSCacheService que irá chamar algum dos métodos estáticos CreateCache da classe CacheService

**Exemplo:**

private static IRMSCacheService Cache = CacheService.CreateCache(typeof(RMSUserPrefsClient), nameof(Cache), CacheIsolation.IsolatedByDataBase);

 

          O primeiro parâmetro (ownerType) deverá ser sempre o typeof() da classe que contém a variável do cache, e o segundo parâmetro (id) sempre deverá ser o nameof() da variável estática que irá receber a instância do serviço de cache.

## 3.2.  Opções de cache

---

          Exitem 4 tipos de caches que podem ser utilizados:

* CreateCache – O cache KVS será utilizado por padrão, não há limite de itens ou tempo expiração do item.
* CreateLimitedSizeCache – O cache será feito em memória por padrão, contendo um número máximo de itens.
* CreateLimitedSizeWithTimeoutCache – O cache será feito em memória por padrão, contendo um número máximo de itens e um tempo limite de expiração por item.
* CreateTimedCache – O cache será feito em memória por padrão, contendo um tempo limite de expiração por item. Este cache pode utilizar a opção de SlidingExpiration (por padrão false) que faz com que o tempo limite do item do cache seja renovado quando toda vez que ele é consumido.

          Por padrão o número máximo de itens do cache é 100 e o tempo padrão de expiração é 1 minuto.

## 3.3.  Níveis de isolamento

---

          Existem vários tipos de isolamento que podem ser utilizados, a classe CacheIsolation define os tipos de isolamento mais utilizados. Por padrão, quando o cache for no servidor de aplicação, o isolamento será feito por banco de dados e no cliente é feito sem isolamento.

          Os isolamentos disponibilizados por padrão são:

* NoIsolation – Sem isolamento
* IsolatedByDataBase – Isolamento por banco de dados
* IsolatedByDataBaseColigada – Isolamento por banco de dados e coligada
* IsolatedByDomain – Isolamento por domínio
* IsolatedByDomainMachine – Isolamento por domínio e máquina
* IsolatedByDomainMachineProcess – Isolamento por domínio, máquina e processo
* IsolatedByVersion – Isolamento por versão do RM

# 4 KVSCache - Utilização avançada

---

Atenção!Essa implementação não deve ser utilizada pelos produtos sem avaliar junto à framework a real necessidade. 

          Esse é o nível mais baixo da implementação que pode ser útil em alguns momentos e, caso seja necessário, a classe cacheService documentada no tópico anterior é capaz de entregar um objeto KVSCache.

**É extremamente importante passar pela camada CacheService(tópico 3), pois toda a estrutura de monitoramento do cache só será aplicada utilizando essa camada.**

          A camada de serviço de cache centralizado KVSCache encontra-se disponível no namespace RM.Lib.Cache.KVSCache do assembly RM.Lib.dll e, apesar de sua localização, inicialmente estará disponível para ser utilizada apenas na camada server, caso você tente inicializá-la fora da referida camada será levantada uma Exception.

## 4.1.  Inicializando o KVSCache

---

          O acesso ao serviço é feito a partir da classe KVSCacheProvider onde você poderá verificar se o serviço está configurado e habilitado.

**Ex 1:** Obtendo a instância default do IKVSCacheProvider

          A instância do IKVSCacheProvider retornada na propriedade *Instance,*conforme mostrado acima, utilizará internamente um container Castle para carregar as dependências. Caso seja necessário você poderá instanciar a partir do seu próprio container, conforme exemplo abaixo:

**Ex 2:** Obtendo a instancia default do IKVSCacheProvider

## 4.2.  Níveis de Isolamento

---

          Imagine que você queira armazenar um valor que depende de qual banco você está logado. Neste caso sua chave deveria possuir uma parte que distinguisse os valores entre diferentes bancos. Por isso, a primeira coisa que você deve ter em mente ao utilizar este serviço é o nível de isolamento das chaves que utilizará para que você não se preocupe em gerenciar este isolamento. Ao solicitar uma instância do KVSCache você deve informar qual o nível de isolamento você deseja e a partir daí todas as chaves que você utilizar estarão automaticamente isoladas.

          Os níveis de isolamento disponíveis são:

|  |  |
| --- | --- |
| Isolamento | Descrição |
| Domain | As chaves estarão isoladas pelo domínio da máquina onde a requisição está sendo gerada. |
| Machine | As chaves estarão isoladas pelo nome da máquina onde a requisição está sendo gerada. |
| DataBase | As chaves estarão isoladas pelo banco de dados associado à carteirinha (CorporePrincipal) da requisição. |
| Process | As chaves estarão isoladas pelo nome da imagem do processo e seu id (pid) que está rodando na máquina de onde a requisição está sendo gerada. |
| Coligada | As chaves estarão isoladas pelo código da coligada associado à carteirinha (CorporePrincipal) da requisição. |
| NoIsolation | As chaves não terão isolamento. |

          Você pode escolher qualquer combinação de níveis de isolamento, mas ele sempre será gerado com a prioridade: Domain > Machine > DataBase > Process > Coligada. Por exemplo, se você selecionar o isolamento: Coligada e Domain será gerado o isolamento: /Domain/Coligada/ e nunca /Coligada/Domain/.

          Existem algumas combinações prontas que você pode utilizar: DataBaseColigada, DomainMachine, DomainMachineProcess. Todas são acessíveis a partir de classe KVSCacheProvider.

**Ex 1:** No exemplo abaixo é criada uma chave **“last\_logged\_user”** com o isolamento de Domain, Machine.

          Neste exemplo o conteúdo da variável *user* será gravada no cache sob a chave

#303030

/Domain:bh01.local/Machine:bhd050100289/last\_logged\_user

           **Ex 2:** No exemplo abaixo é criada uma chave **“last\_logged\_user”** com o isolamento de Coligada, DataBase.

          Como dito anteriormente, a prioridade do isolamento DataBase é maior do que Coligada, por este motivo a chave final será:

#303030

/DataBase:sql2017,8034;rm12120/Coligada:1/last\_logged\_user

## 4.3.  Prefixo de Chave

---

          Uma vez definido o nível de isolamento é possível ainda estabelecer um prefixo para todas as chaves acessadas pelo objeto IKVSCache:

**Ex 1:** No exemplo abaixo é criada uma chave **“last\_logged\_user”** com o isolamento de Domain, Machine com prefixo “init\_state”.

          Todas as chaves geradas a partir o objeto kvsCache será criada do isolamento Domain, Machine + KeyPrefix:

#303030

/Domain:bh01.local/Machine:bhd050100289/init\_state/

          A chave final gerada será:

#303030

/Domain:bh01.local/ Machine:bhd050100289/init\_state/last\_logged\_user

## 4.4.  KVSKey e KVSValue

---

          Ao utilizar os métodos de IKVSCache, chaves e valores são informadas por meio das structures KVSKey e KVSValue, respectivamente. As chaves (tipo KVSKey) podem conter string e byte[] enquanto os valores (tipo KVSValue) podem conter tipos primitivos da linguagem e alguns dos principais tipos utilizados pela RM.Lib.

**Ex 1:** Atribuindo às chaves:

**Ex 2:** Atribuindo tipos primitivos aos valores:

**Ex 3:** Ao utilizar os métodos get/set os valores são implicitamente convertidos:

## 4.5.  Método de Serialização

---

          Objetos de tipos diferentes de tipos primitivos, DateTime, DataTable e DataSet serão serializados com o serializador informado na propriedade *SerializationType* que pode assumir os seguintes valores:

* MSDataContract: O objeto será serializado via DataContract da Microsoft e fará uso do RMSDataContractResolver da RM.Lib.Communications.
* NSJson: O objeto será serializado em texto via JsonSerializer da NewtonSoft.
* NSBson: O objeto será serializado em binário via JsonSerializer da NewtonSoft. Este é o valor **default** para serialização.

**Ex 1:** Definindo o método de serialização

## 4.6.  Métodos Get/Set

---

          Existem várias sobrecargas para os métodos Get/Set. Serão abordados os métodos mais completos:

**Ex 1:** Neste exemplo, a chave terá um tempo de vida de 30 minutos, além disso os mesmos parâmetros passados para o método GetPfunc são passados para os métodos Get e Set.

          A chave final gerada será:

#303030

/Domain:bh01.local/ Machine:bhd050100289/key.pfunc:mestre:1:true

**Ex 2:** Para colocar objetos complexos no cache é indicado utilizar as sobrecargas onde o Type do objeto é informado.

## 4.7.  Método Let

---

          O método Let foi criado com o objetivo de agilizar a utilização do cache. As operações de validação se a chave existe, get e set são realizadas de forma encapsulada, bastando passar as informações da chave, uma função lambda que retorne o valor a ser submetido ao cache e os parâmetros da função, que poderão ser também utilizados como sufixo da chave como extraKeys.

**Ex 1:** Neste exemplo a variável **paramBase** receberá o valor do cache caso a chave já exista. Se não existir, a função lambda passada como parâmetro será executada, o conteúdo do seu retorno será inserido no cache e em seguida o método Let retornará o valor para ser atribuído à variável **paramBase.**

# 5 Redirecionamento do MemoryCache para KVSCache

---

          Caso a tag abaixo esteja configurada como true as classes RMSMemoryCache, RMSTimedCache, RMSLimitedSizeCached e RMSParamsServer serão redirecionados para o KVSCache. Por isso é importante utilizar os novos construtores para que o KVSCache seja otimizado.

#303030

<add key="KVSCacheRedirectEnabled" value="true" />

          Os novos construtores possuem os seguintes parâmetros:

* **cacheIsolation**: Nível de isolamento
* **keyprefix**: Prefixo para todas as chaves que será acrescido ao isolamento
* **serializationType**: Tipo de serialização
* **expiry**: Tempo de expiração das chaves para esta instância

# 6 Referencias

---

**[1]** Sharding for startups. <http://www>. [startuplessonslearned.com/2009/01/](http://startuplessonslearned.com/2009/01/) sharding-for-startups.html.

**[2]** B. Fitzpatrick. LiveJournal’s backend—a history of scaling. <http://www.danga.com/words/2005_oscon/> oscon-2005.pdf. [19] K. Fraser. Practical lock

**[3]** B. Atikoglu, Y. Xu, E. Frachtenberg, S. Jiang, and M. Paleczny. Workload analysis of a large-scale key-value store. In Proceedings of the SIGMETRICS’12, June 2012

**[4]** R. Nishtala, H. Fugal, S. Grimm, M. Kwiatkowski, H. Lee, H. C. Li, R. McElroy, M. Paleczny, D. Peek, P. Saab, D. Stafford, T. Tung, and V. Venkataramani. Scaling Memcache a

# Download dos arquivos

---

Download arquivo DOCX

Realize o download do documento .

          A classe RM.Lib.Cache.CacheService centraliza todas as funções de Cache da Lib, ele deverá ser utilizada para criar as variáveis de cache por todo o sistema.

          Para criação de um novo cache, o desenvolvedor deverá declarar uma variável estática do tipo IRMSCacheService que irá chamar algum dos métodos estáticos CreateCache da classe CacheService

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.20 ou Superior

false

Cache Centralizado - **Guia de Utilização**

falsefalse

**Status:** **Finalizado**

false

**Data:**

false

**Autores:**

false 250
