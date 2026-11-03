---
article_id: 8263524391575
category: Integrações Outros BackOffice
content_hash: 9312743731ab1c3e1f28fa514d20a3587835c9de6d4b1cd748d08f9b100244ca
fetched_at: '2026-06-28T22:46:42.121443+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: 'RH - RM - FOP - Integração Folha de Pagamento x Protheus - Erro AUTHENTICATION:
  USER NOT AUTORIZED'
type: support-article
updated_at: '2026-06-08T18:44:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8263524391575-RH-RM-FOP-Integra%C3%A7%C3%A3o-Folha-de-Pagamento-x-Protheus-Erro-AUTHENTICATION-USER-NOT-AUTORIZED
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29720429388439) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao tentar realizar a integração contábil ou financeira do modulo folha de pagamento com o Protheus, é apresentado o erro " AUTHENTICATION: USER NOT AUTORIZED ".  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas Versões  
  
**Causa**  
Este erro ocorre, quando o usuário do Protheus informado na autenticação do aplicativo EAI do RM está com o usuário ou senha incorreta.  
  
**Solução**  
Para correção deste erro, é necessário informar no campo de autenticação do aplicativo de integração EAI no **RM,** o login e senha de um usuário que tenha acesso válido ao **Protheus.**

**Integração na versão EAI 1.0**  
Acesse no RM o módulo **Integração > Mensagem Única > Integrações.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40889137508759)

Edite o aplicativo  da integração, em **usuário Autenticação** informe as credenciais de um usuário que tenha acesso ao Protheus e clique em salvar.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40889137512343)

**Integração na versão EAI 2.0:**  
Acesse no RM o M**ódulo Integração** >aba **EAI 2.0 > Aplicativos.**Edite o aplicativo da integração, em Endereços do Endpoint **SOAP** e **REST,** informe as credenciais de um usuário que tenha acesso ao Protheus e clique em salvar.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40889121388439)

Após realizar esta modificação, faça um novo teste da integração. Se o erro persistir, aguarde o prazo de 30 minutos para nova validação, ou reinicie os serviços Host para efetivação imediata dos ajustes: [Framework - Linha RM - Frame - Reiniciar Host](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000095827-Framework-Linha-RM-Frame-Reiniciar-Host)  
  
**Importante:** Caso o erro ocorra ao tentar enviar alguma informação do Protheus para o RM, será necessário executar o [**Configurador EAI**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8660755750167-Cross-Segmentos-Backoffice-RM-Integra%C3%A7%C3%A3o-EAI-Configurador-EAI-2-0) para atualizar as credenciais do usuário RM no aplicativo de integração do Protheus.
