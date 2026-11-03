---
article_id: 14960829703575
category: Financeiro
content_hash: 395c69f9bb5ad633b4b03425ad5b196ce5a08d468c54c3bd740b178660aa55ef
fetched_at: '2026-06-28T22:38:01.045709+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - Portal do Cliente apresenta lentidão
  após login
type: support-article
updated_at: '2023-05-31T12:51:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14960829703575-Cross-Segmento-Backoffice-Linha-Protheus-Portal-do-Cliente-apresenta-lentid%C3%A3o-ap%C3%B3s-login
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**No Portal do Cliente, ao acessar a tela de Títulos ou Notas Ficais, as informações demoram a ser carregadas ou não são apresentadas.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Causa**Esse incidente ocorre, pois a chave **MaxQuerySize**, presente no arquivo appserver.ini, está com conteúdo **MaxQuerySize=1024.**

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o arquivo appserver.ini do ambiente REST onde o Portal do Cliente está configurado.  
2. Localize a chave *[General]*.  
3. Altere ou inclua a configuração:  
*[General]*  
*MaxQuerySize=31960*

**Saiba Mais**<https://tdn.totvs.com/display/tec/MaxQuerySize>
