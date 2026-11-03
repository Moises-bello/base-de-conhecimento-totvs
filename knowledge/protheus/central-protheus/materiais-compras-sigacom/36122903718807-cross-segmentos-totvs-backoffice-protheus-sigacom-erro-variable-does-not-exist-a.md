---
article_id: 36122903718807
category: Materiais - Compras (SIGACOM)
content_hash: 1d6a717898d555ccf69b1641854f6856dd8e3f670092d264bcdc3234e3dab60d
fetched_at: '2026-06-28T22:41:17.627064+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Erro variable does
  not exist ao processar um Execauto no módulo de Compras
type: support-article
updated_at: '2025-11-05T15:38:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36122903718807-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Erro-variable-does-not-exist-ao-processar-um-Execauto-no-m%C3%B3dulo-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36122903703959) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Ao rodar um Execauto é gerado o erro ***variable does not exist*** ou o erro ***NOCPOSX3,*** como corrigir?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - a partir da versão 12.  
  
**Solução**

Esta ocorrência é reproduzida quando uma expressão AdvPL fizer referência a uma variável que não exista, não tenha sido declarada ou não seja visível no código-fonte atual devido ao escopo da declaração da mesma.

Algumas sugestões para solucionar esta ocorrência são:

* Caso a variável refira-se a um nome de campo de uma tabela, tenha certeza que a mesma esteja aberta e selecionada da área de trabalho atual. Verifique se o campo que está sendo indicado no erro realmente existe na tabela, se realmente existe na SX3.
* Caso a referência esteja sendo feita a uma variável PUBLIC ou PRIVATE, tenha certeza que a variável foi criada utilizando as instruções PRIVATE e/ou PUBLIC. Verifique a qual campo essa variável está relacionada e valide se esse campo existe na SX3.
* Se a referência foi realizada a uma variável LOCAL ou STATIC, em uma expressão de macro-execução, rearrange seu código-fonte para referenciar à variável diretamente ; pois **variáveis declaradas LOCAL e/ou STATIC não são visíveis para macro-execução.**

Para maiores informações consulte documentação sobre o erro abaixo:

<https://tdn.totvs.com/display/tec/Variable+does+not+exist>
