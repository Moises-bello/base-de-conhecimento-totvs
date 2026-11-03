---
article_id: 26319444407703
category: Materiais - Compras (SIGACOM)
content_hash: f0aca334730ea5d4624cb09a72e32ec3ee468577678f9f51e296cda2045d05de
fetched_at: '2026-06-28T22:41:12.910766+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM  - Carregar Solicitação
  de Compras de todas as Filiais na rotina Gera Cotação (MATA131)
type: support-article
updated_at: '2024-09-12T16:10:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26319444407703-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Carregar-Solicita%C3%A7%C3%A3o-de-Compras-de-todas-as-Filiais-na-rotina-Gera-Cota%C3%A7%C3%A3o-MATA131
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26319485834903) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Como carregar as Solicitações de Compras de todas as Filiais na rotina Gera Cotação (MATA131) ?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12  
  
**Solução**

Para que as solicitações de compra de todas as filiais, sejam carregadas em tela na rotina de Gera Cotações é necessário configurar as perguntas abaixo da rotina:

* **Filtra por Data = Não**
* **Filtra SC já Gerada = Não**

**![filiais.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26319444402071)**

Caso opte por filtrar por data e/ou Filtra SC já gerada igual sim, serão apresentadas somente as solicitações da filial logada.

Este procedimento é necessário, devido a rotina Gerar Cotação (MATA131), trabalhar com o filiais de entrega onde as mesmas podem ser diferentes da filial de inclusão da solicitação.

***Saiba Mais:***

[PCOM19004 - Carregar Solicitação de Compras de todas as Filiais](https://tdn.totvs.com/x/F_-qK)

[PCOM19005 - Parâmetro MV\_COTFILT - Habilitar tela de filtro](https://tdn.totvs.com/x/Fw-1K)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
