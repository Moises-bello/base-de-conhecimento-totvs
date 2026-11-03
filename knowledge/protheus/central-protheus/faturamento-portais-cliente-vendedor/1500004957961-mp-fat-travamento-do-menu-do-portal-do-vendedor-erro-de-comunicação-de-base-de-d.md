---
article_id: 1500004957961
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: e0366d5de9fc9f28a6f07f6c9d33ebeb80b13c104ae80ed6c47d06ff811d7a55
fetched_at: '2026-06-28T22:38:23.990512+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: 'MP - FAT - Travamento do Menu do Portal do Vendedor / Erro de comunicação
  de Base de Dados '
type: support-article
updated_at: '2021-04-28T15:15:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004957961-MP-FAT-Travamento-do-Menu-do-Portal-do-Vendedor-Erro-de-comunica%C3%A7%C3%A3o-de-Base-de-Dados
---

**Dúvida**Após acessar o Portal o sistema trava ao clicar nas rotinas do Menu.  
  
**Ambiente**Microsiga Protheus -  a partir da versão 12.  
  
**Solução**

1) Procure deixar os parâmetros **MV\_PORTAL1, MV\_PORTAL2, MV\_PORTAL3 e MV\_PORTAL4** em branco para um novo teste.

Abaixo link sobre os parâmetros e configurações do Portal

**<https://tdn.totvs.com/pages/viewpage.action?pageId=236596491>**

2) Desative o ponto de entrada **PEGETPRES** (caso esteja em uso)

**<https://tdn.totvs.com/pages/viewpage.action?pageId=6804839>**

3) Verifique se o programa **WSPORTAL02.PRX** está atualizado
