---
article_id: 360026389733
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 119c2e31bc800add1753c149a7d7b81c335cecc7af5983465bab539a297630c9
fetched_at: '2026-06-28T22:38:28.551494+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Erro ao excluir
  documento quando o tipo do documento utilizar fornecedor
type: support-article
updated_at: '2023-01-30T18:04:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026389733-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Erro-ao-excluir-documento-quando-o-tipo-do-documento-utilizar-fornecedor
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:04:00 min****Ocorrência**Erro ao excluir documento de saída quando o tipo do documento utilizar fornecedor:

***Update error - lock required - File: SA1010 in file D:\bamboo-agent-5.7.2\xml-data\build-dir\TP11-BUILDV2APPSRV-TEC11WIN32RPO32\advtec9\_tt11\advpl\advplfile.cpp at line 74***  
 ***on MA521ATSA1(MATA521.PRX) 17/05/2018 14:07:10 line : 7318***

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FAT - A partir da versão 12.  
  
**Causa**O erro ocorre devido a falta de atualização da rotina.

**Solução**

1. Baixe o pacote mais atual da rotina **MATA****521 contida na Expedição Continua da Versão: [Portal Downloads e Atualizações](https://suporte.totvs.com/portal/p/10098/download?e=761808)**

2. Aplique o pacote, via TDS, em seu ambiente de testes para validação e posteriormente, no ambiente de produção.

**Obs**:  A aplicação do pacote deve ser efetuado por um analista que detenha o conhecimento técnico para o procedimento, caso tenha dúvidas de procedimento, entre em contato com a equipe de FrameWork para auxiliá-lo.
