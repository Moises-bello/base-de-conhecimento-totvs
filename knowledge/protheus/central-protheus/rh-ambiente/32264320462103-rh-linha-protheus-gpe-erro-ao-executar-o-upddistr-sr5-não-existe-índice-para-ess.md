---
article_id: 32264320462103
category: RH - Ambiente
content_hash: c694aab541a5d2e72580bc5508f321df0f6a1f875d3cc7e81d63920aade3df49
fetched_at: '2026-06-28T22:43:09.548713+00:00'
product: protheus
section_id: 20669342808471
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro ao executar o UPDDISTR: SR5: Não existe índice
  para esse alias no SINDEX'
type: support-article
updated_at: '2026-06-25T13:25:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32264320462103-RH-Linha-Protheus-GPE-Erro-ao-executar-o-UPDDISTR-SR5-N%C3%A3o-existe-%C3%ADndice-para-esse-alias-no-SINDEX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32264343643031) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao executar o UPDDISTR ocorre o erro: SR5: Não existe índice para esse alias.   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Causa**  
O erro ocorre devido informação incorreta no campo **Nome (X2\_ARQUIVO)**, da tabela SR5.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Via SIGACFG > Base de Dados >Dicionário>Base de Dados, abra a tabela SR5 e verifique como está o preenchimento do campo **Nome** (**X2\_ARQUIVO)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32271935756695)  
  
2. Caso o campo esteja com a informação diferente de **SIGAGPE**, efetue o ajuste deixando conforme a imagem demonstrada no passo 1.;  
  
3. Salve a alteração.  
  
4. Após efetuar os ajustes, execute novamente o processo que apresentou o erro.

**Saiba Mais:**

[RH - Ambiente](https://centraldeatendimento.totvs.com/hc/pt-br/sections/20669342808471-RH-Ambiente)
