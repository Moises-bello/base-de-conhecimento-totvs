---
article_id: 360053817373
category: Materiais - Compras (SIGACOM)
content_hash: 55b443a31d2908d755823b61ef0e5b737c00b8c43f1ae37d30b7feae90117b72
fetched_at: '2026-06-28T22:41:12.921724+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM  - Configuração dos parâmetros
  da Sugestão de Compras MATA297
type: support-article
updated_at: '2022-05-16T21:12:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053817373-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Configura%C3%A7%C3%A3o-dos-par%C3%A2metros-da-Sugest%C3%A3o-de-Compras-MATA297
---

**Dúvida**

O que representa os parâmetros da sugestão de compras.  
  
**Ambiente**

Protheus– Compras – A partir da versão 11.80  
  
**Solução**

A configuração dos parâmetros da sugestão de compras  devem ser realizadas de acordo com o tempo em que deseja que seja gerada a demanda para a sugestão.

*Obs: Os parâmetros devem ser preenchidos após a execução da rotina Gera Demanda ( MATA295 ).*

|  |  |  |
| --- | --- | --- |
| ***Parâmetro*** | ***Uso*** | ***Opções*** |
| ***MV\_PAR01: Dias p/ Sugestão?*** | Quantidade de dias para cálculo de sugestão | quantidade de dias Ex: 120 |
| ***MV\_PAR02: Classf. de Custo ?*** | Ao Gerar Demanda isso é definido a partir do Custo Stand. do Produto e os parâmetros utilizados na rotina Gerar Demanda | 1 - Alta ; 2 - Média; 3-Baixa ; 4 - Todos |
| ***Cust. Stand***. (Produto) MENOR que "Class. Custo Med. De ?"(Gerar Demanda) a sugestão de compra será definida como custo "3 - Baixa" |
| ***Cust. Stand***. (Produto) MAIOR que "Class. Custo Med. Ate ?"(Gerar Demanda) a sugestão de compra será definida como custo "1 - Alta" |
| ***Cust. Stand.*** (Produto) ENTRE  "Class. Custo Med. De ?"(Gerar Demanda) e"Class. Custo Med. Ate ?"(Gerar Demanda) a sugestão de compra será definida como custo "2 - Média" |
| ***MV\_PAR03: Tipo Preço ?*** | O Tipo de Preço será responsável por definição do valor total definido por: Quantidade Sugerida multiplicado por Preço Standart(Custo Stand. B1\_CUSTD ) ou Reposição(Ult. Preço B1\_UPRC ) ou Preço de Venda(Preco Venda B1\_PRV1 ) | 1- Preço Standart ; 2 - Reposição ; 3 - Preço de Venda |
| ***MV\_PAR04: ABC Venda/Custo*** | Ao Gerar Demanda isso é definido a partir dos parâmetros "% Class 'A' Venda ?", "% Class 'B' Venda ?", "% Class 'A' Custo ?", "% Class 'B' Custo ?". | Asterisco "\*" irá fazer um filtro avaliando todos os tipo de ABC Venda/Custo "AA/AB/AC/BA/BB/BC/CA/CB/CC/" |
| O primeiro caractere é definido pelo ABC Venda | ***Caso queira avaliar o ABC Venda/Custo específicos, necessário adicionar o tipo de ABC Venda/Custo sem Barra, pois é adicionada pelo sistema. Ex: AAABACBABBBC*** |
| O segundo caractere é definido pelo ABC Custo |  |
| Caso no momento em que foi gerado a demanda estivesse tudo 0 a sugestão de compra será gerada automaticamente como "CC/" |  |
| ***MV\_PAR05: Importado ?*** | Irá adicionar apenas produtos importados caso o parâmetro esteja configurado como "1 - Sim" ou não importados caso o parâmetro esteja configurado como "2 - Não". | 1 - Sim ; 2 - Não |
| ***MV\_PAR06: Grupo de ?*** | Grupo inicial a ser considerado na filtragem do cadastro do produto (SB1). | Definido por conteúdo em banco |
| Definido pelo grupo de estoque do produto (B1\_GRUPO). |
| ***MV\_PAR07: Grupo Ate ?*** | Grupo final a ser considerado na filtragem do cadastro do produto (SB1). | Definido por conteúdo em banco |
| Definido pelo grupo de estoque do produto (B1\_GRUPO). |
| ***MV\_PAR08: Produto de ?*** | Produto inicial a ser considerado na filtragem do cadastro de sugestão de compra (SBL). | Definido por conteúdo em banco |
| Produto de criação de sugestão de compra pelo gerar demanda (BL\_PRODUTO). |
| ***MV\_PAR09: Produto ate ?*** | Produto final a ser considerado na filtragem do cadastro de sugestão de compra (SBL). | Definido por conteúdo em banco |
| Produto de criação de sugestão de compra pelo gerar demanda (BL\_PRODUTO). |

***Saiba Mais :***

[MP - SIGACOM - Como utilizar a rotina de Gerar Demanda MATA295 ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053860653)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
