---
article_id: 5179357116055
category: Financeiro - Contas a Pagar
content_hash: f3fd17d186d9ad7346ad59bdab530d0f9bdc267336a7eb7987a0b20d44361484
fetched_at: '2026-06-28T22:38:08.314039+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA435 - Não foi possível
  copiar o arquivo fRename Erro ## - Baixa via retorno automático'
type: support-article
updated_at: '2022-04-04T14:41:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5179357116055-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA435-N%C3%A3o-foi-poss%C3%ADvel-copiar-o-arquivo-fRename-Erro-Baixa-via-retorno-autom%C3%A1tico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar baixa automática via retorno Schedule é apresentada a mensagem de Não foi possível copiar o arquivo fRename Erro ##  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA435 - A partir da release 12.1.25  
  
**Causa**Esse incidente ocorre, após uma falha em operação com arquivos ( File I/O ). Quando utilizadas funções de manipulação de arquivo em baixo nível ( FCreate, FOpen, FSeek ... ), e uma operação desta natureza apresentou falha e/ou não foi realizada com sucesso, utilizamos a função FError() para recuperar um código de ocorrência que aponta a condição de falha da última operação.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique no *console.log* o código da mensagem de erro e ajuste conforme lista abaixo

-- A tabela abaixo lista os principais códigos de erro fornecidos por esta função:

![ferror.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5179281127575/ferror.png)

**Saiba mais**  
<https://tdn.engpro.totvs.com.br/display/tec/FError>
