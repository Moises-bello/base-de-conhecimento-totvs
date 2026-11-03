---
content_hash: c295069f10e82376fa7165c06dd386bd4a44035d11bd8bb674b7e5c79a83ba88
fetched_at: '2026-07-02T19:24:25.082714+00:00'
page_id: '497457031'
product: protheus
source: tdn-tec
title: Seção [BTMonitor] - Chave LicenseServerECBehavior
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=497457031
version: 2
---

Define o comportamento das ECs geradas a partir das mensagens enviadas ao License Server.

## Valores válidos

| Valor | Descrição |
| --- | --- |
| 0 (Padrão) ou diferente das opções abaixo | Caso exista BT corrente, tenta adicionar as ECs geradas a partir das mensagens do License Server nesta BT corrente;  caso não exista BT corrente, **não cria BTs específicas** para mensagens enviadas ao License Server **e perde as ECs correspondentes.** |
| 1 | Caso exista BT corrente, tenta adicionar as ECs geradas a partir das mensagens do License Server nesta BT corrente;  caso não exista BT corrente, **cria BTs específicas** para mensagens enviadas ao License Server **e as associam às ECs correspondentes.** |

## Observações

* Caso sejam criadas, as BTs específicas dependem dos tipos das mensagens enviadas ao License Server:

  | Tipo da mensagem | Nome da BT criada |
  | --- | --- |
  | Conexão com o License Server | BT\_LICENSE\_SERVER\_CONNECT |
  | Todas as outras | BT\_LICENSE\_SERVER\_CALLPROC |

## Exemplo

Caso exista BT corrente, tenta adicionar as ECs geradas a partir das mensagens do License Server nesta BT corrente; caso não exista BT corrente, **não cria BTs específicas** para mensagens enviadas ao License Server **e perde as ECs correspondentes**:

## Abrangência

Builds [17.3.0.11](http://tdn.totvs.com/display/tec/Application+Server+-+17.3.0.11).

## Veja também
