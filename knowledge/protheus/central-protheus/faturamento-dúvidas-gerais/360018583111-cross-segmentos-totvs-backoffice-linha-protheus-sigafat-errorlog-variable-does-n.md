---
article_id: 360018583111
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 63902e531a0ad233d32733a3436ffaa39e18dcb23d13f3d29b1e944283194dc5
fetched_at: '2026-06-28T22:38:29.971171+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - ErrorLog variable
  does not exist LVISUAL na Oportunidade de Venda
type: support-article
updated_at: '2021-11-04T11:30:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018583111-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-ErrorLog-variable-does-not-exist-LVISUAL-na-Oportunidade-de-Venda
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:03:00 min***

**Ocorrência**   
Ao tentar realizar a inclusão ou alteração de uma Oportunidade de Venda é apresentado um ErrorLog: **Variable does not exist LVISUAL.**  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - todas as versões.

**Causa**

O erro ocorre por causa do campo **AD1\_MEMEOB**. Na versão **Protheus** **11** foi criado o **UPDFAT37** que incluia o campo **AD1\_MEMEOB** (**Observação** **de Encerramento**) na tabela **AD1**(**Oportunidade** **de** **Venda**). O objetivo desse campo era registrar uma observação para o encerramento da oportunidade, porém, esse campo foi descontinuado na versão **Protheus** **12**sendo substituído pelo campo **AD1\_MTVENC** (**Motivo**).

**Solução**

Passos para limpar o conteúdo do campo**X3\_WHEN** do dicionário **SX3**.  
  
1 - No módulo **Configurador** acessar: **Base de** **Dados** → **Dicionário** → **Base de Dados.**

2 - Na opção **Dicionário de Dados1** selecionada, clique no botão **Pesquisar2**.

3 - Em **Procurar Por**, informe o nome da tabela **AD1**e pressione no botão **Buscar.**Posicionado no registro **AD1 (Oportunidade de Venda) 3** clique no botão **Editar****4**.

4 - Encontre o campo**AD1\_MEMEOB**e clique em no botão**Editar****5****.**

5 - Selecione a pasta**Opções**. No campo **Modo Edição (X3\_WHEN)**limpe o conteudo **lVisual**, e em seguida clique em **Salvar**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412159833495/mceclip0.png)

Após a alteração.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412165504407/mceclip1.png)

6 - Clique no botão **Confirma**e feche o configurador.

7 - Clique em **Salvar**e confirme as alterações realizadas.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412159894295/mceclip2.png)

7 - Clique em **Finalizar**e feche o módulo **Configurador**.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412172970007/mceclip3.png)
