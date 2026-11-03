---
article_id: 28455916986007
category: Financeiro - Novo Gestor Financeiro
content_hash: ed9116c6318b82141e3f222cca120e09ca8abed803b1d6b9f220373ac1630c5c
fetched_at: '2026-06-28T22:37:41.481558+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Novo painel
  gestor não carrega
type: support-article
updated_at: '2026-01-07T18:28:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28455916986007-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Novo-painel-gestor-n%C3%A3o-carrega
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28455890264087) Tempo aproximado para leitura: **00:05 min**

**Dúvida**  
O que validar para a atualização dos saldos no Novo Painel Gestor?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**

1. **Validação da Configuração das Tags**  
   Solicita-se a validação da configuração das tags apresentadas abaixo para garantir que estão corretamente configuradas:

* **[GENERAL]**

  + `app_environment=Ambiente`
* **[Drivers]**

  + `MultiProtocolPortSecure=0`
  + `MultiProtocolPort=1`

2. **Renomeação da Pasta**  
   Solicita-se a renomeação da pasta denominada "http-root", localizada dentro da pasta "Protheus data".
3. **Reinicie os serviços**
4. Caso o problema persista, encaminhe o log do console com a tag **FWTRACELOG** ativada.

* **Parar o Serviço do Protheus.**
* **Acessar a pasta APPSERVER** do serviço e renomear o arquivo **CONSOLE.LOG**.
* **Editar o arquivo appserver.ini**:
  + Adicionar a chave `CONSOLELOG=1` na seção **[GENERAL]**.
  + Adicionar a chave `FWTRACELOG=1` na seção **[ENVIRONMENT]**.
* Salvar o arquivo **appserver.ini**.
* Iniciar o Serviço.
* **Reproduzir o Erro**.
* Acessar a pasta BIN -> APPSERVER.
* **Encaminhar o arquivo Console.log** gerado ao suporte para análise.

**Saiba mais**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - O que validar para a atualização dos saldos no Painel Gestor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/26466475830935-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-O-que-validar-para-a-atualiza%C3%A7%C3%A3o-dos-saldos-no-Painel-Gestor)
