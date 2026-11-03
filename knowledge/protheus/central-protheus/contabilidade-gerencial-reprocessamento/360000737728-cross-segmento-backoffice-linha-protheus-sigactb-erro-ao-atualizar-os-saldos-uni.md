---
article_id: 360000737728
category: Contabilidade Gerencial - Reprocessamento
content_hash: 9f3500b7c8ef6d0d912b75b28e17c6cbbb447b6bc57658661b8744b584d2a0a7
fetched_at: '2026-06-28T22:40:41.947548+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Erro ao atualizar os
  saldos (Unique constraint)
type: support-article
updated_at: '2025-06-17T18:03:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000737728-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Erro-ao-atualizar-os-saldos-Unique-constraint
---

As entidades contábeis Centro de Custo, Item Contábil e Classe de Valores devem ter o mesmo tamanho em função da tabela de saldos compostos CQ8 e CQ9. As tabelas CQ8 e CQ9 armazenam o saldo por entidade gerencial de forma isolada, é utilizada por relatórios como o Balancete por Centro de Custo, Balancete por Item, Balancete por Classe de Valor além de outras rotinas e funções.

* Veja se a alteração do tamanho de grupo de campos está [REFLETINDO PARA TODAS AS TABELAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050034853-MP-SIGACTB-AO-REALIZAR-ALTERA%C3%87%C3%83O-NO-TAMANHO-DE-GRUPO-DE-CAMPOS-CONFIGURAR-N%C3%83O-ESTA-REFLETINDO-PARA-TODAS-AS-TABELAS?source=search)do sistema
* Altere para  20 as entidades ("Centro de Custo", "Item Contábil" e "Classe Valor") "Salvar "
* Veja se a alteração do tamanho de grupo de campos está [REFLETINDO PARA TODAS AS TABELAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050034853-MP-SIGACTB-AO-REALIZAR-ALTERA%C3%87%C3%83O-NO-TAMANHO-DE-GRUPO-DE-CAMPOS-CONFIGURAR-N%C3%83O-ESTA-REFLETINDO-PARA-TODAS-AS-TABELAS?source=search)do sistema, posteriormente volte para o tamanho que utiliza normalmente em seu sistema
* Veja se a alteração do tamanho de grupo de campos está [REFLETINDO PARA TODAS AS TABELAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050034853-MP-SIGACTB-AO-REALIZAR-ALTERA%C3%87%C3%83O-NO-TAMANHO-DE-GRUPO-DE-CAMPOS-CONFIGURAR-N%C3%83O-ESTA-REFLETINDO-PARA-TODAS-AS-TABELAS?source=search)do sistema e altere para  50 a conta contábil "Salvar "
* Veja se a alteração do tamanho de grupo de campos está [REFLETINDO PARA TODAS AS TABELAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050034853-MP-SIGACTB-AO-REALIZAR-ALTERA%C3%87%C3%83O-NO-TAMANHO-DE-GRUPO-DE-CAMPOS-CONFIGURAR-N%C3%83O-ESTA-REFLETINDO-PARA-TODAS-AS-TABELAS?source=search)do sistema, posteriormente volte para o tamanho que utiliza normalmente em seu sistema
* Veja se a alteração do tamanho de grupo de campos está [REFLETINDO PARA TODAS AS TABELAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050034853-MP-SIGACTB-AO-REALIZAR-ALTERA%C3%87%C3%83O-NO-TAMANHO-DE-GRUPO-DE-CAMPOS-CONFIGURAR-N%C3%83O-ESTA-REFLETINDO-PARA-TODAS-AS-TABELAS?source=search)do sistema
* Veja se o [GRUPO DE PERGUNTAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028526532-MP-SIGACTB-CTBA211-GRUPO-DE-PERGUNTAS-?source=search) e [Tamanho de Campos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050034853-MP-SIGACTB-AO-REALIZAR-ALTERA%C3%87%C3%83O-NO-TAMANHO-DE-GRUPO-DE-CAMPOS-CONFIGURAR-N%C3%83O-ESTA-REFLETINDO-PARA-TODAS-AS-TABELAS?source=search) estão corretos

2. Verifique o compartilhamento de todas as tabelas do ambiente contábil, conforme a documentação disponibilizada em: <http://tdn.totvs.com/display/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB>

3. Realize a atualização de saldos em seu ambiente.

[**Pacotes de Atualização - Contabilidade**](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777)

**Veja também**

Além deste processo, disponibilizamos uma documentação sobre a nova estrutura de tabelas do ambiente contábil e o novo conceito de gravação dos mesmos: <http://tdn.totvs.com/pages/viewpage.action?pageId=274843987>

Ao alterar o tamanho da entidade o sistema reflete em todos os [GRUPO DE PERGUNTAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028526532-MP-SIGACTB-CTBA211-GRUPO-DE-PERGUNTAS-?source=search)e [Tamanho de Campos.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050034853-MP-SIGACTB-AO-REALIZAR-ALTERA%C3%87%C3%83O-NO-TAMANHO-DE-GRUPO-DE-CAMPOS-CONFIGURAR-N%C3%83O-ESTA-REFLETINDO-PARA-TODAS-AS-TABELAS?source=search) Exemplo [CTBA211 GRUPO DE PERGUNTAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028526532-MP-SIGACTB-CTBA211-GRUPO-DE-PERGUNTAS-?source=search)

**Erro na chamada do processo:** [MP - SIGACTB - Reprocessamento de Saldos: Erro na Chamado do Processo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115016125428-MP-SIGACTB-Reprocessamento-de-Saldos-Erro-na-Chamado-do-Processo)

[Procedimento para alteração do tamanho das entidades contábeis -- 23592](http://tdn.totvs.com/pages/releaseview.action?pageId=233760901)

[Ampliação da quantidade de casas decimais em outras moedas -- 23593](http://tdn.totvs.com/pages/releaseview.action?pageId=6068431)

[Ampliação do Código de Entidades no SigaCTB -- 11346](http://tdn.totvs.com/pages/releaseview.action?pageId=6068420)
