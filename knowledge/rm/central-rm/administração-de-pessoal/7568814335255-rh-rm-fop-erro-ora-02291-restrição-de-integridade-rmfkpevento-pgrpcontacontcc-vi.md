---
article_id: 7568814335255
category: Administração de Pessoal
content_hash: 219d17b485e8a0c60ce2f91bff812ef9b80802e0576fb4f82738dbfd0279045f
fetched_at: '2026-06-28T22:47:01.314080+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: 'RH - RM - FOP - Erro ORA-02291: restrição de integridade (RM.FKPEVENTO_PGRPCONTACONTCC)
  violada - chave mãe não localizada'
type: support-article
updated_at: '2025-03-11T11:08:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7568814335255-RH-RM-FOP-Erro-ORA-02291-restri%C3%A7%C3%A3o-de-integridade-RM-FKPEVENTO-PGRPCONTACONTCC-violada-chave-m%C3%A3e-n%C3%A3o-localizada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:31 min****Dúvida**Como realizar a correção do erro ORA-02291: restrição de integridade (RM.FKPEVENTO\_PGRPCONTACONTCC) violada - chave mãe não localizada apresentado no processo de cópia de eventos entre coligadas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para a correção do erro apresentado será necessário copiar os dados das tabelas dinâmicas **GRPGER**, **GRPCONT**.

**GRPGER**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9698937990935)

**GRPCONT**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9698993697303)

Segue abaixo mais informações referente ao processo de cópia de eventos entre coligadas:

[RH - RM - FOP - Cópia de registros entre coligadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021778232-RH-RM-FOP-C%C3%B3pia-de-registros-entre-coligadas?source=search)
