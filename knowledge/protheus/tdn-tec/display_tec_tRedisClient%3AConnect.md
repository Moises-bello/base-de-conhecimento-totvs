---
content_hash: 593a8f0c97ced1a18b75ad47e41a30961610e9ddd15ed4ce57de242529b69518
fetched_at: '2026-07-02T19:24:24.036806+00:00'
page_id: '454835023'
product: protheus
source: tdn-tec
title: tRedisClient:Connect
type: documentation
url: https://tdn.totvs.com/display/tec/tRedisClient%3AConnect
version: 35
---

Conecta um cliente ao servidor Redis.

## Sintaxe

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência | Default | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| ``` cServer ``` | Caracter | Endereço do servidor Redis na rede | Sim | Não |  |  |
| `nPort` | Inteiro | Porta de rede do servidor | Sim | Não |  |  |
| ``` cParameter ``` | Caracter | Informações para autenticação no servicor | Não | Não | `""` | Se fornecido, deve ser o terceiro parâmetro |

## Retorno

| Nome | Tipo | Descrição | Observações |
| --- | --- | --- | --- |
| ``` oRedisAfter ``` | objeto `tRedisClient` | Cópia do objeto sobre o qual foi feita a chamada de `::Connect`, já afetado pela tentativa de conexão.\* |  |

`*`Isto permite acoplar outros métodos e propriedades à chamada de `::Connect()`  
   Por exemplo,   
`oRedisClient:Connect(cServer, nPort, cAuth):lConnected`

   testará se a conexão foi bem sucedida, sem a necessidade de uma consulta à parte a `::lConnected` sobre o objeto `oRedisClient`.

## Observações

* O método `::Connect()` realiza a conexão a um servidor Redis, de um objeto que apenas foi instanciado através de `::New()`

* Os parâmetros servidor, porta e autenticação permitem a conexão com um servidor remoto (em qualquer ponto da Internet), até mesmo com acesso seguro (ou autenticado) a ele.

* A propriedade `::lConnected` permite detectar se a conexão foi bem sucedida.

* Depois de uma conexão bem sucedida, deve ser feita a desconexão, antes do final do programa, para informar ao servidor Redis que os recursos usados para a conexão não são mais necessários.

## Exemplos

### Exemplo 1 - Informação de todos parâmetros  true

cpptrue

### Exemplo 2 - Omissão de `cAuth` terceiro parâmetro   true

cpptrue  

## Veja também
