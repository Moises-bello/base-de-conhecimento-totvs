---
article_id: 360026014991
category: Materiais - Compras (SIGACOM)
content_hash: 76e665d7c5512169e0f83037983944482d9704308524afa1fbba75178a069e1f
fetched_at: '2026-06-28T22:41:10.332422+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Quais os eventos do
  Totvs Colaboração para envio de e-mail pelo Eventviewer ou M-Messenger ?
type: support-article
updated_at: '2023-08-31T13:28:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026014991-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quais-os-eventos-do-Totvs-Colabora%C3%A7%C3%A3o-para-envio-de-e-mail-pelo-Eventviewer-ou-M-Messenger
---

* EVENTOS

  | Evento | Descrição |
  | --- | --- |
  | 052 | Aviso de inconsistências (Totvs Colaboração) |
  | 053 | Documento disponíveis (Totvs Colaboração) |

* PARÂMETROS (Para informar a conta de quem o e-mail sera enviado)

  | Parâmetro | Tipo | Descrição |
  | --- | --- | --- |
  | MV\_RELAUTH | Logico | Servidor de e-mail necessita de Autenticação? |
  | MV\_EMCONTA | Caracter | Indica qual conta utilizada para envio de e-mails automáticos pelo sistema. |
  | MV\_RELSERV | Caracter | Nome do servidor de envio de e-mail utilizado nos relatórios |
  | MV\_RELPSW | Caracter | Senha da conta de e-mail para envio de relatórios |
  | MV\_RELACNT | Caracter | Conta a ser utilizada no envio de e-mail para os relatórios |
* EVENTVIEWER  
    
  1. No cadastro de usuário (SIGACFG->USUÁRIOS->SENHAS->USUÁRIOS), ao editar um usuário na aba "restrições de acesso->acessos" liberar o acesso ao código "**174 - Acesso a inscrição nos eventos do EventViewer"**, e o usuário deve ter o e-mail cadastrado.
  2. O **próprio usuário que irá receber os e-mails** deve se inscrever no *eventviewer*, informando os eventos 052 e 053 correspondentes ao Totvs Colaboração.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052534774)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053442293)  
  
Obs: Para cadastrar corretamente deve ser configurado da seguinte forma: "Canal: AMBIENTE", "Categoria: 001", "E-mail: SIM".

* M-MESSENGER  
    
  1. No cadastro do M-Messenger (SIGACOM->CADASTROS->M-Messenger), incluir um usuário ou grupo de usuários informando os eventos 052 e 053.

**OBSERVAÇÃO : É possível configurar o Eventviewer ou o M-Messenger, caso os dois estejam configurados o Eventviewer é o principal.**

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Exemplo de configuração Messenger](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011724292-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Exemplo-de-configura%C3%A7%C3%A3o-Messenger-?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
