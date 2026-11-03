---
article_id: 29370920808215
category: Relatórios
content_hash: bd1ce6b4faddc6707f44c0c2f1471bd693324eaf0c33cb3d46b5cb7026778ea1
fetched_at: '2026-06-28T22:46:39.229890+00:00'
product: rm
section_id: 1500000861642
source: central-rm
title: RH - RM - PTO - Como é o cálculo do Gráfico de Absenteísmo
type: support-article
updated_at: '2026-04-17T17:46:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29370920808215-RH-RM-PTO-Como-%C3%A9-o-c%C3%A1lculo-do-Gr%C3%A1fico-de-Absente%C3%ADsmo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29370920790423) Tempo aproximado para leitura: **00:00:40 min**  
  
**Dúvida**  
Como é efetuado o cálculo de absenteísmo no sistema para geração do Gráfico de Absenteísmo?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 12.  
  
**Solução**  
Para obter a fórmula do cálculo de absenteísmo, acesse a documentação [**Gráfico de Absenteísmo**](https://tdn.totvs.com/pages/viewpage.action?pageId=452718996)  
  
**Saiba Mais**  
Segue abaixo um exemplo da query de uma base SQL onde é efetuado o cálculo/geração do gráfico:  
  
SELECT 1 CODSECAO, AAFHTFUN.CHAPA CHAPA, (CONVERT(FLOAT, ( CONVERT(NUMERIC, SUM(AAFHTFUN.FALTA)) / 60 + CONVERT(NUMERIC, SUM(AAFHTFUN.ATRASO)) / 60 + CONVERT(NUMERIC, SUM(AAFHTFUN.ABONO)) / 60 ) / (CONVERT(NUMERIC, SUM(AAFHTFUN.BASE)) / 60) ) \* 100.00) AS ABSENT FROM AAFHTFUN(NOLOCK), PFUNC(NOLOCK), PSECAO(NOLOCK)  
WHERE (AAFHTFUN.CODCOLIGADA = PFUNC.CODCOLIGADA) AND  
(AAFHTFUN.CHAPA = PFUNC.CHAPA) AND  
(PFUNC.CODCOLIGADA = PSECAO.CODCOLIGADA) AND  
(PFUNC.CODSECAO = PSECAO.CODIGO) AND  
(AAFHTFUN.CODCOLIGADA = '**INFORMAR A COLIGADA**') AND  
(AAFHTFUN.DATA >= '**INFORMAR A DATA INÍCIO DO PERÍODO**') AND  
(AAFHTFUN.DATA <= '**INFORMAR A DATA FIM DO PERÍODO**') AND (AAFHTFUN.BASE > 0) AND (((PFUNC.CODCOLIGADA = '**INFORMAR A COLIGADA'**) AND ( (CODSITUACAO IN ('A','C','D','E','F','G','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z')) AND (PFUNC.CODTIPO IN ('A','B','C','D','E','F','I','M','N','O','P','R','S','T','U','V','W','X','Z')) AND (1=1) AND ((1 = 1)))) AND ((PFUNC.CODSECAO LIKE '%%%%%%') )) AND (EXISTS (SELECT 1 FROM APARFUN(NOLOCK)  
WHERE CODCOLIGADA = PFUNC.CODCOLIGADA AND  
CHAPA = PFUNC.CHAPA)) GROUP BY AAFHTFUN.CHAPA ORDER BY AAFHTFUN.CHAPA

**Exemplo:**

![img1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29371057337495)

![img2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29371057340695)

**Importante**

O sistema efetua o cálculo a partir da média ponderada. Ou seja, é mais precisa, pois leva em conta o total de horas previstas de trabalho, demonstrando o cenário real mesmo quando os funcionários têm cargas horárias diferentes.  
  
Exemplo Prático: Média Simples vs. Média Ponderada - Exemplo de cálculo com Estoque

Para entender como o sistema calcula o valor dos seus produtos, imagine que você fez duas compras de **Parafusos** em momentos diferentes:

* **Compra A:** 100 unidades a **R$ 1,00** cada.
* **Compra B:** 10 unidades a **R$ 2,00** cada (o preço subiu).

**Cálculo Passo a Passo de média ponderada:**

1. **Multiplique** o Preço Unitário pela Quantidade de cada compra.
2. **Some** os resultados dessas multiplicações (Valor Total Acumulado).
3. **Divida** esse Valor Total pela soma de todas as Quantidades.

### 1. Se o sistema usasse Média Simples:

A média simples ignora a quantidade e olha apenas para os preços unitários.

* Cálculo: (1,00 + 2,00) dividido por 2 = R$ 1,50
* **O problema:** O sistema diria que cada parafuso no seu estoque vale R$ 1,50. Mas isso está errado, pois você tem muito mais parafusos que custaram barato (R$ 1,00) do que parafusos caros. Isso "mentiria" o valor real do seu patrimônio.

### 2. Como o RM calcula (Média Ponderada):

O sistema leva em conta a quantidade (o peso) de cada compra para chegar ao valor real investido.

* **Passo 1 (Valor total em dinheiro):**

  + 100 unidades x R$ 1,00 = R$ 100,00
  + 10 unidades x R$ 2,00 = R$ 20,00
  + **Total Investido:** R$ 120,00
* **Passo 2 (Quantidade total de itens):**

  + 100 + 10 = **110 unidades**
* **Passo 3 (Cálculo do Custo Médio):**

  + R$ 120,00 (dinheiro) dividido por 110 (unidades) = **R$ 1,09**

### Conclusão:

> No exemplo acima, a **Média Ponderada (R$ 1,09)** é muito mais próxima do preço da primeira compra, porque você comprou uma quantidade muito maior naquela vez. A **Média Simples (R$ 1,50)** estaria incorreta para o controle financeiro, pois inflaria o valor do seu estoque artificialmente.

**Saiba Mais:**  
Para importar a estrutura do relatório no sistema, acesse: [RH - RM - PTO - Importar gráfico de absenteísmo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014853512-RH-RM-PTO-Importar-gr%C3%A1fico-de-absente%C3%ADsmo)  
Para gerar o relatorio acesse: [RH - RM - PTO - Como gerar o Gráfico de Absenteísmo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30564823524887)
