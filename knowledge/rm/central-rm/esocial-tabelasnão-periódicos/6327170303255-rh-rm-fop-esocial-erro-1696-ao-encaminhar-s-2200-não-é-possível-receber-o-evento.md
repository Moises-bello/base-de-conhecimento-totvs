---
article_id: 6327170303255
category: eSocial - Tabelas/Não Periódicos
content_hash: 5f378baf929ebb7a096d25424b92cafa277659dd7a5d5e4318e74e16467d8e62
fetched_at: '2026-06-28T22:47:10.311937+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 1696 ao encaminhar S-2200: Não é possível receber
  o evento porque existe um evento de Registro Preliminar correspondente (S-2190)
  no RET com versão diferente deste'
type: support-article
updated_at: '2026-01-02T17:19:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6327170303255-RH-RM-FOP-eSocial-Erro-1696-ao-encaminhar-S-2200-N%C3%A3o-%C3%A9-poss%C3%ADvel-receber-o-evento-porque-existe-um-evento-de-Registro-Preliminar-correspondente-S-2190-no-RET-com-vers%C3%A3o-diferente-deste
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37399809937047) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao integrar o evento S-2200 com o Governo é apresentada a inconsistência **Erro 1696: Não é possível receber o evento porque existe um evento de Registro Preliminar correspondente (S-2190) no RET com versão diferente deste.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6328644731671)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
O erro ocorre quando o S-2190 é encaminhado no leiaute 1.0 e o S-2200 é encaminhado no leiaute 1.1.

Na virada do leiaute 2.5 para o S-1.0, o governo passou a realizar a validação de leiaute entre os eventos S-2190 e S-2200. Na ocasião, o governo também publicou uma Nota Orientativa com as seguinte informação:

![](https://totvssuporte.zendesk.com/attachments/token/44T9Gk8mW84pV2J2MlWfzrQDu/?name=image.png)

Na virada entre os leiautes S-1.0 e S-1.1, o governo não publicou nenhuma Nota Orientativa, mas identificamos que estão realizando a mesma validação, apresentando o erro 1696 quando o S-2190 é enviado no leiaute S-1.0 e o S-2200 é enviado no leiaute S-1.1.

**Solução**  
Como a partir do dia 20/03/2023 é obrigatório o envio de eventos no leiaute S-1.1, para solucionar a inconsistência é necessário:

1. Acessar o menu **eSocial | Fila de Eventos/Eventos Periódicos;**  
2. Localizar o evento **S-2190** e clicar em **Processos | Gerar eventos de Exclusão (S-3000);**  
3. Gerar o XML do **S-3000** e enviar ao eSocial;  
4. Em seguida, gerar o XML do S-2200 e envie ao Governo.  
  
**Saiba mais**  
Para mais informações, acesse:  
     - [Leiaute S-1.0 Nota Técnica 06/2022 e Leiaute S-1.1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8560601056023)
