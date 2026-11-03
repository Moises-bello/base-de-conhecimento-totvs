---
article_id: 360034455774
category: UBA - Unidade de Beneficiamento de Algodão
content_hash: 68c259d1c9c932b9b23aaa097453d1cbd1fdea78ca309696e4b14fabc93abebc
fetched_at: '2026-06-28T22:45:35.619035+00:00'
product: protheus
section_id: 360005717853
source: central-protheus
title: Agro - Linha Protheus - UBA - Mensagem de fardão inválido no relacionamento
  com a esteira
type: support-article
updated_at: '2025-06-18T20:11:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034455774-Agro-Linha-Protheus-UBA-Mensagem-de-fard%C3%A3o-inv%C3%A1lido-no-relacionamento-com-a-esteira
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21880937253783)**Tempo aproximado para leitura: **00:00:30 min**  
 **Ocorrência**Na rotina **UBAA020 - Esteira X Fardão**ao informar o código do fardão é exibida a mensagem: **Atenção! Informe um Fardão Válido**.  
  
 **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - UBA - Unidade de Beneficiamento de Algodão - Versão 12  
  
 **Causa**Essa mensagem é exibida porque não foi cadastrado, na rotina **AGRA601 - Cadastro de Fardão**,um fardo com o mesmo código utilizado no relacionamento com a esteira.  
  
 **Solução**Para solucionar essa ocorrência realize os seguintes passos:

**1.** Acesse a rotina **AGRA601** e cadastre um fardão;

**2.** Após efetuar o cadastro do fardão será possível relacioná-lo com a esteira na rotina **UBAA020**.
