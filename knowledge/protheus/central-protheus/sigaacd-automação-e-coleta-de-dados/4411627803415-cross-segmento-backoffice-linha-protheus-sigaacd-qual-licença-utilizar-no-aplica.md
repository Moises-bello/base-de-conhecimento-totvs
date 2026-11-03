---
article_id: 4411627803415
category: SIGAACD - Automação e Coleta de Dados
content_hash: 421d70ce6be4852a9b5d150e8114e522d45ae5406647dc718e51fea95a018aa4
fetched_at: '2026-06-28T22:39:13.782963+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Qual licença utilizar
  no aplicativo Meu Coletor de Dados?
type: support-article
updated_at: '2025-12-30T20:10:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411627803415-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Qual-licen%C3%A7a-utilizar-no-aplicativo-Meu-Coletor-de-Dados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37350691588375) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Qual licença necessária para utilização do Aplicativo Meu Coletor de Dados?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Solução**  
As licenças para o uso do Aplicativo Meu Coletor de Dados são:

* TOTVS **FULL**
* TOTVS **T**
* TOTVS **I**

Exclusivamente para o aplicativo Meu Coletor de Dados, é necessário incluir a chave MODULE na seção HTTPURI:

```
[HTTPURI]
Module=46
```

Se você está na modalidade Intera de licenciamento, a configuração do REST terá uma pequena particularidade. Estamos falando da chave "**stateless**" na sessão **[URIHTML]**, que define a maneira em que as licenças serão consumidas: Na inicialização da thread ou por demanda.

Para habilitar o comportamento de consumo de licença por demanda, o conteúdo da chave deve ser "1". Caso a chave não exista ou contenha o valor zero, o consumo de licença na inicialização da thread será mantido.

**Exemplo de configuração para Intera**

```
[URIHTML]
URL=/rest/app
PrepareIn=All
Instances=2,2
CORSEnable=1
AllowOrigin=*
Stateless=1
```

**Chaves para análise de erro do REST**

```
---------Verificar problemas nas funcionalidades-------------

[environment]
FWLOGMSG_DEBUG=1
FWTRACELOG=1

[general]
LogHttpFuncs=1

---------Verificar problemas de Licença-------------

LSDebug=2
FWTRACELOG=1
```

**Saiba mais:**

[*Configuração do REST Protheus para uso com os aplicativos Mobile*](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=519719292)

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
