---
content_hash: 6c789c3a82d7c2074455e6e5774a8c27dd34ccb3cbdd48a04d52f9535d9e401d
fetched_at: '2026-07-02T19:24:23.469178+00:00'
page_id: '450157051'
product: protheus
source: tdn-tec
title: Seção [RPC], chave onCall - Validação de Clientes RPC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450157051
version: 3
---

Validação de Clientes RPC

A validação de clientes RPC é uma medida opcional de segurança implementada para permitir que o servidor de uma chamada RPC verifique se o solicitante pode ou não executar chamadas RPC.

Através da execução de uma função true, definida pelo usuário e indicada no arquivo de configurações do servidor RPC, é possível criar uma política flexível de permissões de execução de funções via RPC.

A medida de segurança é opcional pois depende da configuração ou não da função de validação. No entanto, uma vez configurada, a validação será executada de maneira obrigatória e a cada chamada de método RPC por parte do cliente, até que o servidor seja reiniciado com validação desabilitada.

## Configuração da Função de Validação

A função de validação de clientes RPC é indicada no arquivo de configuração do servidor RPC na seção , chave .  
 Caso configurada, habilita a validação de clientes RPC; caso não configurada, o cliente RPC é considerado válido por padrão.

## Localização da Função de Validação

A função definida pelo usuário deverá estar no mesmo ambiente (environment) a ser utilizado para execução das tarefas (funções) RPC no servidor, conforme instância da classe  em uso.

## Resultado da Validação

O resultado da validação de um cliente RPC é um valor lógico que depende do resultado bem sucedido da função de validação de clientes RPC.

Caso válido, o cliente RPC estará habilidato a executar chamadas RPC durante o período de latência de sua validação.

Caso não-valido, o cliente RPC não estará habilitado a executar chamadas RPC e a função de validação RPC será executada novamente na próxima requisição RPC do cliente após o período de latência.

## Período de Latência de uma Validação

A validação do cliente RPC é executada a cada chamada de método RPC por parte do cliente, até que o servidor seja reiniciado com validação desabilitada.

No entanto, a execução ou não da função de validação de clientes RPC, quando de uma validação, depende do resultado prévio da função de validação e de quando a validação ocorre em relação ao seu período de latência.

Caso bem sucedida, a função de validação somente será executada novamente após o período de 300 segundos (5 minutos), independente do resultado da validação do cliente RPC.

Durante este período, o resultado da validação do cliente RPC retornado será o mesmo.

Após o período de latência, o resultado da validação expira, e a próxima chamada de método RPC por parte do cliente executará a função de validação novamente e o processo se repete.

Caso mal sucedida, a função de validação será executada novamente quando da chamada de método RPC por parte do cliente.

## Veja também
