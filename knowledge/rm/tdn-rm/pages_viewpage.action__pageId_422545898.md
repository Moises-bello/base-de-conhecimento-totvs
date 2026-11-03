---
content_hash: fa7859d8f2d9f8db1cc4709b1303e2a9704e34cb5f7612ff70ecaafdc7631879
fetched_at: '2026-06-29T00:09:21.761509+00:00'
page_id: '422545898'
product: rm
source: tdn-rm
title: Apuração ISS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545898
version: 6
---

Ao final do período de apuração definido por lei, o contribuinte do ISS deve apurar o imposto devido por ele sobre operações próprias e também os valores que foram retidos por fornecedores e recolher os valores ao município.  
Por ser um tributo de âmbito municipal é importante que os cadastros de todos os participantes envolvidos em todas as operações estejam devidamente preenchidos, principalmente o município.  
Para as empresas do ramo de Construção Civil devem ser informados todos os projetos da empresa, com endereço da obra, informações do cliente e alíquota do ISS.   
O cadastro de projeto estará disponível para as empresas em que o parâmetro "emite livro de construção civil" esteja marcado. Nesses casos também é possível fazer o controle de dedução e subempreiteiras no cálculo do ISS, quando autorizado pela prefeitura  
O Tributo ISS deve ser inserido na pasta "outros tributos" do lançamento Fiscal e, para a correta apuração, são necessárias algumas informações:

* Tributo com a Sigla ISS
* Tipo de recolhimento
* Base de cálculo, Alíquota e valor  do Imposto
* Município para qual o imposto é devido

Com relação ao tipo de recolhimento estarão disponíveis os seguintes tipos:

* Devido
* Retido na Fonte
* Retido na Fonte Deduzido
* Depósito Juízo
* ISS Isento

A apuração é realizada, individualmente, por filial. Influenciam nessa apuração toda a escrituração fiscal e os lançamentos de ajustes gerados através de lançamentos de outros débitos/créditos.  
O resultado a apuração do ISS é registrado no Período de Apuração. Ao final do período, após realizar as conferências e encerrar o período, o sistema calculará o valor devido ou o saldo credor a ser transportado para o período subsequente. O sistema totaliza as operações de entrada/saída por alíquota e município onde o serviço foi prestado.

**Seleção de Lançamentos**

A seleção dos Lançamentos Fiscais de Entrada e Saída obedece aos parâmetros informados em Opções | Parâmetros | Gerais/Tabelas, no processo "03.02.03 – Apuração de Tributos ISS", item "Apuração ISS por Filial", etapa "Datas Apuração do ISS". Os parâmetros são:

* Lançamento de Entrada: Corresponde a data a ser utilizada para seleção de Lançamentos de Entrada;
* Lançamento de Saída – Entidade Privada: Corresponde a data a ser utilizada para seleção de Lançamentos de Saída – Participante entidade privada;
* Lançamento de Saída – Entidade Pública: Corresponde a data a ser utilizada para seleção de Lançamentos de Saída – Participante entidade pública;

Cada um desses parâmetros poderá receber qualquer dos três valores determinados abaixo:

* Data de Emissão;
* Data de Entrada/Saída;
* Data de Pagamento/Vencimento.

Caso seja selecionada a terceira opção (Data de Pagamento/Vencimento) o sistema se comportará da seguinte forma:

* Se existir integração com o Financeiro, serão selecionados os Lançamentos Fiscais de acordo com a Data de Baixa do Lançamento Financeiro vinculado, entrando na seleção somente os Lançamentos Fiscais cujo Lançamento Financeiro associado esteja baixado e será considerada a data da primeira baixa;
* Se não existir integração com o Financeiro, serão selecionados os Lançamentos Fiscais de acordo com a Data de Vencimento, existente na aba "Dados Financeiros" do Lançamento Fiscal.

**Lançamentos Fiscais de Entrada**

A Legislação dos municípios para a seleção dos Lançamentos Fiscais de **entrada** é divergente. Algumas rezam que a declaração deve ser feita pela data de **emissão** do Documento Fiscal e outras rezam que a declaração deve ser feita pela data de **pagamento** do Serviço.

**Lançamentos Fiscais de Saída**

A seleção dos Lançamentos Fiscais de **saída** deve ser feita, em sua grande maioria, pela data de Emissão do documento fiscal, porém, no município de Belo Horizonte existe uma exceção: quando o destinatário da operação for um Órgão da Administração Pública a seleção deve ser feita com base na data de **pagamento** do serviço;

**Consistências na Inclusão/Alteração de Lançamentos Fiscais**

A consistência realizada na Inclusão/Alteração de Lançamentos Fiscais que possuam ISS foi feita de acordo com as Datas definidas nos parâmetros criados, mas, será verificado apenas o parâmetro de entrada de lançamentos, obedecendo à parametrização pré-definida.

**Consistência na Apuração do ISS**

Ao encerrar o período de apuração, também serão consistidos os parâmetros de seleção para a apuração do imposto, ou seja, somente serão apurados os lançamentos que obedeceram à parametrização.

---
