---
article_id: 1500000567281
category: SIGAEST - RELATORIOS
content_hash: 96dec1a301a2f78d78e7156b101e0ed5220d739f5da3b3fd578002fa5aa26b33
fetched_at: '2026-06-28T22:39:06.078426+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR260 - Linhas em
  branco no relatório quando aglutinado por Armazém
type: support-article
updated_at: '2023-03-01T11:15:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000567281-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR260-Linhas-em-branco-no-relat%C3%B3rio-quando-aglutinado-por-Armaz%C3%A9m
---

**Dúvida**Por que o relatório Posição de Estoque (MATR260) ***exibe linhas em branco*** quando aglutinado por Armazém?

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12760354618391)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução:**

 - O relatório padrão foi criado de forma para não repetir as informações do produto nas linhas das seguintes enquanto for o mesmo produto, evitando ter o resultado menos poluído possível.

 - Para suprimir esta opção e fazer a impressão é necessário alterar o relatório padrão, neste caso, somente é possível por customização, não tratando-se de erro do relatório.

 - Também justificando esse comportamento na impressão do relatório devido melhorar a performance na emissão do mesmo em ambientes com alta massa de dados.

 - A partir do fonte do relatório MATR260 de 17/02/2023 ao emitir o Relatório em ***Planilha*** e ***Formato de Tabela*** são exibidas as colunas para facilitar a filtragem caso necessário. Pacotes pontuais abaixo.

***12.1.2210:<https://suporte.totvs.com/portal/p/10098/download?e=1097225> ;***

***12.1.33:<https://suporte.totvs.com/portal/p/10098/download?e=1097228> ;***

***12.1.27:<https://suporte.totvs.com/portal/p/10098/download?e=1097227> ;***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12759721662103)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12759785757079)

**Observações:**

 - Caso não atenda no padrão, a TOTVS [disponibiliza o fonte do relatório no Portal do Cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058126794-SIGAEST-Fontes-de-relat%C3%B3rios-Estoque-para-altera%C3%A7%C3%A3o-ou-customiza%C3%A7%C3%A3o-fora-do-padr%C3%A3o?source=search) e efetuar os ajustes de customização conforme necessidade;

 - Veja nos exemplos abaixo que o resultado final do relatório não é alterado.

**- RELATÓRIO AGLUTINADO POR EMPRESA:**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12759986139415)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12760027122583)

**- RELATÓRIO AGLUTINADO POR FILIAL:**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12760129865623)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12760146709015)

**- RELATÓRIO AGLUTINADO POR ARMAZÉM:**

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12760207804567)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12760273730839)

**Saiba mais:**

*[SIGAEST - Fontes de relatórios Estoque para alteração ou customização fora do padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058126794)*

*[Clique aqui e veja mais artigos sobre Relatórios no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000567281)*
