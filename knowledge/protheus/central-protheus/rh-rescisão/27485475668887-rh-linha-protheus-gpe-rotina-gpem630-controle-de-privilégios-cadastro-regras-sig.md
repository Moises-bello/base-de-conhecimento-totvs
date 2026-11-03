---
article_id: 27485475668887
category: RH - Rescisão
content_hash: 6b2d459e06413e929b6bbe309de3b268221e5ca5a62f5ab9575928b5aa81c089
fetched_at: '2026-06-28T22:43:54.454185+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Rotina GPEM630 controle de Privilégios/ Cadastro
  Regras (SIGAGPE)
type: support-article
updated_at: '2024-11-01T14:57:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27485475668887-RH-Linha-Protheus-GPE-Rotina-GPEM630-controle-de-Privil%C3%A9gios-Cadastro-Regras-SIGAGPE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27485475662615) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Como cadastrar Rotina GPEM630 controle de Privilégios/ Cadastro Regras (SIGAGPE)?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**

Cenário: Usuário vinculado a um grupo com controle de privilégios, em que o acesso a rotina de Rescisão (GPEM040) está permitido e mnemônico: P\_LMEMCALC = .T., o sistema bloqueia ao consultar a memória de cálculo.

Neste caso, para que o usuário consiga acessar as opções: *Rescisão Coletiva* ou *Outras Ações -> Consulta de Memória de Cálculo*, é necessário permitir no controle de privilégios, a rotina **GPEM630**(Rescisão Coletiva), pois este menu em específico é definido nela.

A rotina GPEM040 cria dois *Browse*(conforme print abaixo), onde dentro dela, executa o GPEM630:

![](https://tdn.totvs.com/download/attachments/872696402/image-2024-10-4_8-31-53.png?version=1&modificationDate=1728041673210&api=v2)

![](https://tdn.totvs.com/download/attachments/872696402/image-2024-10-4_8-32-6.png?version=1&modificationDate=1728041673147&api=v2)

Ao adicionar o GPEM630 no cadastro de privilégios, o sistema não apresenta mais a mensagem de *'Usuário não autorizado':*

![](https://tdn.totvs.com/download/attachments/872696402/image-2024-10-4_8-32-11.png?version=1&modificationDate=1728041673077&api=v2)

![](https://tdn.totvs.com/download/attachments/872696402/image-2024-10-4_8-32-30.png?version=1&modificationDate=1728041672980&api=v2)

****Saiba Mais:**  
Para adquirir maior conhecimento acesse o link abaixo:**

**<https://tdn.totvs.com/pages/viewpage.action?pageId=872696402>**
