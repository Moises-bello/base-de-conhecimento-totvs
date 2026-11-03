---
content_hash: 0a8703540bc817d3f6989b5a074b673aa35f149f30517f5561a9d52be9fa6ce8
fetched_at: '2026-06-28T21:35:19.093177+00:00'
page_id: '190515357'
product: fluig
source: tdn-fluig
title: ESB - Alto consumo de memoria e CPU
type: documentation
url: https://tdn.totvs.com/display/fluig/ESB+-+Alto+consumo+de+memoria+e+CPU
version: 4
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**TOTVS ESB

# Ocorrência

Consumo excessivo de memória e CPU pelo Java do serviço do TOTVS ESB.

# Causa

O montante de memória em megabytes que a JVM deve alocar não é suficiente.

# Solução

Alocar mais memória para o TOTVS ESB pelo campo Maximum Memory.

Confira o passo a passo para configurar a memoria do TOTVS ESB.

0.5falsesamplesfadetrue1Passo 1

* Entrar no TOTVS Developer Studio.

2Passo 2

* Entrar no TOTVS ESB servers e escolher o ESB desejado.

3Passo 3

* Na aba System Properties, selecionar as opções de Memory.

4Passo 4

* Configurar o uso de memória do TOTVS ESB.

| Campo | Descrição |
| --- | --- |
| Maximum Memory (MB) | Tamanho máximo em megabytes do pool de alocação de memória. |
| Initial Memory (MB) | Tamanho inicial em megabytes do pool de alocação de memória. |
| Allocation Memory by Thread (MB) | Tamanho em kilobytes de alocação de memória por thread. |
