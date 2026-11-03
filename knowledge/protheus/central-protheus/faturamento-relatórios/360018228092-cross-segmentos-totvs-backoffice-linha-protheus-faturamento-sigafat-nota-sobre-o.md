---
article_id: 360018228092
category: FATURAMENTO - RELATÓRIOS
content_hash: 1e8a14770f9738c0e2a6d58593b46e1b0e906f001790f0e657f9cb181118c21f
fetched_at: '2026-06-28T22:38:22.963269+00:00'
product: protheus
section_id: 1500001539381
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Nota sobre o Parâmetro Descrição nos Relatórios do módulo Faturamento
type: support-article
updated_at: '2021-06-08T14:06:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018228092-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Nota-sobre-o-Par%C3%A2metro-Descri%C3%A7%C3%A3o-nos-Relat%C3%B3rios-do-m%C3%B3dulo-Faturamento
---

**Dúvida**Estamos com um problema em relatórios como **MATR550 e MATR780** ,onde a descrição do produto não aparece.  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - todas as versões.  
  
**Solução**

Relatórios como matr550 e matr780 que possuem a pergunta "**quanto a descrição"** ou **utiliza descrição**, tem a opção de seleção para **cadastro de produto(SB1)** ou **cadastro de produto x cliente (SA7).**

Se escolher utilizar produto x cliente , certifique que haja registros na tabela SA7, do contrário, a descrição sairá em branco, o ideal é a utilização por produto, pois o sistema buscará a descrição do **cadastro de produtos (mata010).**

*Exemplo da pergunta no relatório:*

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402317102999/mceclip0.png)

Para mais detalhes, acesse a FAQ: **[Nota sobre o Parâmetro Descrição nos Relatórios do módulo Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=285649743)**
