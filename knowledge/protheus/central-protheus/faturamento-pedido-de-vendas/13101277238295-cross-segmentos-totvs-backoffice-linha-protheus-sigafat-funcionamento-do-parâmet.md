---
article_id: 13101277238295
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 95ba99c66f0669198ed6e74216cc68a3c0a3e764de2345e2254ac2478810c83c
fetched_at: '2026-06-28T22:38:42.734275+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Funcionamento
  do parâmetro MV_DATAPD3
type: support-article
updated_at: '2023-03-20T17:14:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13101277238295-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Funcionamento-do-par%C3%A2metro-MV-DATAPD3
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Qual o conceito e como utilizar o parâmetro **MV\_DATAPD3**?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**O parâmetro **MV\_DATAPD3** define um número de dias **retroativos** na **pesquisa** de notas com **poder de/em terceiros** na linha do item do Pedido de Vendas, ao pressionar a tecla **[F4]** no campo **"Quantidade (C6\_QTDVEN)**" é gerada uma **interface gráfica** para digitação do intervalo de data de pesquisa das notas de poder de terceiros.

Desta forma, fica disponível a opção para pesquisar qualquer intervalo de datas para retorno da nota, **otimizando a performance** da rotina. A data inicial para pesquisa carregada na tela é definida como a Data Base do sistema menos o número de dias definido no parâmetro **MV\_DATAPD3**.

**MV\_DATAPD3** = 0 (desativado)

**MV\_DATAPD3** = 1+ (ativado)

**Exemplo**

Data base do sistema é **DDATABASE = 15/03/2023** e **MV\_DATAPD3 = 10.**

* Data inicial exibida na interface de pesquisa: 05/03/2023 (Data base - 10)
* Data final exibida na interface de pesquisa: 15/03/2023 (Data base)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13100910930583)

**Importante:** Os campos com as datas para pesquisa são editáveis, sendo o parâmetro utilizado apenas para carregamento prévio da data inicial.

Ao pressionar o botão "**OK**" o sistema irá filtrar o intervalo definido nos campos "**Data de**" e "**Data até**", caso queira que o sistema não realize o filtro e traga todas as notas disponíveis pressione o botão "**Cancelar**" e em seguida o botão "**Confirma**".

**Saiba Mais**

**[MV\_DATAPD3 - Retorno de notas de/em terceiros\_TRNLU3](https://tdn.totvs.com/x/1Q4yCw)**
