---
article_id: 32266048848407
category: RH - Ambiente
content_hash: bfe19b0123c73bc37c9ed289d1e15f52e435c6550650eb0218bd458553123995
fetched_at: '2026-06-28T22:43:09.545702+00:00'
product: protheus
section_id: 20669342808471
source: central-protheus
title: RH - Linha Protheus - GPE - Erro Invalid column name 'R5_XXXX' ao executar
  a rotina CheckDupl
type: support-article
updated_at: '2026-06-25T13:27:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32266048848407-RH-Linha-Protheus-GPE-Erro-Invalid-column-name-R5-XXXX-ao-executar-a-rotina-CheckDupl
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32266052161687) Tempo aproximado para leitura:  **00:01:00 min****Ocorrência**  
Ao executar o CheckDupl ocorre o erro: Invalid column name 'R5\_XXXX'.  
  
**Ambiente** TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Causa**  
O erro ocorre devido informação incorreta no campo **Nome (X2\_ARQUIVO)**, da tabela SR5.  
  
**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Via SIGACFG > Base de Dados >Dicionário>Base de Dados, abra a tabela SR5 e verifique como está o preenchimento do campo **Nome** (**X2\_ARQUIVO)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32272008301719)

2. Caso o campo esteja com a informação diferente de **SIGAGPE**, efetue o ajuste deixando conforme a imagem demonstrada no passo 1.;  
  
3. Salve a alteração;  
  
4. Após efetuar os ajustes, execute novamente o processo que apresentou o erro.

**Saiba Mais:**

[RH - Ambiente](https://centraldeatendimento.totvs.com/hc/pt-br/sections/20669342808471-RH-Ambiente)
