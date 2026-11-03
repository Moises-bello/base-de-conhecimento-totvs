---
article_id: 360037387633
category: Materiais - Compras (SIGACOM)
content_hash: cf7c827e35071c3d5bf8cd6a50ce1326242a32093f72826283f14e13e2977762
fetched_at: '2026-06-28T22:41:07.483683+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - CICLO DE VIDA - Rotina
  Gera Cotações (MATA130)
type: support-article
updated_at: '2022-05-16T22:10:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037387633-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-CICLO-DE-VIDA-Rotina-Gera-Cota%C3%A7%C3%B5es-MATA130
---

**Dúvida**

CICLO DE VIDA - Rotina Gera Cotações (MATA130)

**Ambiente**

Protheus – Compras – A partir da versão 12.1.17

**Solução**

Ao acessar a rotina "Gera Cotações" (**MATA130**) o sistema retorna os helps abaixo sobre Clico de Vida e substituição da rotina.:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049106853/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049106953/mceclip1.png)

A rotina de Geração de Cotação será substituída por uma nova rotina com mesma finalidade que já está disponível no repositório de objetos. A substituição da rotina visa a evolução do produto.

Somente a nova rotina possibilitará gerar cotações a partir de Julho/2019.

*- Rotina anterior:* MATA130 - Gera Cotações

*- Rotina atual:* MATA131 - Gera Cotações

***Vantagens**:*

- Com o parâmetro **MV\_SELFOR** igual a **S** é possível visualizar a disposição dos produtos que fazem parte da cotação conforme o grupo de produto.  
- É permitido a inclusão de fornecedor participante para a cotação sem a necessidade de cadastrá-lo previamente na rotina de Fornecedores.  
- Funcionalidade para replicar os Fornecedores para o Grupo de Produtos ou para Todos os grupos.

***Procedimentos para utilização:***

Não há a necessidade de realizar nenhuma configuração para utilização da nova rotina. É necessário somente alterar no Configurador a chamada do programa no menu do Protheus de "**MATA130**" para "**MATA131**".

***Customizações**:*

Caso possua customizações na rotina antiga, será necessário revisá-las pois a estrutura e a tecnologia da rotina nova é diferente.

***Estrutura de Dados:***

**- SC8** - Cotações é a responsável pela gravação dos dados referente ao processo.

***Documentos relacionados:***

[MATA130: Gera Cotações](https://tdn.totvs.com/pages/viewpage.action?pageId=372558827)

Saiba Mais :

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
