---
content_hash: 842c598ce4975cc34a0dfd173c4cc29d9152bad24a688ebcaa35aa026ec832e2
fetched_at: '2026-07-02T19:24:29.367097+00:00'
page_id: '865430155'
product: protheus
source: tdn-tec
title: Monitoramento dos Servidores
type: documentation
url: https://tdn.totvs.com/display/tec/Monitoramento+dos+Servidores
version: 2
---

O Broker para Smartclient Desktop utiliza por padrão o "monitoramento ativo": o broker está permanentemente conectado aos servidores configurados, que a cada 5 segundos enviam ao broker informações sobre o consumo de recursos pelos servidores: memória, usuários do ERP, threads do ERP, e consumo de cpu (da máquina onde está o servidor).

Até as versões 20.3.2.x o Broker HTTP utiliza o "monitoramento por conexão": a cada 1 minuto o broker abre uma conexão com cada servidor configurado, para verifica se está ativo. Os servidores que não respondem ao pedido de conexão são colocados em "quarentena", isto é, o broker não redireciona novas conexões de clientes para estes servidores.

A partir da versão 24.3.0.0 o Broker HTTP também passa a utilizar o monitoramento ativo.

Importante: o monitoramento ativo funciona apenas com servidores que utilizam a "porta multi protocolo" para acesso aos seus serviços pelo Smartclient (tanto Smartclient Desktop quanto Smartclient HTML Webapp).

=/=
