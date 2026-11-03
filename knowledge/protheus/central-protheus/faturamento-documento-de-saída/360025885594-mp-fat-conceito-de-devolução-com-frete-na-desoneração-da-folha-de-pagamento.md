---
article_id: 360025885594
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 820e19340daa2a3de12a4cf6b78df7389e60b581c7bd7426c24adf967dd4e293
fetched_at: '2026-06-28T22:38:45.158208+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: MP - FAT - Conceito de Devolução com Frete na Desoneração da Folha de Pagamento
type: support-article
updated_at: '2021-04-28T15:13:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025885594-MP-FAT-Conceito-de-Devolu%C3%A7%C3%A3o-com-Frete-na-Desonera%C3%A7%C3%A3o-da-Folha-de-Pagamento
---

**Dúvida**

Conceito de Devolução com Frete na Desoneração da Folha de Pagamento.  
  
**Ambiente**

Microsiga Protheus -  a partir da versão 12.  
  
**Solução**

Qual o tratamento que o sistema realiza na devolução de uma venda Desonerada nas tabelas SV5 e S033?

**Para um melhor entendimento do calculo, segue um exemplo prático**

1) Realizado uma NF desonerada de saída com valor R$ 100,00 + 10,00 digitado no campo de Frete (após rodar o programa GPEM013 tabela SV5 estará com valor de R$ 110,00);

2) Realizado uma Devolução da NF no compras no mesmo mês com valor R$ 100,00 + 10,00 digitado no campo de Frete - sistema não alimenta o frete automaticamente na devolução por entender que o frete pode ser outro valor (após rodar o programa GPEM013 tabela SV5 estará com valor de R$ 110,00)

Após rodar o programa GPEM013 (Modulo Gestão de Pessoal - Desoneração da Folha) o sistema alimenta a tabela SV5 e atualiza a tabela S033  
  
Retorno da operação na tabela SV5

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041153253/mceclip0.png)  
  
Retorno da operação na tabela S033

![](https://totvssuporte.zendesk.com/attachments/token/jKBIy8E9jsTyDSYZZ2uzrfAup/?name=inline-2109093123.png)​  
  
**Conclusão:**

**Receita Bruta** é o valor Bruto, isto é, total da saída = R$ 110,00

**Valor das Exclusões** é o valor Bruto da Devolução (devolução no compras) = R$ 110,00

Um valor menos o outro fez com que a base de calculo fosse zerada e, desta forma, a contribuição devida zerada também.  
  
**Importante** : Para que o calculo da desoneração da folha sempre esteja atualizado é necessário que os programas **FATXFUN** e **GPEM013** esteja atualizados.
