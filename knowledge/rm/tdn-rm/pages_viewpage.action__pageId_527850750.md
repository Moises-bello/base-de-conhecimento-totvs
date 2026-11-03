---
content_hash: f6244dddaec2b65507e0c16a80241272b6bbae0c2343e2139dc6fbb7360949b0
fetched_at: '2026-06-29T00:10:32.744869+00:00'
page_id: '527850750'
product: rm
source: tdn-rm
title: Cópia dos Parâmetros de Tipo de Movimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=527850750
version: 2
---

O processo "Cópia de Tipo de Movimento" tem o objetivo de copiar todas parametrizações de um ou de todos Tipos de Movimento para um novo Tipo de Movimento. A cópia pode ser realizada dentro da coligada atual ou para outra coligada.

**Pré-Condições:**

Para realizar a cópia de Tipos de Movimento entre Coligadas, deve-se executar o processo próprio para tal. O mesmo se encontra na visão de Tipos de Movimento no parametrizador.

*Caminho: TOTVS RM/ BackOffice / Gestão de Estoque, Compras e Faturamento/ Ambiente / Parâmetros / Gestão de Estoque, Compras e Faturamento*

**Copiando Parâmetros de Tipo de Movimento:**

Na visão de Tipos de Movimento no parametrizador Para isto basta selecionar o registro desejado e acessar o processo "Cópia de Tipo de Movimento".

**Apenas Coligada Local**

A Opção apenas Coligada Local permite a cópia entre um Tipo de Movimento para Outro Tipo de Movimento. Após Executado o processo o Tipo de Movimento 2 terá as mesmas parametrizações do Tipo de Movimento 1.

**Entre Coligadas**

Para realizar a cópia de Tipos de Movimento entre Coligadas, deve-se executar o processo marcando a opção: 'Entre Coligadas'

As opções '***Copiar***' e '***Se registro existir no destino***' são liberadas para seleção.

**→ Copiar**

Apenas Registro Atual → Irá Copiar apenas o Tipo de Movimento selecionado anteriormente na visão;

Todos os Registros → Irá Copiar Todos os Tipos de Movimento exibidos anteriormente na visão.

**→Se registro existir no destino**

Mantém o registro de Destino → Se o código de Tipo de Movimento informado já existir na coligada destino o mesmo não será copiado;

Sobrepõe o registro de Destino → Se o código de Tipo de Movimento informado já existir na coligada destino o mesmo será substituído pelo novo Tipo de Movimento.

Após escolher as opções acima basta escolher a(s) Coligada(s) de destino e finalizar a execução.

\*\* Recomenda-se utilizar os processos de Exportação / Importação de Tipo de Movimento (XML) somente na mesma Coligada, e se for realmente necessário, pois o procedimento acima funciona para ambos os casos.
