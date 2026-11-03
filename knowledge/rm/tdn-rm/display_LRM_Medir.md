---
content_hash: da74fca8a7bf07a6988be26eedeeeb8602ed3d3bf3f55f34847f0910f05336f8
fetched_at: '2026-06-29T00:11:56.443529+00:00'
page_id: '866026203'
product: rm
source: tdn-rm
title: Medir
type: documentation
url: https://tdn.totvs.com/display/LRM/Medir
version: 4
---

**Medição do período de contrato**

Observação: A medição pode ser realizadas para contratos de serviços, contratos de insumos, contrato Extra e Extra Histograma.

**Tela de medição do período de contrato de serviços**

**Medições de Contratos**:

A configuração de casas decimais dessa tela será de acordo com os [parâmetros do projeto](https://tdn.totvs.com/display/public/LRM/Casas+Decimais) do contrato em questão.

É possível alterar a ordem e definir a visibilidade das colunas no botão Gerenciador de colunas:

* Definir a visibilidade das colunas:

* E ordena-las da melhor forma:

* Se desejar voltar a visualizar as colunas como estavam, ainda é possível clicar no botão de **Restaurar Padrão**.
* As preferências do usuário são salvas para futuras sessões e para demais medições no Portal.

#### Workflow do status de contrato

Na ilustração a seguir, é possível observar o fluxo de todos os contratos vinculados ao seu projeto, de acordo com os parâmetros de filtragem estabelecidos. A imagem exemplifica as etapas do contrato em que é possível efetuar alterações, por meio da ação de manter pressionado e arrastar para a coluna ao lado.

**Medições via Excel**

É possível exportar do portal medições as tarefas/insumos para o Excel através do processo **Baixar planilha de medições**.

Ao executar o processo, um arquivo do tipo .XLSX será baixado contendo as tarefas (quando contrato de serviços) ou insumos (para o contrato de insumo).

Na imagem abaixo executamos o processo para um **contrato de serviços**:

E um arquivo foi baixado contendo as informações das medições do contrato de serviços:

Para o **contrato de insumo**, ao baixar o arquivo:

Diferente do arquivo gerado para o contrato de serviços, para o contrato de insumo, o arquivo terá uma planilha para cada insumo e listará todas as tarefas que utilizam o insumo, para que a medição seja feita na respectiva coluna:

É possível importar para o portal de medições as tarefas/insumos via Excel através do processo **Importar medição via Excel**.

Ao executar o processo, um arquivo do tipo .XLSX será importado contendo as tarefas (quando contrato de serviços) ou insumos (para o contrato de insumo), com ajustes que foram realizados na planilha.

Na imagem abaixo executamos o processo para um **contrato de serviços**:

No arquivo anteriormente baixado contendo as informações das medições do contrato de serviços realize as alterações necessárias e importe o Excel:

Para o **contrato de insumo**, depois das alterações na planilha, importe o arquivo:

Lembrado que diferente do arquivo gerado para o contrato de serviços, para o contrato de insumo, o arquivo terá uma planilha para cada insumo e listará todas as tarefas que utilizam o insumo, para que a medição seja feita na respectiva coluna:

Depois de alterado e importado é possível visualizar as alterações no portal e no sistema.

A ordem das colunas e planilhas não deverão ser alteradas. Apenas as colunas Quantidade medida, Valor medido e % medido devem ter seus respectivos dados informados para importação.

Observação: Para que a importação funcione, é necessário seguir as regras na primeira aba da planilha.

**Visualizar hierarquia de tarefas nas medições:**Com esse parâmetro de projeto [(Contratos>Portal de Medição)](https://tdn.totvs.com/pages/viewpage.action?pageId=421385359) marcado, as informações de etapa/obra serão exibidas na visão de medição. Esse comportamento também será aplicado ao arquivo Excel gerado ao baixar a planilha de medição.

Abaixo a tela de medições trazendo as linhas referente a obra e etapa (Parâmetro marcado):

Em seguida, com o parâmetro desmarcado:

Os itens associados a aditivos contratuais passaram a ser identificados visualmente na tabela de itens da medição. Para isso, foi inserida uma nova coluna na tabela, onde um ícone é exibido ao lado de cada item vinculado a um aditivo.

A exibição dos itens de aditivos depende da configuração de parâmetros do projeto > contratos > geral  chamada **“Utilizar status do contrato”**:

* **Quando a configuração está habilitada**: serão listados **apenas os aditivos que possuem em seu histórico um status diferente de “Em negociação”**.
* **Quando a configuração está desabilitada**: todos os aditivos serão listados, **independentemente de seu histórico**.
