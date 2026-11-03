---
article_id: 16275703559575
category: TAF - eSocial - Eventos Não Periódicos
content_hash: eb3b67286f3138b4bfeef3b835bf0807a3075fdce06d8970e7349c3b12179032
fetched_at: '2026-06-28T22:45:18.018622+00:00'
product: protheus
section_id: 1500001548002
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Integração - S-3000 - Desprezado pois
  não foi transmitido/ Não foi encontrado. A exclusão será desprezada/ Desprezado
  pois está aguardando retorno do governo
type: support-article
updated_at: '2026-06-25T11:07:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16275703559575-RH-Linha-Protheus-TAF-eSocial-Integra%C3%A7%C3%A3o-S-3000-Desprezado-pois-n%C3%A3o-foi-transmitido-N%C3%A3o-foi-encontrado-A-exclus%C3%A3o-ser%C3%A1-desprezada-Desprezado-pois-est%C3%A1-aguardando-retorno-do-governo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16275689314071) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**

Ao tentar integrar o evento de exclusão S-3000 (TAFA269) para o TAF, alguns eventos não são integrados, podendo ser apresentado as mensagens abaixo:

**\*\*Desprezado pois não foi transmitido**

**\*\*Não foi encontrado. A exclusão será desprezada**

**\*\*Desprezado pois está aguardando retorno do governo**

*Exemplo no log:*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16274289760279)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16274338932375)

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Todas as versões  
  
**Solução**Caso seja apresentada as mensagens citadas, durante tentativa de integração do evento S-3000, segue explicação:

**Atenção:**

Ocorrendo uma das mensagens que vamos explicar neste documento, pedimos que, entre no módulo do TAF (módulo 84) e rode a rotina de ***"Ajuste de Status de Exclusão"***, conforme explicamos no link abaixo:

[RH - Linha Protheus - TAF - eSocial - NÃO PERIÓDICOS - Como ajustar status de exclusão no TAF - S-3000](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055468253)

O evento que originou o S-3000, exemplo, o S-1200 ou S-1210, devem ficar com legenda **"vermelha"**, o que indica que o S-3000 foi transmitido e o status no TAF está correto, como no exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26492158964887)

Após executar o ***"Ajuste de Status de Exclusão"***, tente integrar novamente ao TAF o registro, verifique se a mensagem permanece a mesma no log de integração do GPE (Protheus Recursos Humanos).

**Mensagens do sistema:**

**a) Desprezado pois não foi transmitido**

A rotina de integração analisa se já existe um evento S-3000 para o CPF em questão, pendente de transmissão no monitor.

A rotina não gera outro para substituir, é mantido o que já existe no TAF para aquele CPF.

Para excluí-lo é necessário entrar na rotina do evento que originou o S-3000, localizar o registro e solicitar, "**Desfazer Exclusão**"; (não é possível realizar o processo para mais de um registro)

[Automação Fiscal - eSocial - Como desfazer um evento de exclusão (S-3000) criado indevidamente no TAF.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035089373)

**b) Não foi encontrado. A exclusão será desprezada**  
Se o sistema não encontra o evento que originou o S-3000 ( exemplo: o S-1210 que deseja excluir), ele também não integra o S-3000 para o TAF.

E neste caso é apresentada a mensagem:

*Registro S-XXXX do funcionário  XXX (CPF)  - XXX (nome) não foi encontrado. A exclusão será desprezada.*

**c) Desprezado pois está aguardando retorno do governo**

A rotina de integração identifica um evento S-3000 para o CPF, inconsistente no monitor.

O sistema não gera outro para substituir, é mantido o que já existe no TAF para aquele CPF.

Entre no monitor do TAF (Painel eSocial do Futuro) e verifique a inconsistência retornada para o evento S-3000.
