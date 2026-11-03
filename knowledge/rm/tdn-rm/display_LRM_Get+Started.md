---
content_hash: 40ad0ae48711a670fbcacd6a5d8b7f2eda23a7588dcd94d388f92bcd4f33548d
fetched_at: '2026-06-29T00:08:57.332758+00:00'
page_id: '354451606'
product: rm
source: tdn-rm
title: Get Started
type: documentation
url: https://tdn.totvs.com/display/LRM/Get+Started
version: 12
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é orientar como é feita a utilização de alguns recursos do Snowden em seu formato mais simples. O tópicos abordados serão os citados acima no índice.

# Access Token:

---

       Para realizar a integração com o Snowden é necessário o envio do Access Token no campo Authorization do Header em todas as requisições. O Snowden utilizada o Fluxo Client Credentials para recuperação do Token, então deve ser feita um chamada ao WSo2 para geração do mesmo. Este fluxo necessita apenas do ClientId e ClientSecret.

**Exemplo de Requisição:**

css

Obs: O **ClientId** e **ClientSecret** podem ser passados no Body da requisição ou no Header Authorization codificado para base64 ClientId:ClientSecret

# Enviando Logs de erros para o Snowden:

---

       Atualmente existem 3 formas de interagir com o Snowden para envio dos logs de erros. São eles:

* **Envio assíncrono:** Onde enviamos um único log para o Snowden, contendo uma ou mais ocorrências, porem seu processamento é feito em paralelo e em outro momento da requisição. Essa requisição irá apenas retornar o protocolo para acompanhamento.
* **Envio síncrono:** Como no envio assíncrono enviamos apenas um erro, mas ele retorna imediatamente o registro de incidente criado para aquele log.
* **Envio em Bloco:** Envio de grandes volumes de logs, contendo n registros e n ocorrências.

## Envio Assíncrono:

---

     Uma requisição de envio de log no modo assíncrono, trata-se de um POST contendo as informações sobre o log em seu corpo, segmentado em aplicação, cliente, log e suporte.

Sessão de Aplicaçãofalse

Trata-se das informações exclusivas e gerais da aplicação, contendo os campos:

* **productLine:** Trata-se do nome da linha de produtos, como exemplo o **“rm”**
* **application:** Trata-se do nome da aplicação em si, como exemplo o **“portal-do-cliente”**
* **version:** Versão cheia da aplicação em que foi identificado, como exemplo a versão **“12.1.20”**
* **environment:** Campo para identificar se o erro encontrado ocorreu em produção/homologação etc. a diferenciação desta informação faz com que o mesmo incidente possa ter 2 identificações diferentes, uma para cada ambiente. As principais opções de valor são as listadas abaixo, valores diferentes destes podem ser enviados, porém, não possuem suporte nas interfaces e aplicações produzidas para o Snowden.
  + production
  + test
  + development
Sessão do Clientefalse

É composto pelos campos:

* **totvsId:** Campo para identificação do cliente, esse identificador é o mesmo que é utilizado nas instalações do License Server e o mesmo oferece uma forma de recupera-lo através de uma mensagem LS006. OBS: não se trata do identificador do cliente dentro da totvs ou seu cnpj.
* **displayName (opcional):** trata-se de um valor temporário para o nome de exibição do cliente, recomenda-se o não envio, pois todas informações serão sincronizadas automaticamente com os dados oficiais.
Sessão de Logfalse

É onde são enviadas todas informações sobre a falha do sistema.

* **message:** Campo que recebe um texto explicando do que se trata o erro, recomenda-se aqui conter o texto de maior abstração da falha, porém, sem conter informações relativas ao contexto como parâmetros. Ex: mensagem de uma exception.
* **detail:** Campo que contém um detalhe de baixo nível (extremamente técnico) do erro, como no campo de mensagem esse campo também não deve conter informações de contexto como parâmetros, mas deve fornecer informações para reconhecer o local de onde a falha ocorre. Ex: stacktrace ou callstack;
* **type:** Tipo do log enviado, sendo as seguintes opções:
  + 000: não classificado;
  + 100: Erro ocasionado pelo ambiente. Ex: falha de comunicação com o banco de dados;
  + 200: informacional: Ex: usuário sem permissão;
  + 300: erro lógico: Ex: operação não esperava valores menores que 0.
* **module:** Modulo da aplicação em que o erro foi identificado, esse campo é opcional caso existam cadastros de  que façam posteriormente a identificação do mesmo.
* **tags (opcional):** São informações para segregação do incidente gerado.
* **occurrences:** Aqui vem o registro de ocorrências deste erro. Todo incidente enviado deve conter ao menos 1 registro. Trata-se de uma lista de objetos contendo:
  + **data:** Maiores informações da falha como os parâmetros de entrada da operação; o formato deste campo é livre mas recomenda-se utilizar o envio de uma string contendo um json.
  + **timestamp:** Momento em que a falha ocorreu;
  + **fileData (opcional):** Dados de um arquivo vinculado a ocorrência codificado em base64;
  + **fileContentType (opcional):** MIME type do arquivo enviado, é obrigatório caso o campo fileData seja informado.
  + **fileName (opcional):** Nome do arquivo enviado, é obrigatório caso o campo fileData seja informado;
Sessão de Suportefalse

É para casos onde queiramos abrir um ticket junto da integração com o Zendesk.

* **openTicket:** Trata-se de uma flag booleana indicando se o Snowden deve realizar o procedimento de abertura do ticket para o incidente vinculado ao cliente informado.

**Exemplo de Requisição:**

css

 O resultado com sucesso da operação acima, retorna um código HTTP 200, contendo um objeto com a seguinte propriedade:

* **protocols:** Um vetor de strings onde cada valor é um protocolo de acompanhamento do cliente, é sempre gerado um para cada ocorrência do incidente.

**Exemplo de resposta:**

css

## Envio Síncrono:

---

     O envio síncrono é muito similar ao assíncrono, a diferença real estará no resultado da operação, onde conterão informações sumarizadas do incidente e do ticket aberto (caso requisitado).

falseObservação:

Essa forma de comunicação é crítica e deve ser utilizada com cautela. Para a maioria dos casos incentivamos utilizar o método assíncrono ou o em bloco para grandes volumes.

      Para que a requisição então seja executada de forma síncrona, precisamos enviar um parâmetro de query na requisição apontando como async sendo false. Já o corpo da requisição será o mesmo utilizado no assíncrono.

**Exemplo:**

* https://snowden.totvs.com.br/api/v1/entries**?async=false**

Como mencionado, o resultado da operação conterá também as informações do incidente gerado. São elas:

* **id:** Identificação utilizada pelo Snowden;
* **hash:** Identificação alternativa utilizada pelo Snowden para identificação do erro;
* **type:** Tipo do incidente, igual ao valor enviado no log, salvo em casos onde haja pipelines que façam alteração deste valor;
* **productLineId:** Identificação da linha de produto em que esta  vinculado o incidente;
* **productLineHeaders:** Informações rápidas da linha de produto, como seu nome logico (utilizado em comunicações com o Snowden) e o seu nome de exibição em interfaces;
* **applicationId:** Identificação da aplicação vinculada;
* **applicationHeaders:** informações rápidas da aplicação, como seu nome logico (utilizado em comunicações com o Snowden) e o seu nome de exibição em interfaces;
* **moduleId:** identificação do Snowden para o módulo;
* **moduleHeaders:** informações rápidas do módulo, como seu nome logico (utilizado em comunicações com o Snowden) e o seu nome de exibição em interfaces;
* **environmentId:** identificação do ambiente que foi encontrado o erro;
* **environmentHeaders:** informações rápidas do ambiente, como seu nome logico (utilizado em comunicações com o Snowden) e o seu nome de exibição em interfaces.
* **dateFirstOccurrence:** data da primeira ocorrência junto ao Snowden, para geração deste campo é sempre pego o menor valor do timestamp dentre as ocorrências envidas;
* **elastorresistência:** como na data da primeira ocorrência neste caso temos a data mais recente;
* **recurrence:** número de vezes em  que foi identificação a repetição do erro entre todos os clientes;
* **message:** Mensagem do erro enviado no log;
* **detail:** detalhe do erro enviado no log;
* **tags:** Trata-se de uma lista de tags para segregação de incidentes.

**Exemplo:**

c#

## Envio em Bloco:

---

     O envio em bloco é quando precisamos fazer o envio de grandes quantidades de incidente. Essa forma de comunicação vem para suprir essa necessidade. Através de uma única chamada é possível enviar pacotes com grandes quantidades simultaneamente (recomendamos o envio de pacotes de 100).

     Essa operação está disponível apenas de forma assíncrona, e não é possível recuperar os protocolos de envio uma vez que não há como relacionar a qual incidente estão relacionados. Esta é a forma recomendada de comunicação sempre que for enviar um erro onde não há iteração do usuário, ou seja, erros onde ele não fará o acompanhamento ativo.

     O pacote de dados a ser enviado é muito similar aos outros, os campos de aplicação estarão presentes da mesma forma. O que muda então é que agora temos um novo campo chamado “Entries” que se trata de um vetor onde irão os logs enviados. Então cada um dos objetos deste vetor conterá:

* **log:** O campo log é igual aos métodos síncrono e assíncrono, ele contém as informações do erro em questão;
* **occurrences**: Igualmente no síncrono e assíncrono, são os registros de ocorrência do erro contendo os detalhes adicionais e o momento em que ocorreu;
* **support:** Igualmente também ao síncrono e assíncrono, porém, agora vai estar presente para cada log e não mais no topo da requisição.

**Exemplo de Requisição:**

css

     O resultado desta operação em bloco é um HTTP status 202, e não existe um conteúdo de resposta.

# Recuperação do TotvsId através do License Server:

---

     A funcionalidade de recuperar o totvsId do cliente foi disponibilizada na versão 01.03.013 do License Server, essa funcionalidade pode ser utilizada através do modelo requisição e resposta, onde enviando uma mensagem no padrão LS006 ele retornará à confirmação com o totvsId da instalação Veja exemplos abaixo:

**Requisição:**

css

**Resposta:**

css

# Detalhes sobre a Identificação de Incidentes no Snowden:

---

     Como mencionado anteriormente o Snowden utiliza de alguns valores sensíveis nos logs para identificar a recorrência dos incidentes, são eles: linha de produto; nome de aplicação; ambiente; mensagem do log e detalhe do log; então a menor variação de qualquer um destes campos faz com que o Snowden passe a identificar como um novo incidente;

     Em ambientes onde é utilizado ofuscação de código recomendamos procurar se a solução utilizada fornece uma opção de sempre ofuscar gerando os mesmos símbolos, isso faz que com implementações onde sejam avaliados callstacks ou stacktraces os nomes dos métodos e objetos mesmo que ofuscados sempre gerem o mesmo nome.

# Segregação de incidentes:

---

     Todos sabemos que a segregação de incidentes é importante e que apenas as informações se é um ambiente de produção e qual aplicação nem sempre será o suficiente. Para resolver isso o Snowden conta com um mecanismo de tags, assim flexibilizando a forma de relacionar incidentes.

## Onde Aplicar:

---

     Pensando em um cenário onde precisamos identificar todos os incidentes que estão acontecendo em nosso ambiente cloud; se é um incidente que acontece de forma transparente para o usuário e qual o patch se encontra aquela aplicação, então criamos as tags :

* **cloud:** Essa tag estará presente em todo incidente que originar de um erro da aplicação em cloud;
* **background:** Essa é para identificar que é um erro background, ou seja, transparente para o usuário;
* **path {numero}:** Substituindo o {numero} pelo patch corrente, sabemos então a versão de patch.

## Como Fazer o Envio:

---

     As tags não precisam de cadastro prévio e devem ser enviadas no campo log de qualquer uma das formas de envio de erro ao Snowden [LINK]. A partir daquele momento, o incidente gerado através deste log sempre terá todas tags enviadas a ele funcionando de forma incremental. Já as ocorrências relacionadas, conterão as tags vinculadas daquela requisição.

**Exemplo:**

css

     Vemos na requisição acima que estamos vinculando 5 tags, 3 das quais são utilizadas para identificar o cenário apontado acima.

## Filtrando incidentes:

---

     O filtro de incidentes por tags é através do endpoint da coleção de incidentes, neste temos um parâmetro de query chamado tags que recebe um CSV com as tags que deseja no incidente. O filtro funciona buscando incidentes que possuam todas as tags do filtro.

**Exemplo:**

* https://snowden.totvs.com.br/api/v1/incidents**?tags=cloud,patch:20.1.21.129,background**

    O retorno é o padrão do método de pesquisa de incidentes.

## Padrões:

---

     O Snowden possui algumas tags padrões para identificação de alguns cenários, são elas:

* **background:** Representa um erro identificado pelo sistema sem que haja interação com o usuário.
* **user-reported:** Quando o erro é reportado com explicita intenção do usuário, recomendado utilizar em telas de erro principalmente quando forem retornar o protocolo de acompanhamento do usuário.

     Em caso de omissão das tags ***background*** e/ou ***user-reported***, todo incidente é interpretado como background e por mais que a tag esteja ausente, em caso de pesquisa por erros com a tag background estes erros serão retornados.

## Nomenclatura:

---

     O Snowden aplica as seguintes regras para as tags:

* Tamanho máximo de 32 caracteres;
* Diferenciação de maiúsculas de minúsculas;
* Apenas caracteres ASCII

     Para melhor integração das interfaces, quando houver tags que sejam propriedades, recomenda-se utilizar a notação de {nome}:{valor} como mostra o exemplo abaixo:

**Exemplo**: patch : 12.1.20.129

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.20

false

**Processo:** Get Started (Snowden)

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
