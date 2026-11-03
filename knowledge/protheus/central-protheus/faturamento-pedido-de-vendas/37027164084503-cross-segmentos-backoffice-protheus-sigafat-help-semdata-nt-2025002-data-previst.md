---
article_id: 37027164084503
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: a0d218ef41c10641739a1cd7ed6c61b6b65f9c752993c0a70943401c1057708d
fetched_at: '2026-06-28T22:38:39.846072+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - HELP SEMDATA - "NT 2025.002
  - Data Prevista de Entrega"
type: support-article
updated_at: '2026-03-30T20:36:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37027164084503-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-HELP-SEMDATA-NT-2025-002-Data-Prevista-de-Entrega
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37027153509399) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Ao preparar um documento de saída pela rotina **"Pedidos de Venda (MATA410)"** é apresentado o **Help SEMDATA**, como resolver?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões.  
  
**Solução**

O **Help SEMDATA** é apresentado devido a nova tag **<**`dPrevEntrega`**>** — que representa a **data prevista de entrega** no cabeçalho da Nota Fiscal Eletrônica (NF-e) — introduzida pela Reforma Tributária (**Nota Técnica "NT 2025.002**"), o sistema passou a validar a **data de entrega**para a geração do documento de saídaquando o campo "**Tipo Frete (C5\_TPFRETE)**" no Pedido de Vendas está preenchido como:

* **C - CIF**
* **T - Por conta terceiros**
* **R - Por conta remetente**

Devido ao fato de a geração do documento de saída, realizada pela rotina **"Pedidos de Venda (MATA410)"**, faturar os itens aptos como um todo, neste cenário a data de entrega nos itens (**C6\_ENTREG**) **não será tratado**.

Para continuar utilizando o controle pelo campo (**C6\_ENTREG**) utilize a rotina **"Documentos de Saída (MATA460A)"**.

Ao preparar o documento de saída pela rotina "**Pedidos de Venda (MATA410)**" temos 3 opções:

**1 -** **Parâmetro "Data de Entrega?" preenchido:** Preencher o parâmetro "**Data de Entrega ?**" no momento de preparar o documento de saída, essa data é levada para o campo "**F2\_DTENTR**".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37115477858071)

**2** - **Parâmetro "Data de Entrega?" em branco**: Nesse caso é necessário que o campo "**Dt. Entrega** (**C5\_FECENT**)"no cabeçalho do pedido esteja preenchido, essa data é levada para o campo "**F2\_DTENTR**".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37115494358935)

Ao acionar a preparação do documento de saída com o campo "**Dt. Entrega** (**C5\_FECENT**)" preenchido, será exibido um help perguntando se realmente deseja utilizar a data que está nesse campo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37350270946711)

**3 -** Campo "**Dt. Entrega** (**C5\_FECENT**)" <**em branco**> e parâmetro "**Data de Entrega ?**" <**em branco**> será exibido o **help SEMDATA**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37115494359575)  
   
O Help é apresentado somente na rotina **"Pedido de Vendas (MATA410)"**, não é apresentado pela rotina **"Documento de Saída (MATA460A)".**

**Observação:**

Para habilitar ou desabilitar o tratamento da data de entrega prevista na NF utilize o parâmetro [**MV\_LDTENTR**](https://tdn.totvs.com/x/STO_PQ).  
Esse parâmetro estará disponível na próxima **Expedição Contínua do Backoffice com previsão para FEV/26.**

### Dicas

Existe um ponto de entrada executado na rotina **Documentos de Saída (MATA461)** e no **Pedido de Vendas (MATA410),** permitindo definir a data de entrega no momento de preparar o **Documento de Saída**, conforme documento técnico: [PE MT46DTEN Definir data de entrega nos Documentos de Saída](https://tdn.totvs.com/x/FyaFPQ). Este ponto de entrada foi criado no dia 13/01/2026, por este motivo, é necessário aplicar o pacote a partir dessa data de corte para o ponto funcionar:

O pacote pode ser acessado no endereço:

12.1.2210:<https://r.totvs.io/p/1233690> ;   
12.1.2310:<https://r.totvs.io/p/1233691> ;  
12.1.2410:<https://r.totvs.io/p/1233688> ;   
12.1.2510:<https://r.totvs.io/p/1233689> ;

**Importante validar se há algum pacote disponível com data de corte posterior à 13/01/2026:** [Pacotes de Atualização - Faturamento](https://tdn.totvs.com/x/Iw4dHw)

O campo de itens do Pedido de Vendas (**C6\_ENTREG**) possui o comando *dDataBase*em seu inicializador padrão, logo, você poderá ajustar com alguma regra padrão da empresa EX: (dDataBase + 60), para que o sistema siga uma regra personalizada quanto a data de entrega dos itens do pedido, neste sentido, você também pode realizar esta regra pelo campo (**C5\_FECENT**), que replica a mesma data informado no mesmo, aos itens do Pedido de Venda.

**Saiba Mais:**

* [**Data prevista de entrega**](https://tdn.totvs.com/x/flCZP)
* [**Cross Segmentos - Backoffice Protheus - SIGAFAT - Pedido gerando várias notas**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37036636655767-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Pedido-gerando-v%C3%A1rias-notas)
