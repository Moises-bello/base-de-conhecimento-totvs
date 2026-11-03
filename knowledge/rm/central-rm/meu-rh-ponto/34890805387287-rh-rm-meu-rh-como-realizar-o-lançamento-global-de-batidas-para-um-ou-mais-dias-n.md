---
article_id: 34890805387287
category: Meu RH - Ponto
content_hash: 4946ac08ec36232bd7787244cce136cd62222dc10379721537b872bf1459e587
fetched_at: '2026-06-28T22:47:30.261638+00:00'
product: rm
section_id: 1500000861782
source: central-rm
title: RH - RM - Meu RH - Como realizar o lançamento global de batidas para um ou
  mais dias no espelho de ponto do funcionário.
type: support-article
updated_at: '2026-01-13T18:48:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34890805387287-RH-RM-Meu-RH-Como-realizar-o-lan%C3%A7amento-global-de-batidas-para-um-ou-mais-dias-no-espelho-de-ponto-do-funcion%C3%A1rio
---

Colaborador: Acesso via menu **Ponto → Espelho de Ponto → Incluir Batidas;**

Gestor: Acesso via menu **Minha Equipe** **→ Clique nas opções dos três pontinhos (...) → Ponto → Espelho de Ponto → Incluir Batidas.**

Observações: Esta opção está condicionada a liberação de permissão ([Como Personalizar Permissões de Funcionalidade no Meu RH](https://tdn.totvs.com/pages/viewpage.action?pageId=287067720));

## **TELA DE INCLUSÃO DE BATIDAS**

Para realizar a inclusão da batida é necessário incluir uma justificativa, podendo utilizar as justificativas da seguinte forma:

* Justificativa Individual: Deve preencher uma justificativa para cada dia que está inserindo a marcação. Não é permitido inserir uma justificativa para cada marcação;
* Justificativa Global: Marque a flag 'Justificativa única para todas as batidas', e digite a justificativa desejada, esta será considerada para todas as marcações inseridas;
* Justificativa Pré-Definida: Marque a flag 'Justificativa única para todas as batidas', parametrize no ERP as justificativas pré-definidas e selecione a justificativa desejada, esta será considerada para todas as marcações inseridas. [Justificativas pré-definidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25747268602135-RH-RM-PTO-Cadastro-e-utiliza%C3%A7%C3%A3o-de-Justificativas-Predefinidas).
* **Utilizando Justificativa Individual**

![](https://tdn.totvs.com/download/attachments/931601078/image-2025-4-9_12-7-59.png?version=1&modificationDate=1744212215203&api=v2) ![](https://tdn.totvs.com/download/attachments/931601078/image-2025-4-9_12-10-53.png?version=1&modificationDate=1744212215140&api=v2) ![](https://tdn.totvs.com/download/attachments/931601078/image-2025-4-9_12-11-17.png?version=1&modificationDate=1744212215067&api=v2) ![](https://tdn.totvs.com/download/attachments/931601078/image-2025-4-9_12-11-39.png?version=1&modificationDate=1744212215007&api=v2)![](https://tdn.totvs.com/download/attachments/931601078/image-2025-4-9_12-22-17.png?version=1&modificationDate=1744212214427&api=v2)![](https://tdn.totvs.com/download/attachments/931601078/image-2025-4-9_12-22-36.png?version=1&modificationDate=1744212214353&api=v2)

* **Utilizando Justificativa Global**

![](https://tdn.totvs.com/download/attachments/931601078/image-2025-4-22_12-29-19.png?version=1&modificationDate=1745335759207&api=v2)

* **Utilizando Justificativa Global Pré-Definida**

![](https://tdn.totvs.com/download/attachments/931601078/image-2025-4-9_12-13-56.png?version=1&modificationDate=1744212214863&api=v2) ![](https://tdn.totvs.com/download/attachments/931601078/image-2025-4-9_12-14-33.png?version=1&modificationDate=1744212214803&api=v2) ![](https://tdn.totvs.com/download/attachments/931601078/image-2025-4-9_12-14-51.png?version=1&modificationDate=1744212214740&api=v2) ![](https://tdn.totvs.com/download/attachments/931601078/image-2025-4-9_12-19-53.png?version=1&modificationDate=1744212214620&api=v2) ![](https://tdn.totvs.com/download/attachments/931601078/image-2025-4-9_12-20-8.png?version=1&modificationDate=1744212214557&api=v2)

## **PRINCIPAIS CAMPOS E PARÂMETROS**

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| **Data** | Data da batida que será alterada. |
| **Entradas** | Relação das batidas do tipo 'Entradas'. |
| **Saídas** | Relação das batidas do tipo 'Saídas'. |
| **Justificativa** | Campo texto onde deve ser informada a justificativa. Esta deve possuir no mínimo 4 e no máximo 100 caracteres. |
| **Justificativa única para todas as batidas** | Flag que permite utilizar uma única justificativa para todas as batidas. Marcando esta flag será habilitada uma caixa de texto para digitar a justificativa.  RM: Se estiver utilizando as justificativas pré-definidas (Parametrizador > Ponto > Iniciais > Usar justificativas predefinidas) e houver cadastro de justificativas no ERP (Cadastro >> Justificativas Pré-Definidas), será habilitado um campo de seleção para que possa selecionar a justificativa. Lembre-se que para serem exibidas devem estar com a flag 'Ativo' e 'Exibe no Portal' marcadas. |

## **INFORMAÇÕES ÚTEIS**

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto** | **Liberação** | **Permissão** | **Observações** |
| **RM** | 12.1.2502.137 | [Como Personalizar Permissões de Funcionalidade no Meu RH](https://tdn.totvs.com/pages/viewpage.action?pageId=287067720) | 1. A batida deverá estar dentro do período definido na parametrização de acesso do RM Portal (Parametrizador > Ponto > RM Portal > Batidas > Período de inserção de batidas).  2. Não será possível incluir batidas caso o parâmetro de sistema "Parametrizador > Ponto > RM Portal > Permissões > Bloqueia acesso aos cadastros do RM Portal" estiver habilitado.  3. Não será possível incluir uma batida igual a uma já existente. |
