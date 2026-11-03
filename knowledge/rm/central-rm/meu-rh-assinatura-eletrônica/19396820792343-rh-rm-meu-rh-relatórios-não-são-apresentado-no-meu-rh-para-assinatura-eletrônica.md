---
article_id: 19396820792343
category: Meu RH - Assinatura Eletrônica
content_hash: 6d8a3157ffd99df728b1ce8577c0be31d750e869fb5227bb8f7cd5700fc6ab55
fetched_at: '2026-06-28T22:47:28.746200+00:00'
product: rm
section_id: 19399655101335
source: central-rm
title: RH - RM - Meu RH - Relatórios não são apresentado no Meu RH para Assinatura
  Eletrônica
type: support-article
updated_at: '2026-03-10T14:50:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19396820792343-RH-RM-Meu-RH-Relat%C3%B3rios-n%C3%A3o-s%C3%A3o-apresentado-no-Meu-RH-para-Assinatura-Eletr%C3%B4nica
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19396816081559) Tempo aproximado para leitura: **00:02:30 min**  
  
**Ocorrência**  
Ao acessar o menu Assinatura Eletrônica no Meu RH, não são apresentados os relatórios integrados para visualização e assinatura.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.2302.164  
  
**Causa**  
Ocorre quando o usuário informado no **Processo de Integração do Relatório** é diferente do usuário configurado no **RM Portal / Grupo Quiosque**, ou quando o usuário cadastrado nas configurações do **RM Portal / Grupo Quiosque** não possui perfil de **Publicador**.

A situação também pode acontecer caso o funcionário esteja sem o e-mail principal preenchido.

**Solução**  
Para visualização e assinatura do relatório no Meu RH,  deverá validar todos os passos abaixo:  
  
1. Configure o usuário(e-mail e senha) do publicador da plataforma TAE em **Folha de Pagamento / aba configurações / parametrizador / RM Portal / Totvs Assinatura Eletrônica.**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19396791607063)**  
  
2- Acesse a plataforma de Assinatura Eletrônica (TAE) e confirme se o usuário informado está com o perfil Publicador devidamente marcado.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19488553554455)  
  
**Importante:** Confira também, se a data de validade do usuário publicador no TAE, está vigente.  
  
3. Verificar se nos parâmetros do tipo de relatório do módulo **Folha de Pagamento**, o campo **“Requer Aprovação”** está **desmarcado.** Caso esteja marcado, o documento **não será apresentado no Meu RH**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19396816088471)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19396830771735)

4. Ao integrar um documento do RM com o TAE pela primeira vez, por meio do Processo de Integração de Relatórios, será solicitado usuário (e-mail) e senha da plataforma. É **obrigatório** informar o mesmo usuário (e-mail) e senha cadastrados no **Grupo Quiosque** (RM Portal). Caso seja informado um usuário diferente, o documento não será disponibilizado no Meu RH.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19396775279383) 

5. Certifique-se de que o campo PPESSOA.EMAIL (e-mail principal do funcionário) esteja preenchido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38583259809943)

Caso o campo e-mail principal esteja em branco para utilização do e-mail pessoal, no Grupo de Quiosque do colaborador, acessado pelo caminho: **Folha de pagamento > Configurações > Parametrizador > RM Portal > Edite o Quiosque > Portal Meu RH**, marque o parâmetro  **“Utilizar e-mail pessoal do destinatário caso o principal não esteja preenchido”.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38934242845463)

**Aviso Importante:**

* Para a integração com o TAE (TOTVS Assinatura Eletrônica) obrigatoriamente deverá ter o protocolo SSL configurado, caso contrário o TAE não aceitará as requisições vindas de um protocolo sem SSL.

  **Saiba mais:**

  [RH - RM - Meu RH - Integração do Meu RH com o Tae(Totvs assinatura eletrônica)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13740154028823-RH-RM-Meu-RH-Integra%C3%A7%C3%A3o-do-Meu-RH-com-o-Tae-Totvs-assinatura-eletr%C3%B4nica-)

  [RH - RM - Meu RH - Como utilizar o e-mail pessoal na integração do Meu RH com o TAE (Totvs Assinatura Eletrônica)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38833430081687-RH-RM-Meu-RH-Como-utilizar-o-e-mail-pessoal-na-integra%C3%A7%C3%A3o-do-Meu-RH-com-o-TAE-Totvs-Assinatura-Eletr%C3%B4nica)
