---
article_id: 360025984513
category: Materiais - Compras (SIGACOM)
content_hash: 2211829b85d37e7d0bbc43d168a3c8dc37020fe30a32fe5c8b1afe6c40f6568e
fetched_at: '2026-06-28T22:41:15.869401+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como filtrar o pedido
  de compras para mostrar por legenda no browser
type: support-article
updated_at: '2025-10-06T18:02:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025984513-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-filtrar-o-pedido-de-compras-para-mostrar-por-legenda-no-browser
---

**Dúvida**

Como filtrar o pedido de compras para mostrar por legenda no browser.  
  
**Ambiente**

Protheus – Compras – A partir da versão 12.17  
  
**Solução**

No Browser clique em Filtrar no canto direito superior e crie o filtro através da tela conforme abaixo:

![filtro.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360040189674/filtro.PNG)

Não existe um campo especifico para definição da legenda; diversos campos são verificados.  
O sistema utiliza os seguintes campos de acordo com as cores e mencione-os no filtro:

* **Verde:** Verifica se o campo C7\_QUJE e C7\_QTDACLA tem conteúdo 0. Neste filtro, para não serem listados os pedidos "Azuis" (Bloqueados), "Pretos" (Autorização de Entrega) e com "Resíduo Eliminado", deve-se acrescentar ao filtro C7\_CONAPRO Diferente de B, C7\_TIPO = 1 (Pedido) e C7\_RESIDUO =      (vazio).
* **Amarelo:** Verifica se o campo C7\_QUJE tem conteúdo diferente de 0 e seu conteúdo é menor que o conteúdo do campo C7\_QUANT.
* **Vermelho:** Verifica se o conteúdo do campo C7\_QUJE é maior ou igual ao conteúdo do campo C7\_QUANT.
* **Azul:** Verifica se o conteúdo do campo C7\_CONAPRO é igual a B e se o conteúdo do campo C7\_QUJE é menor que o conteúdo do campo C7\_QUANT.
* **Cinza:** Verifica se o campo C7\_RESIDUO não está vazio.
* **Laranja:** Verifica se o conteúdo do campo C7\_QTDACLA é maior que 0.
* **Preto:** Verifica o campo C7\_TIPO.
* **Branco:** Verifica se o campo C7\_CONTRA e C7\_RESIDUO não estão vazios.
* **X Vermelho:**Verificar se o campo C7\_CONAPRO é igual a R.

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Legendas - Rotina Pedido de Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029175971)

*[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)*

*[Mais Artigos Materiais - Compras](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)* *[(SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)*
