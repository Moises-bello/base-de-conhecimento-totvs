---
article_id: 360026146874
category: RH - Rescisão
content_hash: f4d6c9d86e1377c56cb350efc0b667920cb352d4b9bc155f0ce19f4e8f3dd219
fetched_at: '2026-06-28T22:43:49.779961+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Multa Contrato Experiencia - O que verificar quando
  não esta calculando
type: support-article
updated_at: '2025-05-21T11:23:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026146874-RH-Linha-Protheus-GPE-Multa-Contrato-Experiencia-O-que-verificar-quando-n%C3%A3o-esta-calculando
---

**Dúvida**Ao calcular rescisão por dispensa ou pedido de demissão onde deveria ser calculada a multa por contrato de experiência e o sistema não esta calculando, o que verificar?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução** **1**. Verificar se no **Cadastro do Funcionário** os campos referente as datas de termino da experiência estão preenchidos:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040772274)  
  
**2**. Para **Dispensa antes do término da experiência**, na rotina Manutenção Tabela, na Tabela S043, ter um Tipo de Rescisão cadastrado para o cálculo, onde a coluna **Pgt. Mul. Contr.EXP deve estar com S**:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040774794)

**3**. Verificar se na rotina Roteiros de Cálculo, no roteiro **RES** as sequencias abaixo estão **habilitadas**:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041607053)

**4**. Para **desconto da multa** por pedido de demissão antes do término da experiência, na rotina Manutenção Tabelas, na Tabela S043 deve ter um Tipo de Rescisão cadastrado para esse cálculo, onde na coluna **Des. Mul. Contr EXP deve estar com S**:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040772834)

**5**. Verificar no cadastro de verbas se o **ID 0176** (Multa Provento) e o **ID 0177** (Multa Desconto) estão cadastrados corretamente.

**6**. Verificar se na rotina Roteiros de Cálculo, no roteiro **RES** as sequencias abaixo estão **habilitadas**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18145649003799)

**Saiba mais:**[MP - GPE - Como somar os adicionais para pagamento de multa por contrato de experiência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044717114-MP-GPE-Como-somar-os-adicionais-para-pagamento-de-multa-por-contrato-de-experi%C3%AAncia)

[RH - Linha Protheus - GPE - Como conferir cálculo id 0177 (desconto multa experiência) quando a demissão é na sexta-feira pagando o sábado e domingo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407074970775-RH-Linha-Protheus-GPE-Como-conferir-c%C3%A1lculo-id-0177-desconto-multa-experi%C3%AAncia-quando-a-demiss%C3%A3o-%C3%A9-na-sexta-feira-pagando-o-s%C3%A1bado-e-domingo)

[RH - Linha Protheus - GPE - Multa por Contrato de Experiência para categoria Horista](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052084533)
