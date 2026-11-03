---
article_id: 360017681391
category: ADVPL - Classe e Função
content_hash: 63f10809e453e672bbbe0dab384d9881c46cc218845c0cee956ef4d5bb5a5f1b
fetched_at: '2026-06-28T22:40:17.159865+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Restringir o acesso
  do usuário para alterar informação de um campo
type: support-article
updated_at: '2025-03-12T15:06:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017681391-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Restringir-o-acesso-do-usu%C3%A1rio-para-alterar-informa%C3%A7%C3%A3o-de-um-campo
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como restringir o acesso do usuário para alterar informação de um campo específico?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL– A partir da versão 11.80  
  
**Solução**Este procedimento poderá ser efetuado para qualquer campo do sistema para que somente um ou mais usuários possam alterar a informação.  
Selecionar ‘**Editar**’ e na aba ‘**Opções**’, no campo ‘**Modo Edição**’ informar a variável ‘**\_\_cUserId**’ que é carregada automaticamente quando o usuário acessa o sistema, com o código do**Id** do usuário que terá acesso. O **Id** do usuário que terá acesso (**$ “000002”**).  
Exemplo:**\_\_cUserId $ “000002”**Caso queira liberar o acesso para outros usuários, informar ‘vírgula’ e os demais **Ids**.  
  
**Saiba mais**[**PSIGABD0039 - Como restringir o acesso do usuário para alterar informação de um campo específico?**](http://tdn.totvs.com/pages/viewpage.action?pageId=240310489)

#
