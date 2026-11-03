---
article_id: 4402387769623
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 68545fcbae7ad551ce8c3e31572b8c0cf36f566379736c0722713f06774847ac
fetched_at: '2026-06-28T22:40:48.929971+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - TAF - TAFA433-  Simulação apuração
  LALUR
type: support-article
updated_at: '2025-09-12T14:27:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402387769623-Cross-Segmento-Backoffice-Linha-Protheus-TAF-TAFA433-Simula%C3%A7%C3%A3o-apura%C3%A7%C3%A3o-LALUR
---

**Dúvida**Cadastro e funcionalidade do processo de simulação de apuração do LALUR.

**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - TAF - Todas as versões  
  
**Solução**A simulação tem como objetivo comparar o calculo de duas formas de tributação, por exemplo: Apuração mensal pela Receita Bruta X Estimativa mensal Real. Ou pode simular a apuração de uma única forma de tributação.

**Passo 1-** Rotina [Cadastro de tributo (TAFA430) :](https://tdn.totvs.com/display/public/TAF/Cadastro+de+Tributos+-+TAFA430+-+TAF+-+P12#CadastrodeTributosTAFA430TAFP12-principaiscampos)

Para que a Simulação compare qual a forma mais vantajosa de apuração é necessário informar a alíquota do IRPJ, Alíquota de adição e a parcela isenta.

Para o calculo da presunção da Receita Bruta, na parte inferior, "Informações especificas do IRPJ" informar a alíquota de presunção e a descrição da receita, no padrão temos 4 alíquotas que poderão ser informadas. Não é necessário que todas as alíquotas sejam preenchidas, deve corresponder as receitas conforme atividade da empresa.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402386844951)

**Passo 2** - [Rotina Evento Tributário (TAFA433)](https://tdn.totvs.com/pages/releaseview.action?pageId=248578386):

* Incluir um evento tributário 000003 - Lucro Real, estimativa por Receita Bruta

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402387291799)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402393864087)

* Criar um outro evento tributário, desta vez com o código 000002- Lucro Real, Estimativa por levantamento de Balanço.

Importante! O cadastro "TRIBUTO" deve ser o mesmo para os dois eventos tributários. Essa é a única forma que o sistema irá relaciona-los para simular a apuração.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402393988887)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402387538967)

* Simulação -> Posicione em um evento tributário + Ações relacionadas + Simulação de apuração.

No campo evento tributário 1: Virá o cadastro do evento posicionado.

Assinale a opção Simulação comparativa + ENTER e selecione o outro evento tributário criado (ambos com o mesmo tributo no cadastro).

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402388310167)

Clique em Selecionar Período, selecione o período + simular

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402388394903)

Obs. Os períodos que a SIMULAÇÃO considera são períodos cadastrados na rotina TAFA444.

Evento 1-  Representa os dados e apuração considerando a Receita Bruta.

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402388436503)

Evento 2 - Representa os dados e apuração considerando o Lucro Real, Estimativa por levantamento de Balanço.

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402394648471)

Na Aba Detalhamento e Log de apuração, constam os históricos das movimentações que estão sendo consideradas no calculo.

**Saiba mais:**

Boletim Técnico TDN: [Simulação da Apuração](https://tdn.totvs.com.br/pages/releaseview.action?pageId=270906240)

Cadastro Evento Tributário: [Evento Tributário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404225269527-Cross-Segmento-Backoffice-Linha-Protheus-TAF-TAFA433-Cadastro-do-Evento-tributario-BLOCO-M-e-BLOCO-N)

Compensação de Prejuízo: [Compensação de prejuízo parte B, com reflexo na parte A](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037921673-MP-SIGACTB-LALUR-COMPENSA%C3%87%C3%83O-DE-PREJU%C3%8DZO-PARTE-B-COM-REFLEXO-NA-PARTE-A-)
