---
article_id: 6220584766743
category: ACOMPANHA CUSTOS - JORNADA DE FECHAMENTO (NOVO)
content_hash: b6d5570a90f7f8f74c9bd4b9a8876dcf25f7cd3d735a7c2745bb209ab37ee35a
fetched_at: '2026-06-28T22:38:48.143184+00:00'
product: protheus
section_id: 5367899706647
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 -  Error.log
  "JOB threads doesn't support remote/visual components."
type: support-article
updated_at: '2025-03-12T12:25:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6220584766743-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-Error-log-JOB-threads-doesn-t-support-remote-visual-components
---

**Ocorrência**

Ao fazer o processo de fechamento de Estoque na rotina Acompanha Custos (MATA038) é gerado um errorlog "JOB threads doesn't support remote/visual components."

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**

Ao executar a rotina de Acompanha Custos, e aparecer o errorlog abaixo:

![](https://p23.zdusercontent.com/attachment/888110/Gx93dy8RWxA6welRrkugysCq9?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..vD-S30-AcWhY5PtTSKyO_w.E8yZ8WY9zusT11l-lcnlrpKlhlw12VXeaMtSgPQoj0HRtA6uMLF6anLm776NEV6mpufpzuFxDhKsr0_YpOHpRAJkljTkHBdSrFJjEIzkAT5YTySDovMzT1CIgMK2p9XZ7d1xDZ3lBfaGuB8-k_dqm6Xd56I--jPqo3W68o_1QcrJ6VBjdpugCoTkuTiQz2DVGQs5Uz8CrCf9xBXwRp4Yj4LLWc0s39RU8NTTIEX6Y77P7yfN0jWVIcCVY32SG7Q5THU80WzMMKzzdctD7sACZZDO9qsqh_wfPVSHdRfcjTU.rhdzRfK0o9x3PyRHjn8zVw)

**Solução**

Nesse cenário, é necessário aplicar o ultimo pacote acumulado para sua release.

<https://tdn.totvs.com/pages/releaseview.action?pageId=522000602>

Quando o erro ocorre, e existe a chamada de uma função dentro do error log, por exemplo algum fonte com **U\_** é necessário validar se esse ponto de entrada, esteja tentando exibir componentes visuais em tela, Caso sim não será mais possivel na Acompanha Custos.

Os pontos de entrada existentes nas rotinas de fechamento continuam disponíveis, porém por conta da tecnologia utilizada, não permitem mais a apresentação de interface.

Caso você utilize algum ponto de entrada com abertura de tela, será necessário adaptá-lo para que ele trabalhe considerando que o processamento da rotina ocorrerá sem possibilidade de exibição de interface, como se fosse uma execução via schedule ou execauto. 

**Saiba mais**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - O que é a rotina Acompanha Custos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5065773526039)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Validação para inicia a rotina Acompanha Custos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5240908654999)*
