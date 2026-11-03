---
content_hash: c3296954e822e911e2039e7dd0d29dfd7e339b66e07375a50e5ec2d7abcf6cb8
fetched_at: '2026-06-29T00:08:15.463819+00:00'
page_id: '244739013'
product: rm
source: tdn-rm
title: ER_FRW_FRW002-32_PADRAO_DE_SEGURANCA_CLIENT_SERVER
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_FRW_FRW002-32_PADRAO_DE_SEGURANCA_CLIENT_SERVER
version: 133
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Framework | **Módulo** | Globais |
| **Segmento Executor** |  | | |
| **Projeto1** |  | **IRM1** |  |
| **Requisito1** | [FRW\_FRW002-32](http://jiraproducao.totvs.com.br/browse/FRW_FRW002-32) | **Subtarefa1** | FRW\_FRW002-80 |
| **Chamado2** |  | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

        Em consonância com o mercado e com a estratégia da TOTVS, estamos expondo nossos serviços para consumo externo em um padrão REST, inclusive os DataServers.

        O FrameHTML por ser tratar de uma aplicação baseada em javascript e HTML irá usufruir dessa infraestrutura criada.

        Diante disso surgem algumas definições e mudanças necessárias para que sejamos 100% SOA e, consequentemente, tenhamos nossos serviços prontos para serem consumidos por qualquer aplicativo.

## Definição da Regra de Negócio

*Nossa arquitetura está preparada para ser 100% SOA, porém precisamos pensar como os nossos DataServers funcionam para então perceber as deficiências dos mesmos e tratá-las.*

Cenário atual:

Temos duas formas de chamadas de serviços no RM.Host, são elas:

1. **Chamada Client (Winforms/WebForms)**  
     
   Neste caso, a Lib se encarrega de recuperar o RMSContext que está no contexto da aplicação cliente (WinForms/WebForms) e entregar para o serviço no server (RM.Host). Esta forma permitiu que os DataServers de produto fossem herdados do RMSDataServer e as informações de contexto ficassem disponíveis nos serviços (ReadView, ReadRecord,etc) executados.
2. **Chamada WebService (SOAP/REST)**

         Para expor nossos DataServers, foi criado um WebService genérico que recebe como parâmetro o nome do DataServer, o contexto (coligada, sistema, usuário, etc.) e demais parâmetros pertinentes ao serviço executado (ReadView, ReadRecord, etc.), com isso o DataServer do produto recebe o contexto que ele precisa para ser executado.

          Com a chegada do FrameHTML (100% HTML e Javascript), nossa arquitetura sofreu uma evolução para expor nossos serviços. Hoje temos uma camada que expõe os serviços em HTTP (REST/JSON ou XML) utilizando WebAPI 2.0, com isso qualquer aplicação, inclusive o FrameHTML, pode chamar nossos serviços, porém como vimos, nossos DataServers dependem de um contexto de execução (RMSContext). Contudo, o RMSContext traz consigo muitas informações que podem ou não ser úteis à execução do DataServer em questão.

          No primeiro momento para tornar o desenvolvimento produtivo, criamos um serviço *RMSDataServerController* que recebe o nome do DataServer como o parâmetro. Para entregar ao DataServer em questão o contexto da aplicação o FrameHTML tem um *interceptor* que resgata o contexto (está armazenado em uma variável chamada *currentContext* no escopo do AngularJS) e adiciona todas as propriedades do contexto no *header* da requisição. O RMSDataServerController resgata o contexto do *header* e entrega ao DataServer em questão.

          Como podemos notar o nosso serviço depende de informações de contexto que são trafegadas no *header* da requisição. Neste ponto precisamos entender alguns termos utilizados na arquitetura SOA que estão diretamente relacionamos às mudanças que teremos.

| Termo | Definição / Comentário |
| --- | --- |
| Serviço | É uma função independente, sem estado (*stateless*) que aceita uma ou mais requisições e devolve uma ou mais respostas através de uma interface padronizada e bem definida. Serviços podem também realizar partes discretas de um processo tal como editar ou processar uma transação. Serviços não devem depender do estado de outras funções ou processos. A tecnologia utilizada para prover o serviço, tal como uma linguagem de programação, não pode fazer parte da definição do serviço. |
| Orquestração | Processo de sequenciar serviços e prover uma lógica adicional para processar dados. Não inclui uma representação de dados. |
| Stateless | Não depende de nenhuma condição pré-existente. Os serviços não devem depender de condições de outros serviços. Eles recebem todas as informações necessárias para prover uma resposta consistente. O objetivo de buscar a característica de *stateless* dos serviços é possibilitar que o consumidor do serviço possa sequenciá-lo, ou seja, orquestrá-los em vários fluxos (algumas vezes chamados de pipelines) para executar a lógica de uma aplicação. |
| Provedor | O recurso que executa o serviço em resposta a uma requisição de um consumidor. |
| Consumidor | É quem consome ou pede o resultado de um serviço fornecido por um provedor. |
| Descoberta | SOA se baseia na capacidade de identificar serviços e suas características. Consequentemente, esta arquitetura depende de um diretório que descreva quais os serviços disponíveis dentro de um domínio. |
| Binding | A relação entre os serviços do provedor e do consumidor deve ser idealmente dinâmica; ela é estabelecida em tempo de execução através de um mecanismo de binding. |

          Ao confrontarmos os conceitos SOA e as definições da TOTVS com o que está implementado hoje, vemos que precisamos das seguintes mudanças:

1. O serviço deve ser stateless, hoje nossos DataServers dependem do contexto.
2. O serviço deve ser auto-documentável, portanto esperar somente o que precisa para execução, o RMSContext têm muita informação que pode ser dispensável para determinadas rotinas.
3. Nenhuma informação deve ser enviada pelo *header*, pois dificulta a documentação e utilização.

          O Controller genérico RMSDataServerController criado na WebAPI juntamente com o intercepctor criado no FrameHTML permanecerá funcionando para manter compatibilidade. Porém é expressamente recomendado que as novas funcionalidades migradas para o FrameHTML nasçam respeitando todas as premissas apontadas acima.

         Veja o desenho simplificado da nossa nova estrutura.

      Outro ponto importante que devemos tratar é a segurança das informações armazenadas no cliente.

      Vamos nos ater a falar na aplicação web (Portal). Hoje grande parte das informações armazenadas no lado cliente, como por exemplo o contexto da aplicação (RMSContext), está na sessão do ASP.NET(Sevidor Web na imagem acima) e, consequentemente, protegida.

       Já o FrameHTML, entrega somente os componentes em HTML e Javascript, ou seja, não possui uma implementação em cima de servidor web(isso deverá ser feito pelo produto), portanto se for utilizar a infraestrutura do mesmo(angularJS) para armazenar informações, lembre-se que a mesma é passível de alteração por estar no Browser. Veja o exemplo abaixo:

      O usuário (U) se autentica e acessa a funcionalidade de histórico salarial. Considere que o DataServer de histórico salarial utilize o usuário do contexto para filtrar o retorno dos dados, ou a segurança da informação. Neste ponto temos a seguinte diferença entre o Portal e o FrameHTML:

**Portal**:

                O RMSContext está na sessão do ASP.NET, protegida pelo servidor de aplicação. Portanto, podemos confiar na informação atribuída ao RMSContext.

**FrameHTML**:

                O RMSContext está no escopo do AngularJS, ou seja, no navegador e totalmente vulnerável à intervenção do usuário. Portanto, passível de alteração pelo usuário que se autenticar para acesso ao histórico salarial. Outro exemplo seria uma chamada de WebService, autenticando-se com um usuário e passando outro usuário no Contexto.

**Diante do exposto é expressamente recomendado que os serviços utilizem o usuário do *Principal* (carteirinha), pois esse a Lib garante. Já o usuário do RMSContext não é garantido pela Lib e o exemplo acima é apenas um de várias formas que temos de enviar um usuário logado diferente do usuário do contexto.**

*Pra finalizar vamos ver algumas dicas para criação dos EndPoints:*

1. ****Requisitos fundamentais para API****

   Lembre-se que você está desenvolvendo uma interface que será utilizada por outro desenvolvedor, então, é importante tomar alguns cuidados:

   * possuir documentação adequada;
   * ser o mais simples e intuitivo possível (*affordance*), seja na URI, *payload*, *request* ou *response*;
   * deve-se levar em conta a experiência do usuário. Procurar seguir o padrão já utilizado pelo mercado, evitar “coisas” mirabolantes;
   * manter a padronização, nas URIs, tipo de retorno, etc.
2. ****Padrões HTTP****REST é baseado no protocolo HTTP, é importante seguir os padrões definidos por ele e aplicá-los onde eles fazem sentido, por exemplo, nos*status code* de retorno de um método.
3. ****Utilize JSON****  
   Evite utilizar XML, eles são verbosos, difíceis de ler. Basta analisar o gráfico abaixo extraído do *Google Trends*. Nele fica claro o crescente interesse na utilização de APIs JSON frente a APIs XML.
4. ****URI, recursos****  

   Um dos princípios fundamentais de REST é separar a API em recursos semânticos, que serão manipulados através de solicitações HTTP, e eles devem fazer sentido para os usuários da API.  
   A identificação do recurso deve ser um substantivo e não um verbo. Não há uma regra que diga se o recurso deve estar no singular ou plural, porém, o escolhido, deve seguir um padrão em toda a API. Exemplo de recursos em uma API disponibilizada em um domínio denominado “*[meudominioxpto.com](http://meudominioxpto.com)”*:

                     /cliente  
                    /produto  
                    /pedido

   E como lidar com relações? Por exemplo, o telefone de um cliente.

                   /cliente/33/ telefone – manipular os telefones do cliente 33;  
                   /cliente/33/ telefone/10 – manipular os telefones 10 do cliente 33.
5. **Verbos HTTP**  
   Use o verbo correto para as operações de CRUD (*Create*, *Read*, *Update* e *Delete*):
6. ***Status code HTTP***  
   *O uso correto do*status code* facilita muito a vida dos clientes (consumidores) de sua API, utilize-os da maneira correta e padronizada.*
7. ***Passagem de Parâmetros***  
   *Para API REST, as mais mais utilizadas são: Path Parameters; Query Parameters; Header Parameters e Body Parameters. É uma boa prática utilizá-las da seguinte maneira:*
8. **Por fim**.  
   Quando for construir um serviço, pense que o seu serviço deve ser:
   1. Stateless
   2. Simples de usar
   3. Auto documentável
   4. Esperar somente o que precisa
   5. Deve confiar somente no usuário da carteirinha(Principal), todas as outras informações(RMSContext por exemplo) são vulneráveis.
   6. Assinatura padronizada.

### 

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
