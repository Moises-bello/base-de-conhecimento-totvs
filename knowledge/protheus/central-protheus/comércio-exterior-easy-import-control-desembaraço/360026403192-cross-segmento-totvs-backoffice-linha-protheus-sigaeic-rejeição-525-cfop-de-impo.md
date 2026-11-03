---
article_id: 360026403192
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: eb1334938165d47552507986d5163c9f4ce94ca4a727ed525a37ec6bacc8394f
fetched_at: '2026-06-28T22:39:50.203294+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Rejeição 525:
  CFOP de Importação e não informado dados da DI'
type: support-article
updated_at: '2024-02-21T14:05:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026403192-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Rejei%C3%A7%C3%A3o-525-CFOP-de-Importa%C3%A7%C3%A3o-e-n%C3%A3o-informado-dados-da-DI
---

**Dúvida**

Rejeição 525: CFOP de Importação e não informado dados da DI - Quais as verificações para esta rejeição?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.

**Solução**

1. Campo C7\_SEQUEN deve possuir o mesmo conteúdo do campo W3\_POSICAO, caso C7\_SEQUEN esteja em Branco:

* O parâmetro MV\_EXECCOM deve estar habilitado;
* Verifique no SIGACFG se o C7\_SEQUEN esta Usado por todos os módulos;
* Campo C7\_SEQUEN deve possuir o mesmo tamanho e tipo do campo W3\_POSICAO;
* Na impossibilidade de refazer o Purchase Order, preencha o conteúdo do campo C7\_SEQUEN de acordo com o W3\_POSICAO, estorne a nota gerada no SIGAEIC e gere novamente.

2-  Informação de Lote

* Caso informado os Lotes no SIGAEIC na Manutenção de Lotes do Desembaraço o parâmetro MV\_LOTEEIC deve estar habilitado;
* Caso o lote seja informado apenas na classificação do Documento de entrada o parâmetro MV\_LOTEEIC deve estar desabilitado;

3- Inconsistência na gravação da SD1 e SC7

* Verifique se os campos da D1\_PEDIDO e D1\_ITEMPC estão preenchidos, para preenchimento dos campos é necessário que estejam como usados para todos os módulos.   
  ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067316893)
* Verifique se os campos da SWN WN\_PO\_NUM e WN\_ITEM, estão preenchidos:   
  ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360066260594)
* Verifique se na SC7 os campos C7\_NUMIMP e C7\_SEQUEN estão preenchidos, é necessário que os mesmos estejam como usado para todos os módulos, ao incluir a *Purchase Order* serão preenchidos automaticamente.  
  ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067322913)  
  \*Observação: A SC7 é gravada de acordo com o conteúdo da SW3 (W3\_POSICAO).

Importante os fontes AVGERAL e NFESEFAZ devem esta atualizados atualizados.
