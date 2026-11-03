---
content_hash: 66fc2090ffb4f5c3db4d8d90180aad142b4c0fc878b0391f2027debb9b1f0025
fetched_at: '2026-06-29T00:10:14.389679+00:00'
page_id: '458780850'
product: rm
source: tdn-rm
title: Reliable Session (Reliable Connection)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=458780850
version: 18
---

# Introdução à sessões confiáveis

**Sessões confiáveis** fornecem transferência confiável de ponta a ponta de mensagens entre uma origem e um destino usando o protocolo **[WS-Reability](http://docs.oasis-open.org/wsrm/ws-reliability/v1.1/wsrm-ws_reliability-1.1-spec-os.pdf)** de mensagens, independentemente do número ou tipo de intermediários que separam os pontos de extremidade de mensagens (origem e destino). Isso inclui qualquer intermediário de transporte que não usa **SOAP** (por exemplo, **proxies HTTP**) ou intermediários que usam o **SOAP** (por exemplo, **roteadores baseados em SOAP ou pontes**) que são necessários para que as mensagens fluam entre os pontos de extremidade. **Sessões confiáveis** usam uma janela de transferência na memória para falhas de nível de mensagem **SOAP** e restabelecer as conexões no caso de falhas de transporte.

**Sessões confiáveis** fornecem transferências de mensagens confiáveis de baixa latência. Eles fornecem transferência confiável de mensagens **SOAP** sobre quaisquer **proxies ou intermediários**, equivalente ao que o **TCP** fornece para pacotes em **pontes IP**.

# Sessões confiáveis no RM

## Ganhos com a implementação

Com a implementação das **sessões confiáveis** no **RM**, ele estará preparado para trabalhar com **Buffer** no envio de pacotes e de **manter a conexão de um serviço viva** por mais tempo para reaproveitar as novas chamadas. Desta forma, evita-se novos **handshakes** e aspira-se um ganho de performance em cenários onde a comunicação do client com o server tenha uma **latência muito alta**.

## Configuração

Adicionar a tag **EnableReliableConnection** no arquivo de configuração do client **(RM.exe.config)**.

## Versões do RM disponíveis

Está disponível no RM o uso de sessões confiáveis **(Reliable Connection)** nas versões:

* 12.1.24

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

Havendo algum problema de comunicação entre o client e o server, o sistema irá tentar durante um intervalo de tempo manter a conexão ou restabelecê-la automaticamente. Conseguindo restabelecer a comunicação o sistema voltará a funcionar corretamente.

A sessão confiável a partir da versão 12.1.24 do RM, permite que a resiliência da conexão entre client e server, utilize um ambiente de múltiplos hosts, onde caso a conexão não consiga ser mantida ou restabelecida com um host, um outro host poderá ser utilizado para receber dali em diante as requisições client, ou seja, assumir o papel do host cuja conexão foi interrompida.

## Diferenças entre versões 12.1.23 e 12.1.24

A maior diferença entre as duas versões é que na versão do Reliable Nativo do WCF, existe afinidade com o Host, ou seja, caso haja falha na conexão com o Host, ele irá esperar até que o mesmo responda, para prosseguir a troca de mensagens entre client e server, mesmo que um outro host seja ativado na rede, já no Reliable da 12.1.24, caso haja falha na comunicação com o host ele poderá remontar a mensagem e enviá-la a um outro host.

### Reliable Nativo WCF 12.1.23

### Reliable 12.1.24

# Reliable com TGM

Quando utilizado Reliable com TGM e houver uma queda do host, a tela de problemas de conexão (mensagem: aguarde estamos tendo dificuldades) não será apresentada. Será apresentado erro depois do Timeout.
