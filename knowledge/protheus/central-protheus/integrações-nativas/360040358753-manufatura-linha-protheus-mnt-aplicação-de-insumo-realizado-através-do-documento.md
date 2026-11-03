---
article_id: 360040358753
category: Integrações Nativas
content_hash: 92eaf2ee9686d0cb4a9f2b7a4ffa86c9aa06f60b9b32dedd17532b491033d33f
fetched_at: '2026-06-28T22:42:35.318259+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Aplicação de insumo realizado através do
  Documento de Entrada
type: support-article
updated_at: '2023-03-29T20:27:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040358753-Manufatura-Linha-Protheus-MNT-Aplica%C3%A7%C3%A3o-de-insumo-realizado-atrav%C3%A9s-do-Documento-de-Entrada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)**Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Qual a regra utilizada para que as mesmas características de **Tarefa** e **Destino** de um insumo previsto sejam utilizadas no insumo realizado através do **Documento de entrada**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - A partir da versão 12  
  
**Solução**Para que um insumo previsto de uma **O.S. - Ordem de serviço** seja realizado com as mesmas características através do **Documento de entrada**, é necessário que os parâmetros sejam configurados e que seja relacionado o **Pedido de compra** ao **Documento de entrada** de acordo com o passo a passo abaixo:  
  
Parâmetros:

* **MV\_NGMNTCM - Integração Manutenção com Compras = S**
* **MV\_NGMNTES - Integração Manutenção com Estoque = S**
* **MV\_NGMNTPC - Integração Manutenção com Planejamento e Controle de Produção = S**
* **MV\_NGMNTNO - Vincula O.S. automática aos pedidos da NFe= 1**
* **MV\_ESTNEG - Permite que os saldos em estoque fique negativo. = N**

No módulo de **Manutenção de Ativos - SIGAMNT**, cadastrar uma **O.S.** através da rotina de **O.S. Corretiva - MNTA420**informando um insumo que gere uma **SC - Solicitação de Compras**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052907654/mceclip0.png)

Acessar o módulo de **Compras - SIGACOM** e incluir um **P****edido de Compra - MATA121**relacionando a **SC** gerada através do botão **Outras Ações / Solicit.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052908054/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052908214/mceclip2.png)

Continuando no módulo de **Compras - SIGACOM**,incluir o **D****ocumento de entrada -MATA103** relacionar o **Pedido de compra** incluído anteriormente através do botão **Outras Ações / Item Ped**.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053803153/mceclip3.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053803173/mceclip4.png)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052908374/mceclip5.png)

Após incluir o **D****ocumento de Entrada**, retornar ao módulo de **Manutenção de Ativos - SIGAMNT**, acessar a rotina de **Retorno Mod2 - MNTA435** e verificar que o insumo previsto está realizado.
