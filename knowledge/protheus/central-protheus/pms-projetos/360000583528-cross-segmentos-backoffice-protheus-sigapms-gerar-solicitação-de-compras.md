---
article_id: 360000583528
category: PMS - Projetos
content_hash: da331fd4781b0469a50fd79de15b4851a5df56e0a0e308bafa4d8223009afc63
fetched_at: '2026-06-28T22:37:14.917956+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Gerar Solicitação de Compras
type: support-article
updated_at: '2024-04-22T13:47:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000583528-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Gerar-Solicita%C3%A7%C3%A3o-de-Compras
---

Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Como gerar uma solicitação de compras no módulo Gestão de projetos (SIGAPMS)?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - A partir da release 12  
  
**Solução**

Veja nosso vídeo How To sobre o assunto:

A execução do projeto consiste tem como objetivo providenciar os insumos para a execução do projeto, ou seja, a compra de material, verificar quem deverá ser alocado e planejar as necessidades para que não falte nada na hora de executar as tarefas.

O controle de execução tem esse objetivo, o planejamento das necessidades. Neste momento é que vamos decidir se o material necessário será comprado, produzido ou solicitado ao almoxarifado, ou ainda se deverá ser reservado material já disponível no estoque para executar as tarefas.

Sendo que existem duas formas de fazer isso, sendo elas: a automática e a manual.

**Para gerar a solicitação de compras através do módulo de PMS, realize os seguintes passos:**

1°  Cadastre o Projeto e inclua a Tarefa, através da rotina PMSA410 ou PMSA200.

2°  Na Tarefa inclua o produto através do campo **"Codigo do Produto (AFA\_PRODUT)"** e a data de necessidade através do campo **"Dt. Necess. (AFA\_DATPRF)"**.

* A inclusão do campo **"Dt. Necess. (AFA\_DATPRF)"** é muito importante, a data informada deve estar entre a data inicial e final do projeto **"Data Inicial Prevista (AF9\_START)"** e **"Dt. Fin. Prv (AF9\_FINISH)"**, se não estiver, a solicitação de compras não é gerada.

**OBSERVAÇÃO 1:** ara gerar a solicitação de compras através do módulo Gestão de Projetos, o produto não deve ter saldo em estoque, caso contrário, não irá gerar.

3° Após a inclusão do projeto, entre na rotina Gerenciamento de Execução (**PMSA220**), localize o projeto e clique em Planejamento

4° Inclua o Planejamento através da opção Gerar, conforme abaixo:

![](http://tdn.totvs.com/download/attachments/255755522/image2016-9-16%2018%3A19%3A57.png?version=1&modificationDate=1474061561000&api=v2)

5° Após a inclusão do planejamento, visualize, clique em ações relacionadas - Detalhes, conseguirá  visualizar a geração da Solicitação de Compras;

![20220131_110048.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4420943339543)

**OBSERVAÇÃO 2:** Não há uma limitação de valor do Orçamento para o lançamento de Solicitações de Compra. As solicitações de compras vinculadas ao Orçamento se baseiam na **quantidade cadastrada em x lugar, e não, por valor**.

**OBSERVAÇÃO 3:** Cheque os parâmetros envolvidos na documentação do saiba mais.

**Saiba mais:**

[Gerenciamento de Execução](https://tdn.totvs.com/x/P4oOFQ)
