---
content_hash: 5b206817b88d2b6019523b75f4aef4306725360408d3f6daeb54deffe188de9f
fetched_at: '2026-06-29T00:05:49.067787+00:00'
page_id: '1036765537'
product: rm
source: tdn-rm
title: Tela de Diagnóstico SmartLink
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1036765537
version: 11
---

# **Índice**

---

Índice

# **Objetivo**

---

Este documento visa introduzir, demonstrar e ensinar a respeito da tela de Diagnóstico SmartLink.

Não serão abordadas questões sobre a integração em si, apenas desta tela.

Disponibilidade

A tela de Diagnóstico SmartLink está disponível a partir das versões **12.1.2602**, **12.1.2510.161** e **12.1.2506.233**.

# **Informações sobre o menu**

---

## **Como acessar**

A tela se encontra no módulo **Integração**, no menu **Totvs App**:

## **Segurança**

É necessário liberar a permissão para o perfil do usuário:

# **Funcionalidades**

---

A tela possui quatro abas diferentes, cada um com um foco específico:

## **Integração**

Tem como intuito mostrar o status da integração, e auxiliar no diagnóstico de algum mal funcionamento da mesma.

### Explicação dos campos:

* **Status do ambiente:**Informa se o ambiente esta Integrado ou não.  
  Caso não esteja integrado, o motivo deve ser analisado na .
* **Totvs Id:** Identificador no Smartlink.
* **Tenant Id:** o ID do tenant que está sendo utilizado no SmartLink. Útil para diagnósticos.
* **Client Id:** caso esteja preenchido, significa que a integração está rodando corretamente.   
  Este campo vazio implica em que a integração está completamente parada.
* **Url base do Rac:** deve estar vazio; caso esteja preenchido, implica que o ambiente está acessando um ambiente de desenvolvimento ou homologação.
* **Hash de ambiente:** Identificador do ambiente no Smartlink.

### Servidores executando:

Essa visão mostra o status dos mecanismos executores da integração.

#### Explicação dos campos:

* **Nome do serviço:** identifica a parte da integração;
* **Servidor de execução:** mostra o servidor com a porta que está controlando a execução do serviço.   
  Importante ressaltar que este servidor deve estar dentro da portabilidade da integração para que ela funciona corretamente.
* **Status:** caso o último acesso do serviço ao banco de dados seja nos últimos 10 minutos, estará como Ativo. Caso contrário, será Inativo.
* **Última atualização do serviço:** mostra quando a respectiva integração executou a última vez. Tempo de Pooling.  
  Data Sharing Delta, a cada 15 segundos. (Tempo mínimo) e leva 2 minutos para começar após iniciado o serviço do Host.  
  Data Sharing FR, a cada 2 minutos. (Tempo mínimo) e 3 minutos após iniciado o serviço do Host.  
  Credential Helper, a cada 10 minutos e 1 minuto após o Host.  
  Behavior Sharing, a cada 5 segundos e 2 minutos após o Host.

  Observação

  Devido a um possível tempo maior de processamento do que o tempo de pooling é esperado que a próxima execução ocorra em um tempo maior do que o definido para cada serviço.

  Ou seja, o tempo de pooling é um tempo mínimo de execução.

## **Data Sharing**

Aqui temos informações sobre os dados enviados através do Upstream Data Sharing.

Ambas as visões possuem como referência o campo **Identificador do Batch**, o qual é utilizado para identificar o pacote de dados enviados também na plataforma SmartLink.

### Controle dos dados sincronizados

Nesta visão são apresentadas as informações de envio de cada tabela e pacote, com um resumo geral do que esta sendo realizado pela integração.

#### Explicação dos campos:

* **Identificador do pacote:** Número BatchId, que identifica o pacote ao Smartlink.
* **Nome da tabela enviada:** Tabela que foi enviada para o Smartlink.
* **Status:** Informa a situação atual da tabela:  
  Sucesso: Indica que o envio foi realizado corretamente.  
  Suspenso: Indica que a tabela esta em processamento ou aguardando seu envio.  
  Erro: Indica algum problema no envio. Abrir os detalhes da mensagem para analisar o motivo do erro.
* **Tipo de mensagem:** Informa se é Detal ou ForceReload
* **N. de pacotes enviados:** Quantidade de mensagens enviadas para a tabela em questão.
* **N. de registros encontrados:** Quantidade total de registros encontrados e possíveis de serem enviados.
* **N. de registros enviados:** Quantidade total de registros enviados.
* **Começo do envio:** Data e hora de início do envio da tabela.
* **Fim do envio:** Data e hora de término do envio.

### Informações dos pacotes

Nesta visão podemos ver a informação dos sumários enviados à plataforma.

O sumário é uma informação enviada logo após a finalização do envio dos dados. A função dele é garantir que todos os dados enviados foram recebidos.

#### Explicação dos campos:

* **Identificador do pacote:** Número BatchId, que identifica o pacote ao Smartlink.
* **Número de registros enviados no pacote:** valor enviado à plataforma para sincronizar com a quantidade dos registros enviados.
* **Status do Sumário:** determina se o resumo foi enviado à plataforma. O valor 0 denuncia um pacote ainda em envio, ou um possível problema no envio.
* **Tipo de execução:** identifica se o pacote enviado foi enviado como ForceReload (carga forçada ou inicial) ou um Delta (carga normal/apenas a diferença).
* **Começo do envio:** Data e hora de início do envio.
* **Última atualização:** Data e hora de última atualização do sumário.

### Registros sincronizados

Esta é a visão dos registros enviados à plataforma, organizados por **nome da tabela** e **identificador do pacote**.

Nem todos os registros sincronizados são mantidos aqui, pois a tabela é sanitizada regularmente e apenas os registros enviados como Delta são mantidos aqui.

## **Behavior Sharing**

Aqui temos informações sobre a comunicação realizada com os Totvs Apps, através do Behavior Sharing.

### Mensagens pendentes de execução

Nesta primeira view, visualizados as mensagens ainda não processadas pelo NotifyServer.

Em um cenário ideal, esta tabela vai possuir registros por pouco tempo, pois logo serão processados.

Caso possua registros antigos, é um bom indício de que há algum problema com o processamento das mensagens.

### Mensagens executadas

Aqui podemos ver as mensagens já executadas, e seu histórico, com o **Corpo da mensagem** enviada/recebida.

Já o campo Tipo da mensagem, determinada se ela foi **enviada** (valor 0), ou **recebida** (valor 1).

## **LoglinkLog**

Na visão de Log, todo o histórico de execuções da integração está presente. São mantidos dados de no máximo 10 dias.

Apresenta informações detalhadas do que esta sendo realizado pela integração, sendo possível analisar e ver detalhes de cada log.

#### Explicação dos campos:

* **Data do Log:** Data e hora de registro da ação.
* **Tipo do Log:** Informação, Aviso ou Erro.
* **Tipo do processo:** Identifica qual é o Serviço que gerou esta ação. Credential Helper,  Behavior Sharing Downstream,  Behavior Sharing Upstream,  Credential Helper,  Data Sharing ou  NotifyServer
* **Chave de pesquisa:** Identificar para auxiliar em filtrar os Logs e agrupar por assunto.
* **Texto do Log:** Informação detalhada relativa a ação registrada.
