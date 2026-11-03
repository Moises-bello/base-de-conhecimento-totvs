---
content_hash: 6dd0f546e82eb0666e43121931ce3995281f58969984dcc259064d5b8c0a9e80
fetched_at: '2026-06-29T00:06:21.836567+00:00'
page_id: '223182505'
product: rm
source: tdn-rm
title: ER_PCREQ-8782_Integração de Funcionários que não batem ponto e de Rescisão
  com o TSA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223182505
version: 127
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Automação de Ponto | **Módulo** | Integração com o TSA |
| **Segmento Executor** |  | | |
| **Projeto1** | Contrução e Projetos | **IRM1** | PCREQ-8780 |
| **Requisito1** | PCREQ-8782 | **Subtarefa1** | PDR\_CP\_PTO003-25 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** | 11.82.42 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

 

 

* Permitir a integração de funcionários que não utilizam cartão de ponto com o TSA.
* Permitir a integração de rescisão dos funcionários com o TSA.

## Definição da Regra de Negócio

#### Integração de funcionários que não utilizam ponto

Será feita uma evolução na integração de funcionários do RM. Atualmente são integrados somente funcionários que utilizam ponto, porém pode ocorrer de funcionários que não utilizam ponto terem seu acesso bloqueado.

Por isso qualquer alteração de campo integrado do cadastro de funcionários irá enviar as informações atualizadas para o TSA.

Portanto um novo campo será informado, para que o TSA saiba se o funcionário bate ou não bate ponto.

Ao enviar as informações do funcionário, o Chronus irá fazer o mapeamento através do campo **exceptionREP**. Se o funcionário não bater ponto, será definido como verdadeiro, caso contrário, será definido como falso.

#### Integração de rescisão dos funcionários

Toda vez que uma rescisão for cadastrada, alterada cancelada  para um funcionário, as informações do funcionário deverão ser enviadas para o TSA.

Se um funcionário estiver demitido no RM, também deverá estar demitido no TSA, assim como se ele tiver ativo no RM, deverá estar ativo no TSA.

Para realizar essa integração, três novos processos passaram a ser considerados:

* Cadastro da rescisão: Para o cadastro de rescisão, será feita uma evolução na fórmula visual **Funcionário - TSA**, adicionando o gatilho para o DataServer "**FopRescisaoData"**:
* Rescisão coletiva: Para a rescisão coletiva, será colocado um gatilho interno no código, que chamará a fórmula visual **Funcionário - TSA** após a conclusão do processo, enviando as informações de todos os funcionários impactados.
* Cancelamento da rescisão: Para o cancelamento da rescisão, será colocado um gatilho interno no código, que chamará a fórmula visual **Funcionário - TSA** após a conclusão do processo, enviando as informações de todos os funcionários impactados.

Como a fórmula visual **Funcionário - TSA** será atualizada, o pacote que contém as fórmulas visuais **"Formulas\_Visuais\_TSA.TotvsWF"** também será atualizado, sendo necessária uma nova importação por parte dos clientes para atualização do ambiente.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
