---
article_id: 360034458534
category: UBA - Unidade de Beneficiamento de Algodão
content_hash: c2eda817fbb6bab386a151d9265818283ebdc88443d388109c53a9c14b14c861
fetched_at: '2026-06-28T22:45:35.622417+00:00'
product: protheus
section_id: 360005717853
source: central-protheus
title: Agro - Linha Protheus - UBA - Mensagem de fardão relacionado a outra esteira
type: support-article
updated_at: '2025-06-20T12:51:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034458534-Agro-Linha-Protheus-UBA-Mensagem-de-fard%C3%A3o-relacionado-a-outra-esteira
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21880843175447)**Tempo aproximado para leitura: **00:00:40 min**  
 **Ocorrência**Na rotina**UBAA020 - Esteira X Fardão**ao informar o código do fardão é exibida a mensagem: **Atenção! Fardão já incluso ou relacionado a outra Esteira.**  
  
 **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - UBA - Unidade de Beneficiamento de Algodão - A partir da versão 12.1.17  
  
 **Causa**Essa mensagem é exibida porque não é possível relacionar a uma esteira um fardão que já foi anteriormente relacionado a outra esteira.  
  
 **Solução**Para solucionar essa ocorrência, realize os seguintes passos:

**1.** Informe o código de um fardão que ainda não tenha sido relacionado a nenhuma esteira;

**2.** Acesse a rotina **UBAA010 - Cadastro de Esteira** e desfaça o relacionamento do fardão com a esteira.

**Importante**  
O relacionamento do fardão com a esteira apenas pode ser desfeito se ainda não foi efetuado o beneficiamento do fardão.
