---
article_id: 360052125413
category: Financeiro - Contas a Pagar
content_hash: 11224fd9274e77fecf3040f568c0373e80693105a3c3069f216a6ad03db1ba4a
fetched_at: '2026-06-28T22:38:07.181723+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus  - SIGAFIN - FINA080 - Baixa manual
  a pagar gerando o campo E5_TIPODOC = "BA". por quê?
type: support-article
updated_at: '2026-05-27T19:06:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052125413-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA080-Baixa-manual-a-pagar-gerando-o-campo-E5-TIPODOC-BA-por-qu%C3%AA
---

**Dúvida**  
Ao realizar a baixa manual a pagar utilizando o motivo de baixa **NORMAL**, o campo **E5\_TIPODOC** é preenchido com **"BA",** por quê?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – A partir da versão 11.80  
  
**Solução**  
Para esclarecer a dúvida inicial, seguem abaixo as possibilidades para o cenário apresentado:

1. Inserir outro motivo de baixa que não exija cheque.

O tipo **DÉBITO CC** realiza movimentação bancária, porém não por cheque. Neste caso, a baixa do título é gerada com o valor no campo **E5\_TIPODOC = "VL"**.  
  
**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080752214)**  
  
2. Alterar **Motivo de baixa NORMAL** para **Cheque = 'N'**

No cadastro de **Motivos de baixa** (**FINA490**), notamos que o tipo de baixa **NORMAL** movimenta banco e aguarda movimentação de cheque. No padrão, ambos estão com o **Motivo de baixa** "**S**" neste caso, a movimentação do título ficará como **E5\_TIPODOC**  = **BA**, aguardando inclusão de cheque para movimentação bancaria.  
  
**![](https://totvssuporte.zendesk.com/attachments/token/AIBs9ubG5li5fLPmgs1B2Jl8A/?name=inline1930067672.png)**  
  
3. Informar o cheque na baixa

Manter o motivo de baixa NORMAL e preencher o número do cheque no momento da baixa.

Caso o parâmetro **MV\_LIBCHEQ** esteja configurado com conteúdo = **"S"**:

* Baixa automática com motivo **NORMAL** e número do cheque informado:  
  O sistema gera a movimentação bancária no momento da baixa.
* Baixa automática com motivo **NORMAL** sem número do cheque informado:  
  Após a baixa do título, o sistema ficará aguardando que o usuário realize a vinculação do cheque para então gerar a movimentação bancária correspondente.

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080752654)**  
  
4. Criar um novo Motivo de Baixa

Na rotina **FINA490**, é possível incluir um novo motivo de baixa configurando o campo **Cheque = "N"**.

Dessa forma, o sistema passará a gerar a movimentação bancária com **E5\_TIPODOC = "VL"**, sem necessidade de informar ou vincular cheque para efetivar a baixa.

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081816413)**
