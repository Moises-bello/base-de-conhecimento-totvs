---
article_id: 1500005763142
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 02a9c7a50af856e93661d63991b4c2734e0fcda9fd6d3f93dc703ffbe58199a3
fetched_at: '2026-06-28T22:38:38.640318+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Uso do Campo
  C5_TXMOEDA
type: support-article
updated_at: '2024-07-17T13:05:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005763142-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Uso-do-Campo-C5-TXMOEDA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Qual o conceito de uso do campo Campo C5\_TXMOEDA?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - todas as versões.  
  
**Solução**No módulo faturamento é realizado as seguintes configurações e possui as premissas:  
  
**1 -** Para que o sistema gere o titulo na moeda corrente (Real) ou na moeda do pedido de venda(Dólar) é necessário verificar a configuração do parâmetro **MV\_MOEDTIT**;  
  
**2 -** A primeira moeda sempre será **REAL,** sendo que  no pedido de venda nunca haverá conversão de moeda. Deve ser preenchido no cadastro do cliente e no pedido de venda, os campos **C5\_MOEDA** e **A1\_MOEDALC**, de forma manual,  de acordo com a moeda desejada;  
  
**3 -** A conversão será apresentada através das tabelas **SD2 e SF2**.  
  
**4 -** Na tabela **SE1**, o campo **E1\_VALOR** apresenta o valor original do titulo e o campo **E1\_VLCRUZ** apresenta o valor em ***moeda corrente***;  
  
**5 -** O sistema não acata a taxa definida no campo **C5\_TXMOEDA**, se houver interesse é necessário utilizar ponto de entrada:

* **M460PROC -** É chamado logo após efetuar a seleção dos registros da tabela SC9 - Pedidos Liberados):  **<https://tdn.totvs.com/x/xIRn>**
* **M460FIM -** Gravação da NF saída: **<https://tdn.totvs.com/x/tIRn>**

*Não há por padrão pontos de entrada específicos para o cálculo de taxa através do pedido de vendas. Existem os pontos de entradas, mas é no processamento da nota fiscal (geração da nota fiscal [SD2/SF2]).*

**6 -** O sistema só utiliza a taxa definida no cadastro de moedas (**SM2 - Moedas do Sistema**). A taxa de conversão utilizada é a taxa do dia da preparação do documento e não da inclusão do pedido de venda.  
  
  
**7 -** Campo **E1\_TXMOEDA** não grava a taxa na preparação do documento de saída para ambiente Brasil.

**Saiba mais: [Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Uso Moeda Modulo Faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000731448-MP-FAT-Uso-Moeda-Modulo-Faturamento)**
