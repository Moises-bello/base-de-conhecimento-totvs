---
article_id: 360016420332
category: Ativo Fixo - Baixa e Baixa de Adiantamento
content_hash: d26e8348039fe11742946cd6c72fcbd3bb4255d24e54b28eba41bb2ed29d61de
fetched_at: '2026-06-28T22:41:55.537903+00:00'
product: protheus
section_id: 1500001535901
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA036 : Ao visualizar
  o bem o sistema apresenta mensagem AT36VISUAL'
type: support-article
updated_at: '2023-11-20T16:25:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016420332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA036-Ao-visualizar-o-bem-o-sistema-apresenta-mensagem-AT36VISUAL
---

**Dúvida**

Bem Cuja legenda esteja "Rosa"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012598932)

Ao visualizar o bem o sistema apresenta mensagem AT36VISUAL

Problema : O registro selecionado não possui Baixas ativas para visualização

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012601871)

**Causa**

* Bem foi baixado através de outra rotina (ATFA060 ,ATFA251,ATFA250..)

**Ambiente**

Protheus – Ativo Fixo  – A partir da versão 11.80  
   
**Solução**

Ao acessar a rotina ATFA036 de um F12  e selecione "Visualizar =  Baixa ou Ativo" para que o sistema permita visualizar o bem baixado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012599152)  
  
Modo de visualização da Browse da rotina de baixa de Ativos:  
1 - Baixas de Ativo: Serão exibidos os registros de baixas de ativos já efetuadas.  
2 - Tipos de Ativo: Serão exibidos os registros dos tipos de ativo das fichas cadastradas no ambiente Ativo Fixo, baixados e/ou com saldo disponível.  
3 - Ativos: Serão exibidos os registros dos ativos cadastrados no ambiente Ativo Fixo, baixados, disponíveis e/ou transferidos de filial.
