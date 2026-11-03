---
content_hash: 63413493d7afdb93519c147eab6d938431b3e5824ac9165cc1c6cdf2d295ce1a
fetched_at: '2026-06-29T00:09:21.967531+00:00'
page_id: '422545933'
product: rm
source: tdn-rm
title: Bloco 0 (EFD Contribuições)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545933
version: 20
---

## Informações do contribuinte e tabelas utilizadas nas movimentações como Produtos, Clientes e Fornecedores, Naturezas de Operação e Unidades de Medida.

1lefttrue1Registro 0000

**Registro 0000  –  Abertura do arquivo digital**  
São gravadas neste registro informações da filial matriz do estabelecimento e informações digitadas na tela de geração da rotina.

2Registro 0001

**Registro 0001  –  Abertura do bloco 0**  
Este registro informa se houve movimentação no bloco 0

3Registro 0035

**Registro 0035 – Identificação da Sociedade de Sociedade em Cotas de Participação - SCP**  
Para a geração deste registro, serão selecionadas filiais no caso de pessoa jurídica sendo ostensiva de Sociedade em Cotas de Participações (SPC), incluindo a própria sócio ostensiva.  
Este registro é gerado de acordo com o Indicador da Natureza da Pessoa Jurídica selecionado nos parâmetros da tela de geração da rotina. Neste registro serão gravadas informações da filial SCP, como CNPJ e o nome.

4Registro 0100

**Registro 0100  –  Dados do contabilista**  
Para a geração deste registro são selecionados os dados do contabilista que estão no anexo da filial (Dados Fiscais) definida como matriz dos estabelecimentos.

1Registro 0110

**Registro 0110  –  Regimes de Apuração da Contribuição Social e de Apropriação de Crédito**  
Este registro é gerado com as informações dos seguintes parâmetros da tela de geração:

* Código indicador da incidência tributária no período
* Código indicador de método de apropriação de créditos
* Código indicador do Tipo de Contribuição Apurada no Período
5Registro 0111

**Registro 0111  –  Tabela de Receita Bruta Mensal para Fins de Rateio de Créditos Comuns**  
Este registro é gerado com as informações  dos seguintes parâmetros da tela de geração:

* Receita Bruta Não-Cumulativa - Tributada Mercado Interno (R$)
* Receita Bruta Não-Cumulativa - Não tributada Mercado Interno (R$)
* Receita Bruta Não-Cumulativa - Exportações (R$)
* Receita Bruta Cumulativa (R$)
6Registro 0120

**Registro 0120 - Identificação de períodos dispensados da escrituração fiscal digital das contribuições**  
Este registro deve ser apresentado na escrituração referente ao mês de dezembro de cada ano calendário, contendo as informações dos meses em que a empresa esteve dispensada da entrega da EFD Contribuições.  
Este registro não será implementado. Caso o contribuinte se enquadre nesta situação e tenha que gerá-lo as informações deverão ser inseridas manualmente no PVA após importar o arquivo gerado pelo RM.

7Registro 0140

**Registro 0140  –  Tabela de Cadastro de Estabelecimentos**  
Este registro é gerado com as informações das filiais que foram movimentadas no período da escrituração.

8Registro 0145

**Registro 0145 - Regime de Apuração da Contribuição Previdenciário sobre a Receita Bruta**  
Este registro indica a obrigatoriedade do [Bloco P](http://tdn.totvs.com.br/pages/viewpage.action?pageId=422545977) no arquivo. Este registro só será gerado se houver no período de escrituração digital atividade sujeita a Contribuição Social sobre a Receita Bruta. A existência desta contribuição será verificada através da existência, no período da escrituração, de Lançamentos Fiscais de entrada ou saída que possuam em seus itens o [Tributo](http://tdn.totvs.com.br/pages/viewpage.action?pageId=422546150)do tipo Contr. Previdenciária.  
Para a geração do valor da Receita Bruta sujeita a contribuição serão totalizados os itens dos lançamentos de saída que possuam o tributo do tipo Cont. Previdenciária subtraindo-se o valor totalizados dos itens de  todos os lançamentos de entrada (Devolução/Cancelamento de vendas) que também possuam este  tributo.  
Para este registro o campo Informações Complementares não será gerado.

9Registro 0150

**Registro 0150 – Tabela do Participante**  
Este registro é gerado com os dados dos clientes e fornecedores movimentados nos blocos A, C, D e registro F100, F200. Para a correta geração destas informações o cadastro dos Clientes e Fornecedores devem estar completamente preenchido.

Veja mais sobre a geração deste Registro (0150) quando houver caso de Devolução por Recusa:

10Registro 0190

**Registro 0190  –  Identificação das Unidades de Medida**  
Este registro é gerado com a sigla e descrição das unidades de medida movimentadas  nos blocos A, C e D.

Registro 0200

**Registro 0200  –  Tabela de Identificação do Item (Produtos e Serviços)**  
Este registro é gerado com as informações dos itens movimentados nos blocos A, C e D cujos lançamentos estão vinculados ao Código Modelo de Documento 07, 08, 8B, 09, 10, 11, 26, 27 e 57.   
O campo **COD\_GEN** é gerado com a informação "00" quando se trata de serviço. Para produtos são gravados os dois primeiros dígitos do NCM ( Nomenclatura comum do Mercosul).  
Será gerado conforme a unidade utilizada em cada lançamento.

A partir da versão 12.1.2506 os campos **08 COD\_NCM** e **09 EX\_IPI** serão gerados com dados do novo cadastro de **Classificação de Bens e Serviços**, campos "**Número**" e "**Código EX**" respectivamente. O cadastro deve ser vinculado ao produto gerado no registro 0200 (Tabela relacionada **DCLASSIFBENSSERVICO**) conforme imagens abaixo:

ImagensObservação:

O Cadastro de Classificação de Bens e Serviço não permite o preenchimento dos dados de NCM, Referência, Número e Código EX, quando selecionado o tipo "Serviço", neste caso, os campos **08 COD\_NCM** e **09 EX\_IPI**, são gerados **vazios.**

11Registro 0205

**Registro 0205  –  Alterações do Item.**  
Este registro é gerado com as informações das alterações na descrição no cadastro dos produtos  e serviços movimentados nos blocos A, C e D. Não são geradas informações de alterações no código do produto (COD\_ANT\_ITEM) uma vez que este tipo de alteração não é permitido nos produtos TOTVS (Linha RM).  As alterações do produto são gravadas no anexo Log de Produtos.

12Registro 0206

**Registro 0206  –  Código de produto conforme tabela ANP (Combustíveis)**  
Este registro será gerado para produtos movimentados nos blocos A, C e D e que possuam o código ANP nos anexo do cadastro do produto (Dados fiscais).

13Registro 0400

**Registro 0400  –  Tabela de Natureza da Operação/Prestação**  
Neste registro é gerada uma entrada para cada CFOP movimentado nos blocos C e D com exceção dos lançamentos associados a Código Modelo de Documento 02 e 2D.

14Registro 0450

**Registro 0450  –  Tabela de Informação Complementar do Documento Fiscal**  
Para que este registro seja gerado deverá ser criado o campo complementar INFCOMPLDOCFISCAL no lançamento.

Observação

Dado que em um determinado período existem Observações (campo complementar INFCOMPLDOCFISCAL) iguais para diferentes lançamentos fiscais e/ou situações tributárias:  
 - Ao Gerar a EFD Contribuições,  
 - O Registros 0450 deve ser único por conteúdo (campo 03-TXT do Registro 0450),  
 - E que os C110  possuam os respectivos conteúdos (TXT\_COMPL), reutilizando o mesmo 0450.

15Registro 0500

**Registro 0500  –  Plano de Contas Contábeis**  
Este registro é gerado somente para os bens movimentados nos registros F120 e F130. Para os outros registros esta informação não é gerada por não se ter chegado a um entendimento sobre qual conta deverá ser carregada para o arquivo uma vez que a contabilização é livre e pode-se incluir várias contas, inclusive de grupos diferentes em cada lançamento fiscal.  
Para os blocos A[Alterar](https://tdn.totvs.com/pages/editpage.action?pageId=422545933), C, D e M e registro F550 (gerados através de Lançamento Fiscal) o sistema irá consistir na a seguinte regra:  
1º - Primeiramente verificará se existe Default Contábil no [Cadastro do Produto/Serviço](http://tdn.totvs.com.br/display/LRM/Produto) sub aba Integração, e que possua a Classificação "SPED" informada. Contas cadastradas como Débito, serão para os lançamentos fiscais de entrada, e por sua vez, as contas cadastradas como Crédito serão para os lançamentos fiscais de saída.   
***Importante!!!*** O campo Classificação da Conta preenchido com "**SPED**" (em CAIXA ALTA).

2º - Não existindo essa informação no Cadastro do Produto, será verificado se existe um Default Contábil no cadastro do CFOP associado ao Lançamento Fiscal, localizado na aba Integração. Contas cadastradas como Débito, serão para os lançamentos fiscais de entrada, e por sua vez, as contas cadastradas como Crédito serão para os lançamentos de saída.

3º - Não existindo Default Contábil no CFOP que atenda a regra acima, será utilizada a conta contábil informada no cadastro do produto em Anexos | [Dados Fiscais](http://tdn.totvs.com.br/display/LRM/Dados+Fiscais+do+Produto) | campo Conta Contábil Sped.

A conta do Plano de Contas Paralelo será gerada caso seja vinculado ao cadastro da conta. Esse vínculo pode ser feito através do cadastro de Plano de Contas Paralelo | Anexos | Contas Paralelas, posteriormente dê duplo clique a Conta Paralela desejada, acesse a aba Associação do Plano Contábil, selecione a conta através da caixa de seleção, selecione a seta para a direita para a conta seja transferida para a coluna Contas Contábeis Selecionadas e salve.  
***Observação:***Caso haja mais de uma conta selecionada dentro da Conta Paralela, o sistema automaticamente irá considerar apenas a primeira conta. Para que a Conta Paralela, campo 08-COD\_CAT\_REF seja gerada no arquivo, o código do [Plano de Conta Paralelo](http://tdn.totvs.com.br/pages/viewpage.action?pageId=423938681) deve ser informado na tela da geração da rotina.

16Registro 0600

**Registro 0600  –  Centros de Custo**  
Este registro é gerado com as informações dos centros de custo movimentados nos blocos A, C e D.

**Obs:** A regra para geração deste registro está disponível no link : 

17Registro 0990

**Registro 0990  –  Totalizador do bloco 0**  
Gerado automaticamente pela rotina com a quantidade de linhas constantes no Bloco 0.

---
