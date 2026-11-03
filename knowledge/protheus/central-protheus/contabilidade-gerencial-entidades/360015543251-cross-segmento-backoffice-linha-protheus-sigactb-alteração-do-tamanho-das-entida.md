---
article_id: 360015543251
category: Contabilidade Gerencial - Entidades
content_hash: efc272d87a8a568b77a29d75850511c2e86e9d21eee77a48fd3ba389b46ff574
fetched_at: '2026-06-28T22:40:49.689538+00:00'
product: protheus
section_id: 1500001537661
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ALTERAÇÃO DO TAMANHO
  DAS ENTIDADES CONTÁBEIS
type: support-article
updated_at: '2022-04-12T17:06:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015543251-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ALTERA%C3%87%C3%83O-DO-TAMANHO-DAS-ENTIDADES-CONT%C3%81BEIS
---

**Dúvida**

Possibilidade em  alterar tamanho do campo de centro de custo.  
  
**Ambiente**

PROTHEUS – Contabilidade gerencial  – A partir da versão 11.80  
  
**Solução**

Documentação referente a alteração das entidades contabeis

Os campos relativos à códigos das entidades contábeis Conta Contábil, Centro de Custo, Item Contábil e Classe de Valores disponíveis no módulo SIGACTB podem ter seu tamanho alterado de acordo com a necessidade.   
  
Cabe avaliar os casos em que pode-se desdobrar um código em outro nível de entidade contábil, evitando a criação de códigos repetitivos, um exemplo comum é o desdobramento do centros de custo “contábil” para “extra-contábil” evitando a necessidade de criação do código de centro de custo sob todas as contas onde pode-se efetuar um lançamento com o mesmo, com o centro de custo extra-contábil cria-se apenas o novo código de centro de custo no cadastro apropriado e define-se através de amarrações as contas que poderão ou não receber este centro de custo nos lançamentos.  
  
Mesmo assim se ainda for necessário, pode-se variar o tamanho dos códigos das entidades contábeis nas seguintes proporções (vide tabela SXG):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072207473/mceclip0.png)

Veja se o sistema  replicou a alteração para todos os [GRUPO DE PERGUNTAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028526532-MP-SIGACTB-CTBA211-GRUPO-DE-PERGUNTAS-?source=search)e [Tamanho de Campos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050034853-MP-SIGACTB-AO-REALIZAR-ALTERA%C3%87%C3%83O-NO-TAMANHO-DE-GRUPO-DE-CAMPOS-CONFIGURAR-N%C3%83O-ESTA-REFLETINDO-PARA-TODAS-AS-TABELAS?source=search) .![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072207793/mceclip1.png)

Caso esteja sendo apresentado erro de chave duplicada em tela ou no Trace

Provável que em algum campo do sistema o tamanho esteja errada em comparação com o grupo de campo e ou grupo de perguntas .  
Diante disso é indicado através da base teste realizar os procedimentos abaixo grupo de campo  

* altere para  20 as entidade ("Centro de Custo", "Item Contábil" e "Classe Valor") "Salvar "
* Veja se a alteração do tamanho de grupo de campos esta  [REFLETINDO PARA TODAS AS TABELAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050034853-MP-SIGACTB-AO-REALIZAR-ALTERA%C3%87%C3%83O-NO-TAMANHO-DE-GRUPO-DE-CAMPOS-CONFIGURAR-N%C3%83O-ESTA-REFLETINDO-PARA-TODAS-AS-TABELAS?source=search)do sistema
* altere para  50 a conta contabil  "Salvar "
* Veja se a alteração do tamanho de grupo de campos esta  [REFLETINDO PARA TODAS AS TABELAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050034853-MP-SIGACTB-AO-REALIZAR-ALTERA%C3%87%C3%83O-NO-TAMANHO-DE-GRUPO-DE-CAMPOS-CONFIGURAR-N%C3%83O-ESTA-REFLETINDO-PARA-TODAS-AS-TABELAS?source=search)do sistema
* Veja se o [GRUPO DE PERGUNTAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028526532-MP-SIGACTB-CTBA211-GRUPO-DE-PERGUNTAS-?source=search)  e [Tamanho de Campos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050034853-MP-SIGACTB-AO-REALIZAR-ALTERA%C3%87%C3%83O-NO-TAMANHO-DE-GRUPO-DE-CAMPOS-CONFIGURAR-N%C3%83O-ESTA-REFLETINDO-PARA-TODAS-AS-TABELAS?source=search) estão corretos
* [Erro ao atualizar os saldos (Unique constraint) e Chave duplicada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000737728-MP-SIGACTB-Erro-ao-atualizar-os-saldos-Unique-constraint-?source=search)
* Veja se a alteração do tamanho de grupo de campos esta  [REFLETINDO PARA TODAS AS TABELAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050034853-MP-SIGACTB-AO-REALIZAR-ALTERA%C3%87%C3%83O-NO-TAMANHO-DE-GRUPO-DE-CAMPOS-CONFIGURAR-N%C3%83O-ESTA-REFLETINDO-PARA-TODAS-AS-TABELAS?source=search)do sistema

Link sobre as alterações e  procedimentos das entidades contábeis

<http://tdn.totvs.com/pages/releaseview.action?pageId=6068430>

Link   referente ocorrência relacionado ao tamanho dos campos das entidades contábeis e CTU

<http://tdn.totvs.com/pages/releaseview.action?pageId=126190310>

Ao alterar o tamanho da entidade o sistema reflete em todos o grupo de campos e grupo de pergunta exemplo [CTBA211 GRUPO DE PERGUNTAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028526532-MP-SIGACTB-CTBA211-GRUPO-DE-PERGUNTAS-?source=search)

Saiba mais:

[MP - SIGACTB - Alterar o tamanho do campo código das entidades contábeis adicionais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024401031-MP-SIGACTB-Alterar-o-tamanho-do-campo-c%C3%B3digo-das-entidades-cont%C3%A1beis-adicionais?source=search)
