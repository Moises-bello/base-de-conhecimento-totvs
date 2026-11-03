---
content_hash: d6b65db5e5ebb002e15bb21d02406c36467ac2e03d1bb1310c2044f6e893f98f
fetched_at: '2026-07-02T19:24:28.884941+00:00'
page_id: '865427250'
product: protheus
source: tdn-tec
title: Monitoramento dos Servidores (Broker HTTP)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=865427250
version: 10
---

Até as versões 20.3.2.x o Broker HTTP utiliza o "monitoramento por conexão": a cada 1 minuto o broker abre uma conexão com cada servidor configurado, para verifica se está ativo. Os servidores que não respondem ao pedido de conexão são colocados em "quarentena", isto é, o broker não redireciona novas conexões de clientes para estes servidores.

A partir da versão 24.3.0.0 o Broker HTTP utiliza por padrão o "monitoramento ativo": o broker está permanentemente conectado aos servidores configurados, que a cada 5 segundos enviam ao broker informações sobre o consumo de recursos pelos servidores: memória, usuários do ERP, threads do ERP, e consumo de cpu (da máquina onde está o servidor).

O monitoramento ativo funciona com servidores que utilizam a "porta multi protocolo", especialmente o Smartclient HTML Webapp.

**Importante**: quando o balanceamento for feito para outros tipos de aplicação web que não utilizam a porta multi protocolo, será necessário configurar explicitamente o "monitoramento por conexão" na configuração do broker:

    [BALANCE\_HTTP]  
    ....  
    ....  
    MONITORING\_TYPE = CONNECTION  
    ....  
    ....

Caso isso não seja feito, os servidores serão colocados em "quarentena", ficando indisponíveis para uso.

|  |
| --- |
|  |
