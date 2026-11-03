---
article_id: 4416171562775
category: Gestão de Armazenagem (WMS)
content_hash: b13a7014f75d65b781a8ebd8fabd82b0247626bb2fb567e7cdd4fe240fb68f78
fetched_at: '2026-06-28T22:45:48.023653+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Determinação dos valores dos níveis dos
  endereços
type: support-article
updated_at: '2021-12-16T22:52:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416171562775-Log%C3%ADstica-Linha-Protheus-WMS-Determina%C3%A7%C3%A3o-dos-valores-dos-n%C3%ADveis-dos-endere%C3%A7os
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**De que forma é feito o cálculo dos níveis dos endereços dos armazéns no **WMS (Linha Protheus) - Warehouse Management System**?  
  
**Ambiente**TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS) - Todas as versões  
  
**Solução**Os níveis de endereço são usados para que um **endereçamento de um produto** seja feito próximo a outro endereço que já possua este mesmo produto.

1. Primeiramente, é verificada a configuração do na tela de cadastro de **WMSA160** - **Configuração de Código de Endereço**.  
   Como estão distribuídos nos níveis e a formação deste utilizada para obter o código de endereço.
2. Tomando como exemplo o Endereço **R020305** tem-se:  
   Rua: R02  
   Prédio: 03  
   Nível: 05
3. Para calcular os valores dos níveis 1, 2 e 3, respectivamente, é usada a seguinte tabela:  

   |  |  |  |  |  |  |  |  |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | **Conteúdo** | **Valor** | **Conteúdo** | **Valor** | **Conteúdo** | **Valor** | **Conteúdo** | **Valor** |
   | 0 | 01 | A | 11 | K | 21 | U | 31 |
   | 1 | 02 | B | 12 | L | 22 | V | 32 |
   | 2 | 03 | C | 13 | M | 23 | W | 33 |
   | 3 | 04 | D | 14 | N | 24 | X | 34 |
   | 4 | 05 | E | 15 | O | 25 | Y | 35 |
   | 5 | 06 | F | 16 | P | 26 | Z | 36 |
   | 6 | 07 | G | 17 | Q | 27 |  |  |
   | 7 | 08 | H | 18 | R | 28 |  |  |
   | 8 | 09 | I | 19 | S | 29 |  |  |
   | 9 | 10 | J | 20 | T | 30 |  |  |

   Cada caracter do nível é substituído pelo respectivo valor da tabela, chegando-se assim ao **valor do nível**.  
   Tomando o exemplo acima tem-se:  
   Rua: R02 🡪 (R = ‘28’) + (0 = ‘01’) + (1= ‘02’) = 280102  
   Prédio: 03 🡪 (0 = ‘01’) + (3 = ‘04’) = 104  
   Nível: 05 🡪 (0 = ‘01’) + (5 = ‘06’) = 106  
   \* Por ser um valor numérico, os zeros à esquerda são suprimidos.
4. A Rotina **WMSA575 - Recálculo de Nível de Endereço**  é a responsável por efetuar este cálculo para todos os endereços. Ela não possui tela, apenas exibe uma pergunta que, se confirmada, dá início ao recálculo.
5. Na tela **MATA015 - Endereço Físico** , na aba **WMS** os conteúdos dos campos **Vl. Niv 1** - Valor Nível 1, **Vl. Niv 2** - Valor Nível 2  e **Vl. Niv 3** - Valor Nível 3 são ajustados após o cálculo.
