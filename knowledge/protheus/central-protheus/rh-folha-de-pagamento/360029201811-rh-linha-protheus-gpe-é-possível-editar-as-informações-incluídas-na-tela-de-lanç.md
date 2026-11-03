---
article_id: 360029201811
category: RH - Folha de Pagamento
content_hash: 882e30cc86ed321370b9a5c3e338eabb571617e73938b5048bc7a269d410c547
fetched_at: '2026-06-28T22:44:11.856695+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE -  É possível editar as informações incluídas na
  tela de lançamentos múltiplos vínculos
type: support-article
updated_at: '2025-08-11T21:51:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029201811-RH-Linha-Protheus-GPE-%C3%89-poss%C3%ADvel-editar-as-informa%C3%A7%C3%B5es-inclu%C3%ADdas-na-tela-de-lan%C3%A7amentos-m%C3%BAltiplos-v%C3%ADnculos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26329178487447) Tempo aproximado para leitura: 00:04:00 min**

**Dúvida**É possível editar as informações incluídas na tela de lançamentos múltiplos vínculos?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Foi disponibilizado a rotina **GPEA924** onde será possível visualizar e efetuar manutenção nos dados de múltiplos vínculos (gravados nas tabelas RAW e RAZ).

Nessa rotina **NÃO** será possível efetuar inclusão de dados uma vez que para gerar essas informações é necessário que as verbas de INSS Outras Empresas (ID's 0288 e 0289) tenham sido incluídas e calculadas na folha de pagamento dos funcionários, com isso, possíveis inconsistências serão evitadas.

Importante

Para a utilização da rotina, deve ser feito a inclusão manual no menu do módulo GPE - Gestão de Pessoal através do módulo **SIGACFG** - Configurador:

|  |  |
| --- | --- |
| **Menu** | Miscelânea |
| **Submenu** | eSocial |
| **Nome da Rotina** | Múltiplos Vínculos |
| **Programa** | GPEA924 |
| **Módulo** | Gestão de Pessoal |
| **Tipo** | Padrão |

Atualização disponível neste link: [Edição dos Dados de Múltiplos Vínculos (GPEA924)](http://tdn.totvs.com/pages/viewpage.action?pageId=463814769)

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
