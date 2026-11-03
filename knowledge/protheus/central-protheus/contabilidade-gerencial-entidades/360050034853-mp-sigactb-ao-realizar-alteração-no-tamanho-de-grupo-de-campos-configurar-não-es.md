---
article_id: 360050034853
category: Contabilidade Gerencial - Entidades
content_hash: 0cf9230b3841509a5617d9813328cf5bd880c4cbe8578d82d67d7f8fb265864f
fetched_at: '2026-06-28T22:40:49.717112+00:00'
product: protheus
section_id: 1500001537661
source: central-protheus
title: MP - SIGACTB - AO REALIZAR ALTERAÇÃO NO TAMANHO DE GRUPO DE CAMPOS CONFIGURAR
  NÃO ESTA REFLETINDO PARA TODAS AS TABELAS
type: support-article
updated_at: '2021-04-28T14:47:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050034853-MP-SIGACTB-AO-REALIZAR-ALTERA%C3%87%C3%83O-NO-TAMANHO-DE-GRUPO-DE-CAMPOS-CONFIGURAR-N%C3%83O-ESTA-REFLETINDO-PARA-TODAS-AS-TABELAS
---

**Dúvida**

 Ao realizar a alteração no tamanho de  [Alteração do tamanho das entidades contabeis](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015543251-MP-SIGACTB-ALTERA%C3%87%C3%83O-DO-TAMANHO-DAS-ENTIDADES-CONT%C3%81BEIS?source=search)  e [Tamanho do campo código das entidades contábeis](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024401031-MP-SIGACTB-Alterar-o-tamanho-do-campo-c%C3%B3digo-das-entidades-cont%C3%A1beis-adicionais?source=search) no configurador o sistema não esta refletindo para todos os campos , com isso o sistema esta gerando erro [Erro ao atualizar os saldos (Unique constraint) e Chave duplicada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000737728-MP-SIGACTB-Erro-ao-atualizar-os-saldos-Unique-constraint-?source=search)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074847753/mceclip0.png)

**Ambiente**Microsiga Protheus – Contabilidade  – A partir da versão 11.80  
  
**Causa**

* Ao realizar alteração

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073679014/mceclip2.png)

* Neste exemplo selecionamos a conta contabil
* Obs: sugiro que realize essa analise em todas as entidades (Conta contabil, centro de custo, item contabil e classe de valor

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074848053/mceclip3.png)

* O sistema irá atualizar somente para o campos e tabelas  apresentada nesta tela

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074848133/mceclip4.png)![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074848313/mceclip5.png)

**Solução**

* Realize a mesma analise para o **[GRUPO DE PERGUNTAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028526532-MP-SIGACTB-CTBA211-GRUPO-DE-PERGUNTAS-?source=search)**
* Veja que neste exemplo o sistema não possui [todas as tabelas](https://tdn.totvs.com/display/public/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB) e campos , com isso o sistema não estava refletindo para o campos da CQ0 ...CQ9 ..CT2...

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074851913/mceclip0.png)

* Neste caso o campo **X3\_GRPSXG** não estava preenchido

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074856573/mceclip3.png)

* No padrão o campo **X3\_GRPSXG**  é preenchido 003

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073689474/mceclip1.png)

* Da mesma forma que esta preenchido na tabela SXG campo XG\_GRUPO

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073692834/mceclip5.png)

* Quando o campo **X3\_GRPSXG** está preenchido o sistema apresenta  o campo no grupo de campos

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074856733/mceclip4.png)

* Ao criar a SX3  o campo é alimentado automaticamente , caso campo esteja em branco , sugerimos analista Inloco de sua confiança para ajuste do campos , para todos as tabelas
* veja documentação sobre o campo **X3\_GRPSXG**

**[Regras para atualização do dicionário SX3 - UPDDISTR e migrador de versão](https://tdn.totvs.com/pages/viewpage.action?pageId=181965333).**

[MP - FRAME - Erros críticos em migrações de versão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025450971-MP-FRAME-Erros-cr%C3%ADticos-em-migra%C3%A7%C3%B5es-de-vers%C3%A3o?source=search)

[SX3 - Campos das tabelas](https://tdn.totvs.com/display/framework/SX3+-+Campos+das+tabelas)
