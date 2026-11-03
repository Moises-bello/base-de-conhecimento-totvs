---
article_id: 10085045337879
category: MDT - PPRA
content_hash: 568d252c121dbf668761e8b8dcb311fcf716a7ee7f2667dd1dd6e107580170aa
fetched_at: '2026-06-28T22:44:27.515994+00:00'
product: protheus
section_id: 360010945454
source: central-protheus
title: RH - Linha Protheus - MDT - Quais são as referências das perguntas para geração
  do relatório Geral PGR
type: support-article
updated_at: '2025-07-31T14:30:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10085045337879-RH-Linha-Protheus-MDT-Quais-s%C3%A3o-as-refer%C3%AAncias-das-perguntas-para-gera%C3%A7%C3%A3o-do-relat%C3%B3rio-Geral-PGR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25279278370199) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Quais são as referências das perguntas para geração do relatório Geral PGR, rotina MDTR851?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**De acordo com a parametrização preenchida serão verificadas todas as informações pertencentes ao range configurado, bem como verificados os riscos de exposição dos funcionários.  
  
No módulo MDT, no menu **Relatórios - PPRA - Rel. Geral PGR** (*MDTR851*) será apresentado as perguntas abaixo para parametrização:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30596799766423)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30596816503063)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30596799776919)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30596816511767)  
  
Referências:

|  |  |  |
| --- | --- | --- |
| **CAMPO** | **DESCRIÇÃO** | **ATALHOS QUE UTILIZAM** |
| Laudo? | Define o código do laudo **PGR**.  Exemplo: PGR2022 | * Não se aplica. |
| Coordenador? | Define um Usuário (**TMK**) como coordenador do laudo.  Exemplo: 000000000001 | * Não se aplica. |
| De Filial? | Define a filial inicial a ser considerada na impressão do relatório. Caso necessário, para considerar todos, deve-se deixar o campo vazio. Quando utilizado um intervalo com mais de uma filial, o código do laudo deve estar vazio.  Exemplo: D MG 01 | * Não se aplica. |
| Até Filial? | Define a filial final a ser considerada na impressão do relatório. Caso necessário, para considerar todos, deve-se deixar o campo preenchido com . Quando utilizado um intervalo com mais de uma filial, o código do laudo deve estar vazio.  Exemplo: D MG 01 | * Não se aplica. |
| De Centro de Custo? | Define o centro de custo inicial a ser considerado na impressão do relatório. Caso necessário, para considerar todos, deve-se deixar o campo vazio.  Exemplo: 000000001 | * Acidentes c/vítimas * Acidentes s/vítimas * Cronograma * EPI * Funcionários x Função * Funções * Funções e Tarefas * Quadro Funcionários * Quadro Funcionários por Centro de Custo * Risco * Risco-Calor * Risco-Físico * Risco-Frio * Risco-Químico * Risco-Ruído * Risco-Umidade |
| Até Centro de Custo? | Define o centro de custo final a ser considerado na impressão do relatório. Caso necessário, para considerar todos, deve-se deixar o campo preenchido com ZZZZZZZZZ.  Exemplo: 000000002 | * Acidentes c/vítimas * Acidentes s/vítimas * Cronograma * EPI * Funcionários x Função * Funções * Funções e Tarefas * Quadro Funcionários * Quadro Funcionários por Centro de Custo * Risco * Risco-Calor * Risco-Físico * Risco-Frio * Risco-Químico * Risco-Ruído * Risco-Umidade |
| Impressão? | Define se o relatório será apresentado em tela **(opção Arquivo)** ou se será enviado diretamente a impressora **(opção Impressora)**.  Exemplo: Arquivo  Permite informar o nome do arquivo de saída.  Exemplo: PGR2022 | * Não se aplica. |
| Arquivo Saída? | Permite informar o nome do arquivo de saída.  Exemplo: PGR2022 | * Não se aplica. |
| Ordenar Riscos por? | Permite selecionar a ordenação dos registros de riscos**:**   * Agente * Ambiente físico * Centro de custo * Fonte geradora * Função | * Agente x Medida * Função x Tarefa * Plano * Quadro Agente * Risco |
| Imprimir Data de Avaliação? | Permite selecionar se será impresso a data de avaliação nas informações do risco:   * Sim * Não | * Risco |
| Imprimir imagens? | Permite selecionar se imagens serão impressas:   * Sim * Não | * Local |
| Imprimir junto ao risco? | Permite selecionar as informações adicionais do risco a serem impressas:   * Atividades * Expostos * Não expostos * Planos | * Risco |
| Imprimir matriz de risco? | Permite selecionar se a matriz de risco será impressa:   * No final * Em cada risco * Não imprimir | * Risco |
| Considerar por? | Permite selecionar se levará em consideração o centro de custo ou o departamento do funcionário:   * Centro de Custo * Departamento | * Quadro Funcionários * Quadro Funcionários por Centro de Custo |
| Ordenar Equipamentos por? | Permite selecionar a ordenação dos registros de equipamentos**:**   * Código * Nome | * Bem * Equipamento * MDT-EPC |
| Ordenar Plano de Ação por? | Permite selecionar a ordenação dos registros de planos de ação**:**   * Código do Plano * Centro de Custo * Funcionário responsável | * Parâmetro descontinuado. |
| Imprime Quantidade de Funcionários e Funções? | Permite selecionar se no total de funcionários serão considerados todos os funcionários ou apenas os expostos a risco:   * Todos * Exposto Risco | * Funções * Funções e Tarefas |
| Jornada de trabalho? | Define a jornada normal da empresa.  Exemplo: 08:00 | * Acidentes c/vítimas * Acidentes s/vítimas |
| Dias úteis do ano? | Define quantos dias úteis possui o ano em questão.  Exemplo: 310 | * Acidentes c/vítimas * Acidentes s/vítimas |

**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Consulte os atalhos disponíveis no relatório PGR](https://tdn.totvs.com/pages/viewpage.action?pageId=667375614)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
