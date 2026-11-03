---
content_hash: 7ef395276b5636fc851416555ec305c59badcf5a454a92658e0de54b9f0942fd
fetched_at: '2026-07-02T19:24:21.307275+00:00'
page_id: '266972628'
product: protheus
source: tdn-tec
title: Problem with DELTMPF Semaphore
type: documentation
url: https://tdn.totvs.com/display/tec/Problem+with+DELTMPF+Semaphore
version: 2
---

Problem with DELTMPF Semaphore

|  |  |
| --- | --- |
| Situação | Problem with DELTMPF Semaphore |
| Ocorrência | Ao tentar apagar um arquivo travado por outra rotina usando FErase, era possível apagá-lo |
| Correção | A função FErase irá utilizar o lockserver e se não conseguir acesso exclusivo ao arquivo, retorna erro e não deleta o mesmo. |
| Informações adicionais | * Referente ao chamado: SSIM-408 * Referente à ocorrência: não há ocorrência associada * Disponível em builds superiores a 7.00.131227A - 1.0.3 |
