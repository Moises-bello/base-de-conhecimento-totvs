---
content_hash: 03f69848322dc4c0e69bf139d45d691c237b00ef3e5fe60de42b70e6252c78a4
fetched_at: '2026-06-29T00:10:15.043094+00:00'
page_id: '463799964'
product: rm
source: tdn-rm
title: Reliable Session (Reliable Connection) - Documento Técnico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=463799964
version: 41
---

# Associações (Bindings)

As associações especificam o mecanismo de comunicação a ser usado ao se comunicar com um ponto de extremidade e também indicam como se conectar a esse ponto de extremidade. Uma associação contém os seguintes elementos:

* A **pilha do protocolo**, que determina a segurança, a confiabilidade e as configurações de fluxo de contexto a serem usadas para as mensagens que são enviadas ao ponto de extremidade.
* O **transporte** determina o protocolo de transporte subjacente a ser usado ao enviar mensagens para o ponto de extremidade, por exemplo, TCP ou HTTP.
* A **codificação** determina a codificação de transmissão a ser usada para as mensagens que são enviadas para o ponto de extremidade. Por exemplo, texto/XML, binário ou MTOM (Mecanismo de Otimização de Transmissão de Mensagem).

Na imagem abaixo estão apresentadas quatro associações que o RM dá suporte e suas caracteristicas.

# Canais do WCF (Channels)

Os **elementos de associação (Binding Elements)** lêem as configurações tanto do lado client quanto do lado server e montam a **Fábrica de Canais (Channel Factory)** e o**Ouvinte de Canais (Channel Listener)** respectivamente. A ordem recomendada para os elementos de associação é:

1. Fluxo de Transações (TransactionFlow),
2. Sessões Confiáveis (ReliableSession),
3. Segurança,
4. CompositeDuplex,
5. OneWay,
6. StreamSecurity,
7. Codificação de Mensagem (MessageEncoding)
8. Transporte.

A imagem abaixo ilustra o relacionamento entre o ChannelListener e o ChannelFactory no WCF. O ouvinte de canais cria o canal no lado server e a fábrica de canais cria no lado client.

A forma de comunicação adotada é a Request-Reply (Requisição-Resposta). Essa forma de comunicação faz com que cada parte da comunicação veja o canal. O **cliente usa o canal para enviar requisições**, então é natural que ele o veja como um **IRequestChannel.** Do outro lado, o servidor recebe as requisições pelo canal e quer usá-lo para enviar de volta ao cliente, então ele o vê como um **IReplyChannel**.

# Sessões Confiáveis no RM

Nas versões 12.1.22 (ou superiores) do RM foi habilitado a funcionalidade de **Sessão Confiável**,que fornece transferência confiável de ponta a ponta de mensagens entre uma origem e um destino usando o protocolo **WS-Reability** de mensagens, independentemente do número ou tipo de intermediários que separam os pontos de extremidade de mensagens (origem e destino). Isso inclui qualquer intermediário de transporte que não usa **SOAP** (por exemplo, **proxies HTTP**) ou intermediários que usam o**SOAP** (por exemplo,**roteadores baseados em SOAP ou pontes**) que são necessários para que as mensagens fluam entre os pontos de extremidade. **Sessões confiáveis** usam uma janela de transferência na memória para falhas de nível de mensagem **SOAP** e restabelecer as conexões no caso de falhas de transporte.

Nas versões 12.1.22 e 12.1.23 foi habilitado a sessão confiável nativa do WCF, enquanto que na 12.1.24 (ou superiores), uma nova sessão confiável customizada foi implementada, com o objetivo de não só manter a conexão ativa, mas redirecionar as requisições para diferentes hosts, se caso existirem e estiverem ativos.

Na imagem abaixo é mostrado um diagrama de como a requisição é feita entre o cliente e o servidor, mostra também a resiliência entre eles, ou seja, caso uma conexão seja perdida, o pacote é remontado e enviado à um host aleatório, que poderá ser o mesmo host da primeira requisição, caso esteja ativo, ou outro host disponível e habilitado para receber a requisição e processá-la.

 

# Mensagem do RM

Caso haja alguma falha de comunicação, e não seja possível obter uma resposta o RM irá apresentar a seguinte mensagem:

**Estamos com dificuldade em comunicar com o Host. Aguarde enquanto tentamos recuperar...**
