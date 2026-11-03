---
content_hash: ad30cf38fd18e25abe7d4670df110f5169603187a25b5fcb38c506ca5e67aa31
fetched_at: '2026-06-29T00:08:42.163431+00:00'
page_id: '287058176'
product: rm
source: tdn-rm
title: Caching
type: documentation
url: https://tdn.totvs.com/display/LRM/Caching
version: 2
---

Disponibilizado no projeto **Snowden.Utils** temos uma interface para implementação de cache em soluções do lado do cliente do Snowden.

# A Interface

A interface **Snowden.Utils.Cache.ICache<TKey, TValue>** é então utilizada nas soluções que disponibilizam ferramentas de cache para suas operações.

Esta interface então recebe dois tipos genericos na sua criação, sendo:

* TKey que é a chave de armazenamento do objeto
* TValue que é o valor (tipo) armazenado

# Métodos

## TValue Get(TKey key)

Método utilizado para capturar informações do cache, este irá retornar o objeto mantido em cache para a chave informada. Esta operação já deve considerar a invalidação do cache armazenado.

Parâmetros:

* TKey key: Chave do item procurado

## void Set(TKey key, TValue value, int ttl);

Método utilizado para guardar um novo item no cache, este fará o armazenamento dos itens os atualizando caso necessário. este método é sempre chamado pelas ferramentas que habilitam cache, mesmo que o ttl (tempo de vida) seja informado como 0.

Parâmetros:

* TKey key: Chave do item
* TValue value: Valor do item
* int ttl: Tempo de vida em segundos que deve ser mantido em cache.

## void Remove(TKey key);

Remove um item de cache do repositório, este método é idempotente e não deve tratar se o item existe ou não, apenas garantir sua remoção.

Parâmetros:

* TKey key: Chave do item

## void Clear();

Limpar todos os registros do cache.
