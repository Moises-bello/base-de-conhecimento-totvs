---
content_hash: dd2aaad0344e777722d20286a476dc63e21ba5e039b1f2051b842291a4ba5713
fetched_at: '2026-07-02T19:24:28.888832+00:00'
page_id: '865427746'
product: protheus
source: tdn-tec
title: Balanceamento por Recursos (Broker HTTP)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=865427746
version: 3
---

Até as versões 20.3.2.x o Broker HTTP utiliza por padrão o "balanceamento por sessões": cada usuário que se conecta a um servidor através do broker conta como uma sessão associada ao servidor utilizado. Quando um novo usuário se conecta a um servidor através do broker, este o redireciona para o servidor com menos número de sessões associadas.

A partir da versão 24.3.0.0 o Broker HTTP utiliza por padrão o "balanceamento por recursos": o broker está permanentemente conectado aos servidores configurados, que a cada 5 segundos enviam ao broker informações sobre o consumo de recursos pelos servidores: memória, usuários do ERP, threads do ERP, e consumo de cpu (da máquina onde está o servidor). Cada um desses recursos pode ser utilizado como critério único de balanceamento. O critério de balanceamento padrão é "memória": quando um novo usuário se conecta a um servidor através do broker, este o redireciona para o servidor com menor consumo de memória.

O Balanceamento por Recursos funciona em conjunto com o Monitoramento Ativo. Estas 2 funcionalidades só funcionam com servidores que utilizam a "porta multi protocolo", especialmente o Smartclient HTML Webapp.

**Importante**: quando o balanceamento for feito para outros tipos de aplicação web que não utilizam a porta multi protocolo, será necessário configurar explicitamente o "monitoramento por conexão" na configuração do broker, que também vai desabilitar o balanceamento por recursos, e voltar a utilizar o balanceamento por sessões:

    [BALANCE\_HTTP]  
    ....  
    ....  
    MONITORING\_TYPE = CONNECTION  
    ....  
    ....

Caso isso não seja feito, os servidores serão colocados em "quarentena", ficando indisponíveis para uso.
