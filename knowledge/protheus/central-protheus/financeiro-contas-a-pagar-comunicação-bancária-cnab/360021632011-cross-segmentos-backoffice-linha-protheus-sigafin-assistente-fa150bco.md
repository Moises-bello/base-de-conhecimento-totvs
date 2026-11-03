---
article_id: 360021632011
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: cd154d0919704ebd3e96396e02fcf895fffaf32afcf8b3ad0320e0c2687172fb
fetched_at: '2026-06-28T22:37:55.019062+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Assistente FA150BCO
type: support-article
updated_at: '2022-05-31T02:16:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021632011-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Assistente-FA150BCO
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:05:00 min  
  
Ocorrência**Ao tentar gerar o arquivo de remessa através da rotina de arquivo de cobrança (FINA150), o sistema apresenta o assistente FA150BCO.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois o banco informado no processo de geração do arquivo de remessa não existe na filial logada ou devido a algum problema referente ao tamanho de campos da tabela SA6 com as perguntas da rotina de arquivo de cobrança(FINA150).  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Verificar se o Banco a ser processado existe na filial que esta logado caso a tabela SA6(Cadastro de Bancos) seja exclusiva;  
2. Verificar na SX3 os tamanhos dos campos A6\_COD, A6\_AGENCIA e A6\_NUMCON estão de acordo com o tamanho dos campos de pesquisa na SX1 no grupo "AFI150".
