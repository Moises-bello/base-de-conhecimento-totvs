---
article_id: 360015918631
category: RH - Rescisão
content_hash: 93d451713e4983022984420effbebe073cb58cd0600141221fc1c0210ddeb6f0
fetched_at: '2026-06-28T22:43:50.981593+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: MP - GPE - Como gerar o FGTS pedido de demissão e folha de pagamento
type: support-article
updated_at: '2025-05-09T21:12:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015918631-MP-GPE-Como-gerar-o-FGTS-pedido-de-demiss%C3%A3o-e-folha-de-pagamento
---

**Dúvida** **GPEM040**: Como gerar o FGTS pedido de demissão e folha de pagamento?  
  
 **Ambiente**Protheus - Gestão de Pessoal - Versão 12  
  
**Solução**Quando ocorrer uma rescisão por pedido, deverá ser recolhido o FGTS junto com o FGTS folha, até o dia 07 de cada mês.   
  
O FGTS para pagamento mensal, se constitui em: FGTS da folha + FGTS mês rescisão + FGTS 13º rescisão (esses dois últimos apenas para os pedidos de desligamento), os demais tipos de desligamento considerarão o FGTS com recolhimento através da GRRF - Guia de Recolhimento Rescisório do FGTS.  
  
1. Deve ter cadastrado a verba com ID 0018.  
  
2. No cadastro de **Tipo de Rescisão (Tabela S043)** deve estar com os campos **FGTS Mês Anterior**, **FGTS Mês da Rescisão**, **FGTS Multa 40%**  deve estar = (igual a) N - (não).  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360011023411/mceclip0.png)  
  
3. Efetuar o cálculo da rescisão e conferir se o valor do FGTS foi gerado na verba com ID 0018.  
  
4. Integrar o roteiro RES.

5. Efetuar o cálculo da folha, e conferir o valor do FGTS.  
  
6. Gerar o **Relatório de Folha de Pagamento (GPER040).**  
  
7. Fazer a **Definição de Título**, cadastrando no título a verba de ID 0018. **GPEM640 > Miscelânea > Títulos > Definição:**  
![](https://totvssuporte.zendesk.com/attachments/token/wofBjfFhBIfKI5ZxYjqJZuqcm/?name=inline458273532.png)

![](https://totvssuporte.zendesk.com/attachments/token/QAKaNzhyJ79njNzmJtaVe6uz5/?name=inline-522550809.png)  
8. Efetuar a **geração do título**.**GPEM650 > Miscelânea > Títulos > Geração**.

9. Conferir o valor do título na rotina de **Manutenção de Títulos**. **GPEM660 > Miscelânea > Títulos > Manutenção**. O valor gerado deve ser o mesmo demonstrado no relatório **GPER040** na verba com ID 0018.

**Importante**  
Para que o sistema gere o título de FGTS, considerando o FGTS Folha e FGTS do Pedido de Demissão, deverá ser gerada a verba com identificador de cálculo 0018, que é o mesmo do FGTS da Folha, com isso o sistema considerará tanto na SEFIP como no título o pedido de demissão.  
  
**Saiba Mais**  
Para adquirir mais informações acesse o *link*: [MP - GPE0870 - Como deve ser o recolhimento de FGTS quando ocorrer rescisão por Pedido de Demissão, e como gerar esse título de pagamento para o financeiro?](http://tdn.totvs.com/pages/viewpage.action?pageId=407111097)
