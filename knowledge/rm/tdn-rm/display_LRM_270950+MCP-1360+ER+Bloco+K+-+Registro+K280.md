---
content_hash: 89b7ef5ddb38348927e83e7ad30b73b02f27ca6b5fa341e4828a1823e6670b7a
fetched_at: '2026-06-29T00:08:24.174356+00:00'
page_id: '270893489'
product: rm
source: tdn-rm
title: 270950 MCP-1360 ER Bloco K - Registro K280
type: documentation
url: https://tdn.totvs.com/display/LRM/270950+MCP-1360+ER+Bloco+K+-+Registro+K280
version: 138
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Estoque > Produção > Movimentação |
| **Segmento Executor** | Construção & Projetos | | |
| **Chamado** | 270950 | | |
| **País** | Brasil | | |

   

## Objetivo

Possibilitar ao usuário a geração dos registros de correção de apontamento do estoque escriturado e consequentemente a geração no TOTVS Gestão de Estoque, Compras e Faturamento do Registro K280 do Bloco K conforme disposto no Ato COTEPE/ICMS 7 de 13 de maio de 2016. 

## Definição da Regra de Negócio

*O*Ato COTEPE/ICMS 7 de 13 de maio de 2016 altera a redação de alguns artigos do Ato COTEPE/ICMS 09/08, que dispõe sobre as especificações técnicas para a geração de arquivos da Escrituração Fiscal Digital - EFD, acrescentando alguns dispositivos ao Manual de Orientação do Leiaute da Escrituração Fiscal - EFD, entre eles os seguintes registros do Bloco K: 

| Bloco | Descrição | Registro | Nível | Ocorrência | Obrigatoriedade do bloco (Todos os contribuintes) |
| --- | --- | --- | --- | --- | --- |
| K | Desmontagem de mercadorias – Item de Origem | K210 | 3 | 1:N | OC |
| K | Desmontagem de mercadorias – Item de Destino | K215 | 4 | 1:N | OC |
| K | Reprocessamento/Reparo de Produto/Insumo | K260 | 3 | 1:N | OC |
| K | Reprocessamento/Reparo – Mercadorias Consumidas e/ou Retornadas | K265 | 4 | 1:N | OC |
| K | Correção de Apontamento dos Registros K210, K220, K230, K250 e K260 | K270 | 3 | 1:N | OC |
| K | Correção de Apontamento e Retorno de Insumos dos Registros K215, K220, K235, K255 e K265 | K275 | 4 | 1:N | OC |
| K | Correção de Apontamento – Estoque Escriturado | K280 | 3 | 1:N | OC |

Neste momento iremos tratar do registro de correção de apontamento do estoque escriturado - K280. 

 

 

### Correção de Apontamento

Esse tipo de registro se destina a atender a dificuldade relatada pelas empresas nas quais, em decorrência da natureza física dos produtos, há a possibilidade de ocorrer diferenças no estoque, como, por exemplo, produtos a granel, líquidos etc., que alteram sua quantidade e não podem ser medidos com precisão.

Essas correções poderão ser efetuadas no registro K280 – Correção de Apontamento – Estoque Escriturado: Esse registro visa escriturar a correção de apontamento de estoque escriturado, de período de apuração anterior escriturado no registro K200 – Estoque Escriturado. Portanto, por meio desse registro, é possível fazer ajustes diversos em produtos estocados, sejam eles produtos acabados, insumos ou material de embalagem.

### Registro K280 - Correção de Apontamento - Estoque Escriturado

Este registro tem o objetivo de declarar a correção de apontamento de estoque escriturado no Registro K200, de período de apuração anterior.

A correção de apontamento tem que ocorrer, obrigatoriamente, entre o levantamento de 02 inventários, uma vez que, com a contagem do estoque se terá conhecimento de uma eventual necessidade de correção de apontamento.

A correção do estoque escriturado de um período de apuração poderá influenciar estoques escriturados de períodos posteriores, até o período imediatamente anterior ao período de apuração em que se está fazendo a correção, uma vez que o estoque final de um período de apuração é o estoque inicial do período de apuração seguinte.

As quantidades devem ser expressas, obrigatoriamente, na unidade de medida de controle de estoque constante no campo 06 do registro 0200: UNID\_INV.

A chave deste registro são os campos: DT\_EST, COD\_ITEM, IND\_EST e COD\_PART (este, quando houver).

 

| Nº | Campo | Descrição | Tipo | Tam | Dec | Obrig |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "K280" | C | 004 | - | O |
| 02 | DT\_EST | Data do estoque final escriturado que está sendo corrigido | N | 008\* | - | O |
| 03 | COD\_ITEM | Código do item (campo 02 do Registro 0200) | C | 060 | - | O |
| 04 | QTD\_COR\_POS | Quantidade de correção positiva de apontamento ocorrido em período de apuração anterior | N | - | 03 | OC |
| 05 | QTD\_COR\_NEG | Quantidade de correção negativa de apontamento ocorrido em período de apuração anterior | N | - | 03 | OC |
| 06 | IND\_EST | Indicador do tipo de estoque: 0 = Estoque de propriedade do informante e em seu poder; 1 = Estoque de propriedade do informante e em posse de terceiros; 2 = Estoque de propriedade de terceiros e em posse do informante | C | 001 | - | O |
| 07 | COD\_PART | Código do participante (campo 02 do Registro 0150): - proprietário/possuidor que não seja o informante do arquivo | C | 060 | - | OC |

Observações:

Nível hierárquico - 3  
Ocorrência – 1:N

Descrição dos campos do registro K280:

* Campo 01 (REG) - Valor Válido: [K280];

* Campo 02 (DT\_EST) – Validação: a data do estoque deve ser anterior à data inicial do período de apuração – campo DT\_FIN do Registro K100;

* Campo 03 (COD\_ITEM) – Validação: o código do item deverá existir no campo COD\_ITEM do Registro 0200. Somente podem ser informados nesse campo valores de COD\_ITEM cujos tipos sejam iguais a 00, 01, 02, 03, 04, 05, 06 e 10 – campo TIPO\_ITEM do Registro 0200.

* Campos 04 e 05 (QTD\_COR\_POS e QTD\_COR\_NEG) – Validação: não é admitida quantidade negativa e somente um desses campos pode ser preenchido.

* Campo 06 (IND\_EST) - Valores Válidos: [0, 1, 2]. Validação: se preenchido com valor “1” (posse de terceiros) ou “2” (propriedade de terceiros), o campo COD\_PART será obrigatório.  

  A quantidade em estoque existente no estabelecimento industrializador do produto industrializado para terceiro por encomenda deverá ser:  
  a) quando o informante for o estabelecimento industrializador, do tipo 2 - estoque de propriedade de terceiros e em posse do informante;  
  b) quando o informante for o estabelecimento que realizou a encomenda, do tipo 1 - estoque de propriedade do informante e em posse de terceiros.

  A quantidade em estoque existente no estabelecimento industrializador de insumo recebido do estabelecimento que realizou a encomenda para industrialização deverá ser:  
  a) quando o informante for o estabelecimento industrializador, do tipo 2 - estoque de propriedade de terceiros e em posse do informante;  
  b) quando o informante for o estabelecimento que realizou a encomenda, do tipo 1 - estoque de propriedade do informante e em posse de terceiros.

* Campo 07 (COD\_PART) – Preenchimento: obrigatório quando o IND\_EST for “1” ou “2”. Validação: o valor fornecido deve constar no campo COD\_PART do registro 0150.

O Registro K280 se refere a correções dos saldos de estoque escriturados no registro K200 em períodos anteriores e deve ser gerado a partir do período de apuração da correção até o período de apuração imediatamente anterior ao mês de referência da correção.

Vamos exemplificar uma situação em que a necessidade de correção de apontamento é conhecida somente em mês posterior ao mês de referência do apontamento.

Período de referência do apontamento: janeiro/2017:  
0000 – 31/01/2017 a 31/01/2017  
K100 – 31/01/2017 a 31/01/2017  
K200 – 31/01/2017 – Produto X – Quant. 60

Em abril/2017 detectou-se que na realidade a quantidade em estoque que existia para o Produto X em janeiro/2017 era 40.

Neste caso será feito um ajuste negativo no mês de abril que irá gerar os registros K280 dos meses anteriores, conforme descrito a seguir:

Período de correção do apontamento: abril/2017:  
0000 – 30/04/2017 a 30/04/2017  
K100 – 30/04/2017 a 30/04/2017  
K280 – Data de referência do estoque: 31/01/2017 – Produto X – Quant. de correção negativa: 20  
K280 – Data de referência do estoque: 29/02/2017 – Produto X – Quant. de correção negativa: 20  
K280 – Data de referência do estoque: 31/03/2017 – Produto X – Quant. de correção negativa: 20

Cabe lembrar que se a necessidade de correção do apontamento é conhecida dentro do próprio mês, não há que se falar em utilização do Registro K280, pois a correção deverá ser efetuada nos próprios registros originais relativos ao mês de referência.

No TOTVS Gestão de Estoque, Compras e Faturamento o registro K280 será gerado a partir de movimentos de ajuste positivo ou negativo do saldo atual, saldo do estoque com terceiros ou saldo de terceiros em poder da empresa.

Para que o sistema possa identificar quais são os tipos de movimento que irão gerar os registros K280, serão criados nos Parâmetros do Tipo de Movimento, na Etapa 61 - Fis Dados:

* Group box com o título SPED Fiscal;
* Campo "Data para Registro K280" do tipo drop down e localizado dentro do group box SPED Fiscal.

As opções para preenchimento do campo "Data para Registro K280" serão:

* Não usa;
* Data Emissão;
* Data Extra 1;
* Data Extra 2.

Por default o campo não virá preenchido, ficando a cargo do usuário o fornecimento da informação, sendo que enquanto não estiver preenchido este campo não deve ser considerado nas rotinas que envolverem movimentos desse tipo.

Como o movimento que irá gerar o Registro K280 poderá afetar não só o saldo atual, como também o saldo de estoque de terceiros ou o saldo de estoque com terceiros, deverá ser criado um novo Tipo de Controle de Estoque de Terceiros (TTMVEXT.CONTROLETERCEIROS) que é o 'Ajuste'. No momento em que o usuário selecionar o preenchimento do campo "Tipo de Controle de Estoque de Terceiros", o Ajuste deverá ser sempre o último da lista de tipos de controle de estoque de terceiros disponíveis.

Caso o usuário preencha o campo "Data para Registro K280" com 'Não Usa' não existem consistências a serem feitas pelo sistema, mas caso o campo seja preenchido com qualquer uma das datas disponíveis, no momento da gravação dos parâmetros do tipo de movimento, o sistema deverá efetuar as seguintes consistências:

* O campo referente à edição da data (como por exemplo os campos: "Edição da Data de Entrada", "Edição da Data Extra1", etc., das Etapas 4 e 5 - Mov - Datas 1/2 e Mov - Datas 2/2) que foi definida como a data para o K280, não pode estar preenchido com 'Não Edita';
* A data selecionada para ser a data do Registro K280 não pode estar parametrizada como "Data do Movimento Default" na Etapa 4 - Mov - Datas 1/2, já que a data do movimento é a data em que o estoque será realmente afetado;
* O tipo de movimento deverá obrigatoriamente afetar, aumentando ou diminuindo, pelo menos um dos seguintes saldos: 
  + Saldo Atual (TITMTMV.EFEITOSALDOA2);
  + Saldo de Terceiros (TITMTMV.EFEITODETERCEIROS);
  + Saldo com Terceiros (TITMTMV.EFEITOCOMTERCEIROS);
* O Tipo de Controle de Estoque de Terceiros somente poderá ser de "Ajuste ref. Correção Apontamento - Estoque Escriturado" caso a "Data para Registro K280" esteja preenchida com uma das datas disponíveis, caso contrário esse tipo de controle não poderá ser utilizado.

O sistema irá identificar os movimentos que irão gerar o registro K280, através do preenchimento do campo "Data para Registro K280" se diferente de nulo ou 'Não Usa', e neste caso, no momento em que esses movimentos forem gravados o sistema deverá fazer as seguintes consistências:

* A data configurada como "Data para Registro K280" não poderá estar em branco;
* A data configurada como "Data para Registro K280" tem que ser de meses anteriores à "Data do Movimento";
* Caso o movimento esteja afetando o Saldo de Terceiros ou o Saldo com Terceiros, o preenchimento do cli/for ou do cli/for origem/destino deve ser obrigatório devido à informação do código do participante (consistência já efetuada pela rotina que controla o estoque de terceiros);
* O campo Situação da Mercadoria (TPRDFISCAL.SITUACAOMERCADORIA) de todos os itens constantes do movimento tem que estar preenchido com um dos seguintes conteúdos;  
  + 01 – Mercadoria para Revenda;
  + 02 – Matéria-Prima;
  + 03 – Produto em Processo;
  + 04 – Produto Acabado;
  + 08 – Embalagem;
  + 09 – Subproduto;
  + 10 – Produto Intermediário;
  + 15 – Outros insumos.

Iremos destacar abaixo como deverá ser o preenchimento de alguns dos campos do registro K280: 

* DT\_EST: Verificar o conteúdo da data parametrizada como "Data para Registro K280" e levar para este campo o último dia do mês informado nesta data;
* QTD\_COR\_POS: Traz a quantidade do item dos movimentos cujo tipo de movimento está configurado para Aumentar o saldo, seja ele Atual, de Terceiros ou com Terceiros;
* QTD\_COR\_NEG: Traz a quantidade do item dos movimentos cujo tipo de movimento está configurado para Diminuir o saldo, seja ele Atual, de Terceiros ou com Terceiros;
* IND\_EST: Deve ser preenchido conforme o saldo que será afetado pelo movimento, ou seja:
  + 0 - caso o movimento vá afetar o saldo Atual do item;
  + 1 - caso o movimento vá afetar o saldo Com Terceiros do item:
  + 2 - caso o movimento vá afetar o saldo De Terceiros do item.
* COD\_PART: Código do cliente/fornecedor dos movimentos que afetam Saldo de Terceiros ou Saldo com Terceiros. Este campo não deverá ser preenchido nos registros em que o saldo afetado é o Saldo Atual.

**Importante**: Podem existir tipos de movimento que estejam parametrizados para afetar ao mesmo tempo o Saldo Atual e o Saldo com Terceiros e, nestes casos, deverá ser gerado para o mesmo item e na mesma data, um Registro K280 para cada saldo que está sendo afetado.

Conforme já dissemos, o Registro K280 se refere a correções dos saldos de estoque escriturados no registro K200 em períodos anteriores e deve ser gerado a partir do período de apuração da correção até o período de apuração imediatamente anterior ao mês de referência da correção, assim na geração desses registros o sistema irá considerar tanto a "Data para Registro K280" como a "Data do Movimento", gerando-os desde a Data de Registro até o mês imediatamente anterior ao da Data do Movimento.

Assim, após terem sido gravadas todas as movimentações de correção de estoque escriturado do mês, o TOTVS Gestão Fiscal estará apto a gerar, no SPED Fiscal, os Registros K 280 relativos a estas movimentações.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros dos Tipos de Movimento | Alteração | Ambiente > Parâmetros > Gestão de Estoque, Compras e Faturamento > Gestão de Estoque > Ajuste de Estoque | Conforme definições constantes deste documento |

## Tabelas Utilizadas:

* TTMVEXT - Parâmetros dos Tipos de Movimento

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
