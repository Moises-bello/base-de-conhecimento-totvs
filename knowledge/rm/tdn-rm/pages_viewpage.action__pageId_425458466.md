---
content_hash: 7eababa19e085cb1d17ff98fd0cd44284d0cdcd1b6f9b72798d6d35f2ed2037f
fetched_at: '2026-06-29T00:09:30.690082+00:00'
page_id: '425458466'
product: rm
source: tdn-rm
title: Informações Estratégicas - Totais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458466
version: 2
---

**Informações Estratégicas - Totais**

---

Este anexo é um resumo (somatório) dos valores obtidos pelas consultas representadas por alguns outros anexos: Faturado, Pago, Aberto, Atraso, Mensal. o sistema realiza a soma dos valores faturados, pagos, em aberto e em atraso das empresas (mesmo quando a sentença é personalizada) e exibe na tela os valores. Para que os valores sejam exibidos corretamente é necessário seguir algumas regras na criação da sentença.   
   
Verifique nos Parâmetros do TOTVS Aprovações e Atendimento | Informações Financeiras. Note que em todos os itens citados existe uma coluna chamada VALOR. Esta coluna representa um valor em ponto flutuante de uma parcela em aberto/atraso ou valor faturado/pago, assim por diante, isto é, representa um valor significativo para controle interno do cliente ou uma tomada de decisão.  
Caso o cliente utilize consultas personalizadas para tais itens e tais sentenças não possuam um campo (no SELECT) chamado VALOR então a funcionalidade de Totais pode não se comportar muito bem e um ajuste nas consultas personalizadas será necessário. O sistema simplesmente busca e executa as sentenças SQLs dos outros itens e apresenta os totais representados pelos campos VALOR.  
                   SELECT                    (SELECT ROUND(SUM(Faturado.Valor), 2) Faturado FROM (" + sqlFaturado + ") Faturado) TOTAL\_FATURADO,                     (SELECT ROUND(SUM(Pago.Valor), 2)     Pago     FROM (" + sqlPago + ")     Pago)     TOTAL\_PAGO,                         (SELECT ROUND(SUM(Aberto.Valor), 2)   Aberto   FROM (" + sqlAberto + ")   Aberto)   TOTAL\_ABERTO,                    (SELECT ROUND(SUM(Atraso.Valor), 2)   Atraso   FROM (" + sqlAtraso + ")   Atraso)   TOTAL\_ATRASO,                    (SELECT ROUND(SUM(Mensal.Valor), 2)   Mensal   FROM (" + sqlMensal + ")   Mensal)   FATURADO\_MENSAL   
**Observação.:**  
A consulta SQL que retorna as informações pode ser personalizada e setada nos Parâmetros Gerais do Sistema. Clique no aqui para maiores informações.
