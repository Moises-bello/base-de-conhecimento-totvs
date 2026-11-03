---
article_id: 35866257143703
category: Materiais - Compras (SIGACOM)
content_hash: 0f4691e5d966f1eae288174054bfe5f6af2cda9b5443cd10c3301de66682893c
fetched_at: '2026-06-28T22:41:21.887395+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Preenchimento
  da Data de Entrega no Novo Fluxo de Compras
type: support-article
updated_at: '2025-10-24T18:48:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35866257143703-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Preenchimento-da-Data-de-Entrega-no-Novo-Fluxo-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35866257127447) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como a Data de Entrega é preenchida no Novo Fluxo de Compras?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Protheus Release 12.1.2310  
  
**Solução**  
Na tela de Necessidade de Compra do Novo Fluxo de Compras, é necessário selecionar a Solicitação de Compra. Em seguida será direcionado para a tela de **Solicitação de cotação**. Nesta tela há dois campos obrigatórios, referentes aos **Dados da cotação,**evidenciados com um asterisco '\*'. Será necessário o preenchimento dos mesmos pra prosseguir o processo.

Os respectivos campos são:

1. **Apelido do grupo de cotação:** O usuário definirá como a cotação será chamada;
2. **Recebimento cotação:**O usuário definirá o prazo para o recebimento de cotações. Esta informação será preenchida no campo **C8\_VALIDA** que é a **Data de Validade da Cotação.**

![](https://tdn.totvs.com.br/download/attachments/680260500/eNDERE%C3%87O.gif?version=1&modificationDate=1743789696433&api=v2)

Após isso, quando o usuário for realizar o edição/preenchimento manual ou quando o fornecedor do preencher via workflow da proposta dessa cotação, poderá preencher a Data de Entrega **C8\_DATPRF**.

Foi implementada a melhoria, onde o campo C8\_DATPRF é exibido na tela de Edição de Cotação para o usuário, bem como o campo passa a ser exibido para edição no workflow, para que o fornecedor possa informar a data de entrega de cada item constante no orçamento.

Além disso, quando a análise for feita por proposta, ao utilizar o filtro Menor Prazo, será utilizado a média dos dias de entrega dos itens, não mais o campo Prazo de dias para entrega.

O campo da Data de Entrega está por item da cotação, de forma que o fornecedor possa colocar de forma individualizada a data de entrega de cada item.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35866228157207)

A data que consta no campo Data de Entrega da Solicitação de Compra **C1\_DATPRF não é passada** para o campo **C8\_DATPRF** da Cotação. Porém a **Data de Entrega da Cotação** **C8\_DATPRF**será levada ao **Pedido de Compra** **C7\_DATPRF** gerado na análise da cotação.

A data de Emissão da cotação **C8\_EMISSAO** sempre será a database na qual ela está sendo incluída.

Para estabelecer o **Prazo da Cotação C8\_PRAZO** será feita a média da Data de Entrega **C8\_DATPRF** dos itens da cotação. Depois disso, calcula-se quantos dias da database até a Data de Entrega Média Calculada. Esse número de dias entre essas datas é o **Prazo da Cotação C8\_PRAZO**

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Tabela de Preços (COMA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6922118807703-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Tabela-de-Pre%C3%A7os-COMA010)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-BR/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-BR/sections/1500001537201-Materiais-Compras-SIGACOM-)
