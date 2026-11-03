---
article_id: 37948094370583
category: Financeiro - Borderô contas a Receber
content_hash: d67bc90fa9c776439e1d6853eedc041f8211172f294596b035b2163debf1ef3b
fetched_at: '2026-06-28T22:37:39.693989+00:00'
product: protheus
section_id: 35057237655191
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus  - FINA060 - Operação em Moedas
  estrangeiras não grava variação cambial em carteira descontada
type: support-article
updated_at: '2026-01-29T14:35:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37948094370583-Cross-Segmentos-Backoffice-Linha-Protheus-FINA060-Opera%C3%A7%C3%A3o-em-Moedas-estrangeiras-n%C3%A3o-grava-varia%C3%A7%C3%A3o-cambial-em-carteira-descontada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37948110781335) Tempo aproximado para leitura: **00:03 min**

**Dúvida**  
Operação em moedas estrangeiras não grava variação cambial em carteira descontada.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FINA060 - Todas as versões.

**Solução**

**Emissão do título e taxa inicial**

Ao incluir um título em moeda estrangeira, o sistema utiliza a taxa de câmbio do dia da emissão.

* O valor em Reais (Moeda 1) é fixado com base na taxa de cadastro da Moeda 2 na data da emissão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37951542019351)

* No módulo **Contas a Receber**, o título está sendo apresentado no valor de **R$ 1.000,00**, bem como na **Moeda 2** R$ 2.000,00.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/37951542020503)**

#### **Registro do Borderô (Desconto)**

* Na geração do borderô para envio ao banco (Carteira Descontada), o sistema registra a transferência de custódia **(vende o título para o banco, e o banco antecipa o valor para a empresa, gerando a movimentação bancária no momento da transferência para situação 2 descontada)**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37951549282967)

* **Comportamento Nativo:** No momento da geração do borderô, o Protheus **não realiza a apuração da variação cambial** nos movimentos bancários (Tabela SE5). O sistema mantém o registro do título conforme a taxa original até que ocorra o fato gerador da baixa.  
  Exemplo: Caso o parâmetro da rotina esteja com o conteúdo 'Baixa Título descontada?' "**SIM,**" não será gerada a variação cambial.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37951542026007)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37951542027159)

#### **Baixa do Título e Apuração da Variação**

Caso o parâmetro da rotina esteja com o conteúdo 'Baixa Título descontada? "**NÃO**" o título que foi transferido para a situação 2 descontada permanecerá com status **"Em aberto"** mesmo que tenha movimentado entrada de valor referente à venda do título.

A apuração da variação cambial (correção monetária) ocorre no momento da **baixa do título através da rotina FINA070 - Baixa a receber manual**, utilizando a taxa de câmbio da **data da baixa**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37951549286935)

### 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37951542033687)

**Importante**

O Protheus entende que a liquidação financeira efetivada para fins de variação cambial ocorre na data da baixa informada no sistema.

**Saiba mais**

[**Transferências - FINA060**](https://tdn.totvs.com/pages/releaseview.action?pageId=271405699)
