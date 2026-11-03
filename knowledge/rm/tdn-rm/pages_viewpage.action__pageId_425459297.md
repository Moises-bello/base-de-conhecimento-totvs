---
content_hash: 30abff1be5344c6943a26909d61039a5fc0da9e1e386d00bf3d68bc42fe1acf3
fetched_at: '2026-06-29T00:09:35.290432+00:00'
page_id: '425459297'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT - Processo Solicitações de Armazém/Compra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459297
version: 3
---

**Backoffice RM x Protheus SigaMNT - Processo Solicitações de Armazém/Compra**

---

**Solicitação de Compra**

O processo de Solicitação de Compra consiste em gerar um movimento no TOTVS Gestão de Estoque, Compras e Faturamento para os insumos realizados da Ordem de Serviço aberta pelo PROTHEUS SigaMNT.   
 Após a OS (ordem de serviço) ser gerada no PROTHEUS SigaMNT e forem incluidos os insumus previstos na mesma a integração se encarregará de gerar um movimento de Solicitação de Compra para o TOTVS Gestão de Estoque, Compras e Faturamento.   
 Para que a solicitação de compra seja gerada, além dos parâmetros da integração estiverem já configurados e preciso que o tipo de movimento esteja criado e configurado no TOTVS Gestão de Estoque, Compras e Faturamento, clique aqui para visualisar os parâmetros dos tipos de movimentos.   
 A solicitação de compra segue o processo padrão definido pelo TOTVS Gestão de Estoque, Compras e Fatuarmento, podendo passar pelo processo de cotação ou não, sendo que a baixa de estoque referente aos produtos comprados deve ser inserida no BackOffice via cópia por referência para o movimento de OS com o tipo de relacionamento "Cópia Simples com Relacionamento somente de movimento".  
    
 **Solicitação de Armazém (estoque)**

O processo de Solicitação de Compra consiste em gerar um movimento no TOTVS Gestão de Estoque, Compras e Faturamento para os insumos realizados da Ordem de Serviço aberta pelo PROTHEUS SigaMNT quando os mesmos não existem em estoque.   
 Após a OS (ordem de serviço) ser gerada no PROTHEUS SigaMNT e forem incluidos os insumus previstos na mesma a integração se encarregará de gerar um movimento de Solicitação de Compra para o TOTVS Gestão de Estoque, Compras e Faturamento.   
 Para que a solicitação de armazém seja gerada, além dos parâmetros da integração estiverem já configurados e preciso que o tipo de movimento esteja criado e configurado no TOTVS Gestão de Estoque, Compras e Faturamento, clique aqui para visualisar os parâmetros dos tipos de movimentos.   
 A solicitação de armazém segue o processo padrão definido pelo TOTVS Gestão de Estoque, Compras e Fatuarmento, sendo que a baixa de estoque destas solicitações devem ser efetuadas através do processo de faturamento disponibilizado em tela e com o tipo de movimento parametrizado como sendo de Baixa de Estoque para o SigaMNT.  
 Caso o faturamento não seja feito por tela ou não utilize o tipo de movimento parametrizado como sendo de Baixa de Estoque para o SigaMNT a Fórmula Visual NÃO será disparada, assim o SigaMNT não será informado da mesma.

---

 **Recursos Adicionais**

TDN - Boletim Técnico : [Solicitação de Compra e Armazém](http://tdn.totvs.com/download/attachments/76251259/PROTHEUS_BT_SOLICITACAO+DE+COMPRA+E+ARMAZEM_BR_CON000158.pdf?version=1&modificationDate=1380049346000)
