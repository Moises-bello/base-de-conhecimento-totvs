---
content_hash: 7a9c5afc0dbfe7aec45f3daa24db845f97d0155850a1c7e6d76e5fbb8957f6da
fetched_at: '2026-06-29T00:10:37.203443+00:00'
page_id: '536726674'
product: rm
source: tdn-rm
title: Casas Decimais (F6)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=536726674
version: 5
---

---

**Exibição**

Informe o número de casas decimais visíveis aos valores e cálculos conforme parametrização, para:

**Percentuais:** Determine o número de casas decimais dos campos que expressam percentuais em geral. Exemplo: % na obra, % na planilha, % de reajuste, etc.

**Monetários:** Determine o número de casas decimais dos campos que expressam valores em moeda corrente, (R$). Exemplos: Preço do insumo, preço da tarefa, etc.

**Coeficientes:** Determine o número de casas decimais dos campos que expressam coeficientes.

**Quantitativos:** Determine o número de casas decimais dos campos Quantidades.

**Taxas:**Determine o número de casas decimais dos campos B.D.I. e Taxas de Lei Social.

**Coeficientes Especiais:**

Determine o número de casas decimais para os campos Coeficientes, Coef. Produtivo, Quantidade de Recursos da Composição, DMT das composições, campos livres do custo horário dos insumos, campos livres globais e campo Produção por Hora no cadastro de Composição do tipo Por Produção. Para possibilitar a utilização de 8 casas decimais para os coeficientes especiais os valores armazenados no banco de dados estão multiplicados por 10.000 e por essa razão, na montagem de relatórios deve-se criar uma expressão que divida por 10.000 esses campos. Caso você queira imprimir o valor com as 8 casas decimais, deve-se configurar a expressão, para ser impressa "Sem formato".

**Casas Decimais na Planilha de Tarefas (EMOP)**

Caso habilitado formata o valor do Projeto calculado com o número de casas decimais informado.

**Casas Decimais na Composição**

Este parâmetro possibilita truncar exclusivamente o valor total das Composições em até 4 casas decimais, sendo que a exibição do valor respeita o Parâmetro de Exibição de Casas Decimais para Monetários em Parâmetros de Projeto | Casas Decimais| Exibição;

Exemplo:

* Casas Decimais na Composição: 2;
* Casas Decimais para exibição de Monetários: 4

Na tela o valor será exibido da seguinte forma: 18,2700 \* Casas Decimais na Composição: 2;

* Casas Decimais para exibição de Monetários: 3

Na tela o valor será exibido da seguinte forma: 18,270

**Casas Decimais na Composição Auxiliar**

Este parâmetro marcado estará definindo o número de casas decimais que serão permitidas para os valores dos itens adicionais em uma composição auxiliar.

Exemplo:

* Se  definir o número de casas decimais como 2, todos os valores fracionários ou decimais serão arredondados para duas casas decimais.

**Considerar Casas Decimais:**

Caso esta opção esteja habilitada, os cálculos serão efetuados considerando apenas as casas decimais visíveis, parametrizadas na pasta Exibição. Caso contrário, os cálculos serão efetuados considerando o número máximo de casas decimais e como cada valor exibido é gravado na base, o mesmo é arredondando para quatro casas decimais (número máximo de casas decimais do banco de dados).

O parâmetro 'Arredondar' ou 'Truncar' só pode ser habilitado quando o parâmetro 'Considerar casas decimais' está ativo.

**Observação:**

Sugere-se a utilização deste parâmetro marcado, pois o mesmo poderá gerar diferença entre o orçamento o contratado e a liberação para o BackOffice por arredondamento. No caso de contratos será associado um preço unitário com quatro casas decimais, o que resultara em um valor diferente do calculado na utilização do parâmetro desmarcado para o orçamento.

**Arredondar / Truncar:**

Marque a opção "Arredondar" quando desejar que os cálculos do projeto arredondem ou "Truncar" quando desejar que os cálculos do projeto trunquem. Arredondamento à o valor 1,34567 seria arredondado para quatro casas decimais e seria o valor 1,3457 Truncamento à o valor 1,34567 seria truncado para quatro casas decimais e seria o valor 1,3456

**Tratamento de Valor diferenciado:**

Opção de parametrização para controle de valor das tarefas ou composições do projeto. A quantidade de casas decimais utilizadas para o cálculo pode ser definida e os valores podem ser arredondados, truncados ou respeitarem a parametrização default do projeto.

---
