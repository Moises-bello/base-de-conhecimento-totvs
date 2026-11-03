---
content_hash: 1baa860829a6c6b71b6804f74c332625a61829180e7a37b0f54fc4fcedc2a772
fetched_at: '2026-06-28T21:35:27.910839+00:00'
page_id: '6066533'
product: fluig
source: tdn-fluig
title: System Properties
type: documentation
url: https://tdn.totvs.com/display/fluig/System+Properties
version: 12
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

A aba System Properties permite configurar as propriedades do sistema Fluig ESB. As propriedades do sistema são divididas em 4 (quatro) grupos que serão discriminados a seguir: General, Proxy Settings, Memory, ActiveMQ.

### General

Permite configurar propriedades gerais do Fluig ESB.

| Campo | Descrição |
| --- | --- |
| Reprocess Interval | Intervalo para reprocessamento de mensagens no Fluig ESB. |
| ESB Port | Porta de conexão do Fluig ESB. |
| JMX Port | Porta de conexão para monitor e configurar Fluig ESB remotamente. |
| E-mail Server | Servidor SMTP para o envio de e-mails. |
| Requires SMTP Authentication | Quando selecionado habilita os campos de usuário e senha para serem inseridas informações de autenticação SMTP (se forem requeridas pelo servidor). |
| User Name | Nome do usuário para autenticação SMTP. |
| Password | Senha do usuário para autenticação SMTP. |
| Max Connections | Número máximo de conexões com o banco do Fluig ESB para o envio e recebimento de mensagens. |

### Proxy Settings

Permite configurar um servidor de Proxy para estabelecer conexões com o Fluig ESB.

| Campo | Descrição |
| --- | --- |
| Proxy Enabled | Habilita o servidor proxy. |
| Proxy Host | Nome do servidor Proxy. |
| Proxy Port | Número da porta do servidor proxy. |
| Proxy Domain | Domínio do servidor proxy. |
| SSL | Quando selecionado, indica que será utilizado um protocolo de segurança na comunicação com o servidor proxy. |
| Requires Authentication | Habilita os campos de usuário e senha para a autenticação de usuário na conexão com o servidor proxy. |
| User Name | Nome do usuário que será utilizado na autenticação. |
| Password | Simula um teste de conexão com a URL digitada no campo ao lado do botão, para validar as configurações de Proxy adicionadas anteriormente. |
| Test Proxy | Simula um teste de conexão com a URL digitada no campo ao lado do botão, para validar as configurações adicionadas anteriormente. |

### Memory

Permite configurar o uso de memória do Fluig ESB e também do seu recurso de monitoramento de mensagens (monitor do Fluig ESB).

| Campo | Descrição |
| --- | --- |
| Initial Memory | Tamanho inicial em megabytes do pool de alocação de memória. |
| Maximum Memory | Tamanho máximo em megabytes do pool de alocação de memória. |
| Allocation Memory by Thread | Tamanho em kilobytes de alocação de memória por thread. |

### ActiveMQ

Permite configurar um servidor interno ou externo para estabelecer conexões com o recurso de JMS do Fluig ESB.

| Campo | Descrição |
| --- | --- |
| Queue Size | Tamanho máximo em megabytes utilizado como referência para transferência das mensagens que são trafegadas pelo Fluig ESB por rotas realizadas. A configuração não expressa o limite do tamanho da mensagem a ser trafegada, é somente uma referência que será adotada. |
| Unlimited | Quando habilitado indica que o tamanho como referência para mensagens trafegadas é ilimitado. |
| Keep the queue in database | A flag deve ser marcada quando o Fluig ESB está configurado para processar uma mensagem robusta. Desta maneira não há sobrecarga durante o processamento da rota. |
