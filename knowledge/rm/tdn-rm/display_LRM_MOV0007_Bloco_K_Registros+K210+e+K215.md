---
content_hash: a8061ebf6439e8d586a956b19f5201931e879fa1af2728d405dd981f4ba5ee11
fetched_at: '2026-06-29T00:08:25.601970+00:00'
page_id: '270918914'
product: rm
source: tdn-rm
title: MOV0007_Bloco_K_Registros K210 e K215
type: documentation
url: https://tdn.totvs.com/display/LRM/MOV0007_Bloco_K_Registros+K210+e+K215
version: 111
---

# BLOCO K - REGISTROS K 210 E K 215

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção & Projetos |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Cópia por Referência | MovGeraCopiaReferenciaAction | |
| **Chamados Relacionados** | TVZXFP |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL e Oracle |
| **Tabelas Utilizadas:** | TMOTIVOREFMOV - Motivos de Cópia por Referência |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Esta melhoria tem como objetivo possibilitar ao usuário a geração dos registros de movimentação interna de desmontagem de estruturas e consequentemente viabilizar a geração dos Registros K 210 e K 215 do Bloco K conforme disposto no Ato COTEPE/ICMS 7 de 13 de maio de 2016.

O registro K210 tem o objetivo de escriturar a desmontagem no que se refere à saída do estoque do item de origem que sejam mercadorias dos tipos:

* 00 – Mercadoria para Revenda;
* 01 – Matéria-Prima;
* 02 – Embalagem;
* 03 – Produtos em Processo;
* 04 – Produto Acabado;
* 05 – Subproduto;
* 10 – Outros Insumos.

A quantidade deve ser expressa, obrigatoriamente, na unidade de medida de controle de estoque constante no campo 06 do registro 0200: UNID\_INV.

Quando houver identificação da ordem de serviço, a chave deste registro são os campos: COD\_DOC\_OS e COD\_ITEM\_ORI.  
Nos casos em que a ordem de serviço não for identificada, o campo chave passa a ser COD\_ITEM\_ORI. 

O Registro K210 irá obedecer ao layout abaixo: 

| Nº | Campo | Descrição | Tipo | Tam | Dec | Obrig |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "K210" | C | 004 | - | O |
| 02 | DT\_INI\_OS | Data de início da ordem de serviço | N | 008\* | - | OC |
| 03 | DT\_FIN\_OS | Data de conclusão da ordem de serviço | N | 008\* | - | OC |
| 04 | COD\_DOC\_OS | Código de identificação da ordem de serviço | C | 030 | - | OC |
| 05 | COD\_ITEM\_ORI | Código do item de origem (campo 02 do Registro 0200) | C | 060 | - | O |
| 06 | QTD\_ORI | Quantidade de origem – saída do estoque | N | - | 03 | O |

Onde serão efetuadas as seguintes validações:

* + Campo 01 (REG) - Valor Válido: [K210].
  + Campo 02 (DT\_INI\_OS) - Preenchimento: a data de início deverá ser informada se existir ordem de serviço, ainda que iniciada em período de apuração (K100) anterior. Validação: obrigatório se informado o campo COD\_DOC\_OS ou o campo DT\_FIN\_OS. A data informada deve ser menor ou igual a DT\_FIN do registro K100 (este campo não será gerado pelo TOTVS Gestão de Estoque, Compras e Faturamento).
  + Campo 03 (DT\_FIN\_OS) - Preenchimento: informar a data de conclusão da ordem de serviço. Ficará em branco, caso a ordem de serviço não seja concluída até a data de encerramento do período de apuração. Validação: se preenchido, DT\_FIN\_OS deve estar compreendida no período de apuração do K100 e ser maior ou igual a DT\_INI\_OP (este campo não será gerado pelo TOTVS Gestão de Estoque, Compras e Faturamento).
  + Campo 04 (COD\_DOC\_OS) – Preenchimento: informar o código da ordem de serviço, caso exista. Validação: obrigatório se informado o campo DT\_INI\_OS (este campo não será gerado pelo TOTVS Gestão de Estoque, Compras e Faturamento).
  + Campo 05 (COD\_ITEM\_ORI) - Validação: o código do item de origem deverá existir no campo COD\_ITEM do Registro 0200.
  + Campo 06 (QTD\_ORI) – Preenchimento: não é admitida quantidade negativa.

O registro K215 tem o objetivo de escriturar a desmontagem no que se refere à entrada do estoque do item de destino que seja mercadoria dos tipos:

* 00 – Mercadoria para Revenda;
* 01 – Matéria-Prima;
* 02 – Embalagem;
* 03 – Produtos em Processo;
* 04 – Produto Acabado;
* 05 – Subproduto e
* 10 – Outros Insumos.

Este registro é obrigatório caso exista o registro-pai K210 e o controle da desmontagem não for por ordem de serviço (campos DT\_INI\_OS, DT\_FIN\_OS e COD\_DOC\_OS do Registro K210 em branco). Nesse caso, a saída do estoque do item de origem e a entrada em estoque do item de destino têm de ocorrer no período de apuração do Registro K100.

A quantidade deve ser expressa, obrigatoriamente, na unidade de medida de controle de estoque constante no campo 06 do registro 0200: UNID\_INV.  
A chave deste registro é o campo COD\_ITEM\_DES.

O Registro K215 irá obedecer ao layout abaixo: 

| Nº | Campo | Descrição | Tipo | Tam | Dec | Obrig |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "K215" | C | 004 | - | O |
| 02 | COD\_ITEM\_DES | Código do item de destino (campo 02 do Registro 0200) | C | 060 | - | O |
| 03 | QTD\_DES | Quantidade de destino – entrada em estoque | N | - | 03 | O |

Onde serão efetuadas as seguintes validações:

* Campo 01 (REG) - Valor Válido: [K215]

* Campo 02 (COD\_ITEM\_DES) - Validação: o código informado deve ser diferente do campo COD\_ITEM\_ORI do Registro K210, e o código do item de destino deverá existir no campo COD\_ITEM do Registro 0200.

* Campo 03 (QTD\_DES) – Preenchimento: não é admitida quantidade negativa.

## Procedimento para Utilização

As movimentações internas que irão compor os Registros K 210 / K215 são originadas da desmontagem de uma estrutura ou semiacabado.

Para possibilitar a inclusão do processo de desmontagem no TOTVS Gestão de Estoque, Compras e Faturamento, será realizada a ampliação da rotina de "Cópia por Referência", que passa a atender ao processo de geração das movimentações internas relativas aos Registros K210 e K215. Assim, a partir da cópia por referência do movimento de baixa da estrutura de origem o sistema irá viabilizar a criação automática do movimento de entrada dos itens de destino, além de criar o vínculo entre estes movimentos.

Para a desmontagem do item de origem, que deve corresponder a uma estrutura ou semiacabado, poderá ser utilizado qualquer movimento de baixa (tipo 2.2) já atualmente em uso pela empresa, não sendo necessária nenhuma parametrização específica. Deverão ser informadas nesta movimentação de baixa as estruturas que sairão do estoque da empresa (itens origem) devido ao seu desmonte.

Para utilizar o processo de desmontagem através da cópia por referência, será necessário criar um novo tipo de movimento (1.2.XX) cuja movimentação será a responsável por efetuar a entrada dos novos itens (itens destino) gerados a partir da desmontagem (baixa) do item de origem. Este tipo de movimento deverá ter algumas parametrizações específicas que iremos descrever a seguir:

* Na Etapa 2 - *"Mov - Emitente/Destinatário"*, tanto o "Emitente" como o "Destinatário" deverão ser do tipo 'Empresa'.

* Na Etapa 4 -*"Mov. - Datas 1/2"* a data que estiver informada como "Data do Movimento Default" deverá estar parametrizada como 'Edita' ou 'Mostra'.   
    
  A "Data do Movimento Default" é a data que o sistema irá utilizar na geração dos Registros K210 e K215, ou seja, o sistema somente irá enviar estas movimentações para o bloco K caso a desmontagem ocorra durante o período de apuração do registro K100. Assim, serão enviados para os Registros K210 e K215 os movimentos de entrada dos itens gerados a partir da desmontagem, cuja data de movimento consta do intervalo do período de apuração do K100.

* Na Etapa 6 -*"Mov - Outros Dados"* o campo "Usar Cópia de Movimentos por Referência" deve estar marcado e o campo "Motivo de Referência" deverá estar preenchido com o motivo '29 - Desmontagem de Mercadorias'. Esse novo motivo de referência foi criado especialmente para esse processo e é através dele que o sistema irá identificar quais são os movimentos cujos itens devem ser enviados para os Registros K210 e K215.

Assim, o sistema localizará em determinado período quais foram os movimentos de entrada gerados por cópia por referência com o motivo 29, irá identificar os respectivos movimentos de baixa que os originaram e enviará respectivamente os produtos baixados para o Registro K210 e os produtos originários da desmontagem para o Registro K215.

* Na Etapa 40 - *"Estoque - Estoque 1/3"* deverá ser parametrizado o aumento do "Saldo Atual".

 

* Na Etapa 41 - *"Estoque - Estoque 2/3"* deverá ser parametrizado o efeito sobre o 'Saldo Financeiro' do Estoque, informando que o "Efeito sobre o Saldo Atual' é de aumento. Deverá também ser preenchido o código da 'Fórmula do Valor Financeiro'.

* Apesar da rotina do SPED Fiscal (da qual o Bloco K faz parte) ser gerada no TOTVS Gestão Fiscal, os lançamentos relativos aos Registros K 210 e K 215 serão enviados diretamente pelo TOTVS Gestão de Estoque, Compras e Faturamento, portanto os movimentos que irão gerar esses registros não serão escriturados e não conterão Natureza Fiscal. Sendo assim, não será necessário o preenchimento do CFOP do movimento e na Etapa 60 - *"Fis - Natureza"* os campos "Natureza" e "Natureza 2" deverão estar preenchidos com 'Não Edita'.

* Além disso, como este tipo de movimento é interno e consequentemente não será escriturado, o campo "Gera Escrituração" deverá estar desmarcado na Etapa 62 -*"Fis - Escrituração Fiscal 1/2"*.

 

Fique atento também aos demais parâmetros desse tipo de movimento, que devem ser preenchidos conforme os procedimentos de desmontagem realizados por sua empresa.

Após o tipo de movimento de entrada por Desmontagem de Mercadorias ter sido parametrizado e liberado para os devidos usuários (*"Serviços Globais > Segurança > Usuários > Sistema: Gestão de Estoque, Compras e Faturamento > Anexos > Permissões por Tipo de Movimento"*) as movimentações internas poderão efetivamente ser realizadas.

Conforme dito anteriormente, no TOTVS Gestão de Estoque, Compras e Faturamento, as movimentações que compõem os Registros K 210 e K 215 do Bloco K do SPED Fiscal serão sempre compostas por um movimento de saída e outro de entrada que serão vinculados através do processo de cópia por referência com motivo 29 (Desmontagem de Mercadorias).

Assim, o primeiro passo do procedimento é criar o movimento com a(s) estrutura(s) ou semiacabado(s) que será(ão) desmontado(s) e sua(s) respectiva(s) quantidade(s) de baixa. Para isso pode ser utilizado o tipo de movimento de baixa já comumente usado em sua empresa.

Após a movimentação de saída da estrutura ter sido criada, deve ser incluída a movimentação de entrada dos produtos destino, ou seja, os semiacabados ou componentes gerados a partir da desmontagem do item origem.

Selecione o processo para o qual o tipo de movimento foi criado (*"Estoque" , "Produção",**"Compras", "Outras Movimentações"*, etc.) vá à visão de movimentos e selecione o novo tipo de movimento criado.

Clique em*"Processos > Assistente de Cópia por Referência"*.

O sistema abrirá a tela inicial do *"Assistente de Cópia de Movimento por Referência"*. Clique em "Avançar".

Será apresentada a tela do *"Filtro Inicial para Seleção de Movimentos"*.

Clique no ícone "Incluir" para selecionar o movimento de baixa cuja cópia por referência será efetuada.

O sistema automaticamente abrirá a tela de lookup onde você deverá filtrar o movimento a ser copiado.

Informe o campo a ser filtrado e o respectivo valor, e o sistema preencherá a tela com os movimentos que atendem ao filtro informado.

Marque o movimento a ser copiado e clique em OK.

O sistema irá retornar à tela do *"Filtro Inicial para Seleção de Movimentos"* onde será apresentado o movimento selecionado.

Clique em "Avançar".

Para este tipo de Cópia por Referência poderá ser efetuada a cópia de apenas um movimento por vez, mas um mesmo movimento pode conter vários itens.

Caso seja selecionado mais de um movimento para ser copiado o sistema não permitirá, sendo exibida a seguinte mensagem:

Após escolher o movimento a ser copiado e clicar em 'Avançar', o sistema exibirá a tela com as estruturas que foram baixadas através do movimento selecionado.

Realize a expansão da estrutura para que o sistema apresente os seus semiacabados e/ou componentes.

Para isso marque a estrutura e clique no botão "Expandir Produto".

Ao ser selecionada a expansão do produto, o sistema apresentará a seguinte mensagem:

Caso você informe "Sim", optando pela expansão completa, o sistema apresentará em tela todos os níveis e subníveis da estrutura, chegando até o nível dos componentes definidos como matéria-prima. 

Já, se na mensagem você informar "Não", optando pela expansão parcial, ela será feita apenas até o primeiro nível da estrutura, e somente no movimento destino você poderá intervir expandindo os semiacabados e chegando até outros níveis da estrutura, caso necessário. 

Caso o processo de desmontagem tenha ocorrido sem problemas, basta clicar no ( x ) indicando que todos os componentes foram gerados adequadamente e clicar em 'Avançar' para prosseguir o processo.

 

Mas, se caso durante o processo de desmontagem tenha ocorrido algum problema e algum componente tenha sido danificado e impossibilitado de ir para o estoque, basta selecionar os componentes nesta situação, clicar no botão "Excluir", confirmar a exclusão, marcar os demais itens, que assim irão para o movimento destino e serão enviados ao estoque, e em seguida clicar em 'Avançar' para prosseguir o processo. 

 O sistema apresentará a tela de conclusão do Assistente para Cópia de Movimentos por Referência, contendo um resumo dos dados dos movimentos envolvidos na operação.

 Verifique os dados apresentados e estando todos corretos clique em "Executar", para que o sistema inicie o processo de geração do movimento de entrada dos componentes gerados a partir da desmontagem da estrutura.

O sistema abrirá então a tela contendo os dados do *"Cabeçalho"* do movimento de entrada que será gerado.

As informações serão automaticamente preenchidas conforme parametrizado no respectivo Tipo de Movimento.

Para verificar e/ou alterar alguma informação dos produtos originados da desmontagem clique em "*Itens*".

O sistema apresentará a tela com todos os produtos originados da desmontagem, e se for necessário alterar alguma informação, você poderá fazê-lo na própria grid dos itens de movimento.

Neste exemplo iremos alterar a quantidade do componente 07.74 para 3.

Após efetuar todas as alterações necessárias clique em 'OK'.

O sistema irá finalizar o processo, gravando o movimento de entrada com os dados gerados pela Cópia por Referência.

Na geração do Registro K215 do Bloco K do SPED Fiscal, o sistema levará os dados relativos aos movimentos gerados com Motivo de Referência 29 no período de apuração do SPED, e na geração do Registro K210 serão levados os dados dos movimentos que os originaram, ou seja, do Registro K210 constará a estrutura que foi desmontada (baixada) e do Registro K215 constarão os componentes gerados pela desmontagem da mesma (entrada via cópia por referência com motivo 29).

Assim, após terem sido gravadas todas as movimentações internas de desmontagem do período, o sistema estará apto a gerar os Registros K 210 e K 215 do Bloco K do SPED Fiscal no TOTVS Gestão Fiscal.

divs
