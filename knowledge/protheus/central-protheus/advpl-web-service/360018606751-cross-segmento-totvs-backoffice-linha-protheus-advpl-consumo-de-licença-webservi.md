---
article_id: 360018606751
category: ADVPL - Web Service
content_hash: 433d39ffc618a7154ceb13d31f4d6e25945f15818660a32a7fa2fd42c5ef21dc
fetched_at: '2026-06-28T22:40:10.394821+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Consumo de Licença
  Webservice, EAI e SCHEDULE
type: support-article
updated_at: '2024-04-18T12:47:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018606751-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Consumo-de-Licen%C3%A7a-Webservice-EAI-e-SCHEDULE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22094624844567)**Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Como funciona o consumo de Licença Webservice, EAI e SCHEDULE?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.80  
  
**Solução**

**WebService**

A licença I é consumida em threads HTTP que são usadas para responder portais ou Web Services.  
Seu consumo segue a configuração contida na chave Instances (http://tdn.totvs.com/display/tec/Instances), existente dentro dos arquivos de configuração dos serviços Protheus.

Cada job iniciado consome uma licença Totvs I. Caso o Webservice demore em seu processamento a retornar ao browser, esta licença não poderá ser utilizada por uma outra requisição.

O acesso ao TOTVS I permite ao usuário o processamento de rotinas e sistemas externos que não envolvam o Full ou Light TOTVS, porém se as rotinas e sistemas externos precisarem acessar ou se conectar ao Full ou Light TOTVS, deverão ter licenças de acesso a estes.

**Consumo de Licença por demanda no REST do Protheus:**

O consumo de licença sob demanda é uma abordagem no Protheus que permite que o serviço REST utilize licenças somente quando uma API está sendo usada, em vez de manter uma licença em uso para cada thread em execução no REST.

Para ativar o consumo de licença sob demanda, é necessário configurar uma opção na seção de endereço (URI) no arquivo de configuração do AppServer. Essa opção é chamada de "Stateless" e deve ser definida como "1" para ativar o uso de licenças apenas quando necessário.

**Importante:**  
Não é possível a utilização da chave Stateless nas configurações via SOAP (WebService), pois a chave está preparada somente para uso do Rest.

**EAI**

EAI vai consumir a TOTVS I, sendo SOAP ou REST. Na definição da mensagem será necessário qual webservice será utilizado.

**Schedule**

O Schedule consome a licença conforme a rotina a ser executada.

Execute: São os componentes responsáveis por realizar a chamada das rotinas agendadas. A única das entidades que consome licença no Schedule Protheus, e isto ocorre na execução da rotina agendada.

Sendo assim o consumo de licença irá depender de qual rotina/processo ser executado.

**Saiba Mais**

[Camada WebService EAI](https://tdn.totvs.com/display/public/framework/Camada+de+Webservices+do+EAI+Protheus)

[Schedule](https://tdn.totvs.com/pages/releaseview.action?pageId=271167961)

[Consumo de licença Totvs I](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003971702)

[Consumo de licença em customizações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063533193-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Consumo-de-licen%C3%A7as-em-customiza%C3%A7%C3%B5es)

[Instances - TOTVSTEC](https://tdn.totvs.com/display/tec/Instances)[Consumo de Licença por demanda no REST do Protheus?](https://tdn.totvs.com/pages/releaseview.action?pageId=527852596)

[Controle de Licenças dos Aplicativos - MINGLE](https://tdn.totvs.com/pages/releaseview.action?pageId=544190925)

[Configuração do REST Protheus para uso com os aplicativos Mobile](https://tdn.totvs.com.br/pages/releaseview.action?pageId=519719292)
