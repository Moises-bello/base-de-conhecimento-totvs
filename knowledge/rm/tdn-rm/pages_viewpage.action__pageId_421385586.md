---
content_hash: f5fb46039f7e8343c5c69ce6b9ffa521f8072383aba6c69c93c4c2910635e084
fetched_at: '2026-06-29T00:09:16.859108+00:00'
page_id: '421385586'
product: rm
source: tdn-rm
title: Versão de Estudo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385586
version: 7
---

---

Na criação de um novo estudo devem ser informados os dados do empreendimento. Para que as demais abas do estudo sejam habilitadas devem ser informados o Nome e a Situação para salvar a versão de estudo.

Na Aba "Parâmetros do Estudo" se encontram as informações de análise, e pode ser considerada a parte principal do Estudo.

Esta aba possui uma subdivisão de pastas para cadastro de dados além de dois botões de Função que são: **Calcular:** que só deve ser acionado depois de lançados todos os dados da versão de análise, assim gerando os indicadores da análise de viabilidade, bem como os lançamentos que são a projeção do Fluxo de caixa VP e VF.

**Relatórios:** para geração de relatórios do estudo.

Como Sub-abas da aba "Parâmetros do Estudo" temos:

- Estudo;

- Empreendimento;

- Vendas;

- Obras;

- Impostos;

- Financiamento,

- Despesas Periódicas.

Cada Sub-aba registra um conjunto específico de dados necessários para a geração da análise

Estudo

**Valor Presente:** é o período para o qual serão trazidos os valores do fluxo de caixa projetado

**Valor Base para o Estudo:** é a data inicial do projeto, o período zero

**Valor presente:** taxa de capitalização do dinheiro no tempo (valor presente para calcular o fluxo de caixa, pois R$ 1.000,00 agora não valerá a mesma coisa daqui a um ano, por exemplo)

**Credores:** corresponde ao custo de oportunidade e mostra a melhor taxa de remuneração da aplicação do capital em outro investimento.  A taxa será aplicada na geração dos lançamentos de Fluxo de caixa na obtenção dos "Resultados sem Financiamento"

**Devedores:** corresponde ao custo de oportunidade e mostra a taxa de cobrada pelo mercado para captação de empréstimo.  A taxa será aplicada na geração dos lançamentos de Fluxo de caixa na obtenção dos "Resultados sem Financiamento"

**Valor Presente:** (VP ou PV) será o percentual aplicado sobre os lançamentos financeiros para trazer a valor presente os valores de receita e despesa do fluxo de caixa. Este percentual pode ou não ser o mesmo que o VF e geralmente segue o índice da inflação além dos percentuais estimados de valorização do segmento

**Valor Futuro:** (VF ou FV) este percentual será utilizado para valorizar o dinheiro no tempo e saber qual será o valor de uma parcela daqui um ano. Este percentual tem impacto direto nos lançamentos de fluxo de caixa bem como na estimativa de retorno do Indicadores financeiros

**Período de Início da Cobrança de Juros:** será o período a partir do qual serão cobrados os juros. Terá impacto direto nos lançamentos de fluxo de caixa assim como os demais dados de parâmetros vistos até o momento

**Incorridos:** é a taxa de juros aplicada sobre os valores anteriores ao período de início da cobrança de juros

**Tarifas Bancárias (% de receita):** percentual estimado de despesas gastas com tarifas bancárias.

**Taxa de adm. de carteira (% de receita):** percentual estimado de taxa de administração de carteira

**Taxa de Gerenciamento (% da Obra):** percentual estimado de despesas com o Gerenciamento da Obra

**Gestão Imobiliária (% VGV):** percentual estimado de despesas com a gestão imobiliária. Nenhum dos campos de despesas gerais é obrigatório, no entanto, uma vez informados, seus correspondentes devem ser lançados também como despesas periódicas a fim de gerarem os  lançamentos de Fluxo de caixa, em seus respectivos períodos de gasto.

**Despesas Comerciais** Assim como as despesas gerais, estes são campos destinados a informar percentuais estimados com os gastos comerciais como  comissão, propaganda, decoração e etc.

Nenhum dos campos de despesas comerciais é obrigatório, no entanto, uma vez informados, seus correspondentes devem ser lançados também como despesas periódicas a fim de gerarem os  lançamentos de Fluxo de caixa, em seus respectivos períodos de gasto.

Empreendimento

**Área do terreno:** campo informado pelo usuário correspondente a metragem total do terreno.

**Valor /m2:** campo calculado pelo sistema (Valor Total \ Área do terreno) ou pode ser informado pelo usuário.

**Valor Total:** campo calculado pelo sistema (Área do terreno \* Valor m2 ) ou pode ser informado pelo usuário.

C.A.=  corresponde ao coeficiente de aproveitamento ou também conhecido como taxa de ocupação (TO). O Coeficiente de Aproveitamento é um número que, multiplicado pela área do lote, indica a quantidade máxima de metros quadrados que podem ser construídos em um lote, somando-se as áreas de todos os pavimentos.

**C.A Mínimo:** campo informado pelo usuário, corresponde ao coeficiente de aproveitamento mínimo da área. **C.A. Máximo:** campo informado pelo usuário corresponde, ao coeficiente de aproveitamento máximo da área.  
As taxas de C.A. são determinadas pela legislação urbanística municipal

**Área Computável:** campo calculado pelo sistema (C.A. Maximo\* Área do terreno)

**Definição da área construída:** A área construída pode ser definida de três formas:

"Definir Manualmente": onde o sistema habilitará o campo de área construída para ser digitado pelo usuário. "Utilizar Fator AP/ AC \*": ao optar por esta forma de cálculo o sistema trará a área construída automaticamente de acordo com a fórmula estabelecida para o campo no Tipo de Estudo que está sendo utilizado, mas de qualquer forma respeitará a valor informado no campo de fator AP/AC, que se trata de uma proporção estabelecida em conformidade com a lei de uso e ocupação do solo estabelecidas pelo município e adequação da mesma pela construtora.\*AP: Área privativa e AC: Área construída

"Utilizar configuração dos pavimentos" ao escolher esta opção o sistema fará o calculo de acordo com a fórmula estabelecida no Tipo de Estudo padrão, que basicamente soma todos os pavimentos respeitando o Tipo de Pavimento e sua respectiva Área Equivalente.

A área equivalente de uma construção é uma proporção usada para avaliar a diferença entre área construída  considerada e as áreas que se enquadram na coberta-padrão. (As normas de área equivalente podem ser encontradas na NBR 12721:2006) Exemplo: Subsolo (fator equivalente =0,71) 1 pavimento do tipo Subsolo com 10 m2 Corresponde a um área construída de 7,10 m2 (0,71\*10) Somando a área construída de todos os pavimentos teremos a área total construída. Vale ressaltar que o total da área construída não pode ultrapassar a "Área Computável"

**Fator AP/AC:** campo informado pelo usuário se trata de uma proporção estabelecida em conformidade com a lei de uso e ocupação do solo, estabelecidas pelo município e adequação da mesma pela construtora. \*AP: Área privativa e AC: Área construída

**Área Privativa:** campo calculado pelo sistema, sendo a soma total da área das unidades;

**Área Construída:** resultado da opção escolhida no campo "Definição da área construída" Podendo ser informado manualmente ou calculado pelas formulas acima descritas.

**Custo M2 Privativo:** campo calculado pelo sistema (Área Construída \* AreaConstruida) /AreaPrivativa)

**Custo M2 Construído:** campo calculado por fórmula (Custo M2 Privativo \* Área Privativa) / Área Construída)

Os campos de custo do m2 são calculados de acordo com o campo que for informado primeiro.

**Taxa de administração:** campo informado pelo usuário;

**Custo da Obra:** campo calculado pelo sistema; (Área Construída \* Custo M2 Construído)

**Custo total da Obra:** campo calculado pelo sistema. (Custo da Obra+( Custo da Obra \* Taxa de administração / 100))

**VGV (valor geral de venda)** Área onde os campos serão calculados, e seus resultados são baseados nos dados indicados na grid de UNIDADES e PERMUTA

A partir da versão 12.1.28, nas configurações do tipo de estudo, o sistema apresentará o parâmetro de Represamento, cujo Percentual definido será aplicado sobre o Valor VGV no período de uma curva especifica.

**Total:** soma Preço Total de todas as unidades;

**Permutas:** soma do preço das unidades, percentual ou valor referente a permutas;

**Vendável:** é o VGV Total subtraindo o total de Permuta;

**Taxa de reajuste de custo:** Valor da taxa de reajuste que será utilizada no cálculo

**Tipo:** Periodicidade do reajuste se é ao mensal (a.m.) ou anual (a.a.)

**Mês de início:** Mês de início do reajuste

**Cálculo de Reajuste de Custo:** Tipo de cálculo realizado no reajuste se é juros compostos ou saldo da obra

**Unidades (sub-Aba)** Nesta área serão informados os dados das unidades que serão construídas.

**Tipo de Unidade:** o usuário poderá escolher entre os tipos já estabelecidos pelo sistema;

**Quantidade:** qtd de unidades que será escolhidas para o respectivo tipo de unidade;

**Permutas:** este campo pode ser calculado ou informado pelo usuário. Só será calculado pelo sistema se o campo "Rateio proporcional as unidades" estiver marcado na aba de "permutas";

**Área Privativa:** campo informado pelo usuário que corresponde a qtd de metros2 que a unidade ocupará;

**Valor /M2:** campo informado pelo usuário que corresponde ao valor de venda do m2;

**Preço Unitário:** campo calculado pelo sistema (Área Privativa\* Valor /M2)

**Preço Total:** campo calculado pelo sistema (Quantidade\* Preço Total)

**Preço Total das Permutas:** campo calculado pelo sistema conforme dados de permuta;

**Área Privativa Total:** campo calculado pelo sistema (Quantidade\* Área Privativa)

**Área permutas Total:** campo calculado pelo sistema conforme dados de permuta;

**Percentual de Permutas:** campo calculado pelo sistema conforme dados de permuta;

**Preço M2 médio:** campo sem calculo

**Total por Unidade:** campo sem calculo

**% VGV Total:** campo sem calculo

**Custo M2:** campo sem calculo

**Custo Total:** campo calculado por fórmula (Custo M2 \* Área Privativa Total)

**Área Construída (sub-Aba**

**Tipo de Pavimento:** cadastro pré-fixado onde o usuário poderá escolher entre os tipos já estabelecidos pelo sistema, com seus respectivos fatores equivalentes (FE);

**Quantidade:** QTD de pavimentos correspondente ao tipo selecionado;

**Área do Pavimento:** total da área do pavimento correspondente;

**Área Equivalente:** campo calculado pelo sistema (Área do Pavimento\* fator de equivalência)\* Quantidade

**Permuta (sub-Aba)** A permuta é uma prática comum quando o proprietário de um terreno aceita receber como pagamento (parcial ou total) unidades. A permuta pode ser parte com unidades e parte em valor, no empreendimento que está sendo analisado ou em outro.

**Compra do Terreno:** campo informado pelo usuário que corresponde ao valor cobrado pelo proprietário; Se este campo for utilizado então o valor da compra do terreno também deve ser informada como despesa periódica, para que quando os lançamentos forem calculados, o sistema saber a forma como o valor será distribuído (se é sinal ou mensal, o valor, quantidade de parcelas, início do período). É possível nas despesas periódicas criar mais de um registro do mesmo tipo, desta forma combinando valores mensais com o sinal, por exemplo.

**Física:** campo informado pelo usuário que corresponde ao percentual que será permutado em unidades. Exemplo: se informar 50, significa que metade das unidades serão permutadas

**Local:** indicando este campo, o usuário está informando que o valor a ser reservado será no empreendimento analisado;

**Rateio proporcional as unidades:** o sistema fará a correspondência percentual de todas as unidades do empreendimento reservando (física); Exemplo: se informa 50% no campo "Física" significa que de 10 unidades do empreendimento 5 estarão reservados para a permuta e não poderão ser comercializados.

**Externa:** o valor de permuta deverá ser pago com recurso de outro empreendimento;

**Parar ao atingir o valor (nenhum/ VP/ Nominal):** A permuta deve para ser chegar no valor presente ou no valor nominal, no entanto esta trava não está em vigor.

**Participação do Proprietário** Quando o proprietário participa das despesas tais valores serão deduzidos no fluxo de caixa;

**Sobre % de comissão:** percentual das despesas de comissão que o proprietário custeará;

**Sobre % de propaganda:** percentual das despesas de propaganda que o proprietário custeará;

**Sobre % dos impostos:** percentual das despesas com impostos que o proprietário custeará;

**Totais** Todos os campos da área de totais são calculados automaticamente.

**Total:** quantidade total de unidades que serão construídas;

**Permutas:** quantidade de unidades que serão permutadas;

**Vendável:** (Total- Permutas)

**Área privativa Total:** soma das áreas privativas das unidades;

**Área privativa Permutas:** soma das áreas permutas das unidades;

**Área privativa Vendável:** (Área privativa Total- Área privativa Permutas);

Vendas

**Taxas**

**Taxa de reajuste:** taxa de ajuste do plano de financiamento. Esta taxa será aplicada sobre os valores da velocidade de vendas e da tabela de preço;

**Tipo:** incidência da taxa de reajuste, se ao mês (A.M) ou ao ano (A.A)

**Mês de Inicio:** a partir de que período a taxa de reajuste deve ser aplicado nos planos de financiamento;

**Taxa de Juros TP:** taxa de juros da para calculo do plano de  financiamento utilizado o modelo Tabela Price;

Modo de definição da unidade (Utilizar quantidade de unidades por período/ Utilizar percentual de unidades no período)

A partir dos dados dispostos nos grids de "Perfil de vendas", "velocidade de vendas" e "Tabela de Vendas", o sistem será capaz de montar a previsão de quantas unidades serão vendidas por período e a partir de tal venda como serão suas receitas: Exemplo: Num total de 10 unidades (apenas do tipo 1 quarto) Cada unidade vale R$ 1.000.000,00 Informo que no Perfil de Lançamento teremos a venda de 50% das unidades (período de 0 a 2correspondendo a 2 meses) Com o seguinte plano de financiamento: 50% de entrada e 50% em 10 vezes;

Assim teremos o seguinte cenário Período 0: 5 unidade no valor de R$ 1.000.000,00 cada num total de 5.000.000,00 Se a tabela fosse padrão teríamos o seguinte plano de receita: R$ 2.500.000,00 de entrada e mais dez períodos com receita de R$ 250.000,00 No período 1º mesmo calculo, mas se aplicado o calculo de TP (tabela price os valores distribuídos devem seguir o método de calculo deste modelo. Assim para calcular os lançamentos de fluxo de caixa o sistema pode considerar a quantidade de unidades vendidas ou o percentual das unidades vendidas para o calculo Price.

**Distribuição das Parcelas com término fixo (Distribuir entre parcelas restantes/ acrescentar na primeira parcela):** para cálculo no modelo Price, com planos onde teremos o termino fixo  ("período final") as taxas devem ser distribuídas na primeira parcela ou nas parcelas restantes, a partir da data de inicio do calculo;

**Tipo:** o deve ser informado se a Aplicação da taxa de juros TP informada será ao mês ou ao ano;

**Perfil de Vendas** No perfil de vendas é estabelecido quais são as expectativas de vendas nos períodos estabelecidos. Exemplo: A Incorporadora pretende vender 20% das unidades no lançamento do Empreendimento. As demais unidades serão vendidas nos próximos 6 meses. Será no Perfil de Venda que estas características serão inseridas. Cada perfil pode ser associado a várias tabelas de "Velocidade de Venda".

**Código:** o usuário deve indica o código do perfil;

**Descrição:** o usuário deve indicar a descrição apropriada. Ex: Fase de Lançamento;

**% Velocidade:** campo calculado Soma ("% Total da velocidade" da velocidade de venda ao perfil atrelado)

**% da Tabela de Vendas:** campo calculado Soma ("% sobre o total" da tabela de venda ao perfil associado)

**% Acumulado da Velocidade:** campo calculado pelo sistema (identificar modelo de calculo)

**% Peso do Perfil em unidades:** campo calculado pelo sistema (identificar modelo de calculo)

Percentual de Receita: campo informado pelo usuário e corresponde ao percentual da receita que deve ser repassado (securitizado) para instituição financeira.

**Taxa de Desconto:** valor cobrado pela instituição financeira para adiantar o valor vendido da divida.

**Período de Crédito:** em que período terá a entrada da receita (com desconto da taxa);

**Inicio de Securitização:** campo informado pelo usuário, e indica a partir de quando a dívida será repassada. Geralmente ocorre ao termino da construção onde o cliente tem sua dívida "vendida" para uma instituição financeira e deve ter o restante do imóvel financiado por esta instituição, mas esta prática varia de acordo com a incorporadora;

**Crédito do Repasse:** valor calculado pelo sistema. (Total da Receita \* Percentual da receita /100)- taxa de desconto

**Percentual de Repasse:** campo inativo;

**Velocidade de vendas (sub-aba)**

**% quantidade de Unidades:** de acordo com o perfil de venda criado, qual será o percentual de unidades que serão vendidas no período;

**Quantidade de Períodos:** campo informado pelo usuário e indica em quantos períodos o percentual acima definido deve ser vendido;

**Mês:** este campo é preenchido automaticamente pelo sistema de acordo com o período estabelecido como período inicial,  tomando como referência a data base do estudo (Aba parâmetros de estudo/ Estudos/ Datas- "data base do estudo". Exemplo: Data base do estudo= 12/2011 , o período 3 será março de 2012

**Período Inicial:** campo informado pelo usuário que será utilizado como referência de geração das previsões de receitas dos lançamentos do fluxo de caixa.

**Periodicidade:** campo informado pelo usuário (mensal, semestral, etc) Tipo de Unidade: das unidades que compõe o empreendimento, no Perfil de Venda selecionado, na Velocidade de Venda em questão, deve ser identificado qual tipo de unidade terá a característica especificada. Exemplo de Tipo de Unidade: Cobertura ou Apto 3 quartos.

**% Total da Velocidade:** campo calculado (quantidades total de unidade do tipo selecionado \* % quantidade de Unidades da velocidade/100)

**Numero de Unidades:** correspondência numérica em relação ao percentual acima encontrado;

**% relativo:** campo calculado que representa o a correspondência desta velocidade em relação total de todos os perfis e de todas  as velocidades de venda; **Usar preço médio:** campo utilizado no calculo da tabela de venda;

**Tabela de vendas**

**Parcelas:** quantidade de parcelas que serão geradas a partir da venda;

**Periodicidade:** identifica a periodicidade de calculo da parcelas (ex: mensal, bimestral, semestral, etc)

**% sobre o total:** percentual sobre o valor total que será pago no número de parcelas acima definido; **Período de Inicio:** período de inicio do plano de financiamento;

**Período de Inicio Fixo da Serie:** o plano de financiamento terá período fixo.

**Modo de Término da Série (Período Final/ Número de Parcelas):** O término do pagamento das condições de parcelamento pode ser pelo período final ou número de parcelas.

Caso o usuário opte por número de parcelas será calculado um valor baseado no número de parcelas informado na primeira coluna da tabela. Não tem limite de término.

Na opção de período final, a quantidade de parcelas varia de acordo com o período da venda. Vamos imaginar a seguinte situação:  o número de parcelas informado é de 30 parcelas e o período final determinado foi  40, as vendas efetuadas até o período 10 terão 30 parcelas já as vendas posteriores terão um número de parcelas menor de tal forma que o pagamento seja concluído no período 40, para as unidades vendidas no período 20 o número de parcelas será 20, já os vendidos no período 30 terão 10 parcelas. Tem limite de término Informamos ainda se serão cobrados juros sobre o parcelamento e qual o período de início da cobrança dos juros. Na versão atual o modelo de Empreendimentos Imobiliários utiliza a tabela Price para calcular os juros do financiamento, porém outros métodos de financiamento podem ser facilmente implementados.

**Término:** campo calculado pelo sistema conforme número de parcelas, periodicidade, período inicio e as variáveis de período de inicio fixo da serie e modo de termino da serie;

**Juros (T.P):** informar se tal parcelamento terá seu juros calculado no modelo Pice;

**Mês de inicio dos Juros:** e a partir de que mês do parcelamento haverá incidência de juros;

**Repasse:** se parte desta receita terá repasse;

**Financiamento MCMV:** se a venda for do tipo MCMV os lançamentos das parcelas serão de acordo com o andamento da obra

Obras

**Curvas de Obras** Nesta sub aba será adicionada uma nova curva de obra, ou seja, o tempo da obra. Uma obra pode ter mais de uma curva ficando a critério do planejamento , por exemplo cada torre de uma construção pode ter uma curva de obra diferente com períodos diferentes de construção, e até mesmo financiamento de obra diferente. É possível adicionar uma curva já existente (no botão: Adicionar novo registro) ou então criar uma nova curva.

**Curva:** dado informado pelo usuário, onde o cadastro é fixo do sistema; pois existem calculo internos baseados em nos número estabelecidos na curva;

**% sobre o valor Total:** campo informado pelo usuário onde deve ser indicado o quanto esta curva representa no total da obra;

**Valor:** campo calculado pelo sistema;

**Período de Inicio:** qual é o período de inicio da obra; **Mês:** campo calculado pelo sistema, baseado no período de inicio;

**Financiamento:**Na sub aba "Financiamento" são informados os dados relativos à obra, são eles: no quadro Armotização: quantidade de parcelas, carência e incidir juros na carência (checkbox); no quadro Securitização: % da receita, taxa de desconto, período de crédito e inicio da securitização; quadro Condições: **neste quadro informa-se caso haja juros, se será pago todo mês ou apenas quando a obra ficar pronta**; quadro Liberação: **como o banco irá liberar esse dinheiro, ou seja, o banco pode resolver se vai emprestar sem nenhuma condição ou se a empresa deverá seguir algumas restrições impostas pelo banco**.

**Totais** **Percentual:** campo calculado pelo sistema e Soma % sobre o valor Total de todas as curvas indicadas; **Valor:** campo calculado pelo sistema que representa o Valor total da obra; **Inicio da Obra:** período de inicio da obra baseado no inicio de cada curva informada;

Impostos

Na sub aba Impostos são informadas os impostos regulares, tais como PIS/COFINS (sempre alíquota de 3,65), CSSL (alíquota de 1,00 e base de 100,00), ITBI (alíquota de 2,00 e base de calculo da % do terreno 80,00 – total de vendas no período menos as comissões).

A partir da versão 12.1.28, além do ITBI com valor fixo para determinado período, haverá a possibilidade de definir um valor no mês da Venda.  

**Despesas Periódicas** Nesta parte do cadastro serão informadas as periodicidades de algumas despesas existentes durante a execução da obra, tais como: propaganda, comissão, IPTU, compra do terreno, e etc.

**Exemplo: Propaganda – quantidade de parcelas, periodicidade, mês de início, valor, valor total e a unidade.**

**Botão "Calcular":**

Após preencher todas as informações necessárias nas abas descritas acima, deve-se clicar no botão Calcular, desta forma o sistema tratará as informações gerando os indicadores do estudo.  
Assim que "calcular" a Análise de Viabilidade três novas abas serão criadas.

**Lançamentos:** que é o Fluxo de Caixa no Valor Futuro;

**Lançamentos VP:** que é o Fluxo de Caixa trazidos a Valor Presente;

**Indicadores:** que são os indicadores econômicos/ financeiros gerados a partir dos dadas lançados. Todos os indicadores são resultados de formulas financeiras estabelecidos por métodos acadêmicos. Suas fórmulas podem ser consultadas no cadastro do tipo de estudo.

Os resultados obtidos pela análise de viabilidade podem ser gerados em forma de Excel através do botão de .

A partir da versão 12.1.28, estão disponíveis os indicadores: ROI (Retorno sobre Investimento) e Resultado Liquido (%)

Podemos realizar alguns processos com a Versão de Estudo. São eles:

**Duplicar Versão de Estudo:** Neste processo, criamos uma cópia idêntica da Versão de Estudo Selecionada.

Para facilitar o cadastro de Versões do Estudo que se difere em pequenos detalhes, existe o processo de duplicação de versões. Utilizando este processo, a versão que foi selecionada, será duplicada dentro do Estudo de Viabilidade criando uma cópia idêntica.

**Comparar Versões de Estudo:** depois de criar a versão inicial o usuário poderá duplicar a versão, e depois entrar na versão duplicada fazendo as alterações desejadas. Funciona como uma espécie de cenário, onde na primeira versão podem ser simulados os indicadores de um empreendimento com uma torre de 10 aptos de 100 mt2 cada, e numa segunda versão pode ser quase a mesma coisa alterando apenas a metragem das unidades. Fica a critério do usuário.

Importante: depois de feita a alteração na versão do estudo é importante mandar "calcular" novamente para que os dados dos indicadores e lançamentos sejam atualizados.

**Importar Versão de Estudo:** este recurso pode ser utilizado para recuperar dados de uma versão padrão ou como uma espécie de backup de versões que estão sofrendo alterações.

**Exportar Versão de Estudo:** uma vez formado uma versão de estudo com as características padrões do empreendimento a mesma pode ser exportada e utilizada na mesma análise de viabilidade ou em uma nova, para isso basta importar posteriormente a versão.

Como Fazer

---

[Comparar Versão do Estudo](http://tdn.totvs.com/pages/viewpage.action?pageId=421385386&moved=true)
