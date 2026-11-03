---
article_id: 360037259774
category: RH - Dissídio
content_hash: faae6d7eabe98c7c7c7a176009e6ebf964010444ea8d110690df7749446f0c50
fetched_at: '2026-06-28T22:43:43.347286+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - É possível cancelar a geração do dissídio para
  a folha de pagamento
type: support-article
updated_at: '2025-11-26T14:53:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037259774-RH-Linha-Protheus-GPE-%C3%89-poss%C3%ADvel-cancelar-a-gera%C3%A7%C3%A3o-do-diss%C3%ADdio-para-a-folha-de-pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26492203253911) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**É possível cancelar a geração do dissídio para a folha de pagamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Após o cálculo do dissídio e **geração para folha de pagamento** **não é possível cancelar** a geração desses valores. As diferenças são armazenadas dentro da tabela RHH com o campo RHH\_INTEGR preenchido e as rotinas de cadastro do funcionário e histórico salarial são atualizadas com o novo valor de salário.  
  
Para retornar essa informação é necessário voltar o backup de todas as tabelas que são atualizadas no momento da geração:

* **SRA** - Cadastro de funcionário;
* **SR3** e **SR7** - Histórico Salarial;
* **SRC** - Cálculo de Folha de Pagamento;
* **RHH** - Dissídio Retroativo
* **RGB** - Lançamentos por Funcionário (Exclusiva para versão 12);
* **SRK** - Lançamentos Futuros.

Realizar o backup dessas tabelas é o primeiro passo para o cálculo do dissídio, veja o manual abaixo:  
[RH - Linha Protheus - GPE - Manual do dissídio retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034578653-MP-GPE-Manual-do-diss%C3%ADdio-retroativo-?source=search)

**Saiba mais:**

[RH - Dissidio](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
