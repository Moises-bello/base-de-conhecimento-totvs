---
article_id: 5173637973015
category: SIGAACD - Automação e Coleta de Dados
content_hash: e1c6decee75ee335143f6ba647ba730a2456e19adeb016db04dfcd1599ee7ef8
fetched_at: '2026-06-28T22:39:13.736669+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Pontos de Entrada
  da rotina Mestre de Inventário ACDA030
type: support-article
updated_at: '2023-04-18T17:01:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5173637973015-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Pontos-de-Entrada-da-rotina-Mestre-de-Invent%C3%A1rio-ACDA030
---

**Dúvida**Quais os Pontos de Entrada da rotina Mestre de Inventário ACDA030? Quais as suas funções no Protheus

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Solução**Veja abaixo os Pontos de Entrada relacionados ao Mestre Inventário - ACDA030:

|  |  |  |
| --- | --- | --- |
| **Ponto de entrada** | **Titulo** | **Descrição** |
| **[ACDA30OK](https://tdn.totvs.com/pages/releaseview.action?pageId=6091063)** | Valida Inclusão do Mestre de Inventário | No final da função. O objetivo deste ponto de entrada é permitir ao usuário a inclusão do mestre de inventário. |
| **[AI030PER](https://tdn.totvs.com/pages/releaseview.action?pageId=36798825)** | Ponto de entrada para alterar a função que faz a geração do CBA por endereço | Ponto de entrada para alterar a função que faz a geração do CBA por endereço.  Está localizado na função AIVA30Aut (gera mestre inventário automaticamente).  O ponto de entrada é executado antes de efetuar o processamento da rotina AI030. |
| **[ACDA30VE](https://tdn.totvs.com/pages/releaseview.action?pageId=6091064)** | Valida geração do Mestre de Inventário por endereço | Na loop da tabela SBE.O objetivo deste ponto de entrada é permitir ao usuário incluir validações particulares referentes a esta tabela na geração do mestre de inventário quando o mesmo é por endereço. Valido apenas para geração automática do mestre de inventário |
| **[ACD030FM](https://tdn.totvs.com/pages/releaseview.action?pageId=36798644)** | Executar customizações complementares | Ponto de entrada logo após a gravação da tabela CBA que permite a inclusão de dados adicionais na geração do mestre automático. Localizado no final da função AI030 |
| **[ACDA30VP](https://tdn.totvs.com/pages/releaseview.action?pageId=6091065)** | Valida geração do Mestre de Inventário por produto | O objetivo deste ponto de entrada é permitir ao usuário incluir validações particulares referente a esta tabela na geração do mestre de inventário quando o mesmo é por produto. Valido apenas para geração automática do mestre de inventário. |
| **[ACDA30LG](https://tdn.totvs.com/pages/releaseview.action?pageId=6090983)** | Lançamentos de Inventário Automático | No final da função, após o LOG já conter todas as suas informações padrão. Neste momento o ponto de entrada irá receber um Array principal que poderá conter 'N' Array's internos com as informações a serem inseridas no Log, estes array's internos deverão possuir 2 posições. |
| [**ACD030MNU**](https://tdn.totvs.com.br/pages/releaseview.action?pageId=679731666) | Adicionar botões ao Menu Principal | Adicionar botões ao Menu Principal através do array aRotina. |

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)*
