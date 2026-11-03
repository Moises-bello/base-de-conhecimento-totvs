---
article_id: 4403610578071
category: Meu RH - Pagamento
content_hash: c3705917f45b65207a286e834603e856f715c2ddbcf631b419cc2ccd10e39cec
fetched_at: '2026-06-28T22:47:33.892789+00:00'
product: rm
section_id: 1500000835221
source: central-rm
title: RH - RM - Meu RH - Como restringir a visualização dos funcionários no Histórico
  Salarial a determinados aumentos
type: support-article
updated_at: '2025-02-03T12:18:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403610578071-RH-RM-Meu-RH-Como-restringir-a-visualiza%C3%A7%C3%A3o-dos-funcion%C3%A1rios-no-Hist%C3%B3rico-Salarial-a-determinados-aumentos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24084542704663) Tempo aproximado para leitura: 00:01:45 min**

**Dúvida**Como restringir a visualização dos funcionários no Histórico Salarial a determinados aumentos?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.17  
  
**Solução**Para bloquear temporariamente no Meu RH, do funcionário visualizar um novo aumento, basta acessar o RM - Folha de Pagamento / Configurações / Parametrizador / RM Portal / Edite o Quiosque do funcionário / Demonstrativo de Pagamento:  
**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403610433559)**

**Exemplos:** Foi aplicado um aumento salarial em decorrência de promoção ao funcionário via Folha de Pagamento, porém ele ainda não poderá visualizar via Meu RH ou, foi aplicado um aumento por Dissídio, porém os funcionários ainda não podem visualizar o aumento.

**Mostrar Salário com data de mudança até:**

O parâmetro serve para definir a data limite das alterações salariais a serem exibidas no Meu RH, o parâmetro é válido para funcionários visualizarem seu Histórico Salarial.  
  
Para um melhor entendimento, segue um exemplo:  
-O salário do funcionário Itamar era R$3.192,80 e foi alterado no dia 01/06/2021 para R$4.000,00 em decorrência de um Dissídio:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403610493975)  
  
Histórico Salarial:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403610498455)  
  
Porém eu não quero que o funcionário veja neste momento o aumento, portanto, basta eu preencher no parâmetro do Quiosque, a data: 01/05/2021.Dessa forma, quando o funcionário acessar o Meu RH / Histórico Salarial, não verá o novo salário:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403625763863)  
  
Quando desejar liberar a visualização do novo salário, basta retornar ao parâmetro do quiosque e alterar a data para 01/06/2021.
