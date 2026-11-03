---
content_hash: 56ecfa00c8df7fe4730f205bc47aa611b102f1e4e346252cfd96b9eda59a376b
fetched_at: '2026-06-29T00:09:27.497312+00:00'
page_id: '423938526'
product: rm
source: tdn-rm
title: Reestruturação de Lançamentos por Fato Contábil 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938526
version: 3
---

O processo analisa os Lançamentos/Partidas já cadastrados na base e reorganiza as partidas conforme o período informado, distribuindo as mesmas em novos lançamentos.

A reestruturação irá atender a resolução CFC nº1299/2010, que define as formalidades da Escrituração Contábil Digital - ECD.

Para a reestruturação dos lançamentos os mesmos serão agrupados mediante algumas características que permitam identificar todos os registros que se integram, conforme a regra:

1. Pelo Identificador da Operação (IDOPERACAO, sendo débito = crédito);
2. Pela Chave de Integração (INTEGRACHAVE, sendo débito = crédito);
3. Pelo Código do Histórico Padrão (CODHISTP, sendo débito = crédito);
4. Pelo Número do Documento (DOCUMENTO, sendo débito = crédito).

Além disso os lançamentos devem ser do mesmo sistema de origem.

O processo analisará e aplicará as regras acima à todos os lançamentos do lote zero correspondentes ao período (mês/ano) informado.

**Atenção!**

O processo não poderá ser executado mais de uma vez para mês/ano.

Não serão considerados os lançamentos:

* Lançamentos agrupados;
* Lançamentos gerados pelo processo de transferência de grupos contábeis;
* Lançamento com diferença de débito x crédito.
