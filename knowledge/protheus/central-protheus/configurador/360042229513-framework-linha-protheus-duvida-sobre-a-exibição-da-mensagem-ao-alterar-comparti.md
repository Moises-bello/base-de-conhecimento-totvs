---
article_id: 360042229513
category: Configurador
content_hash: a34a2debd950081c68cd0db2926ee07522d7c0f0580c9aba631dde76c8b9b791
fetched_at: '2026-06-28T22:42:19.048172+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Duvida sobre a exibição da mensagem ao alterar
  compartilhamento de tabela
type: support-article
updated_at: '2024-05-08T12:00:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042229513-Framework-Linha-Protheus-Duvida-sobre-a-exibi%C3%A7%C3%A3o-da-mensagem-ao-alterar-compartilhamento-de-tabela
---

**Ocorrência**Ao alterar compartilhamento de uma tabela é exibida a mensagem:

As tabelas listadas abaixo possuem vínculo de compartilhamento com a tabela XXX e terão seu modo de compartilhamento alterado no dicionário.

A adequação da base de dados existente, caso necessária, NÃO será efetuada por esta rotina.

Caso não esteja certo desse procedimento feche a janela pressionando o botão CANCELAR.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056663773)  
   
 **Ambiente**MP – SIGACFG – A partir da versão 12  
   
 **Causa**  
 Esta mensagem é exibida sempre que houver uma alteração no modo de compartilhamento de uma tabela e a mesma tiver alguma relação com outra(s) tabela(s), neste caso o sistema altera também o compartilhamento da(s) tabela(s) relacionada(s) para manter a integridade dos dados e do modo de acesso do sistema a informação contida na(s) tabela(s) em questão.  
   
 **Solução**

Não é necessário nenhuma ação em relação ao compartilhamento da(s) tabela(s) em si, basta verifique se o novo modo de compartilhamento configurado está de acordo com os dados já existentes na(s) tabela(s) envolvidas.

Ex.: Caso o modo de compartilhamento da(s) tabela(s) seja alterado de exclusivo para compartilhado, o campo de filial deverá ficar vazio caso existam dados na(s) tabela(s) envolvida(s).
