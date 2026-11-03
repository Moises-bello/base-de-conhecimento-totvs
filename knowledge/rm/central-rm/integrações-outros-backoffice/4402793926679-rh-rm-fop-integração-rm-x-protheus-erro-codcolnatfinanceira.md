---
article_id: 4402793926679
category: Integrações Outros BackOffice
content_hash: 11389904254cdb99e4ad3da83912b97e159343da9d504724ad992f98cb84d1be
fetched_at: '2026-06-28T22:46:42.191280+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: RH - RM - FOP - Integração RM x Protheus erro CODCOLNATFINANCEIRA
type: support-article
updated_at: '2025-02-03T19:00:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402793926679-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-x-Protheus-erro-CODCOLNATFINANCEIRA
---

**Ocorrência**Ao integrar o Financeiro originado no TOTVS Folha de Pagamento ao Protheus, é retornado o erro "A column named 'CODCOLNATFINANCEIRA' already belongs to this DataTable"  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
Esse incidente ocorre quando há atualização do sistema, pois o Source Code existente ainda é o da versão anterior, sendo necessário recriá-lo.  
  
**Solução**Para solucionar esta ocorrência, realize os seguintes passos:  
  
**1.** Acessar o módulo Integrações | Mensagem Única | Integrações e editando a integração, acesse Anexos | Mapeamento de Entidades:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402800138647/mceclip3.png)  
  
Edite o adapter ACCOUNTPAYABLEDOCUMENT e clique no link do evento. Faça a Exportação do Código Fonte para XML, guardando um backup para que, caso necessário, importe novamente.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402793911703/mceclip5.png)  
  
**2.** Feita a exportação do Código Fonte como um backup, podemos excluí-lo do RM.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402799998103/mceclip2.png)  
  
**3.** Acesse Integrações | Ferramentas | Configurar e execute a rotina para TOTVS Folha de Pagamento RM x Backoffice Protheus, assim será criado o novo código fonte:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402799944087/mceclip1.png)
