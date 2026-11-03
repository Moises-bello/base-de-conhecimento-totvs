---
article_id: 4416157901463
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 3a54cb1e9e904ba8c99736e91e2fa91a1e4a6014e83050006ea58b9b03586283
fetched_at: '2026-06-28T22:37:21.568348+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como manter ou não
  a competência das parcelas do Cronograma Financeiro conforme a Data Prevista de
  Medição ?  MV_CNFDTCP
type: support-article
updated_at: '2026-02-12T14:00:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416157901463-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-manter-ou-n%C3%A3o-a-compet%C3%AAncia-das-parcelas-do-Cronograma-Financeiro-conforme-a-Data-Prevista-de-Medi%C3%A7%C3%A3o-MV-CNFDTCP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34184561315991) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como manter ou não a competência das parcelas do Cronograma Financeiro conforme a Data Prevista de Medição ? MV\_CNFDTCP

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

Para se manter ou não a competência da parcelas na criação de uma Cronograma Financeiro no cadastro de um contrato de acordo com as datas Previstas de Mediçao dessas parcelas do Cronograma pode-se verificar a configuração do parâmetro ***MV\_CNFDTCP.***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416149163927)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416141369495)

No exemplo de criação de um cronograma conforme os parâmetro abaixo em que a "Competência de Inicio" está em um mês e a "Data Prevista da 1ª Medição" está em outro mês:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416149297175)

Caso o parâmetro ***MV\_CNFDTCP*** esteja habilitado (.T.), as competências das parcelas serão criadas de acordo com as datas prevista de medições dessas parcelas:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416141878551)

Se o parâmetro estiver desabilitado (.F.), as competências das parcelas seguirão iniciando de acordo com a "competência de inicio" inserida nos parâmetros de criação do cronograma:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416157613847)

***Saiba Mais:***

[GCT0077\_Alteracao\_Competencia\_Cronograma(MV\_CNFDTCP)](https://tdn.totvs.com/x/sOA8E)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
