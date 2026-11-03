---
article_id: 19233795380631
category: SIGAACD - Automação e Coleta de Dados
content_hash: d5483b05281c4781f74c3f1c7f854714c84e923c74be8885763c55b5aaf0baf4
fetched_at: '2026-06-28T22:39:12.714402+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Erro de Sincronismo
  no App Meu Coletor de Dados.
type: support-article
updated_at: '2026-02-20T19:40:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19233795380631-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Erro-de-Sincronismo-no-App-Meu-Coletor-de-Dados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19233795362583) Tempo aproximado para leitura: **00:03:00 min**  
  
**Problema**  
Erro de Sincronismo no App Meu Coletor de Dados.

Ocorreu um erro ao sincronizar os dados | Erro ao sincronizar tabela de Produtos | Erro ao sincronizar tabela de Finalizando.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) -Estoque/Custos - Todas as versões.  
  
**Solução**  
Segue abaixo listado por tópicos algumas das principais **"Soluções"** referente ao erro de sincronismo no aplicativo Meu Coletro de Dados.

**1 - Caracteres especiais**

Produtos cujos campos B1\_COD e B1\_CODBAR da sua base de produtos possuem dados com caracteres especiais (representados por símbolos gráficos, matemáticos, sinais de pontuação, acentuação e, até mesmo, por um **espaço**).

Verifique por favor se alguma dessas condições é encontrada nos produtos do B1\_TIPO = **MP**.

**2 - Lentidão no Sincronismo:**

Verifique se o ambiente está devidamente configurado, de acordo com as orientações: [SIGAACD - App Meu Coletor de Dados com lentidão na Sincronização de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14193509486871-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-App-Meu-Coletor-de-Dados-com-lentid%C3%A3o-na-Sincroniza%C3%A7%C3%A3o-de-Dados?source=search)

**3 - PRINCIPAL CONFIGURAÇÃO:**

* Assista o Evento WEBINAR (27/09/2023) sobre os principais pontos de configuração para o correto funcionamento do Meu Coletor de Dados, e equipare as orientações em seu ambiente:

* Assista o How To sobre os pontos de configuração básicos para o correto funcionamento do Meu Coletor de Dados e equipare as orientações em seu ambiente:

Verifique as seguintes documentações que orientam na configuração essencial ao correto funcionamento do Meu coletor de dados. Corrija o que for necessário em seu ambiente:

[Meu Coletor de Dados : Guia de Referência](https://tdn.totvs.com/pages/releaseview.action?pageId=506994322)

[SIGAACD - Configuração do REST Mobile |](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043179314-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configura%C3%A7%C3%A3o-do-REST-Mobile)[Config do REST Protheus para uso em aplicativos Mobile](https://tdn.totvs.com/pages/releaseview.action?pageId=519719292)

[Guia de uso - Assistente de Configuração Mobile](https://tdn.totvs.com/pages/releaseview.action?pageId=620785607)

**4 - TAGs**

* Inserir no seu AppServer.ini do Rest as seguintes Tag's, abaixo das configurações do ambiente:

`[environment]`

**FWLOGMSG\_DEBUG=1**

**FWTRACELOG=1**

**LogProfiler=1**

`[general]`

**Consolelog=1**

**LogHttpFuncs=1**

**LSDebug=2**

**FWTRACELOG=1**

Segue documentações sobre essas Tag's: [Chaves para controle de logs](https://tdn.totvs.com/display/public/framework/Chaves+para+controle+de+logs), [LogHttpFuncs](https://tdn.totvs.com/x/MY5vI), [Tag TraceLS](https://tdn.totvs.com/display/LRM/Habilitar+Tag+TraceLS)

*Observação: Limpar o Console.log na pasta AppServer.ini do seu ambiente para recriar um novo arquivo para validação. E encaminhar o Console.log para análise caso o problema persista.*

* Verificar também se a Tag ***Module=46*** está devidamente configurada no seu AppSever.ini do Rest.

Segue documentação sobre a Tag: [SIGAACD - Qual licença utilizar no aplicativo Meu Coletor de Dados?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411627803415--Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Qual-licen%C3%A7a-utilizar-no-aplicativo-Meu-Coletor-de-Dados-)

*Observação: Quando informar a Tag no seu AppSever.ini reiniciar o serviço do coletor para novos testes no ambiente.*

**5 - Verificar se todos os serviços do aplicativo estão no ar:**

TOTV - RESTFULL API - Informar o seu endereço de IP e Porta do REST.

**Exemplo**: <http://localhost:2626/rest>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19233784308375)

**6 - Atualizações no ambiente**

Verificar se todos os artefatos constam atualizados no ambiente. Realizar um teste em ambiente de Homologação com as atualizações a seguir:

- [Acumulado SIGAEST conforme sua versão](https://tdn.totvs.com/x/2hgdHw)

- [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) -[Logo Guará](https://suporte.totvs.com/portal/p/10098/download?e=989259) | [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526)

- [Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/) - [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947528)  | [Harpia](https://suporte.totvs.com/portal/p/10098/download#detail/1031460)

- Smartclient - [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947510) | [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1031469)

- [DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/)

**7 - Desativar as customizações**

Realize os testes desativando todas as customizações do ambiente através dos [3 métodos indicados nesta documentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292), impreterivelmente.

Saiba mais: [Como ativar e desativar customizações no Protheus? |](https://tdn.totvs.com/pages/releaseview.action?pageId=240308618)[SIGAEST - Como desabilitar customizações através do catálogo de personalização do Configurador?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018286552-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-desabilitar-customiza%C3%A7%C3%B5es-atrav%C3%A9s-do-cat%C3%A1logo-de-personaliza%C3%A7%C3%A3o-do-Configurador-)

**8 - Dados para análise do Suporte Protheus**

Em caso de realizar todas as correções e orientações aqui mencionadas, e persistir o erro de sincronismo no App Meu Coletor de dados, envie os seguintes insumos para análise:

* Print do erro para análise
* AppServer.ini do ambiente do Rest para análise ( caso seja Cloud, informe os dados para consulta via TCLOUD)
* Inspetor de Objetos

É importante reforçar que todas as correções e orientações aqui mencionadas tenham sido devidamente aplicadas. Uma vez que o problema persiste, apesar de realizadas as premissas já mapeadas, é provável que a ocorrência requeira uma investigação mais profunda diretamente no ambiente que apresenta o problema, o que caracteriza atendimento na modalidade de Consultoria. Por isso, é **essencial que as orientações tenham sido criteriosamente aplicadas, evitando assim possíveis custos de consultoria**. Saiba mais: [SUP.PROTHEUS - Modalidades e Escopo de Atendimento do Suporte Técnico](https://tdn.totvs.com/pages/viewpage.action?pageId=543089204).

***Saiba mais:***

[*SIGAACD - Como habilitar bipagem do endereço na transferência pelo Meu Coletor de Dados?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17571768148887-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-habilitar-bipagem-do-endere%C3%A7o-na-transfer%C3%AAncia-pelo-Meu-Coletor-de-Dados-)

[*SIGAACD - App Meu Coletor de Dados com lentidão na Sincronização de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14193509486871-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-App-Meu-Coletor-de-Dados-com-lentid%C3%A3o-na-Sincroniza%C3%A7%C3%A3o-de-Dados?source=search)

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
