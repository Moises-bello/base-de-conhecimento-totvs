---
content_hash: 3ff3be1c0d16cb04e70fc1002ca67ccfbe023ce2edcc1da3eca92a7f78aae0c1
fetched_at: '2026-07-02T19:24:22.556936+00:00'
page_id: '270910540'
product: protheus
source: tdn-tec
title: DBAccess - Seção [General], chave DBWarnings
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270910540
version: 5
---

Ativa as mensagens de warnings de Banco de Dados no dbaconsole.log do ambiente.

Esta configuração está disponível no true com build superior a 20161016.

## Valores válidos

| Valor | Descrição |
| --- | --- |
| 0 (**Padrão**) | Desabilitado para visualizar as mensagens |
| 1 | Habilitado para visualizar as mensagens |

## Observações

* Será necessário reiniciar o true para assumir a nova configuração
* Todas as mensagens de warnings serão visualizadas no console (dbconsole.log)
* Usando na seção [General], será habilitado para todos as configurações de Ambiente/Conexão.

## Exemplos

text
