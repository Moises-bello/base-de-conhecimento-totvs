---
content_hash: 107265f394347722e425977dc13f5c7d619396de95f43a468bfa991aa1bf80b4
fetched_at: '2026-06-29T00:11:55.475298+00:00'
page_id: '861568560'
product: rm
source: tdn-rm
title: RM Atualizador GetLog
type: documentation
url: https://tdn.totvs.com/display/LRM/RM+Atualizador+GetLog
version: 4
---

**Objetivo da documentação:**

Essa documentação tem como objetivo mostrar um pouco da ferramenta **GetLog** e suas funcionalidades.

**Introdução:**

Essa é uma ferramenta do RM que permite a coleta do último log do RM.Atualizador, ela pode ser encontrada na pasta raiz do RM "**...\CorporeRM\RM.Net\**" com o nome de **RM.Atualizador.GetLog.exe** 

Para iniciar a ferramenta você precisa seguir os passos abaixo

1. Realizar a configuração do arquivo RM.Atualizador.GetLog.exe**.config** de acordo com o config do Rm.Host.exe.config para garantir a comunicação
2. Iniciar o Rm.Host.exe
3. Iniciar a ferramenta de fato com duplo clique no RM.Atualizador.GetLog.exe
Obtendo o log

1. Após abrir a aplicação, a seguinte tela será aberta:
2. Criei um Alias (através do RM.AliasManager.exe) para a base que você deseja obter o log.
3. Selecione o Alias.
4. Insira os dados de login dessa base.
5. Insira a versão que você deseja obter o log.
   1. Coloque a versão com pontos e .0 ao final. **Ex:** 12**.**1**.**2410**.0**
6. Clique em OK e aguarde a geração.
7. Após a geração será apresentado a tela a seguir:
8. Pronto, seu Log está salvo, basta ir para a pasta "**...\CorporeRM\RM.Net\Atualizador\Log**"
