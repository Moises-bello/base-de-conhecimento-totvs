---
article_id: 13162459818391
category: Originação de Grãos (OG)
content_hash: f94c3293c319c0374142e183a59fd8fac59037ab9ad4b80bafa93f2904535bf0
fetched_at: '2026-06-28T22:45:36.961462+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Alteração registro de negócio
type: support-article
updated_at: '2025-06-24T19:14:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13162459818391-Agro-Linha-Protheus-AGR-Altera%C3%A7%C3%A3o-registro-de-neg%C3%B3cio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20140116793111) Tempo aproximado para leitura: **00:00:20 min** **Dúvida**Porque ao alterar o registro de negócio, gera erro.log?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Ao incluir um **registro de negocio, compra e venda**, sem informar a entidade que não é obrigatório no registro de negocio, o registro de negocio fica com status de **completar**.  
Porem é possível realizar a aprovação do cliente o qual gera o contrato.Foi alterado a regra de validação do registro de negocio para incluir a regra de bloqueio ao **aprovar cliente** caso não seja informado o **código do emitente**.
