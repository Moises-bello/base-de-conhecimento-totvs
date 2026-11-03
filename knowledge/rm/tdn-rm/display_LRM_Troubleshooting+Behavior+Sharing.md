---
content_hash: c361aeebc8f9b1e2e6c41fb9b50d196bb69cd1f9bb2e97f891a0c5508d9e7d4c
fetched_at: '2026-06-29T00:05:52.845129+00:00'
page_id: '1060235988'
product: rm
source: tdn-rm
title: Troubleshooting Behavior Sharing
type: documentation
url: https://tdn.totvs.com/display/LRM/Troubleshooting+Behavior+Sharing
version: 3
---

# Índice

---

2Índice

# Análise de problemas conhecidos

---

Análises a serem feitas de erros e possíveis soluções para problemas específicos sobre a integração Behavior Sharing.

Conforme situações forem encontradas, elas serão adicionadas nesta documentação. 

## Mensagens não estão sendo lidas

Caso as mensagens não estejam sendo lidas da fila do SmartLink, é provável que haja algum problema na integração como um todo.

Se tudo estiver conforme os padrões esperados, também é possível que haja algum problema na plataforma.

## Mensagens foram lidas mas não houveram respostas

Caso seja possível identificar a leitura das mensagens da fila através do SmartLink, mas não houve resposta, fazer as análises a seguir:

### Query para verificar mensagens não executadas

sql

Nesta tabela são salvas as mensagens pendentes de ação. Tanto as mensagens baixadas mas ainda não executadas, quanto as mensagens executadas mas ainda não enviadas. Logo, as mensagens não devem ficar por muito tempo aqui, somente o tempo da execução do NotifyServer.

### Query para verificar histórico de mensagens

sql

Já nesta tabela, são salvas as mensagens já executadas. Se as mensagens solicitadas estão aqui, quer dizer que foram enviadas corretamente do nosso lado. Neste caso, o mais provável é que o produto (aplicativo do TotvsApps) não esteja tratando as respostas corretamente.

## Informações gerais

### Legendas dos campos da tabela de Behavior Sharing

* + **STATUS:** o status de execução.
    - 0 significa que ainda está pendente
    - 1 significa que executou com erro
    - 2 significa que executou com sucesso
  + **TYPEMESSAGE:** o tipo da mensagem.
    - 0 significa que é uma mensagem para ser enviada ao SmartLink (upstream)
    - 1 significa que é uma mensagem baixada (downstream)
    - 2 significa que é uma mensagem enviada com o status de erro (upstream DLQ)
    - 3 significa que a mensagem foi reenviada para a fila, para ser processada novamente (upstream requeue)
  + **DATA:** os dados da mensagem (seja recebida ou enviada).
