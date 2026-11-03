---
article_id: 4470766676887
category: Encargos
content_hash: 518308277d6922ac20dd503238628f7afed8adc64025c16a1deab0f2765301fb
fetched_at: '2026-06-28T22:46:53.184126+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Bloqueio dos Lançamentos Financeiros do Liquido Salarial, Líquido
  de Rescisão e Líquido de Férias
type: support-article
updated_at: '2025-03-05T18:45:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4470766676887-RH-RM-FOP-Bloqueio-dos-Lan%C3%A7amentos-Financeiros-do-Liquido-Salarial-L%C3%ADquido-de-Rescis%C3%A3o-e-L%C3%ADquido-de-F%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como bloquear os Lançamentos Financeiros do Liquido Salarial, Líquido de Rescisão e Líquido de Férias que estão sendo gerados duplicados?  
 **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**1. Deve certificar se a flag **Bloquear Geração de Lançamentos Financeiros Duplicados** está marcada, caso contrário, marque-a em: **Configurações | Parametrizador | Folha Normal | Lancto Financeiro:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10985870340503)**2. Valide também em: **Encargos | Cadastros Financeiros | Parâmetros.** Acesse o cadastro do lançamento financeiro que está duplicado, edite e vá para a aba de **Lançamentos Ativos** e certifique-se de deixar apenas um marcado:  
  
**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10985965914519)****Importante**Definição do parâmetro **Bloquear Geração de Lançamentos Financeiros Duplicados:****Com o parâmetro marcado**, ao gerar o lançamento financeiro para o mesmo tipo de lançamento, mesma coligada, mesma chapa, mesmo ano, mês e período será verificado se já existem os lançamentos de liquido salarial, liquido de rescisão e liquido de férias. Caso já existam estes lançamentos,  será gerada mensagem de aviso ao final da execução do processo informando que já foi gerado um lançamento semelhante e não será gravado. O usuário deverá excluir este lançamento para conseguir gerar um novo.  
  
**Com o parâmetro desmarcado**, ao gerar o lançamento financeiro para o mesmo tipo de lançamento, mesma coligada, mesma chapa, mesmo ano, mês e período, os campos mês, ano e período não serão preenchidos. Caso já existam estes lançamentos,  será gerada mensagem de aviso ao final da execução do processo informando que já foi gerado um lançamento semelhante e será duplicado.  
  
**Saiba mais**

[Lançamento Financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=452718795)
