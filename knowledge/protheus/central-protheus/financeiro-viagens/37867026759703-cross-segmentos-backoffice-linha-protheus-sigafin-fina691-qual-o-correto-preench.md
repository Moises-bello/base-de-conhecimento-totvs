---
article_id: 37867026759703
category: Financeiro - Viagens
content_hash: d2cb8a2e6837a8f6497b2a6c5f8d13522632132b28032368d17ac2aac1a7bfd6
fetched_at: '2026-06-28T22:38:21.289757+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA691 - Qual o correto
  preenchimento do parâmetro MV_RESGVIA?
type: support-article
updated_at: '2026-01-23T10:01:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37867026759703-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA691-Qual-o-correto-preenchimento-do-par%C3%A2metro-MV-RESGVIA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37867026747159) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Qual o correto preenchimento do parâmetro MV\_RESGVIA?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
  
O cadastro de participante é um código com **6 caracteres** mais **";"** para separá-los. Porem vale ressaltar que este parâmetro tem a finalidade de inserção de códigos somente para **APROVADORES** ou seja gerentes e pessoas que são aprovadoras para visualização de solicitações e aprovações de N funcionários ou viajantes que existir na empresa.  
  
**Exemplo de preenchimento da forma correta.**  
  
**000000;000111;222555**

**Não pode ser inserido um espaçamento após o ponto e virgula, pois o sistema entende que existe esse espaçamento no código e não considera.**
