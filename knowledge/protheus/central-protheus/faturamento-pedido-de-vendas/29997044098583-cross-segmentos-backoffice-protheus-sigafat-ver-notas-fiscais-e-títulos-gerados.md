---
article_id: 29997044098583
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 72bcfbe4dc8a97f04072b9153754aa115ae7d93def782c77a777d9cd327bd031
fetched_at: '2026-06-28T22:38:42.577797+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Ver notas fiscais e títulos
  gerados pelo pedido de venda
type: support-article
updated_at: '2025-02-17T11:13:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29997044098583-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Ver-notas-fiscais-e-t%C3%ADtulos-gerados-pelo-pedido-de-venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29996996691991) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como ver notas fiscais e títulos gerados pelo pedido de venda?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**1 - Entre no pedido de venda (MATA410)

* Caminho: Módulo 05 > Atualizações > Pedidos > Pedidos de venda

2 - Posicione no BROWSE no pedido de venda que quer ver quais títulos e notas fiscais sairam dele

3 - Aperte o botão branco superior "Visualizar"

4 - Vá no botão branco superior "Outras ações > Tracker"

5 - Vá no botão branco na direita "Rastrear"

6 - No menu esquerdo, expanda mais as listas e opções. Assim, é possível ver a nota fiscal de saída gerada, o título gerado e os itens faturados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29996996694807)

No exemplo acima, a nota fiscal de saída gerada foi a de numeração "000003" e série "1" e o título é o

* Triângulo cinza = Nota fiscal gerada
* Triângulo amarelo = Título gerado

7 - Para ver o registro completo, clique no triângulo e vá em "Visualizar"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29996996700311)![](https://centraldeatendimento.totvs.com/hc/article_attachments/29997114326935)

Resultado visualizando o título gerado (triângulo amarelo):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29997141515031)

Resultado visualizando o título gerado (triângulo cinza):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29997141516823)

**OBS 1:** Os títulos ficam na tabela SE1 ou SE2 e podem ser vistos nas rotinas "FINA740 - Funções Contas a Receber" e "FINA750 - Funções Contas a Pagar"

**OBS 2:** As notas fiscais de saída ficam na tabela SD2 e SF2 e podem ser vistas na rotina "MATC090 - Consulta de notas fiscais de saída"
