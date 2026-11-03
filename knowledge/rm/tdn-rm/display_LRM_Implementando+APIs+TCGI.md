---
content_hash: 067893c88fb1ae9992b50ac3587f26a0a31b7861d1a8ae4d122e3d959621df26
fetched_at: '2026-06-29T00:11:16.430259+00:00'
page_id: '668178674'
product: rm
source: tdn-rm
title: Implementando APIs TCGI
type: documentation
url: https://tdn.totvs.com/display/LRM/Implementando+APIs+TCGI
version: 20
---

Este documento tem por objetivo demonstrar o padrão e as dificuldades que poderão ser encontradas durante a implementação de APIs para consumo de frontends interno e externo.

Documentação para padronização:

Importante!

Não deverá implementar rotas para CRUD de entidades do TCGI.   
Para utilização dos serviços de CRUD é recomendado a utilização dos serviços RESTFULL RM.  
Para conhecer todos os serviços do RM:   
  
Para saber qual os dataservers e verbos disponíveis para cada dataserver, poderá ser consultado através da lista generica do TCGI.  
[http://](http://localhost:8051/RMSRestDataServer/service/imobiliario)[{dominio}:{ApiPort}](http://localhost:8099/api/swagger/)/RMSRestDataServer/service/imobiliario

Exemplo - POST - Contrato de Vendatrue

### Classe Controller

- Classe controller onde conterá as rotas e verbos para consumo da API deverá ser criada no projeto RM.IMB.API na pasta Common obrigatoriamente  
   a LIB monta o swagger baseada nas informações da dll com final API.  
- A classe de controller deverá receber minimamente os atributos   
  [RoutePrefix("imb/v1/comissao")] //rota padrão de todos os serviços disponibilizados pelo TCGI   
  [RMSController("ImbComissaoRegraServer")]    
  [AllowAnonymous]  
  [RMSLicense(IgnoreLicense = true)] //Licenças diferenciadas PDC, PI, APP  
- Método que fazem parte das rotas na classe de controller devem estár como publico e receberem minimanente os atributos  
  (Método de exempo da classe controler: public ImbComissaoRegraEntity GetReadRecord(int idcorretor){ regras do metodo } )  
[HttpGet]    
[Route]  
 - Atributo utilizado para determinar se deverá citar no caminho da API o nome ou não, se deverá passar valores na assinatura diretamente ou no caminho.

*Exemplo:* [Route] - não informando nenhum caminho ou parametro - deve seguir o método acima - [http://](http://localhost:8055/api/imb/v1/comissao?idcorretor=1)[{dominio}:{ApiPort}](http://localhost:8099/api/swagger/)/api/imb/v1/comissao?idcorretor=1  
                        [Route("corretores")] - está informando que a rota deverá conter o caminho "corretores" - [http://](http://localhost:8055/api/imb/v1/comissao/corretores)[{dominio}:{ApiPort}](http://localhost:8099/api/swagger/)/api/imb/v1/comissao/corretores  
                        [Route("corretor/{idcorretor}")] - deverá informar o caminho e a chave diretamente.  - [http://](http://localhost:8055/api/imb/v1/comissao/corretor?idcorretor=1)[{dominio}:{ApiPort}](http://localhost:8099/api/swagger/)/api/imb/v1/comissao/corretor?idcorretor=1  
                        [Route("corretor/{idcorretor}")] - deverá informar o caminho e a chave diretamente. - [http://](http://localhost:8055/api/imb/v1/comissao/corretor/1)[{dominio}:{ApiPort}](http://localhost:8099/api/swagger/)/api/imb/v1/comissao/corretor/1  
    
- Deverá ser criada a classe model que será utilizada no controler, está é o modelo utilizado para setar os valores e fazer transformação em Json.  
  Nesta classe as variaveis declaradas para recebimento dos valores deverão conter os atributos para transformação da classe modelo de objeto para um tipo Json.  
  [JsonProperty("IDCOMISSAO")]

Importante: Deletar o \_Broker.dat para ser regerado após criar todas as classes envolvidas no processo de disponibilização da API.

### Swagger

Para saber se seu controller ou mesmo a rota foi publicada corretamente no serviço do host da aplicação você poderá acessar o caminho [http://{dominio}:{ApiPort}/api/swagger/](http://localhost:8099/api/swagger/), a lista das apis e rotas demoram para serem carregadas   
(**Dica:** para carregar mais rápido, antes de chamar o swagger, vá até a pasta BIN da aplicação e apague todas as dlls "RM.\*.API.dll" com exceção da dll RM.IMB.API.dll, assim o carregamento será mais rápido).   
Após serem carregadas, pesquise pelo nome do seu controller e depois pela rota. [Para saber mais sobre swagger Totvs clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058274033-Linha-RM-Integra%C3%A7%C3%B5es-O-que-%C3%A9-o-Swagger-).

**Importante:** O Host da maquina que está sendo verificado o serviço, deverá estar rodando com autorização de administrador, atenção com o firewall.

Video demonstração de verificação da API:

250

### Testando o consumo dos serviços da API

1 - POSTMAN  
    - Você pode utilizar autenticação "Basic Auth" para este formato deverá informar 'Username' e 'Password' campos que abriram logo abaixo na tela após selecionar a opção informada.  
    - Recomendamos utilizar a autenticação 'Bearer', caso a opção não apareça no seu postman, poderá digitar manualmente na aba 'Headers' na opção 'Key' o descritivo "Authorization" e em 'value' "Bearer TOKEN ENCONTRADO APÓS CONSUMO DO SERVIÇO DE FORNECIMENTO DO TOKEN", para geração do token utilize a API <http://localhost:8055/api/connect/token>, quando for utilizar o serviço para geração do token, deverá utilizar a autenicação basica, [Para saber sobre Token Totvs RM](https://tdn.totvs.com/pages/viewpage.action?pageId=539528505).  
  
250
