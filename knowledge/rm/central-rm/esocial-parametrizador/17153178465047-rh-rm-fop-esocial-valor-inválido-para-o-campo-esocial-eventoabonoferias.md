---
article_id: 17153178465047
category: eSocial - Parametrizador
content_hash: cae39b8d09ac73892c1634c899730c31c197c2a2ec36a9cb706c1f50234f7a6d
fetched_at: '2026-06-28T22:47:06.274859+00:00'
product: rm
section_id: 1500000834501
source: central-rm
title: RH - RM - FOP - eSocial - Valor inválido para o campo 'eSocial_EventoAbonoFerias'
type: support-article
updated_at: '2024-06-05T11:50:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17153178465047-RH-RM-FOP-eSocial-Valor-inv%C3%A1lido-para-o-campo-eSocial-EventoAbonoFerias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17153162992663) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao tentar cadastrar um evento no **Configurações |** **Parametrizador | eSocial | Configurações Gerais 6/7** no campo Evento Abono Férias Envelope é apresentado a seguinte mensagem **valor inválido para o campo 'eSocial\_EventoAbonoFerias'**.  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro ocorre quando o campo **Evento Abono Férias envelope**localizado no menu **Configurações | Parametrizador | eSocial | Configurações Gerais 6/7**é preenchido com um evento criado que não condiz com as regras para o campo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17262913861527)

**Solução**Para correção dessa ocorrência, siga os passos abaixo:

1. Acesse o menu **Administração de Pessoal | Eventos**e crie uma verba do tipo **Provento**, sem código de cálculo e sem incidência;
2. Após acesse o menu **Configurações | Parametrizador | eSocial | Configurações Gerais 6/7**e informe a verba criada no campo **Evento Abono Férias envelope**;
3. Transmita o evento S-1010 da nova verba criada.

**Saiba mais**  
Para maiores informações, acesse:  
      • [Configurações Gerais 6/7](https://tdn.totvs.com/pages/releaseview.action?pageId=540899121)
