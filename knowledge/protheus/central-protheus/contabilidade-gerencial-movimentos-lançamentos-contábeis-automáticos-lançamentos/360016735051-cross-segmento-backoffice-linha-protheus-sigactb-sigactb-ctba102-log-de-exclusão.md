---
article_id: 360016735051
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 808eaa49617702911df0c25d6377d013ee5c86ff1ed9fd3d21afc472186ce2c7
fetched_at: '2026-06-28T22:40:32.365603+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - SIGACTB - CTBA102 -
  Log de Exclusão '
type: support-article
updated_at: '2022-06-03T22:55:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016735051-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-SIGACTB-CTBA102-Log-de-Exclus%C3%A3o
---

**Dúvida**

O sistema mostra o **log de exclusão** que já estavam no  **LOGCTB01.FLG** (versão 11), porém as **novas exclusões** (**versão 12**) não esta alimentando este arquivo.

**Ambiente**

Protheus – Contabilidade Gerencial – 12.1.17  
  
**Solução**

No **Protheus 12**, ao excluir um lançamento contábil feito em contabilização de outros módulos com os parâmetros **MV\_CTBAPLA e MV\_CTBFLAG** configurados para a **marcação e exclusão dos FLAG's de contabilização**, é apresentado uma pergunta referente a visualização do log da exclusão realizada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012759631/mceclip0.png)

 Após aceitar a verificação dos logs será apresentado em tela os lançamentos excluídos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012758132/mceclip1.png)

Assim poderá obter mais **detalhes** sobre cada **linha do lançamento, imprimir o log.**

**A partir da versão 12** o Protheus não grava os logs de exclusão no arquivo **LOGCTBXX.FLG** e sim na tabela **QL5** (**Para ambientes com *releases* anteriores a 12.1.23 a atualização do dicionário deve ser realizada pelo usuário via configurador**), [**Clique aqui**](http://tdn.totvs.com/pages/viewpage.action?pageId=372556085) para verificar o **boletim técnico** referente a essa tabela.

Issue  : [DSERCTR1-6297](https://suporte.totvs.com/portal/p/10098/download?e=696448) :Descreve : Descrição Ajuste realizado no Log de exclusão da flag de contabilização no lançamento contábil ( CTBA102 ) Para ambientes com releases anteriores a 12.1.21 a atualização do dicionário deve ser realizada pelo usuário via configurador.

Veja mais :

[MP - SIGACTB - campo CT2\_FILORI não esta sendo preenchido.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018753151-MP-SIGACTB-campo-CT2-FILORI-n%C3%A3o-esta-sendo-preenchido-?source=search)
