---
content_hash: 775bc7a04a7d186e60c3f6aa1931d7d10cea3fe3e9f27adb85cfe3700785bcd7
fetched_at: '2026-06-29T00:09:23.136017+00:00'
page_id: '422546052'
product: rm
source: tdn-rm
title: DAPI (Outras Informações)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546052
version: 9
---

A DAPI possui 3 modelos distintos e um deles deverá ser selecionado na tela da rotina para a geração do arquivo texto.  
Para a geração da rotina nos 3 modelos, serão selecionados os [Lançamentos Fiscais](http://tdn.totvs.com/pages/viewpage.action?pageId=427041477) pertencentes à Filial e Período informados na tela da rotina. O sistema estará selecionando somente os [Lançamentos Fiscais](http://tdn.totvs.com/pages/viewpage.action?pageId=427041477) cujo [CFOP](http://tdn.totvs.com/pages/viewpage.action?pageId=431680880) associado é Fiscal, conforme campo Natureza Fiscal, localizado na pasta Outros Dados do Cadastro de Naturezas de Operação. Não serão selecionados Lançamentos Fiscais Estornados ou Cancelados.    
Se o campo "DAPI Consolidada" estiver habilitado, o sistema gera uma única DAPI para todas as filiais com mesma Inscrição Estadual e UF da filial selecionada na tela da rotina. Dessa forma, todos os [Lançamentos Fiscais](http://tdn.totvs.com/pages/viewpage.action?pageId=427041477) e de Outros Débitos e Créditos de todas essas filiais são selecionados na rotina.   
Serão detalhados apenas os campos com alguma particularidade de difícil entendimento.

**Linha 00 - Identificação da DAPI:**Esta linha será gerada para os 3 modelos da rotina. Ela possui informações referentes ao declarante e ao período informado. É importante o correto preenchimento da Inscrição Estadual e do CNAE, existentes no cadastro de filiais. Além disso, os campos na tela da rotina como Regime Recolhimento, CAE / Desmembramento, Data Limite Pagamento e outros devem estar preenchidos corretamente conforme o período selecionado.

**Linha 99 - Total de Linhas:**Trata-se de uma linha totalizadora comum aos 3 modelos da DAPI.

**DAPI - Modelo 1** 

Os campos 16 a 65 serão gerados em diversas linhas do arquivo texto. Cada linha corresponde a uma coluna indicando valores como Valor Contábil, Base de Cálculo e outros.   
As linhas 16 a 65 são geradas conforme o [CFOP](http://tdn.totvs.com/pages/viewpage.action?pageId=431680880) associado aos [Lançamentos Fiscais](http://tdn.totvs.com/pages/viewpage.action?pageId=427041477)s e cada linha corresponde a um grupo de CFOP['s](http://tdn.totvs.com/pages/viewpage.action?pageId=431680880), conforme manual da rotina.  
Exemplo:  
109999999999999200402290101601000000001000000  
109999999999999200402290101602000000001000000  
...01601... - Valor Contábil total das operações geradas na linha 16.  
...01602... - Base de Cálculo ICMS das operações geradas na linha 16.  
Segue a descrição de cada uma destas colunas:

**Valores Contábeis**  
**Entradas**: coluna 01    **Saídas**: coluna 01  
Esta coluna estará recebendo o Valor Contábil total dos [Lançamentos Fiscais](http://tdn.totvs.com/pages/viewpage.action?pageId=427041477) que se encontram dentro das características das operações geradas nas linhas 16 a 65.

**Base de Cálculo**  
**Entradas**: coluna 02    **Saídas**: coluna 02  
Esta coluna estará recebendo a Base Tributada de ICMS dos [Lançamentos Fiscais](http://tdn.totvs.com/pages/viewpage.action?pageId=427041477) que se encontram dentro das características das operações geradas nas linhas 16 a 65.

**Imposto Creditado**  
**Entradas**: coluna 03      
Esta coluna estará recebendo o Valor ICMS dos [Lançamentos Fiscais de Entrada](http://tdn.totvs.com/pages/viewpage.action?pageId=427041477) que se encontram dentro das características das operações geradas nas linhas 16 a 65.

**Imposto Debitado**  
**Saídas**: coluna 03  
Esta coluna estará recebendo o Valor ICMS dos [Lançamentos Fiscais de Saída](http://tdn.totvs.com/pages/viewpage.action?pageId=427041477) que se encontram dentro das características das operações geradas nas linhas 16 a 65.

**Imposto Sem Aproveitamento de Crédito**  
**Entradas**: coluna 04  
Esta coluna estará recebendo o Valor ICMS preenchido nos itens dos [Lançamentos Fiscais de Entrada](http://tdn.totvs.com/pages/viewpage.action?pageId=427041477) que por algum motivo não geraram crédito imediato do ICMS.   
Estes [Lançamentos Fiscais](http://tdn.totvs.com/pages/viewpage.action?pageId=427041477) devem pertencer à Filial e Período informados na tela da rotina, o CFOP associado deve ser Fiscal, o status diferente de Cancelado e Estornado e o Valor ICMS do [Lançamento Fiscal](http://tdn.totvs.com/pages/viewpage.action?pageId=427041477) deve ser igual a 0 (zero). Além destas características, o Tipo ICMS do CFOP associado deve ser um dos seguintes: Isentos, Isento C/ S.T., Não Incidência, Outros, Compra Ativo Imobilizado, Compra Ativo Imobilizado com Base, Diferido, Suspenso, Compra C/ S.T., Compra C/ S.T. Vlr. S.T. Contábil, Dif. Alíquota, Complementar Outros ICMS, Complementar ICMS, Complementar S.T., Complementar ICMS s/ Vlr. Contábil e ST Retido na Compra.  
Esta coluna será preenchida para as operações informadas nas linhas 16 a 65, onde existir a situação listada acima.  
***Observação***: O sistema estará adotando a seguinte regra para os campos que utilizam Isento ICMS ou Outros ICMS: se o campo Base com IPI do CFOP associado ao [Lançamento Fiscal](http://tdn.totvs.com/pages/viewpage.action?pageId=427041477) está desabilitado e o campo Lança IPI em Isentos ou Outros está habilitado, o IPI **(Tributado ou Não Tributado)** será retirado do valor de Isento ou Outros. Lembrando que o novo RICMS não permite lançamento do IPI na coluna Isentos ou Outros.

**Isentas**  
**Entradas**: coluna 05    **Saídas**: coluna 04  
Esta coluna estará recebendo o campo Isento ICMS para operações cujo Tipo ICMS do [CFOP](http://tdn.totvs.com/pages/viewpage.action?pageId=422545982) associado é Isentos.

**Não Tributadas**  
**Entradas**: coluna 06    **Saídas**: coluna 05  
Esta coluna estará recebendo Isento ICMS + Outros ICMS para operações cujo Tipo ICMS do [CFOP](http://tdn.totvs.com/pages/viewpage.action?pageId=422545982) associado é Não Incidência.

**Parcela de Base de Cálculo Reduzida**  
**Entradas**: coluna 07    **Saídas**: coluna 06  
Se o % Red. ICMS do Lançamento Fiscal é maior que zero e o Tipo ICMS do [CFOP](http://tdn.totvs.com/pages/viewpage.action?pageId=422545982) associado é diferente dos seguintes:

* Red. BC e S.T.
* Compra c/ ST
* Compra ST Vr. ST Contábil
* Complementar ST
* ST Retido na Compra
* Normal e ST
* Isento c/ ST
* Outros c/ ST
* Venda c/ ST
* Compra ST s/ Outros

O sistema estará preenchendo esta coluna com os seguintes valores:

* Se o campo Colocar Redução Em do [CFOP](http://tdn.totvs.com/pages/viewpage.action?pageId=422545982) associado estiver habilitado com o valor Isentos, o campo Isento ICMS será somado à esta coluna.
* Se o campo Colocar Redução Em do [CFOP](http://tdn.totvs.com/pages/viewpage.action?pageId=422545982) associado estiver habilitado com o valor Outros, o campo Outros ICMS será somado à esta coluna.  
  Esta regra vale para os Lançamentos Fiscais que se encontram dentro das características das operações geradas nas linhas 16 a 65.  
  **Diferidas**  
  **Entradas**: coluna 08    **Saídas**: coluna 07  
  Esta coluna estará recebendo o campo Outros ICMS para operações cujo Tipo ICMS do [CFOP](http://tdn.totvs.com/pages/viewpage.action?pageId=422545982) associado é Diferido.   
    
  **Suspensas**  
  **Entradas**: coluna 09    **Saídas**: coluna 08  
  Esta coluna estará recebendo o campo Outros ICMS para operações cujo Tipo ICMS do [CFOP](http://tdn.totvs.com/pages/viewpage.action?pageId=422545982) associado é Suspenso.   
    
  **Substituição Tributária**  
  **Entradas**: coluna 10    **Saídas**: coluna 09  
  Esta coluna estará recebendo o Valor Contábil dos Lançamentos Fiscais que se encontram dentro das características das operações geradas nas linhas 16 a 65, cujo Tipo ICMS do [CFOP](http://tdn.totvs.com/pages/viewpage.action?pageId=422545982) associado é um dos seguintes:

* Red. BC e S.T.
* Compra c/ ST
* Compra ST Vr. ST Contábil
* Complementar ST
* ST Retido na Compra
* Normal e ST
* Isento c/ ST
* Outros c/ ST
* Venda c/ ST
* Compra ST s/ Outros

**Outras**  
**Entradas**: coluna 11    **Saídas**: coluna 10  
Esta coluna estará recebendo o campo Outros ICMS para operações cujo Tipo ICMS do CFOP associado é diferente de:

* Suspenso
* Diferido
* Não Incidência
* Suspenso S/ Valor Contábil
* Red. BC e S.T.
* Compra c/ ST
* Compra ST Vr. ST Contábil
* Complementar ST
* ST Retido na Compra
* Normal e ST
* Isento c/ ST
* Outros c/ ST
* Venda c/ ST
* Compra ST s/ Outros

Além do valor do campo Outros ICMS, esta coluna estará recebendo o valor do IPI (Tributado ou Não Tributado) nas seguintes situações, se o Tipo ICMS é um dos seguintes:

* Complementar Outros ICMS
* Complementar ICMS
* Complementar S.T.
* Complementar ICMS s/ Vlr. Contábil
* Suspenso
* Diferido
* Outros
* Compra Ativo Imobilizado
* Compra Ativo Imobilizado Dif. ALiq.
* Compra Ativo Imobilizado com Base
* Compra Ativo Imobilizado Dif. ALiq. com Base
* Compra C/ S.T.
* Compra C/ S.T. Vlr. S.T. Contábil
* Dif. Alíquota
* Isento
* Não Incidência

Ou o Tipo ICMS não é um dos listados acima e o campo Base com IPI do CFOP associado encontra-se desabilitado. Além disso, o Tipo IPI não poderá ser 50 % do Valor - Ñ Contábil. Se o Tipo IPI é 50% do Valor, o IPI Tributado será somado na coluna Outras multiplicado por 2 (dois).   
Além das consistências acima, o Tipo ICMS não poderá ser um dos seguintes:

* Red. BC e S.T.
* Compra c/ ST
* Compra ST Vr. ST Contábil
* Complementar ST
* ST Retido na Compra
* Normal e ST
* Isento c/ ST
* Outros c/ ST
* Venda c/ ST
* Compra ST s/ Outros

Isso porque para estes tipos o Valor Contábil total é somado na coluna Substituição Tributária e não será necessário o preenchimento do IPI na coluna Outras, para fechamento.  
***Observação***: Serão somados a coluna OUTROS os valores de despesas que não fazem parte da base de cálculo do ICMS e do valor contábil do lançamento fiscal. Para que o valor do IPI do tipo Não Tributado seja totalizado, será necessário ativar os campos "Afeta Base ICMS" habilitado para o IPI, no cadastro da Regra de ICMS.

**Campo 66 - Crédito Recebido em Transferência:**O campo 66 será calculado com o total de Crédito Recebido em Transferência.  
Este total é carregado através dos Lançamentos de Outros Débitos/Créditos do tipo Crédito e subtipo Recebimento de Crédito, lembrando que o período fiscal deverá ser encerrado para que estes totais sejam calculados.  
Existindo valor neste campo, a Linha 20 - Detalhamento dos Créditos Recebidos em Transferência será exigida. Esta linha será gerada no Sistema de Gestão Fiscal através das Referências de Outros Débitos/Créditos, ou seja, o usuário deverá cadastrar as referências com informações sobre a(s) NF(s) de transferência.   
As referências poderão ser vinculadas a Lançamento Fiscal cadastrado na base de dados ou não.  
Informações sobre a Linha 20:

6
incomplete
**Produtor Rural e Inscrição Estadua**l: estes campos serão carregados conforme o Cliente/Fornecedor ou Filial associado ao Lançamento Fiscal vinculado aos Outros Débitos/Créditos.O campo Produtor Rural é um item da lista de Ramos Atividade do Cadastro de Cliente/Fornecedor. Se for uma Filial associada ao Lançamento Fiscal o sistema verifica o campo Produtor Rural que é um item da lista de Ramo Atividade do cadastro de Filial. Se a referência não possui um Lançamento Fiscal vinculado, o sistema estará utilizando os campos Produtor Rural e Inscr. Estadual na própria tabela de referências de Outros Débitos/Créditos. 

* Número, Série, Data e Valor: estes campos serão carregados conforme o Lançamento Fiscal vinculado aos Outros Débitos/Créditos. Se a referência não possui um Lançamento Fiscal vinculado, o sistema estará utilizando os campos Número Doc., Data Emissão, Série e Valor Total na própria tabela de referências de Outros Débitos/Créditos.
* Data Visto e Código Motivo: estes campos serão carregados da própria tabela de referências de Outros Débitos/Créditos, através dos campos Data Visto e Motivo Referência.
* Valor: o sistema estará utilizando o campo Valor das Referências de Outros Débitos/Créditos.

**Campo 68 - Crédito Extemporâneo:**Este campo receberá o total de Outros Débitos/Créditos do tipo Crédito e subtipo Extemporâneo, do período de ICMS correspondente ao da geração da rotina. Para isto, o período deverá se encontrar encerrado.

**Campo 69 - Diferença de Alíquota:**Valor Dif. Alíquota das operações de Entrada interestaduais referentes ao Ativo Imobilizado. Serão considerados todos os bens que ainda têm direito ao crédito de 1/48 que foram adquiridos de outras UF's para ativo imobilizado. O sistema estará aplicando o cálculo sobre o Dif. de Alíquota informado na tela de itens e não sobre o ICMS + Dif. de Alíquota + Frete.

**Campo 70 - Ressarcimento Substituição Tributária:**O campo 70 estará recebendo o total de Outros Débitos/Créditos do tipo Crédito e subtipo Ressarcimento ST. Para isto, o período fiscal deverá se encontrar encerrado para o cálculo. Os detalhes, preenchidos na Linha 27, serão carregados também das referências de Outros Débitos/Créditos, onde existirão informações referentes às notas fiscais de ressarcimento.

**Campo 71 - Outras:** O campo 71 se refere a Outros Débitos/Créditos que não se encaixam em nenhuma categoria definida anteriormente

**Campo 73 - Créditos Transferidos:**Serão considerados todos os bens que ainda têm direito ao crédito de 1/48 que foram adquiridos de outras UF's para ativo imobilizado. O sistema estará aplicando o cálculo sobre o Dif. de Alíquota informado na tela de itens e não sobre o ICMS + Dif. de Alíquota + Frete.

**Campo 76 - Base de Cálculo ST:**Base Tributada ST das operações de saídas internas, se os campos Base Tributada ST e Valor ST forem maior que zero. Estará recebendo também a Base Tributada ST de todas as operações de entrada com Valor ST maior que zero, o Tipo ICMS igual a "ST Retido na Compra" ou "Normal ST Retido na Compra". O campo Contribuinte Credenciado, localizado na Tela de Subst. Tributária, está habilitado e o campo Distribuidor, Atacadista ou Depósito com Regime Especial ST na Tela da rotina encontra-se habilitado. Não serão selecionados os Lançamentos Fiscais cujo CFOP refere-se a Serviço de Transporte (Interno ou Interestadual), visto que este tipo de operação estará preenchendo o campo 103.

**Campo 77 - Valor Retido:**Valor ST das operações utilizadas para o cálculo do campo 76.

**Campo 79 - Ressarcimento ICMS:**Este campo estará recebendo o Valor Contábil das operações de CFOP 5.603. Serão gerados detalhamentos na Linha 28 com informações do próprio Lançamento Fiscal, inclusive o campo Data Visto, localizado na pasta Outros Dados.

**Campo 80 - Devolução:**Valor ST das operações de Entrada referente à Devolução, cujo Tipo ICMS gera débito de ST nas saídas, gera crédito de ST. Este valor é carregado na tabela DPERIODOST ao encerrar período de ICMSST. O valor referente a este crédito para o Estado de MG é carregado no campo 80 da DAPI MG.   
***Exemplo***: operações de entrada com um dos seguintes tipos de ICMS: Venda C/ S.T., Isento C/ S.T., Red. B.C. e S.T. e Complementar S.T., cujo Tipo da Natureza de Operação é Devolução, o valor ST destas operações será preenchido no campo 80, quando se tratar de operação com o Estado de MG. Para isso, o período de ICMS ST deverá se encontrar encerrado.

**Campo 81 - Saldo Credor de ST para o Período Seguinte:**Resultante da subtração do campo 77 os seguintes campos: 78, 79 e 80, isso se o resultado for negativo. Neste caso o sistema preencherá o valor absoluto. Caso contrário o campo receberá o valor zero.

**Campo 82 -ICMS ST a Recolher:**Resultante da subtração do campo 77 os seguintes campos: 78, 79 e 80, isso se o resultado for maior que zero. Caso contrário o campo receberá o valor zero.

**Campo 83 - Base de Cálculo ST:**Base Tributada ST das operações de saídas interestaduais, se os campos Base Tributada ST e Valor ST forem maior que zero.

**Campo 84 - Valor Retido:**Valor ST das operações de saídas interestaduais, se os campos Base Tributada ST e Valor ST forem maior que zero.

**Campo 85 - Base de Cálculo ST:**Base Tributada ST de todas as operações de entrada com Valor ST maior que zero, o Tipo ICMS igual a "ST Retido na Compra", "Normal ST Retido na Compra", o campo Contribuinte Credenciado, localizado na Tela de Subst. Tributária, está habilitado e o campo Distribuidor, Atacadista ou Depósito com Regime Especial ST na Tela da rotina encontra-se desabilitado. Não serão selecionados os Lançamentos Fiscais cujo CFOP refere-se a Serviço de Transporte (Interno ou Interestadual), visto que este tipo de operação estará preenchendo o campo 103.

**Campo 86 - Valor Retido:**Valor ST das operações utilizadas para o cálculo do campo 85.

**Campo 90 - Estorno de Débitos:**Lançamentos de Outros Débitos/Créditos do tipo Estorno de Débito. O sistema estará gerando detalhamento(s) na linha 22 através das referências de Outros Débitos/Créditos.    
A partir da versão 6.1.0 do Sistema de Gestão Fiscal, os registros que utilizam as referências de Outros Débitos/Créditos estarão recebendo o campo Valor, informado na própria tela de referência. Neste caso o sistema não estará utilizando mais o Valor Contábil do Lançamento Fiscal vinculado ao Lançamento de Outros Débitos/Créditos.  
O campo Valor, antes definido como Valor Total, passou a ser obrigatório, independente do usuário informar documento cadastrado ou não.   
Se o usuário selecionar um Lançamento Fiscal cadastrado no sistema, este campo será carregado com o Valor ICMS (somando-se todas as parcelas) se o tipo do Lançamento for Estorno de Crédito ou Estorno de Débito. Caso contrário, o campo Valor estará recebendo o Valor Contábil (somando-se todas as parcelas).   
Se o usuário não selecionar um documento cadastrado, este valor deverá ser informado manualmente.  
Quando o usuário cadastrar um Estorno de Débito e vincular uma nota fiscal cadastrada no sistema, o Valor será carregado com o Valor ICMS desta nota, se não estiver preenchido. Se este campo já estiver preenchido, o usuário tem a opção de atualizar clicando no botão Atualizar Valor, localizado ao lado do campo. Com isso o contribuinte tem a opção de estornar apenas o Valor ICMS da Nota Fiscal emitida anteriormente. Se o estorno não se referir a todo o ICMS, este valor poderá ser alterado, lembrando que a soma de todos os valores de estorno deverá fechar com o Lançamento de Outros Débitos/Créditos do tipo Estorno de Débito, para que a DAPI seja gerada corretamente.  
O campo Motivo será gerado da seguinte forma:

* Ao preencher o Motivo, na Pasta Referências, sub-pasta Outros dados com a informação "Outros" ou com "1", será gerado o Motivo = 1.
* Ao preencher com "Estorno" ou com "2" será gerado Motivo = 2.
* Ao preencher com "3" será gerado Motivo = 3.
* Ao preencher com "6" será gerado Motivo = 6

**Campo 95 - Estorno de Créditos:**Lançamentos de Outros Débitos/Créditos do tipo Estorno de Crédito. O sistema estará gerando detalhamento na linha 29 com informações do próprio Lançamento de Outros Débitos/Créditos do tipo Estorno de Crédito.

1
incomplete
**Código do Motivo do Estorno**: este campo receberá o valor do campo Classificação.

2
incomplete
**Auto de Infração**: este campo receberá o valor do campo Observação se a Classificação for igual a "01".

3
incomplete
**Valor**: valor do Estorno de Crédito.

**Campo 98 - Deduções:**O campo Deduções da DAPI 1 é utilizado por empresas que trabalham com Incentivo à Cultura e também por empresas que utilizam Compensação de Crédito.  
O Sistema de Gestão Fiscal irá gerar as deduções referentes à Compensação de Crédito, ou seja, além do campo 98, serão gerados os detalhes 23, 24 e 25.    
Compensação de Crédito também se refere a crédito recebido em transferência. A diferença básica com o campo 66 da DAPI 1 é a seguinte: o campo 66 deverá ser preenchido com o crédito recebido em transferência de CFOP 1.601 dentro do mesmo período. No caso das deduções, a apuração já aconteceu e uma NF de transferência foi emitida para compensação de saldo do período anterior.   
Para gerar o campo 98 e os detalhes 23, 24 e 25, serão utilizados os Lançamentos de Outros Débitos/Créditos do tipo Deduções e subtipo Compensação de Crédito e Incentivo a Cultura. O usuário deverá informar os dados da NF recebida nas referências da dedução. Neste caso não poderá ser selecionado nenhum documento fiscal, visto que a NF não é cadastrada no sistema.   
Para gerar as informações referentes ao incentivo à Cultura, serão utilizados os Lançamentos de Outros Débitos/Créditos do tipo Deduções e subtipo Incentivo à Cultura. O usuário deverá informar os dados da NF recebida nas Referências da dedução. Outras informações sobre o cálculo efetuado pelo sistema em Período de Apuração / Pasta Incentivos Fiscais.

4
incomplete
**Linha 23**: Será gerada uma única linha 23 com a totalização das deduções. Neste caso serão preenchidos os campos de cabeçalho, o valor referente à Compensação de Crédito e o total de deduções.

***Observação***: Se o CFOP for 1.653 e o campo Tipo Natureza DIPI / DAPI / DIEF / GIM RN for "Combustíveis para uso e consumo" as informações serão geradas na linha 23. Se o CFOP não estiver associado a este tipo, a operação continuará sendo gerada na linha 16.   
Se o CFOP for 2.653 e o campo Tipo Natureza DIPI / DAPI / DIEF / GIM RN for "Combustíveis para uso e consumo" as informações serão geradas na linha 33. Se o CFOP não estiver associado a este tipo, a operação continuará sendo gerada na linha 26. O campo soma detalhamentos recebe o valor igual a zero e a alíquota recebe o valor fixo igual a 3.

5
incomplete
**Linha 24**:Serão geradas N linhas 24, conforme o número de notas fiscais recebidas para compensação de crédito. Os campos referentes à nota fiscal recebida para compensação de crédito deverão ser informados nas referências da dedução cadastrada, lembrando que não poderá ser selecionado um Lançamento Fiscal de referência, visto que a nota fiscal não poderá compor o registro de entrada.

***Exemplo***:  
Em março / 2005, após finalizar a apuração das empresas X e Y, a empresa X ficou com um saldo devedor e a empresa Y com saldo credor. Em abril / 2005 a empresa Y emitiu uma NF CFOP 5.602 para a empresa X. Esta NF de CFOP 5.602 irá compor o livro de saídas de abril / 2005 da empresa Y e o campo 73 da DAPI. Neste caso o campo 73, crédito transferido, recebe informações de crédito transferido através dos CFOP's 5.601 e 5.602. A empresa X deverá lançar como deduções, na DAPI de março / 2005 e a NF não irá compor o livro de entradas.  
***Observação***:Este tipo de transferência é permitido somente entre estabelecimentos da mesma empresa, com o mesmo núcleo de Inscrição Estadual. No caso do campo 66, pode existir crédito recebido em transferência de uma outra empresa. A data emissão da NF de transferência deve ser de período posterior ao período da DAPI.

**Campo 100 - Diferença de Alíquota:**Este campo estará recebendo o Valor Dif. Alíquota das operações de Entrada interestaduais referentes ao Ativo Imobilizado e Uso e Consumo. Receberá também o valor do diferencial de alíquota para as operações de entrada interestaduais referentes a transporte, o CFOP associado ao Lançamento Fiscal deverá estar com o seguinte valor no campo Tipo Natureza DIPI/DAPI/DIEF/GIM: "Serviço Iniciado em Outra UF sem Vínculo com Operação Subseqüente".

**Campo 103 - Serviço Transporte de Responsabilidade do Remetente:**Valor ST de todas as operações de entrada com Valor ST maior que zero, o Tipo ICMS igual a "ST Retido na Compra" ou "Normal ST Retido na Compra" e o CFOP refere-se a Serviço de Transporte (Interno ou Interestadual).

**Campo 104 - Outros:**Este campo será gerado quando houver no cadastro de Outros Débitos/Créditos um registro para o tributo ICMS com o tipo Estorno de Crédito e subtipo Período anterior (DAPI/MG). Estes registros não irão afetar a apuração do ICMS. Para que esta informação seja impressa nos livros fiscais foi criado no grupo de totais a vairável TER.

**Campo 106 – Importação:**Total do ICMS pago no período de referência, no momento do desembaraço aduaneiro, na importação de mercadorias ou bens oriundos do exterior, ainda que não aproveitados como crédito. Este campo será preenchido com o valor do ICMS informado no item do lançamento de importação.

**Campo 107 - Débito Extemporâneo:**Este campo receberá um somatório do Valor Pago de todas as guias do tipo Normal (ICMS) com Classificação "Débito Extemporâneo", do período correspondente ao da geração da rotina. :

**Campo 108 - Substituição Tributária:**Valor ST das operações de entrada com Tipo ICMS ST "Retido na Compra" ou "Normal ST Retido na Compra". Não serão selecionados os Lançamentos Fiscais cujo CFOP refere-se a Serviço de Transporte (Interno ou Interestadual), visto que este tipo de operação estará preenchendo o campo 103.  
***Observação***: Se o campo "Contribuinte Credenciado" está habilitado, campo este localizado na tela de Substituição Tributária do Lançamento Fiscal, o contribuinte não tem obrigação de pagar o ST na barreira e sim na apuração de ST. Neste caso deve ser preenchido no campo 86.   
Se não for credenciado, o valor do ST deverá ser preenchido no campo 108, sendo assim o campo "Contribuinte Credenciado" deverá estar desabilitado.

**Campo 111 - Exportação Indireta:**Valor Contábil das operações de exportação, cujo campo EXPORTAÇÃO INDIRETA da pasta EXTERIOR do Lançamento Fiscalesteja habilitado.

**Campo 112 - Saídas para SUFRAMA:**Valor Contábil das operações de saída, cujo CFOP associado ao Lançamento Fiscal encontra-se com o campo Tipo Natureza DIPI/DAPI/DIEF/GIM preenchido com o valor: Saídas para SUFRAMA.

**Campo 113 - Exportação Direta:**Valor Contábil das operações de exportação, cujo campo EXPORTAÇÃO DIRETA da pasta EXTERIOR do [Lançamento Fiscal](http://tdn.totvs.com/pages/viewpage.action?pageId=427041477) esteja habilitado.   
***Observação***: Os campos 115 – Nº de Empregados no Último Dia do Período, 116 – Valor da Folha de Pagamento, 117 – Valor Devido COFINS e 118 – Energia Elétrica Consumida no Período são campos que se encontram na tela da rotina.  
   
**Campos Não Gerados**

* 67: Crédito Presumido
* 78: Saldo Credor de ST do Período Anterior
* 80: Devolução ST
* 103: Serviço Transporte de Responsabilidade do Remetente
* 104: Outros
* 109: Outros

Os quadros referentes às operações de Café também não serão gerados pelo TOTVS Gestão Fiscal.  
   
**DAPI - Modelo 2**  
As linhas 16 a 23 são geradas conforme o CFOP associado aos Lançamento Fiscale cada linha corresponde a um grupo de CFOP's, conforme manual da rotina.

**Campo 29 - Outras Saídas que não Constituem Receita Operacional:**Valor Contábil das operações de saída com um dos seguintes CFOP's: 5.96, 6.96, 5.904 ou 6.904. Ou ainda o Valor Contábil das operações de saída cujo CFOP associado ao [Lançamento Fiscal](http://tdn.totvs.com/pages/viewpage.action?pageId=427041477) encontra-se com o campo Tipo Natureza DIPI/DAPI/DIEF/GIM preenchido com um dos seguintes valores:

* NF Simples Rem. Emit. Vendas p/ Ent. Futura
* Saídas p/ Depósito, Dentro ou Fora do Estado
* Saídas p/ Demonstração Fora do Estado
* Saídas de Prod. Primários e Sucatas p/ Ind.
* NF Emit. Vendas Merc. Já Registradas por ECF

**Campo 35 - Entradas Tributadas com Posteriores Saídas não Tributadas:**Valor Contábil das operações de entrada cujo CFOP associado ao Lançamento Fiscal encontra-se com o campo Tipo Natureza DIPI/DAPI/DIEF/GIM preenchido com o valor Entrada Trib. c/ Post. Saída Não Trib/Isenta.

**Campo 36 - Parcela de Base de Cálculo Reduzida na Entrada:**Base ICMS – Base Tributada ICMS das operações de entrada com % Red. ICMS maior que 0 (zero).

**Campo 42 - Utilização de Serviço / Aquisição ME e EPP sem ICMS:**Valor Contábil das operações de entrada cujo CFOP associado ao Lançamento Fisal encontra-se com o campo Tipo Natureza DIPI/DAPI/DIEF/GIM preenchido com o valor Uso Serv./Aquis. ME e EPP Sem Dest. ICMS.

**Campo 43 - Valor das Notas Fiscais no Retorno do Comércio Ambulante:**Valor Contábil das operações com um dos seguintes CFOP's: 195, 196, 295, 296, 1904, 1414, 1415, 2904, 2414 ou 2415.

**Campo 45 - Outras Entradas não Sujeitas à Aplicação das Alíquotas Internas de Saída:**O Valor IPI das operações com um dos seguintes CFOP's: 1101, 1102, 1111, 1113, 1116, 1117, 1118, 1120, 1121, 1122, 1401, 1403, 1651, 1652, 2101, 2102, 2111, 2113, 2116', 2117, 2118, 2120, 2121, 2122, 2401, 2403, 2651, 2652, 3101, 3102, 3127, 3651, 3652, 111, 112, 171, 172, 211, 212, 271, 272, 311 ou 312 e o campo Base com IPI encontram-se desabilitado, será somado no campo 45.  
Se o Lançamento Fisal não se encontra dentro das características acima, o sistema estará consistindo se a operação está associada a um dos seguintes CFOP's: 260, 261, 262, 263, 264, 265, 2350, 2351, 2352, 2353, 2354, 2355, 151, 152, 153, 154, 155, 250, 251, 252, 253, 254, 255, 340, 341, 1300, 1301, 1302, 1303, 1304, 1305, 2300, 2301, 2302, 2303, 2304, 2305, 3300, 3301, 140, 141, 142, 143, 144, 145, 146, 240, 241, 242, 243, 244, 245, 246, 330, 331, 1250, 1251, 1252, 1253, 1254, 1255, 1256, 1257, 2250, 2251, 2252, 2253, 2254, 2255, 2256, 2257, 3250, 3251. Se estiver, o sistema estará somando o Valor Contábil no campo 45.

**Campo 47 - Valor das Entradas x Alíquotas Internas de Saída:**Total da Base ICMS dos itens dos Lançamento Fisal x alíquota interna definida para o ICMS no cadastro de produtos do RM Nucleus. Se não existir alíquota de ICMS definida para o produto, o sistema estará utilizando a alíquota interna definida para o Estado.

**Campo 61 - Valor do ICMS Mensal Parcela Fixa:**Este campo será preenchido pelo sistema conforme valor definido no campo ICMS Mensal Parcela Fixa, localizado na tela da rotina.   
Campos Gerados a Partir de Campos de Tela:

* 80: Nº de Filiados no Último Dia do Período de Referência
* 82 e 83: Saldo Devedor / Credor FUNDESE do Período Anterior
* 86: Nº de Empregados no Último Dia do Período
* 91: 50% do Valor Despendido com Capacitação e Treinamento
* 92: 50% do Valor Despendido com Máquinas, Equipamentos e Tecnologia
* 93: 100% do Valor Despendido na Aquisição de ECF  
     
  **Campos Não Gerados:**

* 37: Parcela não Tributada na Saída com Operação Anteriormente Tributada
* 38: Utilização de Serviço Iniciado em Outra UF sem Saída Posterior Tributada
* 57: Crédito de ICMS Decorrente de Pagamento Indevido
* 70: Outros
* 79: Valor da Base de Cálculo de Autuações Fiscais no Período de Referência
* 89: Saldo Excedente de Abatimentos do Período Anterior
* 90: Estorno de Abatimentos Não Absorvidos

**DAPI Modelo 3**

As linhas 16 a 23 são geradas conforme O CFOP associado aos Lançamento Fiscais e cada linha corresponde a um grupo de CFOP's, conforme manual da rotina.

**Campo 29 - Outras Saídas que não Constituem Receita Operacional:**Vide Campo 29 DAPI Modelo 2.

**Campo 36 - Parcela de Base de Cálculo Não Tributada nas Saídas:**Base ICMS – Base Tributada ICMS das operações de saída com % Red. ICMS maior que 0 (zero).

**Campo 46 - Entrada Tributada com Posterior Saída Não Tributada / Isenta:**Vide Campo 35 DAPI Modelo 2.

**Campo 47 - Parcela de Base de Cálculo Reduzida na Entrada:**Vide Campo 36 DAPI Modelo 2.

**Campo 53 - Utilização de Serviço / Aquisição ME e EPP sem ICMS:**Vide Campo 42 DAPI Modelo 2.

**Campo 54 - Valor das Notas Fiscais no Retorno do Comércio Ambulante:**Vide Campo 43 DAPI Modelo 2.

**Campo 56 - Outras Entradas não Sujeitas à Aplicação das Alíquotas Internas de Saída:**Vide Campo 45 DAPI Modelo 2.

**Campo 58 - Valor das Entradas x Alíquotas Internas de Saída:**Vide Campo 47 DAPI Modelo 2.

**Campos Gerados a Partir de Campos de Tela:**

* 75: Nº de Empregados no Último Dia do Período
* 80: 50% Valor Despendido com Capacitação e Treinamento
* 81: 50% Valor Despendido com Máquinas, Equipamentos e Tecnologia
* 82: 100% Valor Despendido na Aquisição de ECF
* 109 e 110: Saldo Devedor / Credor FUNDESE do Período Anterior  
     
  **Campos Não Gerados:**

* 37: Prestação de Serviço de Transporte Iniciada em Outro Estado
* 39: Valor NF Simples Faturamento Emitidas nas Vendas para Entrega Futura
* 48: Parcela Não Tributada na Saída com Operação Anteriormente Tributada
* 49: Utilização de Serviço Iniciado em Outra UF sem Saída Posterior Tributada
* 60: Outras Entradas Consideradas na Composição do Agregado
* 62: Diferença a Menor Entre Saídas e Entradas do Período Anterior
* 78: Saldo Excedente de Abatimentos do Período Anterior
* 79: Estorno de Abatimentos Não Absorvidos
* 89: Crédito de ICMS Decorrente de Pagamento Indevido
* 96 : Estorno de abatimentos já absorvidos
* 97: Outros
* 106: Valor da Base de Cálculo de Autuações Fiscais no Período de Referência
