---
content_hash: b4dc46ea2ee9c3cf6b876697f1125256a97079020b941d3b2c63fe3db6aece2b
fetched_at: '2026-06-29T00:10:14.363964+00:00'
page_id: '458776840'
product: rm
source: tdn-rm
title: Reliable Session WCF
type: documentation
url: https://tdn.totvs.com/display/LRM/Reliable+Session+WCF
version: 34
---

# Introdução à sessões confiáveis

**Sessões confiáveis** fornecem transferência confiável de ponta a ponta de mensagens entre uma origem e um destino usando o protocolo **WS-Reability** de mensagens, independentemente do número ou tipo de intermediários que separam os pontos de extremidade de mensagens (origem e destino). Isso inclui qualquer intermediário de transporte que não usa **SOAP** (por exemplo, **proxies HTTP**) ou intermediários que usam o **SOAP** (por exemplo, **roteadores baseados em SOAP ou pontes**) que são necessários para que as mensagens fluam entre os pontos de extremidade. **Sessões confiáveis** usam uma janela de transferência na memória para falhas de nível de mensagem **SOAP** e restabelecer as conexões no caso de falhas de transporte.

**Sessões confiáveis** fornecem transferências de mensagens confiáveis de baixa latência. Eles fornecem transferência confiável de mensagens **SOAP** sobre quaisquer **proxies ou intermediários**, equivalente ao que o **TCP** fornece para pacotes em **pontes IP**.

# Sessões confiáveis no RM

## Ganhos com a implementação

Com a implementação das **sessões confiáveis** no **RM**, a aplicação estará preparada para trabalhar com **Buffer** no envio de pacotes e de **manter a conexão de um serviço viva** por mais tempo para reaproveitar as novas chamadas. Desta forma, evita-se novos **handshakes** e aspira-se um ganho de performance em cenários onde a comunicação do client com o server tenha uma **latência muito alta**.

## Configuração

Adicionar a tag **EnableReliableConnection** tanto no arquivo de configuração do client **(RM.exe.config),** quanto no arquivo de configuração do host **(RM.Host.exe)**.

## Versões do RM disponíveis

Está disponível no RM o uso de sessões confiáveis **(Nativas do serviço WCF)** nas versões:

* 12.1.22
* 12.1.23

## Sessão confiável ativada VS Sessão confiável desativada

Iremos mostrar agora a diferença de comportamento do sistema quando a sessão confiável está ativada e quando ela está desativada.

### Sessão confiável desativada

A sessão confiável estará desativada quando:

* Não existir a tag **EnableReliableConnection** nos arquivos de configuração**RM.exe.config** e **RM.Host.exe.config**.
* A tag **EnableReliableConnection**estiver presente nos arquivos de configuração do client e host, porém com o valor **false**.

Havendo algum problema de comunicação entre o client e o server, o sistema levantará uma exceção e apresentará uma tela como a apresentada abaixo:

Essa mensagem irá se apresentar enquanto o lado client não conseguir se comunicar com o lado server. Ao se restabelecer a comunicação, o sistema voltará a funcionar corretamente.

### Sessão confiável ativada

A sessão confiável estará ativada quando:

* A tag **EnableReliableConnection**não estiver presente, ou seja, por padrão o**reliable connection**estará ativado.
* A tag **EnableReliableConnection**estiver presente nos arquivos de configuração do client e host com o valor **true**.

Havendo algum problema de comunicação entre o client e o server, o sistema irá tentar durante um intervalo de tempo manter a conexão ou restabelecê-la automaticamente. Conseguindo restabelecer a comunicação, o sistema voltará a funcionar corretamente.

Alerta

Ocorrendo queda do host, poderá haver congelamento da aplicação. Caso aconteça o congelamento, tente novamente, reiniciando o host e a aplicação. Caso o erro persista entre em contato com o administrador do sistema.
