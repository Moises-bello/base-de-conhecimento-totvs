---
article_id: 4578044654231
category: Rescisão
content_hash: a102d1cc441e7a5a2f7e01229933db980eabee9bab55df1f88361ff692dc9bf8
fetched_at: '2026-06-28T22:46:54.409019+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: RH - RM - FOP - Pagamento do artigo 479 na rescisão
type: support-article
updated_at: '2025-01-22T19:31:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4578044654231-RH-RM-FOP-Pagamento-do-artigo-479-na-rescis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29427237550999) Tempo aproximado para leitura: **00:02:17 min****Dúvida**Como realizar o pagamento do artigo 479 na rescisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize o passo a passo abaixo:  
  
1. Primeiramente, será necessário acessar: **Administração de Pessoal | Eventos | Eventos**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29427237553815)  
  
2. Logo, verifique se já existe cadastrado o evento com código de cálculo 124, se está como Provento/Valor e se não utiliza fórmula de valor. Caso não esteja, será necessário a criação do mesmo.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29427237560215)  
  
**Código de Cálculo 124 - Indenização Artigo 479**  
Provento do tipo valor. Utilizado no cálculo das rescisões dos funcionários com contrato de trabalho que tenham termo estipulado. Representará 50% do valor da remuneração a que o funcionário teria direito até o final do contrato.  
  
3. Após a verificação do cadastro do evento com código de cálculo 124, acesse: **Administração de Pessoal | Sindicatos** e edite o sindicato em questão.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29427237566231)  
  
4. Na aba **Identificação** do cadastro do Sindicato, se existir alguma fórmula informada no campo **Fórmula para cálculo de indenização artigo 479**, ela será utilizada como base para o evento da indenização. Se o campo estiver vazio, será considerado o salário de contrato do funcionário.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4577024412055)  
  
Se for necessária a criação de uma fórmula, ela deve retornar apenas o valor de base e não o valor a ser lançado.  
  
5. Logo, acesse: **Administração de Pessoal | Funcionários** e edite o funcionário em questão.

6. Verifique se na aba **Registro | Dados do Contrato**, o campo **Data do Final do Contrato** está informado corretamente.  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4577435867031)  
  
7. Feito isso, acesse o cadastro de rescisão e verifique se na aba **Rescisão** o campo **Contrato com Prazo** está marcado e a data informada corretamente.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29427207769623)  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4577837415703)  
 **Importante**O tipo da demissão deve ser **2- Iniciativa do Empregador sem justa causa**, e não **T- Término de contrato de trabalho**. O tipo **T** deve ser utilizado somente quando a data de demissão for exatamente o dia de término do contrato, e desta forma não terá indenização.
