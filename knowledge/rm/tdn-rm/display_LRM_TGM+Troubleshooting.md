---
content_hash: 69d9d9b5143849961bd5c26098e3d1b0c7c6170d6e83030d27b0bc3bb9d0abdc
fetched_at: '2026-06-29T00:10:21.260500+00:00'
page_id: '490971201'
product: rm
source: tdn-rm
title: TGM Troubleshooting
type: documentation
url: https://tdn.totvs.com/display/LRM/TGM+Troubleshooting
version: 81
---

2

## Serviço não inicia

### Problema

Após instalar o serviço do TGM, não é possível iniciar a execução do mesmo.

Ao verificar os Logs do Visualizador de Eventos do Windows são verificados os seguintes erros:

* Tempo limite esgotado (30000 milissegundos) ao aguardar a conexão do serviço Totvs Gateway Manager.

* Não foi possível iniciar o serviço Totvs Gateway Manager devido ao seguinte erro:   
  O serviço não respondeu à requisição de início ou controle em tempo hábil.

### Possível causa

Um possível problema que pode gerar esse tipo de erro é que o .Net Core na versão esperada pelo sistema não esteja instalada.

### Solução

Instalar a versão designada para que o TGM funcione.

* Verifique no arquivo TOTVSGatewayManager.runtimeconfig.json a chave de caminho "runtimeOptions":"framework":"version" para descobrir a versão necessária para a instalação.

#fffLink para download

<https://dotnet.microsoft.com/download/dotnet-core>

### Artigos relacionados

Os artigos relacionados aparecem aqui baseados nos rótulos que você selecionar. Clique para editar a macro e adicionar ou alterar os rótulos.

false5LRMfalsemodifiedtruepagelabel in ("tgm","totvsgatewaymanager","gateway") and type = "page" and space = "LRM"tgm totvsgatewaymanager gateway

true

|  |  |
| --- | --- |
| Ocorrências relacionadas |  |

---

## Usuário NetworkService

### Problema

Serviço do TGM não inicia utilizando o usuário NetworkService.

### Solução

Para subir o serviço utilizando o **NetworkService**é necessário que o usuário **NetworkService**possua permissão no registro do windows: [HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog\Application]

Para atribuir a permissão acesse regedit no executar do windows( Crt + R)

Localize o registro [HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog], e clique em **Permissões**.

Clique em Adicionar

Clique em Locais

Selecione a máquina local

Adicione o usuário **SERVIÇO DE REDE**

Atenção

Deve-se utilizar o usuário **SERVIÇO DE REDE** com máquina com o sistema operacional em **Português**.

Em sistema operacional em **Inglês** deve ser utilizar o usuário **NetworkService**.

Marque os itens Permitir e clique em Aplicar.

Clique em iniciar o serviço:

Atenção

No exemplo acima foi dado como exemplo de Usuário o **NetworkService** esta solução serve para todos os usuários que não conseguirem iniciar o serviço do TGM com um usuário específico.

---

## Serviço não inicializa automaticamente

### Problema

Após instalar o TGM utilizando o instalador, o serviço não inicializa automaticamente.

Erro no Event Viewer:

### Solução

Remover o serviço criado utilizando o CMD como administrador:

            sc delete TotvsGatewayManager

Utilizar o RM.Host.ServiceManager como Administrador

Instalar o serviço informando a conta de Sistema: LocalSystem

Após iniciar o serviço:
