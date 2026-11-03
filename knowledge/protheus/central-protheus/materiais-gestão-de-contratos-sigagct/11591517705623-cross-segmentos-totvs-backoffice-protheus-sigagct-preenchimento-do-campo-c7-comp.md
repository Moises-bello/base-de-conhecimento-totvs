---
article_id: 11591517705623
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: fb851684868178a99da8fba4708ca78718ac249a908ba3d65432d623a9804b02
fetched_at: '2026-06-28T22:37:24.043486+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Preenchimento do Campo
  C7_COMPRA em Pedidos de Compra Gerados Por Nova Medição de Contratos.
type: support-article
updated_at: '2023-01-11T14:04:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11591517705623-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Preenchimento-do-Campo-C7-COMPRA-em-Pedidos-de-Compra-Gerados-Por-Nova-Medi%C3%A7%C3%A3o-de-Contratos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Preenchimento do Campo C7\_COMPRA em Pedidos de Compra Gerados Por Nova Medição de Contratos.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Gestão de Contratos - Todas as versões.  
  
**Solução**

Na inclusão do Contrato é necessário Importar uma Solicitação de Compras que tenha o campo **Cod do Comprador (C1\_CODCOMP)** preenchido.

Exemplo Solicitação de Compras com o **Cod Comprador** preenchido.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11591341796887)

-Na Rotina Manutenção de Contratos(CNTA300)  >Incluir Preencha os Dados do Cabeçalho do Contrato>Planilha e clique em Outras >Ações >**Importar Solicitações de Compra**para importar a Solicitação de Compras ao Contrato.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11590619651351)

-Ao Realizar a Nova Medição(CNTA121) para o item desse Contrato será Gerado o Pedido de Compra com o **Código do Comprador** Preenchido.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11591418473495)

**Obs**:Por padrão o campo C7\_COMPRA não vem marcado como usado, caso queira o preenchimento do campo marque o mesmo como usado no configurador do sistema.

***Saiba Mais:***

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Preenchimento do campo C7\_COMPRA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8271027854103-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Preenchimento-do-campo-C7-COMPRA?source=search)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
