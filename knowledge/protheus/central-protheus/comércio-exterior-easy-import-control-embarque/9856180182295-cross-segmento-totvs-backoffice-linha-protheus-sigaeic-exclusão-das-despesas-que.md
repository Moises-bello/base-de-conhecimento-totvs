---
article_id: 9856180182295
category: Comércio Exterior - Easy Import Control - Embarque
content_hash: ed9bfab3df8f789edab9fa29e989ef5b80e144e4fd4f8dddb5310845c20c05f0
fetched_at: '2026-06-28T22:39:48.768520+00:00'
product: protheus
section_id: 1500001538381
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC - Exclusão das despesas
  que não constam no arquivo TXT de integração de Despesas
type: support-article
updated_at: '2022-10-28T17:38:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9856180182295-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Exclus%C3%A3o-das-despesas-que-n%C3%A3o-constam-no-arquivo-TXT-de-integra%C3%A7%C3%A3o-de-Despesas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Ao integrar o arquivo txt de Despesa são excluídas as despesas que não constam no mesmo, esta correto este procedimento?   
  
**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**  
No momento que é feita a integração das despesas, o sistema sempre fará a exclusão das despesas integradas para incluir as novas. As despesas do numerário, caso ainda não possuam nota, serão excluídas para que as despesas que estão sendo integradas sejam incluídas.  
Neste caso, pode ser utilizado o Ponto de Entrada **DELDESP**, deverá ser alterada a variável **lDeletaSWD** para .F., assim o sistema não efetuará a exclusão das despesas já existentes, e durante a integração, ao encontrar uma despesa igual, o sistema irá perguntar se deseja sobrepor ou não. Ao responder sim, a despesa será alterada para os dados da nova despesa que está sendo integrada, caso responda não, manterá a despesa atual.  
  
**Saiba mais**  
[DT PE IN100CLI - Integração padrão de arquivo texto](https://tdn.totvs.com/pages/viewpage.action?pageId=692557346)
