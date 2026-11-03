---
article_id: 25681127815575
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 2d277259de574e0899eca3db8ca8df3929c8deb8f1022891164788a9e086aafe
fetched_at: '2026-06-28T22:45:20.923500+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Como ajustar arquivo de configuração
  REST para middleware?
type: support-article
updated_at: '2026-06-23T18:00:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25681127815575-RH-Linha-Protheus-TAF-eSocial-Como-ajustar-arquivo-de-configura%C3%A7%C3%A3o-REST-para-middleware
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25681127804695) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como ajustar arquivo de configuração REST para middleware  
  
**Ambiente**  
RH - Linha Protheus - TAF - eSocial - TOTVS Automação Fiscal - À partir da release 12.1.33  
  
**Solução**

1. Pare o serviço TAF-WS;
2. Acesse a pasta BIN/APP do TAF;
3. Abre o arquivo APPSERVER.INI;
4. Realize as seguintes alterações:  
     
   [HTTPREST]  
   **Security=0**  
   ;Deixe o parâmetro security com o valor 0

   **;[TAF\_CFGJOB]**  
   ;Comentar a seção [TAF\_CFGJOB]  
     
   [ONSTART]  
   **JOBS=HTTPJOB**  
   **;,TAF\_CFGJOB**  
   ;Modificar o parâmetro JOBS comentando o TAF\_CFGJOB  
     
   ;Adicionar a seção abaixo no final do arquivo  
   **[APP\_MONITOR]**  
   **enable=0**
5. Após as alterações, inicie o TAF-WS e prossiga com a integração.
