---
article_id: 360003578531
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 51e1bff82e9e246b0e7da068dfaeab8424deb6db142bfb83ab78c46ef768a4fc
fetched_at: '2026-06-28T22:38:30.008115+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Opção Não
  Disponível Protheus Função: _FWMBPICTV'
type: support-article
updated_at: '2021-11-03T11:42:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003578531-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Op%C3%A7%C3%A3o-N%C3%A3o-Dispon%C3%ADvel-Protheus-Fun%C3%A7%C3%A3o-FWMBPICTV
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:02:00 min***

**Dúvida**

Ao tentar faturar a nota de saída,  o sistema informa o Help: **Opção Não Disponível Protheus Função: \_FWMBPICTV Called By {FWMBPICTVAR ('SC9", "C9\_CODITE','RTPICT'("C9\_\_CODGRP") ')}**  
  
**Ambiente**Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT- Todas as versões  
  
**Solução**

Para solucionar o problema, efetue os seguintes passos:

1-Solicite ao DBA da empresa, avaliar no dicionário de dados ( **SX3),** na tabela **SC9** , se a coluna, **X3\_PICBRV** possui alguma informação. Caso possua:  

* Limpe essa coluna, **X3\_PICBRV.**Essa instrução veio após debug em conjunto com desenvolvimento de Framework. Caso ao rodar o UPDDISTR, essa coluna esteja sendo preenchida,  informe em novo atendimento e para que seja avaliado em conjunto com desenvolvimento, o por que do auto preenchimento da coluna.

2 - Depois, realize um manutenção de profiles do usuário que está apresentado o erro, segue documentação do procedimento;

* Efetue a limpeza do perfil de usuário em manutenção do profile : [Manutenção de Perfil de Usuário (Profile)](https://tdn.totvs.com/pages/viewpage.action?pageId=271165124)
* Apague todos os registros no profile.usr , onde o campo **P\_TYPE** contenha a informação **BROWSESC9** e o problema será resolvido.

**Obs:** Caso o problema também ocorra para a tabela **SC0**, **SA1** - siga o mesmo procedimento indicado acima, e na manutenção do profile, apague os registros **BROWSESA1** e **BROWSESC0**.
