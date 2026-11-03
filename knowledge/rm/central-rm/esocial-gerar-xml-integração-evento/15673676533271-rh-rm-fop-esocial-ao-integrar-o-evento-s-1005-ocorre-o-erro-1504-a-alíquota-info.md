---
article_id: 15673676533271
category: eSocial - Gerar XML/ Integração Evento
content_hash: e62ea7147d8e574cdd63b7c7109a6dda2951f2c5345e034ceee0c5e55888c433
fetched_at: '2026-06-28T22:47:11.970899+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao integrar o evento S-1005 ocorre o erro 1504:
  A alíquota informada deverá ser diferente da alíquota definida na legislação vigente
  para o código CNAE preponderante informado'
type: support-article
updated_at: '2025-07-02T16:56:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15673676533271-RH-RM-FOP-eSocial-Ao-integrar-o-evento-S-1005-ocorre-o-erro-1504-A-al%C3%ADquota-informada-dever%C3%A1-ser-diferente-da-al%C3%ADquota-definida-na-legisla%C3%A7%C3%A3o-vigente-para-o-c%C3%B3digo-CNAE-preponderante-informado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15673695960983) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao integrar o evento S-1005 com o governo ocorre o erro **1504: A alíquota informada deverá ser diferente da alíquota definida na legislação vigente para o código CNAE preponderante informado (neste caso, devera haver informações de processo em procAdmJudRat).**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15672200683799)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro ocorre ao encaminhar o S-1005 com a informação da Alíquota RAT igual à definida na legislação. De acordo com o leiaute, só é necessário enviar a Alíquota RAT, quando a mesma for diferente do que consta na Legislação e se informada, será necessário informar o **número do Processo Administrativo ou Judicial Relativo à Alíquota RAT.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15672857397783)

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Consulte através do [DECRETO Nº 10.410, DE 30 DE JUNHO DE 2020](https://www.in.gov.br/en/web/dou/-/decreto-n-10.410-de-30-de-junho-de-2020-264503344) qual é a alíquota RAT para o código CNAE da empresa. Caso a alíquota RAT esteja correta e a empresa não tenha processo de alteração, não é necessário o envio para o governo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15673107742615)![](https://centraldeatendimento.totvs.com/hc/article_attachments/15673023139479)

2. Caso possua processo judicial, será necessário informar na seção (ou na filial quando a empresa trabalhar com tomador de serviços) as informações da suspensão bem como o número do processo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15673333351191)

**Importante**Caso a empresa possua Processo Administrativo/Judicial com alteração da Alíquota RAT, será necessário que primeiro cadastre os dadas do processo no RM e encaminhe o XML S-1070 para o governo, para depois encaminhar o S-1005 com as informações do processo.

**Saiba mais**  
Para mais informações acesse:

* [Evento S-1005](https://tdn.totvs.com/display/public/LRM/Evento+S-1005)
* [RH - RM - FOP - eSocial - Cadastro do evento S-1070 Tabela de Processos Administrativos/Judiciais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008847432-RH-RM-FOP-eSocial-Cadastro-do-evento-S-1070-Tabela-de-Processos-Administrativos-Judiciais)
