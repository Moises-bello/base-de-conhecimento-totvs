---
content_hash: 52bf4c2e5f7cdf44927cae6cd67156028836a9935da64296659bbe005e22fbcc
fetched_at: '2026-06-29T00:05:58.844021+00:00'
page_id: '189304857'
product: rm
source: tdn-rm
title: Planilha RM - API
type: documentation
url: https://tdn.totvs.com/display/LRM/Planilha+RM+-+API
version: 6
---

# Pré-requisitos

---

2
complete
Linha RM versão 12.1.5 e posteriores

# Objetivos

---

Fornecer à área de segmentos uma API para manipulação de planilhas eletrônicas.

# Descrição

---

API é o acrônimo do termo em inglês *Application Program Interface*. Uma API é um conjunto de rotinas e padrões estabelecidos por um software para a utilização das suas funcionalidades por aplicativos que não pretendem envolver-se em detalhes da implementação do software, mas apenas usar seus serviços.

A API da Planilha RM está disponibilizada no assembly *RM.Glb.PlanilhaNet.Core.dll*. Dentro da arquitetura da Linha RM, esse assembly está disponível tanto no *Client Side* e quanto no *Server Side*.

# Utilização

---

Para utilizar a API, basta adicionar uma referência ao assembly *RM.Glb.PlanilhaNet.Core.dll*. No namespace RM.Glb.PlanilhaNet.Core.API encontra-se a classe **PlanRMFactory** que é o ponto inicial para utilização das funções da API. Essa classe estática disponibiliza métodos para que as planilhas eletrônicas possam ser criadas, carregadas de um arquivo existente ou da base de dados da Linha RM.

Os métodos da classe **PlanRMFactory** retornaram uma instância de um objeto da classe **PlanRMWorkbook** que permite a manipulação das propriedades de uma planilha eletrônica e dos dados que ela contém.

Para maiores informações:

****[@FRAMEWORK](http://fluig.totvs.com/portal/p/10097/subject/rframework)****

**Canais de Atendimento**

**Chamado:** Através do Portal TOTVS - [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2-2-3-9-5 (Framework) ou 2-2-3-9-4 (BI)

|  |  |
| --- | --- |
| **Produto** | Framework |
| **Versão** | 12.1.5 |
| **Processo** | Gestão |
| **Subprocesso** | Ferramentas de Análise |

|  |  |
| --- | --- |
| **Status do documento** | Produção |
| **Data** | 27/05/2015 |
| **Versão** | 1.0 |
| **Versão anterior** | 1.0 |
| **Autores** |  |

| Índice |
| --- |
| nonetrue |
