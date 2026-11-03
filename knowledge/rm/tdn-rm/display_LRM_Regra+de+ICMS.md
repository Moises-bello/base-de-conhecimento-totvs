---
content_hash: ed39c1d2e7e69319477989dc6612091d853b0432b22dbec238d957214f81b2d1
fetched_at: '2026-06-29T00:09:23.862180+00:00'
page_id: '422546143'
product: rm
source: tdn-rm
title: Regra de ICMS
type: documentation
url: https://tdn.totvs.com/display/LRM/Regra+de+ICMS
version: 70
---

Nas Regras de ICMS deverão ser cadastradas todas as situações tributárias relativas ao ICMS, existentes nas operações de Entradas / Saídas ocorridas na empresa. O cálculo do ICMS no lançamento fiscal, bem como a edição dos campos relacionados ao ICMS, considera a informação contida nesse cadastro, que irá ser associado à natureza de operação.

false1true1IdentificaçãoIdentificação

**Código:** Informe o código da Regra de ICMS

**Global:**Define se a regra será global, ou seja, poderá ser vinculada a qualquer natureza de operação, independente do cadastro de naturezas ser Global ou Por Filial. Desabilitando este campo, a regra passa a ser Por Filial, só podendo ser vinculada à natureza de operação da filial em que a regra foi incluída.  
***Observações*:**A alteração de uma regra de Global para Por Filial só poderá ocorrer se não existir natureza de operação vinculada a lançamentos e/ou movimentos. Já a alteração da regra de Por Filial para Global poderá ocorrer sem restrições.

**Descrição**: Preencha a descrição de acordo com o que o usuário desejar.

**Tipo Tributação:** Contém os tipos de ICMS disponíveis no sistema. O tipo selecionado deverá corresponder à operação realizada, exemplo, para uma operação com isenção de ICMS, o tipo escolhido deverá ser o Isento.

**Situação Tributária:** Este campo deve ser preenchido de acordo com o tipo de tributação escolhido (Tributado, Isentos, Outros, etc). Os valores são determinados pelo RICMS e serão utilizados por várias rotinas legais. Os códigos válidos são os seguintes:

| Código | Situação Tributação |
| --- | --- |
| 00 | Tributada Integralmente |
| 10 | Tributada e com cobrança de ICMS por Substituição Tributária |
| 20 | ICMS com Redução de Base de Cálculo |
| 30 | Isenta ou Não Tributada e com cobrança do ICMS por Substituição Tributária |
| 40 | Isenta |
| 41 | Não Tributada |
| 50 | Suspensão |
| 51 | Diferimento |
| 60 | ICMS cobrado anteriormente por Substituição Tributária |
| 70 | Redução de Base de Cálculo e cobrança do ICMS por Substituição Tributária |
| 90 | Outras |

Este campo será utilizado para compor, de acordo com a legislação vigente, o Código de Situação Tributária, que é composto de dois dígitos na forma AB, onde o primeiro dígito indicará a origem da mercadoria, com base na tabela A, e o segundo e terceiro dígitos a tributação do ICMS, com base na tabela B, indicada nesse campo.

O primeiro dígito, que indica a origem da mercadoria, deverá ser informado no campo Procedência do cadastro de Produtos. O segundo e terceiro dígitos serão a primeira e segunda posições, respectivamente, deste campo da Regra de ICMS, exemplo:

Se no campo Procedência foi informado, para determinado produto, o código igual a 0, significando que o produto é nacional, e se o tipo de ICMS da regra for Tributado, deverá ser informado no campo Situação Tributária o valor igual a 00. Com base nestes dados o Código da Situação Tributária será 000, indicando que o produto é nacional, com tributação de ICMS integral.  
***Observações*:** O Código de Situação Tributária é de extrema importância para várias rotinas legais, devendo ser informado em todas as regras de ICMS cadastradas.

**Operação Tributária:** Selecione qual o tipo da operação. Caso não se trate de uma operação com Substituição Tributária  ou Diferencial de Alíquota, selecione Não se Aplica.

* **Substituição Tributária:** Esta opção será utilizada quando a operação for referente à Substituição Tributária do ICMS. Marcando esta opção, será aberta a pasta Dados ICMS ST para parametrização na regra de ICMS. No lançamento fiscal será habilitada a tela de cálculo do ICMS ST.
* **Diferencial de Alíquota:** Esta opção será utilizada quando a operação for referente ao Diferencial de Alíquota. Marcando este campo também será aberta a tela de Dados ICMS ST na regra de ICMS e no lançamento fiscal habilita a tela de cálculo do Diferencial de Alíquota.
* **Não se Aplica:** Quando a operação não se referir nem a substituição tributária e nem ao diferencial de alíquota, esta opção deverá ser utilizada.

**CSOSN:**Este campo deve ser preenchido de acordo com o tipo de Tributação do ICMS pelo SIMPLES NACIONAL (Tributado, Isentos, Outros, etc).

| Código | Situação Tributação |
| --- | --- |
| 101 | Tributada pelo Simples Nacional com permissão de crédito |
| 102 | Tributada pelo Simples Nacional sem permissão de crédito |
| 103 | Isenção do ICMS no Simples Nacional para faixa de receita bruta |
| 201 | Tributada pelo Simples Nacional com permissão de crédito e com cobrança do ICMS por Substituição Tributária |
| 202 | Tributada pelo Simples Nacional sem permissão de crédito e com cobrança do ICMS por Substituição Tributária |
| 203 | Isenção do ICMS no Simples Nacional para faixa de receita bruta e com cobrança do ICMS por Substituição Tributária |
| 300 | Imune |
| 400 | Não tributada pelo Simples Nacional |
| 500 | ICMS cobrado anteriormente por Substituição Tributária (substituído) ou por antecipação |
| 900 | Outros |

***Observações*:** O Código de Situação da Operação no Simples Nacional - CSOSN será usado na Nota Fiscal Eletrônica exclusivamente quando o Código de Regime Tributário - CRT for igual a "1", e substituirá os códigos da Tabela B - Tributação pelo ICMS do Convênio s/nº de 15 de dezembro de 1970.

2Dados ICMSDados ICMS

Nesta pasta serão parametrizados os dados relativos ao ICMS.

**Alíquota ICMS (%):** Alíquota do ICMS que se aplica a operação.

**Redução Base ICMS (%):** Percentual de redução a ser aplicado à base de cálculo do ICMS, de acordo com as regras de aplicação do RICMS, exemplo:

|  |  |
| --- | --- |
| Base do ICMS | 1.000,00 |
| %Redução do ICMS | 10 |
| Base Tributada do ICMS | 900,00 |

**ICMS Dobro:** Habilitando esta opção, o sistema estará dobrando o valor das mercadorias informado, para compor a base de cálculo do ICMS do lançamento.

***Observações:****S*omente após a base dobrada do ICMS, o sistema adicionará os novos valores financeiros (descontos, despesas, seguros, etc) pertencentes à tela de mercadorias do lançamento fiscal.

**ICMS por Dentro:** Marcada esta opção, o sistema passa a calcular o ICMS "por dentro", de forma a integrar a sua própria base de cálculo. O sistema considerará a alíquota do ICMS para calcular o valor do imposto com base no valor total informado na tela de mercadorias do lançamento fiscal, e posteriormente utilizará o valor do imposto para compor a sua própria base de cálculo. Após a apuração da base de cálculo do ICMS, o sistema utilizará a mesma alíquota para cálculo do imposto final.

Sem Redução de Base de Cálculo

|  |  |
| --- | --- |
| Valor das Mercadorias | 1.000,00 |
| Alíquota do ICMS | 18 |
| Base do ICMS | (1.000,00 /  (1 - (18/100))) = 1.219,51 |
| Valor do ICMS | 1219,51 \* (18/100) = 219,51 |

Com Redução de Base de Cálculo

|  |  |
| --- | --- |
| Valor das Mercadorias | 1.000,00 |
| Alíquota do ICMS | 18 |
| Redução de Base de Cálculo | 51,11% |
| Alíquota Reduzida | 18 - (18 \*  (51,11 / 100))  = 18 - 9,20 =  8,80% |
| Base do ICMS (Sem Redução) | 1.000,00 / (1 - (8,8/100)) = 1.000,00 / 0,912 = 1.096,49 |
| Base do ICMS Reduzida | 1.096,49 - (1.096,49 \* (51,11/100)) = 1.096,49 - 560,42 = 536,07 |
| Valor do ICMS | 536,07 \* (18/100) = 96,49 |

**Soma ICMS Por Dentro Valor Contábil:** Ao marcar este campo, o sistema irá somar o valor calculado do ICMS por Dentro ao valor contábil do lançamento fiscal.

**ICMS Indexado:** Esta opção permite que sejam gravados lançamentos em que a base de cálculo do ICMS seja indexada ou pautada, onde o valor da base de cálculo normalmente difere do valor da mercadoria.

**ICMS Metade:** Habilitando esta opção, o sistema dividirá por dois o valor das mercadorias que compõem a base de cálculo do ICMS do lançamento. O valor referente à outra metade da base tributada será lançado no campo Outros ICMS.

**ICMS Desonerado**: Todas as operações que sejam beneficiada com isenção ou não incidência de ICMS, o campo "ICMS Desonerado" será habilitado na aba Dados do ICMS,  do cadastro da Regra de ICMS, quanto Tipo de Tributação  selecionada na aba Identificação da Regra de ICMS for igual a Não Incidência, Isento e Suspenso.

Ao marcar a opção ICMS Desonerado, será habilitado o campo Motivo desoneração do ICMS que devem ser preenchidos com os valores válido:

* 3=Uso na agropecuária;
* 9=Outros;
* 12=Órgão de fomento e desenvolvimento agropecuário

Além do Motivo desoneração do ICMS, será habilitado também o campo Fórmula Base de Cálculo do ICMS Desonerado, fórmula que deve ser criada no TOTVS Gestão de Estoque, Compra e Faturamento.

Importante!

Após desabilitar a Integrações de Sistema é necessário fechar o sistema e reiniciar o Host. A responsabilidade da criação da fórmula é do usuário. Necessitando para isto analisar a resolução que alterou o ICMS Desonerado para saber quais componentes ela deve ter.

Figura

***Observações:***A fórmula é definida pelo usuário e criada no TOTVS Gestão de Estoque, Compras e Faturamento.

**ICMS Desonerado NÃO afeta o Valor da Operação:** Habilitando essa opção, o valor do ICMS Desonerado não afetará o Valor Total da Situação Tributária e o valor de Isentos.

**Operação com FCP**: Habilitado esta opção, o sistema realizará o calculo do valor do FECP ICMS Próprio  de acordo com a Base Tributada de ICMS e percentual (%) FECP ICMS Próprio.

**Afeta Base do ICMS**

* **Frete:** Habilitando este campo o frete passará a compor a base de cálculo do ICMS.
* **IPI:** Habilitando este campo o IPI passará a compor a base de cálculo do ICMS.
* **Diferencial de Alíquota:** Deverão ser informados os valores financeiros do lançamento fiscal que não afetarão a base de cálculo do ICMS. Ao habilitar estes campos, serão apresentados na tela de mercadorias do lançamento fiscal os campos Desconto Condicional e Despesa Condicional.

**Lança IPI em**: Quando o lançamento possuir redução de base, dever ser selecionara entre as opções: Isentos, Outros e Não Lança.

**Colocar Redução em**: Quando aplicada redução do ICMS deve ser indicado onde serrá informado o valor da redução: Isentos ou Outros.

**Lançar Redução de Produto Em**: Selecionar em qual o campo deve ser gerada a redução do produto: Não Lança, Isentos ou em Outros.

**Valores Condicionais**: Quando o desconto for efetivamente concedido depende da ocorrência de fato posterior à emissão da nota fiscal, deverá ser habilitada uma das opções ou as duas caso ocorra Desconto ou Despesa.

3Dados ICMS S.T.Dados ICMS S.T.

Nesta pasta serão parametrizados os dados referentes às operações com substituição tributária. Será apresentada quando a Operação Tributária for Substituição Tributária ou Diferencial de Alíquota.

**Alíquota ST / Interna D.A. (%):** Neste campo é informada a alíquota referente à base de substituição tributária e também a alíquota interna do estado de destino das mercadorias, em operações referentes ao diferencial de alíquota.

**Redução Base ICMS ST / D.A. (%):** Utiliza-se este campo para informar o percentual de redução da base de cálculo do ICMS ST nos casos em que a base não é tributada integralmente.

**Margem de Lucro ICMS ST (%):** Neste campo será informada a margem de valor agregado referente ao ICMS ST.

**Afeta Base ICMS ST**: Habilitar a opção que se encaixe na operação quando a operação destacar desconto, despesa, frete e seguro.

Atenção! Estes parâmetros não afetam o cálculo da Base de Cálculo do Diferencial de Alíquota, apenas do ICMS ST.

**Utiliza ICMS Por Dentro no D.A.**:

* **Não Utiliza**: De acordo com o Convênio 152/2015, será utilizado a forma de cálculo atual, o valor da operação.
* **Base de Cálculo Com ICMS:** Opção: Campo “**Utiliza ICMS por Dentro no D.A**” igual a **Base de Cálculo Com ICMS**

|  |
| --- |
| Vop / (1 - ALQ intra) |

Se o Campo **“% Redução de Base ICMS ST”** estiver habilitado

|  |
| --- |
| ((Vop / (1 - ALQ intra)) \* %Redução) |

**Onde**:

Vop = Valor da Operação;

ALQ intra = alíquota interna aplicável à operação ou prestação no estado de destino.

* **Base de Cálculo Sem ICMS**: Com esta opção será excluído do valor da operação o valor do imposto (ICMS Próprio) correspondente à operação interestadual regularmente destacado no documento fiscal;

|  |
| --- |
| ((Vop - VI) / (1- ALQ intra)) |

Se o Campo % Redução de Base ICMS ST estiver habilitado

|  |
| --- |
| (((Vop - VI) / (1- ALQ intra)) \* %Redução) |

**Onde:**

Vop = Valor da Operação;

VI= o valor do imposto destacado (ICMS Próprio) no documento fiscal;

ALQ intra = alíquota interna aplicável à operação ou prestação no Estado de destino.

* **Base de Cálculo Sem ICMS - Interestadual**: Nesta opção será excluído do valor da operação o valor do imposto (ICMS Próprio) correspondente à operação interestadual regularmente destacado no documento fiscal

|  |
| --- |
| ((Vop-VI) / (1- ALQ intra)) |

Se o Campo % Redução de Base ICMS ST estiver habilitado

|  |
| --- |
| (((Vop-VI)/ (1- ALQ intra)) \* %Redução) |

**Onde**:

Vop = Valor da Operação;

VI= o valor do imposto destacado (ICMS Próprio) no documento fiscal;

ALQ intra = alíquota interna aplicável à operação ou prestação no Estado de destino.

O valor do Diferencial de Alíquota é calculado aplicando a alíquota interestadual sobre a Base de Cálculo do ICMS. Vide fórmula:

|  |
| --- |
| (Base de Cálculo ICMS DIFAL \* Alíquota interna) - (Base de Cálculo ICMS \* Alíquota Interestadual) |

**ICMS ST NÃO considera ICMS próprio:** Este campo deverá ser habilitado para atender as operações em que o ICMS ST não é calculado considerando a diferença entre o ICMS ST total da operação e o ICMS próprio.

**Soma ICMS ST Valor Contábil:** Habilitando este campo o valor do ICMS ST será somado ao valor contábil do lançamento fiscal.

**Situação da Retenção ICMS S.T:** Marcando este campo, o ICMS ST das operações de Entrada será devido na apuração do imposto, ou seja, o destinatário da mercadoria ficará responsável pelo pagamento do ICMS ST.

**Utiliza MVA Ajustada**: Marcando esta opção, serão feitas as seguintes alterações na tela de Substituição Tributária do Lançamento Fiscal:  
O valor a ser considerado para o campo "Margem (%)" não será mais o valor existente no cadastro de Naturezas Fiscais, mas sim o valor calculado de acordo com a Fórmula da MVA Ajustada:

**MVA Ajustada = { [ (1 + MVA-ST original) x (1 - ALQ inter) / (1 - ALQ intra) ] -1} x 100**

Onde:

**MVA Ajustada**: Percentual, com duas casas decimais, correspondente à margem de valor agregado a ser utilizada para apuração da base de cálculo relativa à substituição tributária na operação interestadual. Este será o novo valor da MVA do lançamento fiscal.

**MVA-ST Original:** Coeficiente, com quatro casas decimais, correspondente à Margem de Valor Agregado. Esta é a MVA original, existente no cadastro de naturezas de Operação;

**ALQ Inter:** Coeficiente correspondente à alíquota interestadual aplicável à operação. Esta é a alíquota própria (interestadual). Caso o parâmetro "Busca alíquota da operação própria no Estado" esteja marcado, é utilizada a alíquota existente no cadastro de Estados.

**ALQ Intra:** Coeficiente correspondente à alíquota prevista neste Estado para as operações subsequentes alcançadas pela substituição tributária. Esta é a "Aliq. ST/DA" existente no cadastro de Naturezas de Operação.   
Além da "Base Tributada de ST", que irá considerar o novo MVA, o restante do cálculo do ICMS-ST não será alterado.

***Observações:***Será criada uma nova função no TOTVS Gestão de Estoque, Compra e Faturamento para o cálculo da MVA Ajustada, exemplo:

Aquisição de produto por contribuinte mineiro, remetidos por fornecedor estabelecido no estado de São Paulo.

Marcando a opção  "Utiliza por Produto" será considerado no cálculo a alíquota conforme anexo Dados Fiscais por UF do Produto, os campos Alíquota Interna de ICMS e Margem S.T. (%). Se Marcar "Utilizar por Natureza" será considerado a alíquota ST e Margem de Lucro ICMS S.T. (%)  do cadastro de Natureza.

 ***MVA-ST: 34,87%***

Alíquota interestadual (ALQ Inter) = 12%  
Alíquota Interna (ALQ Intra) = 25%  
A (1  MVA-ST original)  
A (1  0,3487)  
A 1,3487  
B (1  ALQ Inter) / (1  ALQ Intra)  
B (1  0,12) / (1  0,25)  
B 0,88  0,75  
B 1,1733

***MVA Ajustada***

((A  B)  1)  100  
((1,3487  1,1733)  1 )  100  
58,24

**ICMS S.T. Considera Redução no Cálculo do ICMS Próprio:**

Este parâmetro deve ser habilitado para que o cálculo do ICMS S.T. atenda as regras de comercialização de produtos da cesta básica constantes no RICMS-MG. A partir da 12.1.27, a alíquota utilizada será referente a porcentagem informada no campo "Alíquota Redução ICMS Próprio".

**Alíquota Redução ICMS Próprio:**

Campo para informar a alíquota utilizada no cálculo do valor do ICMS S.T. caso o parâmetro "ICMS S.T. Considera Redução no Cálculo do ICMS Próprio" esteja habilitado

* **Cálculo com o parâmetro desabilitado**

ICMS Normal = (Quantidade \* Preço) \* Alíquota Normal  
ICMSST = (((Quantidade \* Preço) + Margem de lucro) - Redução Base Cálculo) \* Alíquota ST  
ICMSST a pagar = ICMSST - ICMS Normal  
Exemplo para um produto de quantidade 1, valor R$100,00, margem de lucro de 25% , redução de base de cálculo de 40%, alíquota interna de 12% e alíquota ST de 18%  
ICMS Normal = (100,00\*1) \* 12% /  R$12,00 de ICMS  
ICMSST = (((100,00\*1) + 25,00) - 50,00) \* 18% / R$13,50 de ICMS ST  
ICMSST a pagar = 13,50 - 12,00 /  R$1,50 de ICMS a Pagar

* **Cálculo com o parâmetro habilitado**

ICMS Normal = (Quantidade \* Preço) \* Alíquota Normal (permanece inalterado)  
ICMSST = (((Quantidade \* Preço) + Margem de lucro) - Redução Base Cálculo) \* Alíquota ST (permanece inalterado)  
ICMSST a pagar = ICMSST - (((Quantidade \* Preço) - Redução Base Cálculo) \* Alíquota informada no campo Redução do ICMS Próprio)  
Exemplo para um produto de quantidade 1, valor R$100,00, margem de lucro de 25% , redução de base de cálculo de 40%, alíquota interna de 12% e alíquota ST de 18%  
ICMS Normal = (100,00\*1) \* 12% |  R$12,00 de ICMS (permanece inalterado)  
ICMSST = (((100,00\*1) + 25,00) - 50,00) \* 18% | R$13,50 de ICMS ST (permanece inalterado)  
ICMSST a pagar = 13,50 - (((100,00\*1) - 40,00) \* 18%  |  13,50 - 10,80  | R$2,70 de ICMSST a pagar

**Utiliza B.C\ST com ICMS por Dentro:** Quando o valor do ICMS ST considerar o ICMS por dentro.

BaseICMSST = (BaseICMS-ValICMS proprio)/1-(AlqICMSST+AlqFECPST)

**Exemplo:**BaseICMS = 1000                     ValICMSProprio = 40,00              AlqICMSST = 18%            AlqFECPST = 2%

X = R$1000,00 - ICMS Próprio(4%) + 20%(18% Alíquota ICMS ST + 2% FECPST) X

X= R$960,00 + 20%(18% Alíquota ICMS ST + 2% FECPST) X

X – 20%X = R$ 960,00

(1 – 0,20)X = R$ 960,00

0.80X= R$ 960,00

X= R$ 960,00 / 0.80

X= R$ 1.200 (vr. Base Calculo ICMS ST)

**Operação com FCP ST:**Habilitado esta opção, o sistema realizará o calculo do valor do FECP ST/Difal.  Para Regra de ICMS parametrizada como Diferencial de Alíquota, o calculo será realizado com a Base ICMS UF Destino e percentual (%) FECP ST/Difal.

Já para Regra de ICMS parametrizada como Substituição Tributária, o cálculo será realizado com a Base ICMS ST e percentual (%) FECP ST/Difal. Neste caso, se a opção "Operação com FCP ST" estiver marcado, o calculo da alíquota de ST será:

Alíquota ICMSST (Cadastro da Natureza) + Percentual FECP (Cadastro Produto | Dados Fiscais por UF)

**%ICMS UF Destinatário:** Informe o % do ICMS  para o cálculo da partilha do tributo entre Estados.

**[Difal utiliza Alíquota Interestadual para Natureza de Entrada:](https://tdn.totvs.com/pages/viewpage.action?pageId=629744634)**Habilita essa opção para utilizar a alíquota interestadual da CFOP e não da alíquota que está no movimento no cálculo do DIFAL. OBS: Este campo deve ser utilizado somente para CFOP's de entrada.

4Outros DadosOutros Dados

**Operação Complementar:** Indique neste campo se a operação é complementar de ICMS ou de ICMS ST. **Redução NÃO AFETA** Indique os campos que o fator de redução do ICMS não afeta

* **Frete:** Habilitando este campo a redução da base de cálculo não afetará o valor do Frete.
* **IPI:** Habilitando este campo a redução da base de cálculo não afetará o valor do IPI.

**Soma ICMS ST Valor Contábil:** Habilitando este campo o valor do ICMS ST será somado ao valor contábil do lançamento fiscal.

**Diferencial de alíquota:** Habilitando este campo o sistema irá utilizar tanto para o cálculo do ICMS interno quanto para o ICMS interestadual o valor da base cheia, ou seja, antes da Redução da base de cálculo.

**Controla fechamento valores ICMS/ICMS ST:** Marque este campo se para esta Natureza de Operação será feito o Fechamento das colunas de ICMS e/ou ICMS ST com o valor contábil, utilizando campos complementares no lançamento.

**Tributação ICMS SEM Valor Contábil:** Habilitando este campo o sistema não irá lançar o valor contábil nos lançamentos fiscais.

**Alíquota Fixa Diferencial de Alíquota:** Habilitando este campo o sistema irá calcular o valor do Diferencial de Alíquota aplicando a alíquota interna (campo Alíq. ST/Interna DA) sobre a base do diferencial. Este campo deve ser utilizado, por exemplo, para operações interestaduais onde a alíquota é fixada independente da alíquota interna e interestadual.

**Lança Valor Despesa Condicional:** Indique se o valor da despesa condicional será lançado no campo de: Outros Isento ou não tributados.

Mais Informações

* [Cópia de Regra de ICMS](http://tdn.totvs.com/display/LRM/Copiar+Regra+de+ICMS)
