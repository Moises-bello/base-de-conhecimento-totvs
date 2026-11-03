---
article_id: 360000753947
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 33affc13c67cb40db4a0de6b1979d78061d4ab6158cb699b14cd81a45ee0663d
fetched_at: '2026-06-28T22:38:29.937110+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Argument #1
  error, expected C->N,  function AT on _FWMBPICTVAR(FWMBROWSE.PRW)'
type: support-article
updated_at: '2022-03-16T13:15:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000753947-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Argument-1-error-expected-C-N-function-AT-on-FWMBPICTVAR-FWMBROWSE-PRW
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:02:00 min***

**Ocorrência**Ao tentar acessar o cadastro do cliente, ocorre o erro: **argument #1 error, expected C->N,  function AT on \_FWMBPICTVAR(FWMBROWSE.PRW).**

**Ambiente**Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT- a partir da release 12.1.17.  
  
**Causa**O erro ocorre em situações que o cliente possui a validação **X3\_PICTVAR** do campo **A1\_CGC** incorreta, ou quando possui na sua estrutura SX3, a coluna **X3\_PICBRV** preenchida ou quando há um erro de profile de usuário.  
  
**Solução**

Para solucionar a ocorrência, valide o cenário do ambiente e  efetue o passo correspondente:

1- Para ajuste **X3\_PICTVAR** incorreto no campo **A1\_CGC** , edite a tabela SA1, e posteriormente o campo A1\_CGC. Ajuste a função **PicCli**para **PicPes**, deixando a função como **PicPes(M->A1\_PESSOA).**

Salve o campo, salve a tabela SA1 e atualize o dicionário de dados.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4799986358679/mceclip1.png)

2- Para ajuste da coluna de estrutura da tabela SA1, **X3\_PICBRV** preenchida , solicite ao DBA da empresa para limpar as informações que estiverem sendo apresentadas nesta coluna .

3- Para ajuste de profile: efetue a manutenção, limpando os profiles de usuário.

Abra o arquivo profile.usr, filtre pelo código do usuário e delete o registro BROWSESA1 na rotina MATA030.

Para efetuar o procedimento, acesse: **[MP - FRAME - Manutenção de Profile de Usuários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025097012-MP-FRAME-Manuten%C3%A7%C3%A3o-de-Profile-de-Usu%C3%A1rios)**

**Obs:** *Para efetuar os procedimentos, é necessário* *conhecimento técnico de ambientes e banco de dados para realização dos processos.*

*Sempre efetue o devido BACKUP antes de efetuar qualquer manutenção nas tabelas do sistema.*
