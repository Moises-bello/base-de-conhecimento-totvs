---
content_hash: 759131b39aa2d8858c7825c83774975833980a429816002c8114b4e611b6fd7b
fetched_at: '2026-07-02T19:24:19.577787+00:00'
page_id: '223172658'
product: protheus
source: tdn-tec
title: TC_ALTER FAILED on file... Table DATA or STRUCTURE should be INVALID or CORRUPTED
type: documentation
url: https://tdn.totvs.com/display/tec/TC_ALTER+FAILED+on+file...+Table+DATA+or+STRUCTURE+should+be+INVALID+or+CORRUPTED
version: 2
---

TC\_ALTER FAILED on file... Table DATA or STRUCTURE should be INVALID or CORRUPTED

Durante a operação de alteração da estrutura de uma tabela, caso alguma de suas etapas intermediárias não for concluída em função de uma estrutura incompleta ou da corrupção de seus dados, é registrado a mensagem `TC_ALTER FAILED on file [<table>]. Table DATA or STRUCTURE should be INVALID or CORRUPTED`.

## Causa

A causa dessa ocorrência pode ser observada nos logs do true e comumente está relacionada a alguma restrição implicada pelo uso de *views*, *triggers*, *statistics* ou qualquer outro recurso que porventura possa impedir a operação.

## Observações

* É uma premissa que a tabela a ser alterada não possua dependências e/ou elementos externos que impeçam uma alteração estrutural.

Muitas vezes os DBAs inserem *triggers* e *statistics* diretamente no SGBD. Essas operações são válidas contanto que não alterem o comportamento esperado pela aplicação e regra de negócio, uma vez que as mesmas deverão ser removidas manualmente e reaplicadas após a alteração estrutural estiver completa

## Exemplo

No exemplo a seguir a coluna está relacionada a uma *statistics* e impede a operação de alteração.
