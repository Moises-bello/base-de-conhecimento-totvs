---
article_id: 12135206547223
category: RH - Folha de Pagamento
content_hash: 476402def17f7110041eb02977568dc608284c546e7e1502aa7f30fbca8b4a9a
fetched_at: '2026-06-28T22:44:12.009888+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Calculo da Folha Finalizado Pela FinalCalc() ou
  Pela EndCalc() - S_CARGAAPD
type: support-article
updated_at: '2024-09-09T17:56:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12135206547223-RH-Linha-Protheus-GPE-Calculo-da-Folha-Finalizado-Pela-FinalCalc-ou-Pela-EndCalc-S-CARGAAPD
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26247677679639) Tempo aproximado para leitura: **00:03:00 min**

**Ocorrência**

Ao efetuar o cálculo da folha de pagamento, sistema não realiza o cálculo para algumas matrículas, e no log de ocorrências é apresentada a mensagem: Calculo Finalizado Pela FinalCalc() ou Pela EndCalc() - S\_CARGAAPD.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12134818453655)

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.

**Causa**A fórmula S\_CARGAAPD durante o cálculo da folha de pagamento, verifica as informações na RGB e gera os dados consolidados na tabela SRC. Esta mensagem é apresentada no log de cálculo, quando, por algum motivo, não é possível realizar está transição.

**Solução**

Um dos principais motivos, para que a mensagem seja apresentada, é a ausência do cadastro da verba de ID 1893 (Informativo dedução IRRF Férias).

Verifique se existe verba cadastrada vinculada a este ID no ambiente. Ele deve ser cadastrado da seguinte forma:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12134820235159)

Após efetuar o cadastro, calcule a folha novamente.

**OBS:** o cadastro dos IDs 1891 e 1892 não é obrigatório, estes IDs são necessários apenas para empresas que possuem processos vinculados. os dados para a tabela RGB, veja se você a integração não foi realizada para um período diferente daquele que está sendo calculado no momento.

**Importante:** é imprescindível sempre manter o ambiente com as últimas atualizações disponíveis no portal do cliente, incluindo o Pacote de Expedição Contínua do RH - <https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA>. Em ambiente, com os arquivos de Helps atualizados, a mensagem referente a obrigatoriedade de cadastro do ID1893 para prosseguir com o cálculo é apresentada corretamente, facilitando a correção.

**Saiba Mais:**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)

<https://tdn.totvs.com/display/PROT/DRHROTPRT-6153+DT+Rdmake+UPDBINFER>
