---
article_id: 23927466918935
category: Financeiro - Contas a Receber - Comunicação Bancária CNAB
content_hash: da5b3d354bc105d1bea17a97dffb0b5269cc718803531521b1eeef259d6e4bb2
fetched_at: '2026-06-28T22:37:48.017571+00:00'
product: protheus
section_id: 26656449081111
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA200 FINA100 - Como
  estonar tarifa bancária (despesa bancária) que foi gerado automaticamente pela rotina
  FINA200 Retorno de CNAB a receber.
type: support-article
updated_at: '2026-03-25T19:45:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23927466918935-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA200-FINA100-Como-estonar-tarifa-banc%C3%A1ria-despesa-banc%C3%A1ria-que-foi-gerado-automaticamente-pela-rotina-FINA200-Retorno-de-CNAB-a-receber
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23927466907927) Tempo aproximado para leitura: **00:08 min**  
  
**Dúvida**  
FINA200 FINA100 - Como estonar tarifa bancária (despesa bancária) que foi gerado automaticamente pela rotina FINA200 Retorno de CNAB a receber.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]  
  
**Cenário:**

Quando o banco é o responsável pela emissão dos boletos,  geralmente é cobrando uma taxa de cada impressão de boletos, e isso é possível ser visualizado ao emitir o relatório "**FINR650 - Relatório de Retorno de CNAB**"

No exemplo baixado será cobrada uma tarifa bancária de R$ 2,00.

[**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23927490160023)**](https://centraldeatendimento.totvs.com/hc/article_attachments/23927490160023)

Ao realizar o recebimento pela rotina "**FINA200 - Retorno CNAB a Receber**", podemos observar que o sistema automaticamente lança uma movimentação bancária a pagar referente à tarifa bancária.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/23927490160535)](https://centraldeatendimento.totvs.com/hc/article_attachments/23927490160535)

Segue outra visualização na posição de título a receber.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/23927490169111)](https://centraldeatendimento.totvs.com/hc/article_attachments/23927490169111)

Segue outra visualização do "**FINR470 - Relatório de Extrato Bancário", em que** é possível visualizar o lançamento da despesa bancária que não é amarrada ao título. Sendo um registro independente

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/23927466911127)](https://centraldeatendimento.totvs.com/hc/article_attachments/23927466911127)

**Solução:**

Caso seja efetuado o estorno da baixa do título, a despesa não será estornada de forma automática, pois ela é um registro independente.

Para realizar o estorno da tarifa bancária, deverá acessar a rotina "**FINA100 - Movimento Bancário**" e realizar uma movimentação bancária a receber referente ao estorno da despesa bancária.

Segue um exemplo:

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/23927466912663)](https://centraldeatendimento.totvs.com/hc/article_attachments/23927466912663)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/23927490173463)](https://centraldeatendimento.totvs.com/hc/article_attachments/23927490173463)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/23927490174103)](https://centraldeatendimento.totvs.com/hc/article_attachments/23927490174103)

Mais informações:

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB - Como gerar despesa bancária no retorno do CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016697191-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Como-gerar-despesa-banc%C3%A1ria-no-retorno-do-CNAB)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA200 - No Retorno de Cobrança não baixa os títulos devido a configuração da despesa de cobrança](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018106252-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA200-No-Retorno-de-Cobran%C3%A7a-n%C3%A3o-baixa-os-t%C3%ADtulos-devido-a-configura%C3%A7%C3%A3o-da-despesa-de-cobran%C3%A7a)
