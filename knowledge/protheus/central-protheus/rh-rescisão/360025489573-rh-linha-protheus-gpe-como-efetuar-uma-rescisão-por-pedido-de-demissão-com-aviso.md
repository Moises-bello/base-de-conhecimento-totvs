---
article_id: 360025489573
category: RH - Rescisão
content_hash: 6701f241c102f45808460853a9f1ba96228c96fe73cf9cce5ca540f921c4d884
fetched_at: '2026-06-28T22:43:48.671454+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como efetuar uma rescisão por pedido de demissão
  com aviso prévio trabalhado quando não há o cumprimento dos 30 dias de aviso
type: support-article
updated_at: '2025-07-17T19:03:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025489573-RH-Linha-Protheus-GPE-Como-efetuar-uma-rescis%C3%A3o-por-pedido-de-demiss%C3%A3o-com-aviso-pr%C3%A9vio-trabalhado-quando-n%C3%A3o-h%C3%A1-o-cumprimento-dos-30-dias-de-aviso
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26670431759639)***Tempo aproximado para leitura: **00:01:00 min****Dúvida** Como efetuar uma rescisão por pedido de demissão com aviso prévio trabalhado quando não há o cumprimento dos 30 dias de aviso?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Quando a rescisão é por pedido de demissão com aviso trabalhado e o funcionário não cumpre os 30 dias de aviso, o aviso prévio se mantém como trabalhado assim em rescisão deve ser lançado como falta os dias não trabalhados.

Exemplo:  
Funcionário trabalhou 11 dias e deixou de trabalhar 19 dias dos 30 dias de aviso prévio trabalhado:  
Lançar na rescisão a verba de ID 0054-FALTAS na quantidade de dias que o funcionário não cumpriu o aviso trabalhados, pois como no ato do pedido de demissão foi acordado que ele cumpriria 30 dias de aviso trabalhado, os dias que ele não cumpriu são caracterizados como faltas, então não deverá ser feita nenhuma manutenção no cabeçalho da rescisão, mantendo ela como Rescisão por Pedido de Demissão com Aviso Trabalhado (na tabela S043 a coluna Aviso Prévio para o tipo de rescisão em questão deve ficar com T).  
Lançamento das faltas:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040123913)  
Cálculo da rescisão:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039283054)  
Caso prefira lançar faltas sem incidências (médias), poderá ser usado os IDs abaixo, que também são de faltas:

|  |  |
| --- | --- |
| Codigo | Descricao |
| 0054 | Faltas |
| 0242 | Faltas (II) |
| 1364 | Faltas III |
| 1365 | Faltas IV |

**Saiba mais:**[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)  
[Faltas no Aviso Prévio](https://tdn.totvs.com/pages/releaseview.action?pageId=676059206)
