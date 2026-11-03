---
article_id: 10470550987671
category: Financeiro - Contas a Receber
content_hash: 67c0ddf84c9fd748f3775ebf5f85c79eb1e204fe03f2dc65e31d73bb49402276
fetched_at: '2026-06-28T22:38:14.153115+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Portal do cliente  -
  Não existem clientes vinculados à este usuário e senha
type: support-article
updated_at: '2025-09-17T13:04:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10470550987671-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Portal-do-cliente-N%C3%A3o-existem-clientes-vinculados-%C3%A0-este-usu%C3%A1rio-e-senha
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17114504839319) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No Módulo Financeiro ao acessar o Portal do Cliente, apresenta a mensagem "Não existem clientes vinculados à este usuário e senha"

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10469948382615)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12.1.33  
  
**Causa**Esse incidente ocorre, pois existem inconsistências no cadastro do usuário na rotina **FATA220** e LIB desatualizada.

1 - Cadastro do cliente na **FATA220** pode não estar atrelado ao usuário;

Necessário amarrar os clientes ao usuário.  
Obs: Status do cliente deve estar ativo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35001648786967)  
  
2 - **Cadastro de Direitos** **para Acesso ao Portal** com tabelas em compartilhamentos diferentes

* **AI3 - Usuários do Portal**
* **AI4 - Usuários do Portal x Cliente**
* **AI6 - Direitos**

3 - No **Cadastro de Direitos** **para Acesso ao Portal** (**FATA220)** em direitos não tem a informação do **PORTALCLIENTEMINGLE**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10480163997975)

4 - LIB abaixo da data de 10/10/2022

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Amarre o cliente ao usuário  
2. Caso esteja diferente o compartilhamento das tabelas **AI3** e **AI4**, ajustar o compartilhamento  
3. Ajustar o **Cadastro de Direitos** **para Acesso ao Portal (****FATA220)** para **PORTALCLIENTEMINGLE**  
4. Aplicar a atualização de LIB para versão igual ou acima de 10/10/2022

Após algumas das alterações acimas, reinicie o REST do Portal do Cliente e acesse novamente.

**Saiba mais:**  
[Portal do Cliente](https://tdn.totvs.com/display/public/PROT/Portal+do+Cliente)  
[Cadastro de Direitos para Acesso ao Portal - FATA220](https://tdn.totvs.com/display/PROT/Cadastro+de+Direitos+para+Acesso+ao+Portal+-+FATA220)
