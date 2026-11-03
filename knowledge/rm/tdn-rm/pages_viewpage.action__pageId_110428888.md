---
content_hash: 09fe85cef5ac62f0af9818a7f80945a2f24ffeafe801690df2b123424c6bc554
fetched_at: '2026-06-29T00:05:54.803989+00:00'
page_id: '110428888'
product: rm
source: tdn-rm
title: Parametrização para Contabilização - 11.0
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=110428888
version: 1
---

Avaliação

A principal finalidade da Contabilidade é fornecer informações sobre o Patrimônio de ordem econômica e financeira, que facilitam assim as tomadas de decisões, tanto por parte dos administradores ou proprietários, como também por parte daqueles que pretendem investir na empresa.

Solução

**Noções básicas de Contabilidade:**

**Conta:**

As contas são utilizadas para se efetuar os registros contábeis e cada conta é distinguida das demais pela sua denominação.

**Convenções para registro: Débito e Crédito**

As transações ocorridas numa empresa podem ocasionar aumentos ou diminuições nos bens, direitos, obrigações e no resultado, que são verificados através de lançamentos chamados de débito e crédito.

DÉBITOS = aplicações

CRÉDITOS = origem

Geralmente, os que desconhecem a matéria são levados a pensar que débito significa algo desfavorável. Na realidade, isto não ocorre, pois débito e crédito são termos técnicos.

**Ex**. Debito: salários (+) aumento da conta salário

Crédito: Caixa (-) diminuição na conta caixa

**Importante:**

- Os valores de débitos sempre corresponderão a um crédito de igual valor.

- Não há débito sem crédito

Para identificar mais facilmente a conta a ser debitada e a conta a ser creditada, observe as notas a seguir:

**I- Para elementos Patrimoniais**

a. Toda vez que aumentar o Ativo, DEBITAR a respectiva conta.

b. Toda vez que diminuir o Ativo, CREDITAR a respectiva conta.

c. Toda vez que aumentar o Passivo, CREDITAR a respectiva conta.

d. Toda vez que diminuir o Passivo, DEBITAR a respectiva conta.

**II- Para os elementos de Resultado:**

e. Toda vez que ocorrer uma Despesa, DEBITAR a respectiva conta.

f. Toda vez que se realizar uma Receita, CREDITAR a respectiva conta.

**Ativo e Passivo:**

Os capitais próprios e de terceiros, representado do lado do passivo, são aplicados na empresa em Bens e Direitos, conforme demonstra o lado do ativo. Portanto os recursos que a empresa utilizou.

**Formas de contabilização**

**Existem 3 formas de contabilização no sistema TOTVS Folha de Pagamento.**

**Contabilização por seção:**

A contabilização por seção é mais comum. Exige como condição que o nível de detalhamento do plano de contas seja aplicável a todos os funcionários de uma mesma seção.

**Contabilização por funcionário:**

A contabilização por funcionário é necessária quando o nível de detalhamento do plano de contas exige uma distribuição dos valores que não pode ser determinada pela seção e quando a empresa não usa a distribuição por centro de custos.

**Contabilização por centro de custo:**

Exige como condição que o nível de detalhamento do plano de contas seja aplicável a todos os funcionários de um mesmo centro de custo. É necessário indicar na pasta rateio fixo da base de cálculo na ficha individual de cada funcionário o percentual ou valor de rateio para cada centro de custo, mesmo que o funcionário trabalhe 100% em um só centro de custo.

**Obs:** Na contabilização por centro de custo, o sistema passa a enxergar os dados contábeis registrados em Cadastros I Centros de custos (RM Labore), ignorando qualquer informação registrada em Cadastros I Seções.

Dentre todas as formas de contabilização é possível utilizar **Contabilização parcial:**

O campo Contabilização Parcial(\*) em Cadastros I Eventos I Dados contábeis, indica que é desejada a contabilização de crédito OU a débito, a parte ausente será contabilizada posteriormente de uma outra forma. Quando este campo não está marcado, obrigatoriamente deve-se informar o grupo de crédito E de débito.

**Módulos relacionados ao processo de contabilização**

**Opções | Parâmetros | RM Labore**

Neste módulo as principais informações verificadas são as informações de utilização de centro de custo “Utiliza cálculo por centro de custo”, na pasta “Param cálculo”. Na pasta “Outros parâmetros | Parâmetros II” são verificados os parâmetros de contabilização.

**Cadastros | Contabilização | Parâmetros do RM Saldus**

Neste módulo são definidas as regras da contabilização, mesmo para quem não utiliza o sistema Saldus (TOTVS Gestão Contábil).

**Cadastros | Contabilização | Histórico Padrão**

A implantação de históricos-padrões tem como finalidade a utilização de expressões iguais para o registro de fatos semelhantes. Deverá atender a ambas as contas envolvidas no lançamento, ou seja, conta devedora e conta credora.

**Cadastros | Contabilização | Plano de contas contábeis (RM Saldus) e Cadastros |Contabilização | Plano de contas Gerenciais (RM Saldus)**

Neste módulo são cadastradas as contas que serão utilizadas pelo sistema. É importante que as contas estejam agrupadas por natureza, para facilitar a identificação e geração de relatórios.

Por exemplo: as contas do ativo começam com 1, as do passivo com 2 e assim por diante. Existem algumas definições dos conselhos de contabilidade sobre a estruturação das contas.

**Cadastros | Tabelas dinâmicas**

Neste módulo estão cadastradas as tabelas dinâmicas utilizadas na contabilização. Para inserir itens clique na aba “Itens da tabela”. Abaixo está a definição de cada tabela utilizada.

**INT01 *-*** Diversos Usos Internos (não permite inclusão de itens)

Tipos possíveis de encargos

**INTCONTFUN -** Uso interno do sistema (permite inclusão de itens)

Códigos Para Integração Contábil de Funcionários

**INTGERFUN -** Uso interno do sistema (permite inclusão de itens)

Códigos Para Integração Gerencial de Funcionários

**PCODATIVO -** Uso interno do sistema (permite inclusão de itens)

Códigos Encargos Ativos

**CODINTCONT -** Uso interno do sistema (permite inclusão de itens)

Códigos Para a Integração Contábil

**CODINTGER -** Uso interno do sistema (permite inclusão de itens)

Códigos Para a Integração Gerencial

**GRPCONT -** Uso interno do sistema (permite inclusão de itens)

Grupos de Contas Contábeis

**GRPGER -** Uso interno do sistema (permite inclusão de itens)

Grupos de Contas Gerenciais

**Cadastros | Contabilização | Agrupamento de contas contábeis (RM Labore) e Cadastros | Contabilização | Agrupamento de contas gerenciais (RM Labore)**

O sistema contábil não tem informações de eventos, seções, encargos e funcionários. Para que a contabilização seja gerada corretamente é preciso fazer um relacionamento dos dados da Folha de Pagamento, agrupamentos e integrações, com a conta contábil.

**Grupo Conta -** Refere-se a um item da tabela dinâmica GRPCONT. É informando no cadastro do evento ou encargo, aba Dados Contábeis.

**Código de Integração -** Refere-se a um item da tabela dinâmica CODINTCONT ou CODINTGER para contabilização gerencial. É informado no cadastro da Seção ou Centro de Custo, aba Dados Contábeis.

**Código de Integração Por Funcionário -** Refere-se a um item da tabela dinâmica INTCONTFUN ou INTGERFUN para contabilização gerencial. É informado no cadastro do funcionário, aba Base de Cálculo | Dados contábeis.

**Conta contábil – Saldus -** Item da tabela CCONTA, cadastrado em Cadastro | Contabilização | Plano de contas contábeis (RM Saldus).

**Filial -** Item da tabela GFILIAL, cadastrado em Cadastros I Filiais.

**Centro de Custo -** Item da tabela PCCUSTO, cadastrado em Cadastro | Centros de custos (RM Labore).

**Obs :**

- No processo de criação dos agrupamentos deve-se definir a utilização de integração, poderão ser criados diversos agrupamentos para um mesmo grupo de conta, desde que a integração seja diferente.

- A integração é utilizada quando um mesmo evento, ou encargo, deve ser lançado em contas diferentes, dependendo da seção ou centro de custo utilizado. Agrupa informações de uma mesma natureza ou procedência.

**São três tipos de integração:**

- Por seção: para quem não trabalha com cálculo por centro de custo relacionado ao funcionário;

- Por Centro de custo: para quem tem o centro de custo relacionado ao funcionário;

- Por funcionário: Cada funcionário tem sua integração.

**Cadastros | Eventos**

No cadastro de eventos a serem contabilizados, devem ser informados os dados contábeis necessários.

Os campos de conta para débito e conta para crédito devem ser preenchidos com os grupos já existentes na base de dados, tabela dinâmica GRPCONT. Se for utilizar integração contábil é preciso marcar a opção de integração contábil ou por funcionário.

Definir qual histórico será utilizado no lançamento em questão (os itens desta tabela são cadastrados em Cadastros | Contabilização | Histórico Padrão – tabela CHISTP).

O complemento do histórico é um campo texto com até 60 caracteres que pode ser informado para complementar o campo anterior.

**Cadastros | Contabilização | Encargos**

De acordo com a legislação tributária brasileira, encargos são aquelas despesas do exercício que normalmente devem ser contabilizadas, sem estarem com os valores totalmente definidos em termos monetários (somente quando pagas ou creditadas na forma da lei é que esse fato se dará, o que deve ocorrer total ou parcialmente em períodos subsequentes ao da competência ou do mês em que ela se iniciou).

Para parametrização dos encargos acesse o módulo e crie quantos encargos forem necessários informando os dados contábeis. Cada encargo deve ter um código e um título que o identifique.

**Tipo de encargo**

Selecione o tipo de encargo. Trata-se de tabela dinâmica (INT01) que já tem tipos pré-definidos.

**Observação:**

Em conformidade com o disposto no artigo 2º da Lei 10.097/00, onde altera o artigo 15º da Lei 8036/90, que determina que os contratos de aprendizagem com admissão a partir de 20/12/2000 tenham sua alíquota do FGTS reduzida de oito por cento para dois por cento. Fique atendo a criar os encargos de FGTS de menores aprendizes separadamente do restante dos demais funcionários.

**Porcentagem**

Alguns encargos são gerados com valores fixos ou podem ter percentuais definidos. Os tipos que permitem a informação de percentuais permitem que o campo fique habilitado.

**Fórmula de seleção**

Informe a fórmula para selecionar os funcionários que participarão do cálculo do encargo.

Exemplo de utilização:Para que os funcionários aprendizes não entrem no cálculo do FGTS 8%.

**Fórmula de valor**

Este campo ficará habilitado apenas para os encargos do tipo “A” (calculados por fórmula).

**Aplicar arredondamento sobre o valor total do encargo**

Com este parâmetro, o cálculo do encargo para cada funcionário é realizado sem arredondamento, para que seja aplicado o arredondamento sobre o valor total.

Este parâmetro garante, por exemplo, que os valores gerados na GPS sejam idênticos àqueles gerados na contabilização, desde que as quebras entre os lançamentos contábeis sejam os mesmos da Guia de INSS.

**Provisão Acumulada**

Selecione esta opção se pretender gerar a contabilização da provisão acumulada para os encargos do tipo "4" (Provisão de Férias), "5" (Provisão de FGTS de Férias), "6" (Provisão de Encargo de Férias), "7"(Provisão de 13º Salário"), "8" (Provisão de FGTS de 13º salário) e "9" (Provisão de encargos 13º salário). Não selecionando, será gerada a provisão mensal.

**Acumulado x Mensal**

Provisão acumulada é o valor que deveria ser pago na data atual e provisão mensal é o valor da provisão acumulada atual menos o valor da provisão acumulada do mês anterior.

**Exemplo:**

Provisão acumulada mês 08/2010: R$ 1.100,00

Provisão acumulada mês 09/2010: R$ 1.200,00

Valor da provisão mensal do mês 10/2010: R$ 100,00

**Considera Centro de Custo da Seção Anterior**

Este parâmetro permite o estorno das provisões de férias e 13º salário. O estorno de provisão é geralmente aplicado na situação em que funcionário estava em centro de custo diferente do atual no mês anterior. Sendo assim, o funcionário que foi transferido de seção (não mudou de CGC) e mudou do centro de custo X para Y, ao gerar a contabilização do encargo de provisão ocorrerá o estorno da provisão do mês anterior.

Para que seja efetuado o estorno deverão ser criados dois encargos. O primeiro encargo, com a opção "Considera Centro de Custo da Seção Anterior" marcada e efetuando o débito (estorno) no centro de custo ligado à seção onde o funcionário estava lotado anteriormente. O segundo encargo, com a opção "Considera Centro de Custo da Seção Anterior" desmarcada e efetuando o crédito no centro de custo ligado à seção atual do funcionário.

Estes encargos deverão utilizar fórmula de seleção para filtrar funcionários que tenham mudança de centro de custo, e ambos utilizarão a fórmula de cálculo que retorne o valor da provisão acumulada da competência anterior.

**Atenção:**

Este parâmetro só será habilitado para o encargo do tipo A – Valor calculado através de fórmula e se o parâmetro "Utiliza Cálculo por Centro de Custo" (Opções | Parâmetros | RM Labore, pasta “Param. Cálculo”) estiver desmarcado. Essa opção só considera alterações onde o centro de custo é informado na seção e não no cadastro do funcionário.

**Códigos ativos**

Permite o agrupamento de encargos com mesmas finalidades ou tipos. Dessa forma, no momento da geração do encargo ou da contabilização, é possível selecionar quais tipos de encargos serão processados. Para criar um novo tipo, acesse as tabelas dinâmicas e localize a tabela com código PCODATIVO.

**Dados contábeis**

Dados a serem utilizados no momento da contabilização.

Atribuir um dos itens da tabela GRPCONT ou GRPGER (esta última para contabilização gerencial)

Se for utilizar integração contábil é preciso marcar a opção de integração contábil ou por funcionário.

Definir qual histórico será utilizado no lançamento em questão (os itens desta tabela são cadastrados em Cadastros | Contabilização | Histórico Padrão – tabela CHISTP).

O complemento do histórico é um campo texto com até 60 caracteres que pode ser informado para complementar o campo anterior.

**Cadastros | Centros de Custo**

Neste módulo deverão ser informados os Centros de custos globais. Esses são utilizados na integração com outros sistemas da TOTVS.

**Cadastros | Centros de Custo (RM Labore)**

Neste módulo devem ser informados os centros de custo que serão utilizados no TOTVS folha de pagamento. A cada centro de custo RM Labore criado deverá ser associado o centro de custo Global.

**Rotinas | Geração de Encargos**

Os encargos podem ser gerados por esse módulo ou no momento da contabilização.Informe as opções de seleção e os dados para realização dos cálculos.

**Competência**

Informe o mês, ano e período de geração do encargo.

**Permite valores negativos para fórmulas**

Marque esta opção caso algum encargo seja calculado por fórmula e queira considerar o valor mesmo que seja negativo.

**Códigos de encargos ativos**

Informe os tipos de encargos que serão gerados.

**Consulta dos valores**

Acesse o menu Cadastros | Contabilização | Histórico de Encargos, para visualizar, alterar ou excluir os encargos.

**Rotinas | Contabilização**

Neste módulo deverão ser feitas as seleções de funcionários, mês e ano de competência dos dados a serem contabilizados e o período da folha a ser contabilizado.

**Lote e Descrição**

Informe o número do lote contábil que será gerado e sua descrição. Caso seja informado um lote já existente o sistema emitirá uma mensagem para sobrescrevê-lo ou não.

**Contabilizar eventos**

Marque esta opção para contabilizar os eventos que tem informações contábeis.

**Contabilizar encargos**

Marque esta opção para contabilizar os encargos que tem parametrizações contábeis.

Marcando este parâmetro o sistema abrirá uma tela para seleção dos tipos de encargos ativos a serem contabilizados.

**Usa encargos já calculados**

Esta opção estará disponível apenas para contabilização de encargos. Caso a contabilização seja de meses anteriores, onde os encargos já foram calculados, é recomendável que este campo esteja marcado, pois se existirem encargos calculados por fórmula o valor contabilizado será o resultado da fórmula atual.

**Permite valores negativos para fórmulas**

Este parâmetro não permite que o sistema envie à contabilização valores negativos. Isto é válido somente para os encargos tipo “A” (valor calculado através de fórmula).

Para eventos e encargos, se o resultado for negativo o sistema inverte as contas de crédito/débito informadas nos eventos ou nos encargos. Além disto, se o resultado for zero não é gerado nenhum lançamento para a contabilização.

**Data contabilização**

O sistema traz a data corrente. Você pode alterá-la, se necessário.

**Observação:**

Caso utilize a integração com o sistema contábil da TOTVS, o sistema apresentará uma mensagem alertando o usuário caso a data de contabilização esteja fora do “Período Contábil” do sistema TOTVS Gestão Contábil.

**Tipo de documento no lançamento**

Neste campo, o usuário poderá selecionar qual o tipo de informação será enviada para o campo "Documento" do lançamento contábil: Competência ou Nº do Lote.

**Cadastros | Contabilização | Lançamentos Contábeis**

Nesta tela são apresentados os dados dos lotes gerados, como total de débitos e créditos.

Na parte inferior da tela são apresentados os detalhes de cada lote. Os valores apresentados são agrupados por conta débito/crédito, centro de custo, histórico padrão e departamento.

**IMPORTANTE: A forma de parametrização da contabilização gerencial é idêntica a parametrização contábil da folha, porém voltada para uma visão gerencial.**

**Exemplo da parametrização da contabilização de um evento por centro de custo: (O mesmo tratamento pode ser feito ao contabilizar por seção, verificar a integração no cadastro de seção ao invés do centro de custo)**

Os funcionários associados ao centro de custo 01.1 terão o valor de salário contabilizado na conta contábil 1.1.1.1.001, porém os funcionários que estão associados ao centro de custo 01.2 terão o mesmo evento contabilizado na conta contábil 1.1.1.1.002. Como se trata do mesmo evento em contas diferentes a parametrização do agrupamento seria:

***Obs :*** *A demonstração abaixo é sobre os campos de grupo de conta, integração e conta contábil. Os outros campos devem ser preenchidos de acordo com a regra da empresa.*

No evento de salário, informar o grupo da conta e marcar a opção “Tem integração contábil”.

Informar no centro de custo 01.1 um código de integração diferente do informado no centro de custo 01.2.

Cadastrar dois agrupamentos em Cadastros I Contabilização I Agrupamentos de contas contábeis, da seguinte forma:
