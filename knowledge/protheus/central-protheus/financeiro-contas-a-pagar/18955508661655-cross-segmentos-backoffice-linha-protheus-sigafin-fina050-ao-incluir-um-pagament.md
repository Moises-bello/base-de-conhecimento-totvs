---
article_id: 18955508661655
category: Financeiro - Contas a Pagar
content_hash: a3323ef628c35052d9599403fb13ad7aa20d69ef166a39f6f7ce68813f74b205
fetched_at: '2026-06-28T22:38:08.529334+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050 - Ao incluir
  um pagamento antecipado do tipo PA parametrizado para não gerar movimentação bancária,
  contudo gera a movimentação bancária
type: support-article
updated_at: '2025-05-30T20:18:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18955508661655-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Ao-incluir-um-pagamento-antecipado-do-tipo-PA-parametrizado-para-n%C3%A3o-gerar-movimenta%C3%A7%C3%A3o-banc%C3%A1ria-contudo-gera-a-movimenta%C3%A7%C3%A3o-banc%C3%A1ria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18955529089687) Tempo aproximado para leitura: **00:10:00 min****Dúvida**Ao incluir um pagamento antecipado do tipo PA parametrizado para não gerar movimentação bancária, contudo gera a movimentação bancária.  
  
  
**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - Financeiro - FINA050 - Todas as versões.  
  
  
**Solução**

Caso o banco que amarrado no **tipo: PA** esteja configurado para ser um banco caixa, esse pagamento antecipado **tipo: PA**  sempre na sua inclusão irá fazer a geração da movimentação bancária, mesmo que na sua inclusão esteja parametrizado os perguntes

**Gera cheque para adiantamento = NÃO**

**Mov. Banc. sem cheque = NÃO**

As perguntas estão localizadas

1. Acesse a **rotina Contas a Pagar (FINA050)**;  
2. Clique na tecla **F12** para acionar os parâmetros;  
3. Localize as perguntas

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/18955521230871)](https://centraldeatendimento.totvs.com/hc/article_attachments/18955521230871)

O que seria o conceito de banco caixa, e onde é cadastrado?

O **banco caixa**, seria tipo um cofre que a empresa possui com dinheiro em espécie, caso precise fazer algum tipo de adiantamento para um colaborador e retire o dinheiro do cofre sempre haverá a movimentação de saída do valor do cofre, por isso ao amarrar um banco caixa em um **tipo: PA** sempre terá a movimentação bancária.

O banco esteja configurado para operar em carteira (parâmetro **MV\_CARTEIR**. Exemplo de conteúdo: "**CX1/CX2/CX3**");

O banco esteja configurado como um caixa geral financeiro (parâmetro **MV\_CXFIN**. Exemplo de conteúdo "**CX1/00001/0000000001**");

**Sabia mais:**

Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA240 - Como incluir um PA (Pagamento Antecipado) em um borderô

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016740191-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA240-Como-incluir-um-PA-Pagamento-Antecipado-em-um-border%C3%B4>

Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA070 - Baixa em Lote

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018358692-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA070-Baixa-em-Lote>

Cross Segmento - Backoffice Linha Protheus -SIGAFIN - FINA100 - Help: F100DTCR2

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404845187095-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA100-Help-F100DTCR2>

Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Como incluir um PA com cheque

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015681912-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Como-incluir-um-PA-com-cheque>

Cross Segmento Protheus - Backoffice Linha Protheus - SIGAFIN - Quais os modos de inclusão de PA

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004726827-Cross-Segmento-Protheus-Backoffice-Linha-Protheus-SIGAFIN-Quais-os-modos-de-inclus%C3%A3o-de-PA>
