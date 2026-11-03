---
article_id: 38507812182295
category: Ativo Fixo - Baixa e Baixa de Adiantamento
content_hash: f580a5d837a89ece299684f7cf83a53637f542dff0a6ef4d61276de975bd789f
fetched_at: '2026-06-28T22:41:55.531219+00:00'
product: protheus
section_id: 1500001535901
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA036 - Ocorre menssagem
  AF036BLOQ ao realizar a baixa do bem.
type: support-article
updated_at: '2026-02-20T10:48:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38507812182295-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA036-Ocorre-menssagem-AF036BLOQ-ao-realizar-a-baixa-do-bem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38507812143255) Tempo aproximado para leitura: 00:10 min  
  
**Dúvida**  
Ao tentar realizar a baixa de um ativo, o sistema impede a operação e apresenta a mensagem de erro "A036BLOQ - Ativo bloqueado".  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo (SIGAATF) - A partir da versão 12  
  
**Solução**  
A mensagem "A036BLOQ" ocorre quando o ativo em questão encontra-se bloqueado no sistema, seja por uma data limite estabelecida ou por um *status* de bloqueio específico.   
Para solucionar essa rejeição e concluir a baixa, é necessário identificar a origem do bloqueio (Campos Data bloqueio (N1\_DTBLOQ) ou *Status* Bem (N1\_STATUS) e executar o desbloqueio na rotina correspondente.

**Passos para verificação e mitigação da mensagem:**

1. **Verifique o cadastro do ativo afetado e valide se o campo Data bloqueio (N1\_DTBLOQ) está preenchido:**

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38507812144151)

   Se o bloqueio for por data onde Data bloqueio (**N1\_DTBLOQ) =** Preenchido:   
     
   Deve acessar a rotina de Bloqueio de Ativos (**ATFA200**) para este bem, e realizar o desbloqueio utilizando a opção "desbloqueia": 

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38507832436119)
2. **Avalie o campo** ***Status*** **Bem (N1\_STATUS) se está com conteúdo igual a** **2** **ou** **3** **(*****status*** **que representam bloqueio).**

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38507832438423)

   Se o bloqueio for por *status* igual a **2** (Status Bem **= 2**):   
     
   Acesse a rotina de Cadastro de Ativos (**ATFA012**), clique em **Outras Ações** e realize o desbloqueio direto do bem, com a opção desbloqueio

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38507812148503)

   Se o bloqueio for por status igual a **3**  (Status Bem **= 3**):   
     
   Isso indica um bloqueio no local do bem. Acesse a rotina de Bloqueio por Local (**ATFA025**) e realize o desbloqueio do local atrelado ao ativo Endereço (**N1\_LOCAL**).

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38507832446615)
3. **Realizadas verificações e ajustes, realize novamente o movimento de baixa do bem.**

**Saiba mais:**  
[Como bloquear a depreciação de alguns Bens](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018886912-MP-SIGAATF-Como-bloquear-a-deprecia%C3%A7%C3%A3o-de-alguns-Bens-?source=search)  
[ATFA036 - BAIXA DE ATIVO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018556171-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA036-BAIXA-DE-ATIVO)  
[Bloqueio e Desbloqueio de bens (ATFA200 - SIGAATF)](https://tdn.totvs.com/pages/viewpage.action?pageId=415704957)  
[Cadastro de baixas (ATFA036 - SIGAATF)](https://tdn.totvs.com/pages/viewpage.action?pageId=306852236)
