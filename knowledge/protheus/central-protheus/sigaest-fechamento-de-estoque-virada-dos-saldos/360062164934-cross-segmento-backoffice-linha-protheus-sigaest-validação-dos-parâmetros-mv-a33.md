---
article_id: 360062164934
category: SIGAEST - FECHAMENTO DE ESTOQUE (VIRADA DOS SALDOS)
content_hash: 47e2e6efc5131144a56c5cacfe421aaf7362619da3f1e5ba1add1dc5ad8a2da5
fetched_at: '2026-06-28T22:38:52.674362+00:00'
product: protheus
section_id: 1500001538921
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Validação dos parâmetros
  MV_A330GRV e MV_A280GRV para produtos obsoletos
type: support-article
updated_at: '2026-04-06T13:00:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062164934-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Valida%C3%A7%C3%A3o-dos-par%C3%A2metros-MV-A330GRV-e-MV-A280GRV-para-produtos-obsoletos
---

Os parâmetros MV\_A280GRV e MV\_A330GRV, no TOTVS Protheus, controlam o processamento de custo médio e virada de saldos, especialmente para produtos obsoletos. Ambos determinam se todos os produtos/armazéns ou apenas os que tiveram saldo/movimentação serão considerados, sendo essencial manter ambos com o mesmo valor e reinstalar as procedures após alterações.

É importante que os 2 parâmetros estejam com o mesmo conteúdo para que não gere conflito nos dados de Custo Médio histórico (B9\_CM1) dos produto

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28999732022423) Tempo aproximado para leitura: **00:03:30 min**

**Dúvida**

Qual o funcionamento dos parâmetros **MV\_A280GRV** e **MV\_A330GRV** durante o processamento de Custo Médio e da Virada de Saldos, para produtos obsoletos?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O **parâmetro MV\_A330GRV** indica se todos os produtos/armazéns terão seu saldo Inicial calculado no início do processamento do custo médio, **só tem efeito com o pacote de procedures 19 instalada no ambiente**, e qualquer alteração que seja realizada no conteudo do parametro é Obrigatório a reinstalação da procedure.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28999748272791)

* **.T.** (True/Verdadeiro) = **Todos os registros** são populados nas tabelas **SB9, SBJ e SBK**
* **.F.** (False/Falso) = **Somente os registros** que tem S**aldo Inicial ou Movimentação no período**.

**Doc referencia tdn:** <https://tdn.totvs.com/x/h_3SGQ>

------------------------------------------------------------------------------------------

O **parâmetro MV\_A280GRV** Indica se todos os produtos/armazéns serão virados para o próximo período, **só tem efeito com o pacote de procedures 17 instalada no ambiente**, e qualquer alteração que seja realizada no conteudo do parametro é Obrigatório a reinstalação da procedure.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28999748273815)

* **.T.** (True/Verdadeiro) = Todos os registros. **Com este conteúdo** todos os produtos e armazéns têm seus saldos levados para as tabelas de saldos iniciais **(SB9, SBJ e SBK)**.
* **.F.** (False/Falso) = somente os registros que possuem saldo inicial ou movimentação. Com este conteúdo somente os produtos e armazéns **que possuem movimentação dentro do período de processamento e produtos e armazéns que não possuam quantidades e custos zerados**,tem seus registros de saldos iniciais gravados. **Os produtos que não se enquadrarem nesta regra (obsoletos) não são mais levadospela rotina.**
* Os registros de saldos iniciais por local de estoque (SB9) só serão gerados caso haja saldo e/ou movimentação do produto no local de estoque dentro do período.
* Os registros de saldos iniciais por lote/sublote (SBJ) só serão gerados caso haja saldo e/ou movimentação do produto no lote/sublote dentro do período.
* Os registros de saldos iniciais por local de estoque (SBK) só serão gerados caso haja saldo e/ou movimentação do produto no endereço/número de série dentro do período.

**Doc referencia tdn:** <https://tdn.totvs.com/x/pgmVBg>

**O produto esta tendo os campos B2\_CM1 e B2\_CMFIM1 zerados no periodo onde não possui movimentos.**

Isso pode ser causado por utilizar a procedure 19 e o parametro MV\_A330GRV estar com conteudo F, para que o seu produto tenha o custo histórico recalculado, e exista esse custo histórico na tabela SB9 no ultimo fechamento, com o campo B9\_CM1 gravado, obrigatoriamente o parametro deve ser alterado para T e desintalado a procedure 19 bem como reinstalar a procedure posteriormente.

***Após alterado os parametros, obrigatoriamente deve-se reinstalar as procedures de 14 a 22.***

**Como reinstalar a procedure com o novo gestor corretamente:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Procedure Desatualizada ou Incompatível](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-ou-Incompat%C3%ADvel)

**Importante que os 2 parâmetros estejam com o mesmo conteúdo.**

Como indicado [***nesse link dessa FAQ***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10392641693591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Custo-m%C3%A9dio-hist%C3%B3rico-B9-CM1-zerado) é necessário que os 2 parâmetros estejam com o mesmo conteúdo para que não gere conflito nos dados de **Custo Médio histórico (B9\_CM1)** dos produto e mantenha o legado adequadamente.

**Saiba mais;**

[Backoffice (Linha Protheus) - SIGAEST - MATA330 - Custo médio histórico B9\_CM1 zerado?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10392641693591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Custo-m%C3%A9dio-hist%C3%B3rico-B9-CM1-zerado)

[Clique aqui e veja mais artigos sobre Fechamento de Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012208793-SIGAEST-FECHAMENTO-DE-ESTOQUE-VIRADA-DOS-SALDOS-)
