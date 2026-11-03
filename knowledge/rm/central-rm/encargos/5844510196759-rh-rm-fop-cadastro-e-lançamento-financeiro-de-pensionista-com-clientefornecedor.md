---
article_id: 5844510196759
category: Encargos
content_hash: 23ac453f0c71e0804f90037b9228d7562f51d7591696cbe3e8f701e5df04c792
fetched_at: '2026-06-28T22:46:52.545178+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Cadastro e lançamento financeiro de pensionista com cliente/fornecedor
type: support-article
updated_at: '2025-08-08T19:43:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5844510196759-RH-RM-FOP-Cadastro-e-lan%C3%A7amento-financeiro-de-pensionista-com-cliente-fornecedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34051082063511) Tempo aproximado para leitura: **00:02:05 min**  
  
**Dúvida**  
Como cadastrar cliente fornecedor especifico para pensionista no cadastro do dependentes da folha de pagamento para lançamentos financeiros?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Para cadastrar um pensionista como cliente fornecedor, acessar o cadastro do dependente do colaborador em **Anexos | Folha de pagamento | Dependentes:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5843989116311)  
  
Dentro do cadastro de dependentes acesse **Processo | Inclusão do cliente fornecedor:**  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5844043307799)  
  
Dessa forma será apresentado uma tela onde deverá ser cadastrado o cliente fornecedor, com os dados bancários do pensionista. Caso conste cliente fornecedor no cadastro do funcionário, automaticamente, o sistema irá retornar o cliente fornecedor do funcionário, só será possível inserir um cliente fornecedor especifico para o dependente, se a informação não constar no cadastro do funcionário no campo cliente fornecedor. No exemplo abaixo, não consta o cliente fornecedor no cadastro do funcionario.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5844095253655)

Feito isso deverá verificar a parametrização do lançamento financeiro utilizado, que deve está parametrizado agrupamento **Individual por dependente** e origem do fornecedor **Dependente**:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5844172690327)  
  
Verificar também o Lançamento ativo utilizado, para que a geração do lançamento financeiro possa ser executada. O lançamento financeiro da pensão será feito rateado pela quantidade de dependentes cadastrados, e para levar corretamente o lançamento na folha deverá ter gerado a movimentação do histórico do dependentes:  
  
![](https://totvssuporte.zendesk.com/attachments/token/XocvBEnsXhziWVHIdhYIetigH/?name=image.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/s8BbQvAmSaYq8OxfBglfvk7eJ/?name=image.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5846740212631)  
  
Geração do lançamento financeiro aba **Encargos | Geração dos Lançamentos** | Parametrizar conforme necessidade especifica da organização, agrupamento deve usar a parametrização marcado | avançar para executar:  
  
![](https://totvssuporte.zendesk.com/attachments/token/u2Tg9KnK6SdaSSmwnrbHeZ1kr/?name=image.png)

Ao acessar a aba **Encargos | Lançamentos ( Gestão Financeira)**, podemos consultar o mesmo:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5844334778647)

**Saiba mais**  
[Inclusão Dependente Cliente/Fornecedor](https://tdn.totvs.com.br/pages/releaseview.action?pageId=563426898)
