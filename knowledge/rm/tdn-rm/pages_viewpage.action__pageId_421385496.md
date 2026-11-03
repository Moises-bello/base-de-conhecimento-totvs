---
content_hash: 4acc812a56a9e58964fa8829f54de3fdfb845f1bf23fe7293cb831b744591dc0
fetched_at: '2026-06-29T00:09:16.260668+00:00'
page_id: '421385496'
product: rm
source: tdn-rm
title: Geração de  Períodos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385496
version: 4
---

Podemos gerar os períodos para medição do contrato de duas maneiras:

* Geração de Períodos, de maneira automática através de processo com este nome;
* Período por período, de forma manual.

1- A primeira maneira é acessando o cadastro de Contrato **Processos/Períodos do Contrato/Geração de Períodos**:

Se o projeto utilizar status de contrato, o processo somente permitirá a geração do períodos para contratos com status 'em andamento', e será exibida a tela "Geração de Períodos" permitindo efetuar a geração automática dos períodos do contrato:

**Contrato**: Vira preenchido com o número do contrato selecionado;  
  
**Medição**: Vira preenchida com a medição escolhida no cadastro do contrato selecionado;  
  
**Período Inicial**: Será possível informar o número do primeiro período que será gerado neste momento, podendo já existir, por exemplo, 10 períodos cadastrados, neste caso, o período inicial será 11.  
  
**Data Inicial**: Será possível informar a data inicial do primeiro período. A data final será calculada de acordo como tipo de medição informado. Por exemplo, se a data inicial for 01/02/2024 e a medição mensal, a data final deste período será 29/02/2024 (ano bisexto), e a data inicial do próximo período será 01/03/2024.  
  
**Períodos**: Será possível informar quantos períodos serão criados. O campo Períodos é preenchido automaticamente, pelo número de períodos máximo, levando em consideração a data de início, a data de término do contrato e o tipo de medição do contrato.  
Depois de preenchidos estes campos clique no botão "Gerar Períodos" para visualizar os períodos antes de executar:

Através do botão "Remover Períodos" será possível remover os períodos selecionados do contrato antes de executar:

Clicando em executar, ao final da execução do processo, os períodos estarão visíveis no respectivo anexo para medição:

Importante

Se a Periodicidade Medida do Contrato estiver como Personalizada, é permitido editar as Datas.  
Na geração de período por período, aparecerá uma janela com os seguintes campos:  
**Período**:  
Informe o número do período do contrato selecionado.  
Data Início:  
Informe a data inicial deste período.  
**Data Término:**  
Informe a data final deste período.  
**Valor previsto:**  
Informe o valor previsto do período.  
Renumerar Períodos Principais:  
O sistema irá refazer a numeração dos períodos principais, para que não haja "buracos" na numeração dos mesmos, por exemplo, depois da exclusão de período(s).  
Renumerar Períodos Complementares:  
O sistema irá refazer a numeração dos períodos complementares, para que não haja "buracos" na numeração dos mesmos, por exemplo, depois da exclusão de período(s).  
Renumerar Períodos de Estorno:  
O sistema irá refazer a numeração dos períodos de estorno, para que não haja "buracos" na numeração dos mesmos, por exemplo, depois da exclusão de período(s).  
Períodos Complementares:  
Botão "Incluir": Insere um novo período complementar.  
Botão "Excluir": Exclui um período complementar existente.  
Quando desejar criar uma medição complementar de um período que já foi liberado e não deseja cancelar a liberação é preciso gerar este período complementar.  
O período complementar é gerado através da edição deste período que deseja complementar a medição, selecionando o período e clicando no botão "Editar".  
Períodos de Estorno:  
Incluir: Insere um novo período de estorno.  
Excluir: Exclui um período de estorno existente
