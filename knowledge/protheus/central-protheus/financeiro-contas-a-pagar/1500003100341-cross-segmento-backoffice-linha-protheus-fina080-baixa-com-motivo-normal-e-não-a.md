---
article_id: 1500003100341
category: Financeiro - Contas a Pagar
content_hash: c8c4f330989de9d00eedb1cf11e969931395380ebf632944e9729dd8823a2fd6
fetched_at: '2026-06-28T22:38:08.364361+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus – FINA080 -  Baixa com motivo normal
  e não aparece no extrato bancário
type: support-article
updated_at: '2023-04-18T23:12:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003100341-Cross-Segmento-Backoffice-Linha-Protheus-FINA080-Baixa-com-motivo-normal-e-n%C3%A3o-aparece-no-extrato-banc%C3%A1rio
---

**Dúvida**Fiz uma baixa com motivo normal e não aparece no extrato bancário?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – A partir da versão 11.80  
  
**Solução**No cadastro de **Motivos de baixa** (**FINA490**), notamos que o tipo de baixa **NORMAL** movimenta banco e aguarda movimentação de cheque. No padrão, ambos estão com o **Motivo de baixa** "**S**" neste caso, a movimentação do título ficará como **E5\_TIPODOC**  = **BA**, aguardando inclusão de cheque para movimentação bancaria.  
![teste_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102144274/teste_1.png)  
Incluir cheque Manter o tipo **Normal** e preencher com o número do cheque.  
Caso seja configurado o parâmetro **MV\_LIBCHEQ** com o conteúdo em **S**:  
**Baixa automática** - Motivo **NORMAL** - informar o número do cheque:  
O sistema gera a movimentação bancária no momento da baixa.   
**Baixa automática** - Motivo **NORMAL** - sem informar o número do cheque:  
Após a baixa do título o sistema aguarda o usuário **Juntar um cheque** e gera a movimentação bancária (do cheque)  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003321961/mceclip0.png)

**Saiba Mais**  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052125413>
