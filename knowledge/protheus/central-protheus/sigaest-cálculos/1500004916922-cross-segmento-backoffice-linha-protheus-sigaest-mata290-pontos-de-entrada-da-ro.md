---
article_id: 1500004916922
category: SIGAEST - CÁLCULOS
content_hash: 6d80d626c0429e674c3691a6ef1a4cae46de7d53c4b199c985b572fe0b897561
fetched_at: '2026-06-28T22:39:04.148064+00:00'
product: protheus
section_id: 1500001550082
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA290 - Pontos de
  Entrada da rotina Consumo e Indicador
type: support-article
updated_at: '2025-03-12T12:23:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004916922-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA290-Pontos-de-Entrada-da-rotina-Consumo-e-Indicador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19639804844951) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

Quais os Pontos de Entrada relacionados à rotina MATA290 - Consumo e Indicador?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Veja abaixo os Pontos de Entrada relacionados à rotina MATA290 - Consumo e Indicador clique no nome do Ponto de Entrada para acessar a documentação de cada Ponto listado

|  |  |  |
| --- | --- | --- |
| **Nome:** | **Título:** | **Descrição:** |
| **[M290QSB1](https://tdn.totvs.com/pages/viewpage.action?pageId=651919664)** | Valida produtos no processamento e gravação | O Ponto de Entrada é executado na montagem da query no processamento do arquivo de Demandas (SB3)(exceto as funções A290CalCon e A290AjuLot) com o cadastro de Produtos (SB1), ANTES do cálculo para gravação dos valores calculados para o Lote Econômico. Deve ser utilizado para validar produtos (ref. ao arquivo SB1) no processamento e gravação. O retorno do ponto de entrada será adicionado à query e deverá ser uma expressão lógica (tipo caracter) e válida (não utilizar 'Order By' pois este será adicionado à query após o ponto de entrada). |
| **[M290QSD2](https://tdn.totvs.com/pages/viewpage.action?pageId=647445305)** | Valida itens para o recálculo do custo Médio mensal | LOCALIZAÇÃO : Executado na função A290CalCon (Recálculo do consumo médio do mês).  EM QUE PONTO : O Ponto de entrada é executado no processamento do arquivo Itens das NFs de Saída/Dev. Vendas (SD2), na montagem da query, antes de sua execução e deve ser utilizado para validar itens das notas que farão parte do recálculo do consumo médio do mês. |
| **[A290CSD2](https://tdn.totvs.com/pages/viewpage.action?pageId=236427335)** | Validação do itens das Nfs de Saída | LOCALIZAÇÃO : Este Ponto de Entrada está localizado na função A290CalCon (Recálculo do consumo médio do mês)  EM QUE PONTO : É executado DURANTE o cálculo; seu objetivo é que o usuário possa validar itens das NFs de Saída (SD2), que farão parte do recálculo do consumo médio do mês. |
| **[M290QSD1](https://tdn.totvs.com/pages/viewpage.action?pageId=647445183)** | Valida itens das notas de consumo médio mensal | LOCALIZAÇÃO : Executado na função A290CalCon (Recálculo do consumo médio do mês).  EM QUE PONTO : O Ponto de entrada é executado no processamento do arquivo Itens das NFs de Entrada (SD1), na montagem da query, antes de sua execução e deve ser utilizado para validar itens das notas que farão parte do recálculo do consumo médio do mês. |
| **[MT290SD1](https://tdn.totvs.com/display/PROT/MT290SD1+-+Valida+itens+das+NFs+de+Entrada+SD1+-+Estoque+e+Custos+-+P12)** | Valida itens das NFs de Entrada SD1 | LOCALIZAÇÃO : Este Ponto de Entrada está localizado na função A290CalCon (Recálculo do consumo médio do mês)  EM QUE PONTO : É executado DURANTE o cálculo; seu objetivo é que o usuário possa validar itens das NFs de Entrada (SD1), que farão parte do recálculo do consumo médio do mês. |
| **[M290QSD3](https://tdn.totvs.com/pages/viewpage.action?pageId=647445402)** | Valida movimentos para consumo médio do mês | LOCALIZAÇÃO : Executado na função A290CalCon (Recálculo do consumo médio do mês).  EM QUE PONTO : O Ponto de entrada é executado no processamento do arquivo de Movimentações Internas (SD3), na montagem da query, antes de sua execução e deve ser utilizado para validar os movimentos que farão parte do recálculo do consumo médio do mês. |
| **[MT290SD3](https://tdn.totvs.com/pages/viewpage.action?pageId=572504431)** | Valida os Movimentos Internos SD3 que farão parte do recálculo do consumo médio do mês | LOCALIZAÇÃO : Este Ponto de Entrada está localizado na função A290CalCon (Recálculo do consumo médio do mês)  EM QUE PONTO : É executado DURANTE o cálculo; seu objetivo é que o usuário possa validar os Movimentos Internos (SD3), que farão parte do recálculo do consumo médio do mês. |
| **[A290CONS](https://tdn.totvs.com/pages/viewpage.action?pageId=236422296)** | Permite manipulação do consumo mensal para o produto | LOCALIZAÇÃO : Este Ponto de Entrada está localizado na função A290CalCon (Recálculo do consumo médio do mês)  EM QUE PONTO : É executado ANTES da gravação do consumo mensal calculado pelo sistema e seu objetivo é que o usuário possa manipular a quantidade do consumo mensal a ser gravado para o produto. |
| **[A290CALP](https://tdn.totvs.com/pages/viewpage.action?pageId=236422191)** | Manipula número de meses para o cálculo da média | LOCALIZAÇÃO : Executado na função A290CalNor, que realiza o cálculo normal da média de consumos (utiliza os pesos).  EM QUE PONTO : O ponto de entrada 'A290CALP' é executado antes do cálculo da média, e deve ser utilizado para manipular o número de meses considerados para cálculo, entre os meses inicial de consumo (B1\_CONINI) e o mês referência para o cálculo (desde que o ponto de entrada retorne um array). |
| **[A290CALL](https://tdn.totvs.com/pages/viewpage.action?pageId=236422158)** | Manipula valor do lote econômico para o produto | LOCALIZAÇÃO : Este Ponto de Entrada está localizado na função A290CalLot (Cálculo do Lote Econômico).  EM QUE PONTO : É executado APÓS o cálculo; seu objetivo é que o usuário possa manipular o valor do lote econômico calculado para o produto. |
| **[A290CAPP](https://tdn.totvs.com/pages/viewpage.action?pageId=236422244)** | Permite manipulação do valor do ponto de pedido | LOCALIZAÇÃO : Este Ponto de Entrada está localizado na função A290CalLot (Cálculo do Lote Econômico).  EM QUE PONTO : É executado APÓS o cálculo e ANTES da gravação do ponto de pedido; seu objetivo é que o usuário possa manipular o valor do ponto de pedido calculado para o produto. |
| **[A290ABC](https://tdn.totvs.com/pages/viewpage.action?pageId=236422113)** | Permite manipulação do registro da SB3 | LOCALIZAÇÃO : Este Ponto de Entrada está localizado na função A290CalLot (Cálculo do Lote Econômico).  EM QUE PONTO : É executado APÓS a gravação da CLASSE. Com o arquivo de demandas (SB3) locado e posicionados: Cad. de Produtos (SB1) ou, a partir da MP8.11, indicadores do produto (SBZ), permite a manipulação do registro do SB3. |
| **[A290AJUL](https://tdn.totvs.com/pages/viewpage.action?pageId=236422140)** | Manipula valores calculados do lote a serem ajustados | LOCALIZAÇÃO : Este Ponto de Entrada está localizado na função A290AjuLot (Ajusta o lote econômico pelo valor disponível para compras).  EM QUE PONTO : É executado APÓS o cálculo; seu objetivo é que o usuário possa manipular os valores calculados do lote econômico que serão ajustados pela rotina A290AjuLot(). |
| **[MTA290FIL](https://tdn.totvs.com/pages/releaseview.action?pageId=6087818)** | Insere condição de filtro antes do cálculo - Lote Econômico | LOCALIZAÇÃO : (Quando ativado o botão) é executado na função Ma290Filtro(), chamada por: A290CalCon (Recálculo do consumo médio do mês); A290CalNor (Cálculo normal da média de consumos - utiliza os pesos); A290CalMin (Cálculo da média de consumos - utiliza o conceito dos mínimos quadrados); A290CalLot (Cálculo do Lote Econômico); A290AjuLot (Ajusta Lote Econômico)  EM QUE PONTO : Este Ponto de Entrada está localizado na função A290Menu (Processa a string das opções de processamento). |
| **[A290PEES](https://tdn.totvs.com/pages/releaseview.action?pageId=572506679)** | Permite manipular o valor do estoque de segurança. | O Ponto de Entrada a290PEES permite customizar o calculo do estoque de segurança atualizando este calculo no produto. |

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cálculos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550082-SIGAEST-C%C3%81LCULOS)*
