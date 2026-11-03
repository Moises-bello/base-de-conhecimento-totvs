---
article_id: 4409301634967
category: Comércio Exterior - Easy Import Control - Solic. de Importação
content_hash: 5ead00836275e379db55b0b7f3221eb2e518eb8bc00d24a5144a86bfddb84a10
fetched_at: '2026-06-28T22:39:46.694534+00:00'
product: protheus
section_id: 1500001538401
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Ponto entrada
  opções no menu Browse rotina EICSI400
type: support-article
updated_at: '2022-09-15T21:01:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409301634967-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Ponto-entrada-op%C3%A7%C3%B5es-no-menu-Browse-rotina-EICSI400
---

**Dúvida**Qual ponto de entrada pode ser utilizado para manipulação da variável **aRotina** adicionar na rotina Solicitação de Importação (**EICSI400)** dentro da opção do ***BROWSE*** uma opção de nossa empresa?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**É possível utilizar o ponto de entrada ISI400MNU que precisa retornar um array com as opções adicionais do **aRotina**. Exemplo:  **{ "Minha Opção de Menu", minhaFuncao()  , 0 , 4    }**

|  |  |  |
| --- | --- | --- |
| **Nome** | **Tipo** | **Descrição** |
| ISI400MNU | Caracter | Permite a manipulação do array de menu da tela manutenção da Solicitação de Importação |

**Saiba mais**  
[PE EICSI400 - Solicitação de Importação](https://tdn.totvs.com/pages/releaseview.action?pageId=625148390)
