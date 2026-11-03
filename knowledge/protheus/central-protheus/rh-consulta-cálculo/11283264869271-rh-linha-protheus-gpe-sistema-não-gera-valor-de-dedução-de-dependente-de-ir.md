---
article_id: 11283264869271
category: RH - Consulta Cálculo
content_hash: 192ec8e2b92bc9de79803d94c17c29a2745ea295f2e8a6c8396df601bd4906ee
fetched_at: '2026-06-28T22:43:13.561321+00:00'
product: protheus
section_id: 360010855834
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema não gera valor de dedução de dependente
  de IR
type: support-article
updated_at: '2025-10-17T11:19:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11283264869271-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-gera-valor-de-dedu%C3%A7%C3%A3o-de-dependente-de-IR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24789853962007) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Porque o sistema não gerou a o valor de dedução de dependente de IR?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões

**Solução**Para que o sistema entenda que haverá dedução de dependentes no cálculo de IR, é necessário realizar as configurações abaixo:  
  
**1.** Cadastro da verba com **Id 0060** em **Atualizações > Definições de Cálculos > Verbas (GPEA040)** . Essa verba será apresenta no cálculo com o valor de dedução total para dependentes. É uma verba de **Base Provento** e **tipo Valor**;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11282949322903)  
  
**2.** Cadastro de Dependente em **Atualizações > Funcionários > Dependentes (GPEA020)**: O campo **RB\_TIPIR** precisa estar preenchido com informação de Dependente de IRRF. Para esse campo o sistema apresenta três opções de preenchimento para Dependente de IR: **1. Sem limite de idade, 2. Até 21 Anos e 3. Até 24 Anos**;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11282527753751)

**3.** Cadastro do Funcionário em **Atualizações > Funcionários > Funcionários (GPEA010)**: Na aba **benefícios** o campo **Dep. de IR** deve estar preenchido com a quantidade de dependentes para IR. É preenchido automaticamente assim que é feito o cadastro de dependente na rotina **GPEA020 - Cadastro de dependentes**;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11282686478103)

**4.** Cadastro da **tabela S002 - IRRF em Manutenção de Tabelas** em **Atualizações > Definições de Cálculos > Manutenção de Tabelas (GPEA320):** Nos campos **Dedução Dependente** e **Limite Dependente**. O campo **Dedução Dependente** informa o valor que será deduzido para cada dependente, já o campo **Limite Dependente**, informa a quantidade limite de dependentes para cada funcionário, aconselhamos nesse campo deixar preenchido com **99**.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11283109600919)

**Saber Mais:**

[Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
