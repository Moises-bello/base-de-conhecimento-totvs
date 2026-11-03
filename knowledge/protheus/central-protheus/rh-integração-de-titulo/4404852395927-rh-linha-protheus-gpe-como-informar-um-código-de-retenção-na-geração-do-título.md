---
article_id: 4404852395927
category: RH - Integração de Titulo
content_hash: f901a4026d5d6bb567e00a011c0cf4c89894a464bea40c38ccf1bc509ac66255
fetched_at: '2026-06-28T22:43:36.273886+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Como informar um código de retenção na geração
  do Título
type: support-article
updated_at: '2025-07-17T12:55:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404852395927-RH-Linha-Protheus-GPE-Como-informar-um-c%C3%B3digo-de-reten%C3%A7%C3%A3o-na-gera%C3%A7%C3%A3o-do-T%C3%ADtulo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33531116301591) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como informar um código de retenção na geração do Título?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as Versões  
  
**Solução**  
Acesse **Miscelânea-> Títulos-> Definição:**1) O título criado deverá ter o campo **Cod Ret Inf - RC0\_CODRET** preenchido com o código de pagamento, será possível informar um conteúdo para o mesmo, após ajustar o conteúdo do campo **Tp Ret Imp. Renda - RC0\_TPRET** para 1 - Informado.  **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404843978007)**

2) Acesse **Miscelânea -> Títulos -> Geração:**Configure a geração do título de acordo com a data de pagamento (data de cálculo da folha no cadastro de períodos), competência e código do título:

3) Acesse **Miscelânea -> Títulos -> Manutenção:**Desta forma o título será gerado com o campo **Cod Retenção - RC1\_CODRET** preenchido.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404844033175)

4) Acesse **Miscelânea -> Títulos -> Integração:**Preencha os parâmetros para integração do título gerado  
  
4) No SIGAGIN - Financeiro Acesse **Atualizações-> Contas a Pagar-> Contas a Pagar:**Com a execução destes procedimentos o campo **Cd. Retenção - E2\_CODRET**  localizado na Aba **Impostos** será preenchido com o código informado pelo **SIGAGPE - Gestão de Pessoal**.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404852279319)**Saiba Mais**  
[Artigos sobre Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
