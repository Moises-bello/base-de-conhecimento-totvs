---
content_hash: 366652bee76f0e826674e8862ffd0d990f3ce9ed86aba95a206582268ac740ad
fetched_at: '2026-06-29T00:09:19.611995+00:00'
page_id: '422545623'
product: rm
source: tdn-rm
title: SPED Fiscal - Bloco K
type: documentation
url: https://tdn.totvs.com/display/LRM/SPED+Fiscal+-+Bloco+K
version: 18
---

#f5f5f5#363636SPED Fiscal - Bloco K

Este bloco se destina a prestar informações mensais da produção e respectivo consumo de insumos, bem como do estoque escriturado, relativos aos estabelecimentos industriais ou a eles equiparados pela legislação federal e pelos atacadistas, podendo, a critério do Fisco, ser exigido de estabelecimento de contribuintes de outros setores (conforme § 4ºdo art. 63 do Convênio s/número, de 1970). As informações deste bloco são obrigatórias a partir de Janeiro de 2016.

BLOCOKleftK010K010

**Registro K010 - Informação sobre o tipo de leiaute**

Este registro indica o tipo de leiaute que o contribuinte adotou na informação do Bloco K

* Indicador de tipo de leiaute adotado:  
  0 – Leiaute simplificado  
  1 - Leiaute completo  
  2 – Leiaute restrito aos saldos de estoque

Observação

Este registro será gerado apenas para ano referência maior que 2023.

Estrutura do Tipo de leiaute

0 - Estrutura do Leiaute simplificado

1 - Leiaute completo

2 – Leiaute restrito aos saldos de estoque

K200K200

**Registro K200 - Estoque Escriturado**

Este registro trata as informações referentes ao Estoque Escriturado.   
Para que as informações sejam retornadas corretamente é necessário revisar o cadastro de Produtos do TOTVS Gestão de Estoque, Compras e Faturamento, informando para cada produto através do caminho Cadastros | Produtos | Anexos | Dados Fiscais do Produto:  
   
**•  Situação da Mercadoria, informar uma das situações que são consideradas para geração do SPED:**  
    01 – Mercadoria para revenda;  
    02 – Matéria-Prima;  
    03 – Produtos em Elaboração;  
    04 – Produto Acabado;  
    08 – Embalagem;  
    09 – Subproduto    
    10 - Produto Intermediário e   
    15 – Outros Insumos.  
   
**• Produto exige inventário fiscal, marcar essa opção na aba Tributação. As informações enviadas para o serviço do SPED Fiscal são:**   
    Código da Coligada  
    Código da Filial  
    Identificador do Produto  
    Quantidade do Produto  
   
**• Indicador do Tipo de Estoque:**  
    Preenchido com valor 0 (zero): para estoque próprio.  
    Preenchido com valor 1:  para estoque de propriedade do informante e em posse de terceiros.  
    Preenchido com valor 2: para estoque de propriedade de terceiros e em posse do informante.  
   
**• Coligada do Cliente/Fornecedor: enviado somente quando Indicador do Tipo de Estoque for 1 ou 2.**

**• Código do Cliente/Fornecedor: enviado somente quando Indicador do Tipo de Estoque for 1 ou 2.**

K210K210

**Registro K210 – Desmontagem Mercadorias: Item de Origem**

O registro K210 trata de informações sobre as mercadorias, que serão destinadas ao desmonte, informando a data da retirada do estoque e a quantidade.  A desmontagem de mercadorias deve ser dos tipos:  00 – Mercadoria para revenda 01 – Matéria-Prima 02 – Embalagem 03 – Produtos em Processo 04 – Produto Acabado 05 – Subproduto  10 – Outros Insumos No TOTVS Gestão de Estoque, Compras e Faturamento são realizadas as movimentações relativas a esse registro, podendo utilizar o mesmo movimento de baixa do TOTVS Planejamento e Controle da Produção.

K215K215

**Desmontagem Mercadorias: Item de Destino**

Esse registro trata de informações sobre as mercadorias, que serão destinadas a entrada do item de destino. Os tipos da mercadoria deve ser: 00 – Mercadoria para revenda 01 – Matéria-Prima 02 – Embalagem 03 – Produtos em Processo 04 – Produto Acabado 05 – Subproduto  10 – Outros Insumos   
Este registro é obrigatório caso exista o registro-pai K210. Nesse caso, a saída do estoque do item de origem e a entrada em estoque do item de destino têm de ocorrer no período de apuração do Registro K100. No TOTVS Gestão de Estoque, Compras e Faturamento são realizadas as movimentações relativas a esse registro, sendo necessário um movimento de entrada com o motivo de cópia referência 29 - Desmontagem de Mercadorias.

K230K230

**Itens Produzidos**

As informações necessárias para geração dos registro K230 serão extraídas das Ordens de Produção geradas através do TOTVS Planejamento e Controle de Produção e das movimentações parametrizadas para trabalhar com Processo Produtivo Simples no TOTVS Gestão de Estoque, Compras e Faturamento.    
O Registro K230 conterá as informações da produção acabada de produto em processo (tipo item 03 do registro 0200)  e produto acabado (tipo item 04 do registro 0200), onde para o Processo Produtivo Simples é considerada que tenha ao menos a movimentação da Baixa da Matéria Prima ou a Entrada do Produto acabado.  
A ordem de produção gerada através do TOTVS Planejamento e Controle de Produção  deverá ser iniciada com os devidos apontamentos de consumo de matéria prima.  Caso a ordem de produção não seja concluída no período informado, ao  gerar o Sped Fiscal  a mesma aparecerá com quantidade apontada. Após a conclusão, a OP será novamente listada no arquivo do Sped Fiscal com o restante dos apontamentos.

K235K235

Este registro tem o objetivo de informar o consumo de mercadoria no processo produtivo, vinculado ao produto resultante informado no Registro K230 – Itens Produzidos.  
O tipo do componente/insumo que será apresentado neste bloco deve ser: 00 – Mercadoria para revenda; 01 – Matéria-Prima;  02 – Embalagem; 03 – Produtos em Processo; 04 – Produto Acabado; 05– Subproduto ou 10 – Outros Insumos.

**Produtos Substitutos**

A finalidade desta melhoria no sistema TOTVS Gestão de Estoque Compras e Faturamento é registrar o código do produto original quando utilizar a opção de troca do item de movimento por um "Produto Substituto/Similar", possibilitando a rastreabilidade entre os itens envolvidos no preenchimento de informação na geração do Ato COTEPE – Bloco K – Controle da Produção e Estoque (Registro K235 – Insumos Consumidos).  
A rastreabilidade do produto original está diretamente ligado ao Processo "Produtivo Simples" e "Industrialização por Terceiros", para os quais, na geração do Ato COTEPE – Bloco K exige-se que seja informado código do item componente/insumo que estava previsto para ser consumido no Registro 0210 e que foi substituído.  
 Além do prévio registro de produtos substitutos/similares no cadastro do produto, para trocar um produto no item de movimento por um produto substituto/similar, é necessário que o tipo de movimento esteja parametrizado na etapa "Estoque – Estoque 3/3" na opção "Trata Produto Substituto/Similar" item "Trata Produto" com um dos seguintes valores:

* Substituto;
* Similar,
* Ambos.

 É de inteira responsabilidade do usuário incluir, no movimento de remessa para industrialização (2.2.XX) ou no movimento de Baixa de Matéria Prima do Processo Produtivo Simples (2.2.XX) o produto original e, somente após esse passo, processar através do botão "Produto Substituto/Similar" e confirmar a substituição do produto para que a rastreabilidade entre o produto substituto e o substituído (produto original) seja registrada.

K250K250

**Industrialização efetuada por terceiros– Itens Produzidos**

O Registro K250 tem o objetivo de informar os produtos que foram industrializados por terceiros e sua quantidade que, por sua vez, conterá as informações relativas aos movimentos que correspondem aos produtos industrializados por terceiros que estão entrando no estoque da empresa e as informações relativas aos movimentos que correspondem ao retorno simbólico de todas as matérias-primas consumidas pelos terceiros na industrialização dos produtos informados nos movimentos. Assim, será feito um relacionamento entre o produto industrializado por terceiros (K250) e as matérias-primas utilizadas nessa produção (K255).  
Os clientes deverão ter as movimentações de Controle de Estoque de/com Terceiros cujo tipo de movimento esteja parametrizado na guia Ambiente, parâmetros, tipo de movimento, Etapa Estoque - Estoque 2/3: Controle Saldo Terceiros: Tipo Controle Terceiros como 3 (Industrialização por Terceiros – 1 NF) ou com 4 (Industrialização por Terceiros – 2 NF) ou com 10 (Industrialização Outra Filial – Outra Mercadoria) corretamente. Processos criados pelo próprio cliente para controle do saldo de/com terceiros não serão contemplados.

K255K255

**Industrialização em Terceiros - Insumos Consumidos**

O Registro K255 tem o objetivo de informar a quantidade de consumo do insumo que foi remetido para ser industrializado em terceiro.  
Os clientes deverão ter as movimentações de Controle de Estoque de/com Terceiros parametrizados corretamente. Processos criados pelo próprio cliente para controle do saldo de/com terceiros não serão contemplados.  
De acordo com resposta à consulta realizada com a Equipe SPED da Receita Federal, quando a empresa produz um determinado produto e terceiriza parte da produção deste mesmo produto, a empresa deverá registrar a estrutura relativa a sua produção própria. Sendo assim, as estruturas produzidas em terceiros deverão ser cadastradas utilizando-se o próprio cadastro de estruturas do TOTVS Planejamento e Controle da Produção ou cadastro de estruturas e componentes do TOTVS Gestão de Estoque, Compras e Faturamento.

Definir tipo de movimento para lançamento das entradas de industrialização onde na guia Ambiente, parâmetros, tipo de movimento, Etapa Estoque - Estoque 2/3: Controle Saldo Terceiros: Tipo Controle Terceiros seja preenchida com 3 (Industrialização por Terceiros – 1 NF) ou com 4 (Industrialização por Terceiros – 2 NF) ou com 9 (Industrialização Outra Filial – Mesma Mercadoria) ou com 10 (Industrialização Outra Filial – Outra Mercadoria).  
Ao criar o movimento, será necessário primeiro informar a matéria-prima original da estrutura de produção, para depois fazer a substituição da mesma pela matéria-prima previamente cadastrada como possível substituta. Assim o sistema terá condições de armazenar as duas informações para, posteriormente, utilizá-las corretamente na geração do Registro K255.

K260K260

**Reprocessamento de Produto/Insumo**

Esse registro informa o produto que será reprocessado ou que foi reprocessado no período de apuração do registro K100, através de ordem de produção.

K265K265

**Mercadorias Consumidas e/ou Retornadas**

Nesse registro é informado o consumo de mercadoria e/ou o retorno de mercadoria ao estoque, ocorrido no reprocessamento de produto/insumo informado no Registro K260 – Reprocessamento de Produto/Insumo – Produtos Acabados/Insumos.   
Para que o sistema registre os blocos K260 e K265 no TOTVS Planejamento e Controle da Produção a ordem deve ter o campo Reprocessamento marcado e está concluída dentro do período informado no SPED.

K280K280

**Correção de Apontamento**

Este registro tem o objetivo de declarar a correção de apontamento de estoque escriturado no Registro K200, de período de apuração anterior e se destina a atender a dificuldade relatada pelas empresas nas quais, em decorrência da natureza física dos produtos, há a possibilidade de ocorrer diferenças no estoque, como, por exemplo, produtos a granel, líquidos etc., que alteram sua quantidade e não podem ser medidos com precisão.  
A correção de apontamento tem que ocorrer, obrigatoriamente, entre o levantamento de 02 inventários, uma vez que, com a contagem do estoque se terá conhecimento de uma eventual necessidade de correção de apontamento. Uma correção de um período de apuração poderá influenciar estoques escriturados de períodos posteriores, até o período imediatamente anterior ao período de apuração em que se está fazendo a correção, uma vez que o estoque final de um período de apuração é o estoque inicial do período de apuração seguinte.  
Com relação a quantidade, essas devem ser expressas, obrigatoriamente, na unidade de medida de controle de estoque e os produtos utilizados deve ter como Situação da Mercadoria umas das seguintes opções:

* 01:Mercadoria para Revenda;
* 02:Matéria-Prima;
* 03:Produto em Processo;
* 04:Produto Acabado;
* 08:Embalagem;
* 09:Subproduto;
* 10:Produto Intermediário;
* 15:Outros insumos.

 Podem existir tipos de movimento que estejam parametrizados para afetar ao mesmo tempo o Saldo Atual e o Saldo com Terceiros e, nestes casos, deverá ser gerado para o mesmo item e na mesma data, um Registro K280 para cada saldo que está sendo afetado. E para a geração do Registro K280 o sistema irá considerar tanto a "Data para Registro K280" como a "Data do Movimento".  
Assim, após terem sido gravadas todas as movimentações de correção de estoque escriturado do mês, o TOTVS Gestão Fiscal estará apto a gerar, no SPED Fiscal, os Registros K 280 relativos a estas movimentações.

K280K290, K291 e K292

**Produção conjunta**

Registros gerados com as informações provenientes do TOTVS Gestão de Estoque e Compras.  
  
A Produção Conjunta é reportada no SPED Fiscal por meio dos Bloco K290 (Ordem de Produção), K292 (Baixa/Consumo realizado) e K291 (Produção Gerada).  
A geração desse Bloco é feita exclusivamente quando existe a movimentação de Baixa/Consumo, ou seja, se existir movimentação somente de Ordem de Produção e/ou Produção Gerada, os dados não são gerados no arquivo do SPED Fiscal.

Documento técnico segue no link: <http://tdn.totvs.com/pages/releaseview.action?pageId=451254002>

#f5f5f5#363636VídeosVideosleftTOTVS Responde

648432

Material apresentado: <https://espacolegislacao.totvs.com/wp-content/uploads/2022/10/TOTVS-Responde-Bloco-K.pdf>

K230/K235

648432
