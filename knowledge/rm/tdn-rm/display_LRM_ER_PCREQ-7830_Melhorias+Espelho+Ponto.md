---
content_hash: 6097b9e8527ff9478d325dd02ea008bf99f3d3d5d571b5f8bc178f9428ce4e6c
fetched_at: '2026-06-29T00:06:11.872181+00:00'
page_id: '204964623'
product: rm
source: tdn-rm
title: ER_PCREQ-7830_Melhorias Espelho Ponto
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-7830_Melhorias+Espelho+Ponto
version: 4
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Automação de Ponto | **Módulo** | Abonos do Funcionário |
| **Segmento Executor** | Contrução e Projetos | | |
| **Projeto1** | PDR\_RH\_PTO008-23 | **IRM1** | PCREQ-7830 |
| **Requisito1** | PCREQ-7831 | **Subtarefa1** | PDR\_RH\_PTO008-20 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** |  |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

## Objetivo

*Permitir ao usuário a possibilidade de visualizar abonos e ocorrências coletadas por período a partir do espelho de ponto.*

## Definição da Regra de Negócio

**Serão listadas a seguir as evoluções que serão necessárias para atender o requisito. Serão realizadas dentro da nova MDI:**

**1.** **Espelho de Ponto** 

O espelho de ponto do funcionário que pode ser acessado através do caminho [**Automação de Ponto -> Cadastros -> Funcionário -> Anexos -> Movimento do Ponto -> Espelho**], irá receber melhorias como a possibilidade de exibir abonos e ocorrências coletadas que estarão contextualizadas no período definido pelo usuário através dos campos data início e data fim do espelho de ponto. Será adicionado um novo botão na barra de ferramentas do espelho de ponto que exibirá anexos por período (***Protótipo Nº 1 – Anexos por período***). Este novo botão funcionará como um menu e exibirá dois itens, um que dará acesso aos abonos do funcionário por período e outro que dará acesso as ocorrências coletadas por período. 

**1.1.** **Abonos por período** 

Ao acessar a opção [**Anexos por período -> Abono funcionário**], será exibido uma visão no formato de anexo, esta visão irá exibir todos os abonos do funcionário que estejam compreendidos no período definido através dos campos data início e data fim do espelho de ponto (***Protótipo Nº 2 – Abonos por período***). Caso as datas de início e fim do espelho de ponto sejam alteradas, será necessário clicar no botão “**Atualizar**” localizado na barra de ferramentas do espelho de ponto para que o anexo seja atualizado com os registros que compreendem o novo período selecionado.  

**1.2.** **Ocorrências coletadas por período** 

Ao acessar a opção [**Anexos por período -> Ocorrências coletadas**], será exibido uma visão no formato de anexo, esta visão irá exibir todas ocorrências coletadas do funcionário que estejam compreendidos no período definido através dos campos data início e data fim do espelho de ponto (***Protótipo Nº 3 – Ocorrências Coletadas por período***). Caso as datas de início e fim do espelho de ponto sejam alteradas, será necessário clicar no botão “**Atualizar**” localizado na barra de ferramentas do espelho de ponto para que o anexo seja atualizado com os registros que compreendem o novo período selecionado.A visão de ocorrências coletadas permitirá a execução do processo “**Alterar Atitude**” que pode deverá ser acessado através do caminho [**Automação de Ponto -> Cadastros -> Funcionário -> Anexos -> Movimento do Ponto -> Espelho -> Anexos por período -> Ocorrências coletadas -> Processos -> Alterar atitude**] (**Protótipo Nº 4 – Alterar atitude de ocorrências coletadas**).

## Protótipo de Tela

## 

**Protótipo Nº 1 – Anexos por período**

**Protótipo Nº 2 – Abonos por período**

**Protótipo Nº 3 – Ocorrências Coletadas por período**

**Protótipo Nº 4 – Alterar atitude de ocorrências coletadas**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
