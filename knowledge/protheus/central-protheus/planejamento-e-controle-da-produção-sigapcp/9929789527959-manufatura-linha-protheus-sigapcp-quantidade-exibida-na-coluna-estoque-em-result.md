---
article_id: 9929789527959
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 40fb8623800249a5432ae35c9c90a366281c17796d79fbc25c47ce7991acf28a
fetched_at: '2026-06-28T22:42:45.815237+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Quantidade exibida na coluna Estoque
  em Resultados do MRP
type: support-article
updated_at: '2022-11-01T13:59:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9929789527959-Manufatura-Linha-Protheus-SIGAPCP-Quantidade-exibida-na-coluna-Estoque-em-Resultados-do-MRP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:35 min** **Dúvida**Como é calculado a quantidade exibida na coluna **Estoque** da rotina **Resultados do MRP**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Na tela de **Resultados do MRP**, a coluna **Estoque** apresenta o valor registrado no campo **HWB\_QTSLES - Sld Estoque**, que será exibido o valor referente a primeira data que existir cálculo para o produto.  
A tabela **HWB - Resultados do MRP Sumarizados** será registrada durante a execução do **PCPA712 - MRP Memória**, que por sua vez, faz leitura da tabela **T4V - Saldos em Estoque do MRP**.  
A tabela **T4V** será registrada durante a sincronização do **MRP - Manufacturing Resource Planning**, executada manualmente por meio da rotina **PCPA140 - Sincronização do MRP** quando marcada a opção **Saldos em Estoque**, ou quando executada automaticamente via **PCPA141 - Configuração de Integração do MRP via Schedule**.  
O campo **T4V\_QTD - Qnt Disp.** irá registrar a quantidade do campo **B2\_QATU - Saldo Atual** e neste momento, não será efetuado nenhum cálculo, apenas registrado o valor contido na tabela **SB2 - Saldos Físicos e Financeiro** no momento da sincronização.  
O campo **HWB\_QTSLES** é um saldo sumarizado de todos os armazéns, e irá somar ou subtrair conforme as parametrizações da tela **03-Estoque** do processamento do **PCPA712**, onde:

* **Estoque EM Terceiro**: soma a quantidade do campo **T4V\_QNPT - Qnt. Em Terc**.
* **Estoque DE Terceiro**: subtrai a quantidade do campo **T4V\_QTNP - Qnt. De Terc**.
* **Estoque Rejeitado pelo CQ**: subtrai a quantidade do campo **HWX\_QTDE - Qtde Rejeit** - **HWX\_QTDEV - Qtde Devol**.
* **Estoque Bloqueado pelo Lote**: subtrai a quantidade do campo **T4V\_SLDBQ - Saldo Bloq**.
* **Considera Estoque de Segurança**: se estiver como **Sim**, irá descontar a quantidade contido no campo **HWA\_ESTSEG - Est. Segur**/**HWE\_ESTSEG - Est Segur** do estoque inicial no primeiro período.
* **Considera Ponto de Pedido**: se estiver como **Sim**, gera as ordens na quantidade do ponto de pedido + 1. Isso ocorre para que no próximo processamento, não entre no ponto de pedido novamente. Ou seja, considera o conteúdo do campo **HWA\_EMIN - Pto Pedido**.

**Importante**  
Além das opções acima, o **MRP** irá verificar o conteúdo do parâmetro **MV\_LOTVENC - Indica se devem ser utilizados Lotes/Sub-Lotes com a data de validade vencida. (S)im ou (N)ao**. Se o parâmetro **MV\_LOTVENC** estiver como **N**, o saldo dos lotes que vencem antes da primeira data do **MRP** não vão ser considerados nesse somatório.  
  
**Saiba mais**  
Para mais informações, verifique o conteúdo do artigo [Manufatura - Linha Protheus - SIGAPCP - Parâmetro MV\_LOTVENC no cálculo do MRP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007708682-MP-SIGAPCP-Par%C3%A2metro-MV-LOTVENC-no-c%C3%A1lculo-do-MRP?source=search).
