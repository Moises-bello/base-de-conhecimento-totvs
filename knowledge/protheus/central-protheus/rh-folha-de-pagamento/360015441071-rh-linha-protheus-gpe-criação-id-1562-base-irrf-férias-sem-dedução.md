---
article_id: 360015441071
category: RH - Folha de Pagamento
content_hash: a1f6455e9f2a4b71ed554eeb78c5fed226399fa0748c7376857666f073a64dca
fetched_at: '2026-06-28T22:44:14.873448+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Criação Id 1562 - Base IRRF Férias Sem Dedução
type: support-article
updated_at: '2026-06-18T20:22:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015441071-RH-Linha-Protheus-GPE-Cria%C3%A7%C3%A3o-Id-1562-Base-IRRF-F%C3%A9rias-Sem-Dedu%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26593986957079) Tempo aproximado para leitura: 00:02:00 min**

**Ocorrência**  
No módulo **Gestão de Pessoa**l foi criado o identificador de cálculo **1562** - Base IRRF Férias sem Dedução.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**  
Quando o funcionário possui **férias no mês**, o cálculo de férias é gerado no evento **S-1210** como tipo de pagamento 7 e também é gerado as verbas de férias no evento S-1200. Isso está correto, pois é necessário para a apuração correta do INSS.

Porém, a **base de IRRF de férias** acaba ficando dobrada no retorno do evento S-5002 pois o sistema do eSocial também considerou as verbas de férias enviadas no evento S-1200, além da enviada no evento S-1210, na apuração da base de IRRF.

**Solução**  
Efetuado a criação do **Id de cálculo** **1562** - Base de IRRF Férias s/ dedução que será gerado no cálculo da folha com o objetivo de deduzir os valores de provento de férias da base de IRRF de férias quando for efetuado o envio do evento **S-1200**. Essa verba será composta pela **somatória das verbas de provento de férias com incidência 13 para IR eSocial** e não irá alterar o líquido de folha do funcionário por se tratar de base e por não ter incidências para folha.

Dessa forma, tanto a base de INSS quanto a base de IRRF apurados pelo eSocial ficarão corretos.

A verba deverá ser cadastrada com natureza informativa **9989**, de tipo **base (desconto)** para ser utilizada como Informativa Dedutora no eSocial e com incidência **13** para IR, para ser deduzida da base de IRRF de férias quando efetuado o envio do evento S-1200.

Por exemplo, segue abaixo como ficaria o cálculo de folha do funcionário:

| **Id de Cálculo** | **Descrição** | **Valor** |
| --- | --- | --- |
| 0031 | Salário | R$ 2.000,00 |
| 0072 | Férias | R$ 2.000,00 |
| 0073 | Férias mês seguinte | R$ 2.000,00 |
| 0077 | 1/3 férias | R$ 700,00 |
| 0078 | 1/3 férias mês seguinte | R$ 700,00 |
| 0082 | Média de horas | R$ 100,00 |
| 0083 | Média de horas mês seguinte | R$ 100,00 |
| 1562 | Base de IRRF Férias s/ dedução | R$ 5.600,00 |

**Saiba Mais**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[DRHESOCP-6885 Criação Id 1562 - Base IRRF Férias Sem Dedução](http://tdn.totvs.com/pages/viewpage.action?pageId=394210801)

[RH - Férias](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597291-RH-F%C3%A9rias)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
