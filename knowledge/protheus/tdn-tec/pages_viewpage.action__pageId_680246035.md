---
content_hash: d5148c61134c4a5058942b2892133add5724827c18b2c73e65f55c265e3529f2
fetched_at: '2026-07-02T19:24:27.738805+00:00'
page_id: '680246035'
product: protheus
source: tdn-tec
title: Seção NetTest (SCPing)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=680246035
version: 10
---

## Seção [NetTest]

```
Configurações gerais de NetTest do TOTVS | SmartClient e Application Server.
```

Verificar a documentação em .

**\*Disponível apenas em versões iguais ou superiores a 20.3.1.0 do Smartclient/Appserver**

**\*Disponível apenas para Smartclient Desktop**

**\*As configurações feitas pelo appserver.ini são prioritárias e para todos os Smartclients que nele se conectarem e irão sobrescrever as configurações do lado do smartclient.ini. Utilize as configurações no smartclient.ini, quando apenas uma estação específica precisa da análise de latência.**

A seguir, as chaves relacionadas a configuração da seção [NetTest] (Clique em cada uma delas para mais detalhes):

| Chave | Descrição |
| --- | --- |
|  | Se deve ligar ou não o controle do NetTest no Smartclient. Padrão = 0 (desligado) |
|  | Define se deve gerar um aviso (warning) caso a latência passe do valor configurado na chave "LatencyWarning". Padrão = 1 (ligado). |
|  | Latência máxima (em milissegundos) que deve gerar um aviso ao usuário. Padrão = 100 (100 milissegundos) |
|  | Intervalo (em milissegundos) entre um Ping e outro que o Smartclient irá realizar, valor mínimo é 100ms. Padrão = 1000 (1 segundo) |
|  | Número máximo do resultado de pings que o Smartclient irá manter em memória. Padrão = 1000  Em números, no padrão isso gera 0,15mb (na memória RAM) e salva os últimos 16 minutos com um ping a cada 1 segundo. |
|  | Número máximo de amostrar que o gráfico irá plotar. Padrão = 100 |
|  | Se deve ou não registrar o atalho Ctrl-Alt-N para abrir a tela do NetTest (única forma de abrir a tela caso não tenha ocorrido um aviso de latência). Padrão = 1 (ligado). |
|  | Número de ciclos que deve ser analisado para considerar um problema de alta latência. Padrão = 60. |
|  | Porcentagem de ciclos acima do LatencyWarning para que o usuário receba o aviso de problema devido a alta latência. Padrão = 10. |

BLOCK

Seção NetTest
