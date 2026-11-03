---
article_id: 360057411914
category: Rescisão
content_hash: 0470f36181ea604f151ea03ebed36164aadee0cff40bf9dc68916e221a538c62
fetched_at: '2026-06-28T22:46:55.273755+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: RH - RM - FOP - Salário família com arredondamento em rescisão
type: support-article
updated_at: '2021-06-15T17:43:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057411914-RH-RM-FOP-Sal%C3%A1rio-fam%C3%ADlia-com-arredondamento-em-rescis%C3%A3o
---

**Dúvida**

Como realizar o lançamento da rescisão sem que o salário família gere o evento de Arredondamento (Código de Cálculo 20).  
  
**Ambiente**

RM - Totvs Folha de Pagamento - Todas as versões  
  
**Solução**

Esta situação se apresenta pois mesmo quando o funcionário não possui nenhum valor para receber, o funcionário deverá receber o Salário Família visto a obrigatoriedade o pagamento.

Após o cálculo geral de proventos e descontos, o sistema irá comparar o líquido com o valor de arredondamento que foi informado no campo Arredondamento em Cadastros | Funcionários | Parâmetros. Quando o líquido for negativo, o sistema irá gerar um arredondamento suficiente para zerar o líquido.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097334934/mceclip0.png)  
  
Desse modo, não podemos efetuar Recálculo, pois já está considerado o pagamento do Salário Família e, novamente, o Líquido será zerado entendendo que não houve esse pagamento, gerando o evento de Arredondamento.  
  
A ordem de processo deverá ser a seguinte:

1. Realize o Cálculo da Rescisão normalmente.
2. Realize a conferência dos valores e faça todos recálculos necessários.
3. Após a conferência, acesse Rescisão | Lançamento do Líquido para zerar o envelope. Neste procedimento, não poderá utilizar o botão Recalcular para não gerar o Arredondamento.  
     
   ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099642433/mceclip1.png)
