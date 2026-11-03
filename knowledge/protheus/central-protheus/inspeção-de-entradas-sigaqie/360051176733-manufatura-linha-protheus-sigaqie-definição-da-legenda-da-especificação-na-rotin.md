---
article_id: 360051176733
category: Inspeção de Entradas (SIGAQIE)
content_hash: bc883032161f125335f8c358d84cf92e4b7583ede5a539236c91f14fab0219f3
fetched_at: '2026-06-28T22:42:26.945830+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Definição da legenda da especificação
  na rotina QIEA010
type: support-article
updated_at: '2021-08-06T14:41:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051176733-Manufatura-Linha-Protheus-SIGAQIE-Defini%C3%A7%C3%A3o-da-legenda-da-especifica%C3%A7%C3%A3o-na-rotina-QIEA010
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:55 min**  
**Dúvida**Como são definidas as **legendas** da especificação do produto na rotina **QIEA010 - Especificação do Produto**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Solução**As **legendas** são definidas da seguinte forma:

* **Verde** - **Revisão Disponível**: o campo **QE6\_SITREV - Situação Esp** tem conteúdo igual à **0** indicando que a data informada no campo **In. Vigência**, registrada no campo **QE6\_DTINI - Ini Vigência** é menor ou igual a data base do **Protheus**;
* **Vermelho** - **Revisão Bloqueada**: o campo **QE6\_SITREV** tem conteúdo igual à **1** onde indica que esta revisão foi bloqueada quando utilizado a opção **Outras Ações/Bloq/Lib** do **QIEA010**;
* **Amarelo** - **Revisão Pendente**: o campo **QE6\_SITREV** tem conteúdo igual à **2** indicando que a data informada no campo **In. Vigência**, registrada no campo **QE6\_DTINI**é maior do que a data base do **Protheus**.
