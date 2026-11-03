---
article_id: 360026147914
category: Gestão de Armazenagem (WMS)
content_hash: f4894287bcdbe6a2e745768aa83ed9b1f6f646ee3680b5b4fc3e22efeedac3e8
fetched_at: '2026-06-28T22:45:48.182459+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Utilizar um endereço de forma compartilhada
type: support-article
updated_at: '2025-10-31T22:22:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026147914-Log%C3%ADstica-Linha-Protheus-WMS-Utilizar-um-endere%C3%A7o-de-forma-compartilhada
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34835267134359)***Tempo aproximado para leitura:**00:01:10 min****Dúvida**Como utilizar um endereço de forma compartilhada?  
  
**Ambiente****TOTVS Distribuição** - **TOTVS WMS** (Linha Protheus) - Gestão de Armazenagem (**WMS**) - Todas as versões  
  
**Solução**Para compartilhar o espaço de um único endereço com vários produtos dentro do **WMS - Warehouse Management System**, existem as seguintes configurações: 

* O compartilhamento via percentual de ocupação. Para isto, no cadastro **WMSA310 -****Percentual de Ocupação** deve ser levado em consideração o percentual que cada produto ocupará no endereço ou;
* O compartilhamento via sequência de abastecimento. No cadastro **WMSA030 -****Sequência Abastecimento** configurar o campo **Tp. Endereçam -****DC3\_TIPEND** com a opção **4 - Compartilha Endereço Produtos Diferentes**.

**Importante**Além destas configurações, o Sistema seguirá as seguintes regras:

* A sequência de abastecimento para o outro produto também deve ser configurada para permitir o compartilhamento do endereço.
* Os campos**Tipo - B1\_TIPO** e **Grupo - B1\_GRUPO**, do cadastro **MATA010 - Produto**, devem ser os mesmos para ambos os produtos.
* Ambos os produtos devem possuir uma mesma norma em comum para a estrutura física cadastrada na sequência de abastecimento.

**Saiba mais**Para mais informações verifique o *link*: [Como utilizar um endereço de forma compartilhada no SIGAWMS](https://tdn.totvs.com/pages/viewpage.action?pageId=653569020)  
Também assista ao *Webinar* sobre o cadastro **Sequência de Abastecimento**: [Webinar TOTVS | Desvendando a Sequência de Abastecimento](https://www.youtube.com/watch?v=LggYlJy-GEc)
