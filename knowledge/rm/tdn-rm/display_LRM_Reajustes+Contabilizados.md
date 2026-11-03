---
content_hash: 08d76707e3d4c32a9a8d78b0fe5eca421495bedfc7f187f338e6c4e9eb967b12
fetched_at: '2026-06-29T00:10:26.080217+00:00'
page_id: '511541789'
product: rm
source: tdn-rm
title: Reajustes Contabilizados
type: documentation
url: https://tdn.totvs.com/display/LRM/Reajustes+Contabilizados
version: 5
---

Este menu foi criado para que possa ser visto todos os **reajustes** de venda que foram contabilizados. Através deste menu, é possível **recontabilizar** o reajuste, **estornar** a contabilização.

Para visualizar os reajustes que criaram a contabilização é necessário ir a aba 'Contabilidade' e posteriormente acessar a opção Reajustes Contabilizados.

Importante:

* É possível visualizar as informações contábeis através do menu Anexos>>Consultar Operação Contábil Reajuste.
* Na versões superiores a 12.1.2506 temos os log dos reajustes contabilizados, justamente para guardar os id operações que foram estornados ou excluídos.

**Processo de Contabilização / Estorno**

As contabilizações de reajuste poderão ser feitas pelo Processo de contabilização/estorno. As seguintes opções poderão ser executadas:

Será possível **Contabilizar o Reajuste**, **Estornar o Reajuste**, **Recontabilizar (Estornar e Contabilizar)**.

A **data de contabilização** poderá ser a data de referência do reajuste ou uma data específica escolhida pelo usuário.

As possíveis entidades do TIN poderão ser contabilizadas:

* **Venda**
* **Entrega de Chaves**
* **Aditivo**
* **Distrato**
* **Reajuste**

A baixa segue sendo reajustada da mesma forma.

**Parâmetros**

Foram criados os seguintes parâmetros que atuam na contabilização assíncrona:

Para habilitar a contabilização assíncrona o primeiro parâmetro deve ser habilitado.

O segundo parâmetro é para que o estorno dos reajustes sejam feitos de forma automática, caso o reajuste seja feita em uma data retroativa.
