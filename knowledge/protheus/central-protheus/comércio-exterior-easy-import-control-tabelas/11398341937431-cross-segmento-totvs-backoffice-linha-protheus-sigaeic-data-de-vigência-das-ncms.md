---
article_id: 11398341937431
category: Comércio Exterior - Easy Import Control - Tabelas
content_hash: 1b0dfed183aaec050949d86f0ab1b5dd467f15ea02a1bc5e0b44f3b9780f17f7
fetched_at: '2026-06-28T22:39:47.850156+00:00'
product: protheus
section_id: 1500001549562
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC -Data de Vigência
  das NCM's via TOTVS COMEX Conteúdo.
type: support-article
updated_at: '2023-01-04T13:28:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11398341937431-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Data-de-Vig%C3%AAncia-das-NCM-s-via-TOTVS-COMEX-Conte%C3%BAdo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:01:00 min** **Dúvida**Data de Vigência das **NCM's** via TOTVS COMEX Conteúdo.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  –*Easy Import Control*– Todas versões  
  
**Solução**Quando são informados os dados da pergunta nos parâmetros, é informada a data de vigência **01/12/2022**, ou seja, das **NCM's** informadas a integração irá retornar apenas as **NCM's** que estão dentro deste parâmetro, vigentes a partir de **01/12/2022**.  
A **NCM 01.03.10.00**, por exemplo, está vigente na data de **01/04/2022**, não sendo retornada pela integração.  
Com isso, ao definir no parâmetro que "o sistema deve efetuar o bloqueio das **NCM's** que estiverem dentro do intervalo selecionado, e que não foram atualizadas" ( O **help** da pergunta "Bloqueia **NCM**?"), esta **NCM** bem como todas as demais que possuem data de vigência diferente da informada serão bloqueadas.  
Neste caso a recomendação é optar por não bloquear a **NCM**, para que apenas as que estão dentro da data de vigência sejam atualizadas sem bloquear as demais, e não informar a data de vigência, para que todas as **NCM's** abrangidas pelo range informado sejam atualizadas.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11398303376151)

**Saiba Mais**

[Integração TOTVS Comex Conteúdo - EICA130](https://tdn.totvs.com/pages/releaseview.action?pageId=551451442)
