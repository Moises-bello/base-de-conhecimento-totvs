---
article_id: 360021877311
category: ADVPL - Ponto de Entrada
content_hash: dfd01f8174a9e13d47b46755103e8e5af270e408e8836c9aa5dc4f9bd41a7975
fetched_at: '2026-06-28T22:40:12.846515+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Problemas com privilégios
  em rotinas inclusa pelo ponto de entrada MA103OPC
type: support-article
updated_at: '2021-12-30T17:15:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021877311-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Problemas-com-privil%C3%A9gios-em-rotinas-inclusa-pelo-ponto-de-entrada-MA103OPC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Estou com problemas em dar acesso(CFG>PRIVILÉGIOS) a opções personalizadas na rotina **MATA103**. Essas opções foram colocadas através do ponto de entrada **MA103OPC**.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Causa**Esse incidente ocorre, pois a rotina de privilégios do configurador só traz as rotinas que estão no *array* **aRotina** dentro do **MENUDEF,** e como o ponto de entrada**MA103OPC** está fora do **MENUDEF** a rotina de privilégios não ira trazer as poções incluídas pelo**MA103OPC.**  
  
**Solução**Para solucionar essa ocorrência, utilize o ponto de entrada **MTA103MNU** que esta localizado dentro do**MENUDEF,**e insere novas opções no *array* **aRotina.****Saiba Mais**[MTA103MNU - Inserir novas opções no array aRotina](http://tdn.totvs.com/pages/releaseview.action?pageId=6085783)
