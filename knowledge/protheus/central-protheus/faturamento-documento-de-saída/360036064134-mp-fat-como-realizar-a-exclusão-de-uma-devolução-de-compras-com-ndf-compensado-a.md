---
article_id: 360036064134
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: f10050bcde93af5e694bdb698a99c02319a1e5410d89dea1ac3b20ab83fee056
fetched_at: '2026-06-28T22:38:45.148100+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: MP - FAT - Como realizar a exclusão de uma devolução de compras com NDF compensado
  automaticamente.
type: support-article
updated_at: '2021-04-28T15:13:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036064134-MP-FAT-Como-realizar-a-exclus%C3%A3o-de-uma-devolu%C3%A7%C3%A3o-de-compras-com-NDF-compensado-automaticamente
---

**Dúvida**Como realizar a exclusão de uma devolução de compras com NDF compensado automaticamente?  
   
 **Ambiente**Microsiga Protheus – todas as versões.  
  
**Solução**Ao ativar o parâmetro **MV\_CMPDEVC** e realizar uma devolução de compras, o sistema realiza a **compensação automática do NDF**.

Se for necessária a exclusão da nota fiscal de devolução, o sistema apresenta a mensagem **FA050BAIXA**:  
  
![01.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360048028833/01.PNG)

Para Estornar a Compensação do NDF, acesse o módulo Financeiro (**SIGAFIN**), acesse a rotina Funções de Contas a Pagar (**FINA750**), selecione o **título gerado pela nota de Compra** (não o NDF gerado pela devolução).

Em Outras Ações > Compensação > Estornar, o sistema demonstrará o NDF que gerou a compensação:

![02.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360048028893/02.PNG)

Confirme a operação, o sistema realizará o estorno da compensação e **permitirá a Exclusão do Documento de Saída de Devolução** normalmente.
