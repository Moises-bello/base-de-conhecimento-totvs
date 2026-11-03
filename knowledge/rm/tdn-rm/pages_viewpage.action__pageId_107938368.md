---
content_hash: c3f722a3776cc7c7815079e9604b83ee90533b5e5b2f2ad0865cccf88ecf60ce
fetched_at: '2026-06-29T00:05:54.361165+00:00'
page_id: '107938368'
product: rm
source: tdn-rm
title: COMO FAZER - TOMADORES DE SERVIÇOS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=107938368
version: 5
---

der

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Folha de Pagamento                     **Versão:**11.5X*,* 11.8X |
| **Processo** | **:** | Tomadores de Serviço |
| **Subprocesso** | **:** | Cadastro de Tomadores de Serviço |
| **Data da publicação** | **:** | 17/12/2013 |

**Como Fazer**

**Tomadores de serviço**

A utilização de tomadores consiste em relacionar os funcionários com as empresas que compram os serviços da empresa onde ele é registrado. Nesse processo o vínculo do funcionário, seus pagamentos e recolhimentos são efetuados pela empresa onde ele é registrado, porém os valores da prestação dos serviços e as empresas onde ele prestou serviço são informados no SEFIP.

Existem dois tipos de tipos de tomadores: construção civil e cessão de mão-de-obra. A construção civil na maioria dos casos está relacionada a obra administrada pela própria empresa, neste caso a empresa deve gerar uma GPS para cada obra (tomador). No caso da cessão de mão-de-obra não existe guia para cada tomador.

**Dependências**

Para que seja possível a consideração de cálculos por tomadores de serviço é preciso que alguns dados estejam informados no sistema.

**Cadastro de Clientes/Fornecedores**

Através do menu CADASTROS / CLIENTES/FORNECEDORES faça o cadastro das empresas/obras que tomarão os serviços. Informe os dados de identificação. 

**Atenção:**

A empresa atual e suas filiais, cadastradas no cadastro de seções, também devem ter um registro que as identifique como tomadores, pois essa informação é necessária para geração do SEFIP e GPS.

**Global**

Marque este campo caso queira que o registro atual seja visualizado em outras coligadas.

**Classificação**

Informe se o registro atual é de um cliente, um fornecedor ou pode ser os dois casos.

**Categoria**

Informe se o registro é referente a uma pessoa física ou pessoa jurídica (empresa). No caso de pessoa física o sistema habilitará compôs para informação de outros dados como: data de nascimento, número de dependentes, etc.

**CPF/CNPJ**

Informe o número do documento legal que identifica o tomador. No caso de empresa identificada por CEI o mesmo deve ser informado neste campo, apesar de existir um campo específico para CEI.

**Ativo**

O sistema só faz processamentos para Clientes/Fornecedores ativados.

**Dados ficais**

Nesta pasta informe os dados utilizados nas guias de recolhimento de INSS e FGTS. Informe o “Tipo de tomador” e o “Código de pagamento de GPS”.

**Parâmetros do sistema**

Acesse o menu CONFIGURAÇÕES | PARÂMETROS | PARAMETRIZADOR | FOLHA DE PAGAMENTO | FOLHA NORMAL | TOMADOR DE SERVIÇOS, na pasta “Param. Cálculo” para e marque o campo “Utiliza tomadores de serviço”. A partir desse momento o sistema passará considerar os tomadores na geração do INSS e FGTS, porém é preciso informar alguns dados.

**Código da Fórmula da Fator de Proporcionalização**

A fórmula de proporcionalizacão não é obrigatória, sem sua informação o sistema sempre calculará 30 dias, independente se o código do recebimento é mensalista ou horista.

**Código da Empresa no cadastro de Tomadores**

Informe o código do Cliente/Fornecedor que identifica a empresa atual. Os funcionários que não prestam serviços em tomadores serão relacionados ao tomador que é a própria empresa.

**Observação:**

No caso de filiais, os funcionários que não prestam serviços em tomadores deverão ter o tomador que identifica a filial informada em seus cadastros.

**Tipo de tomador default**

Informe o tipo de tomador a ser considerado como default na geração do SEFIP.

**Meses de distribuição guardados, para geração do SEFIP em atraso**

Informe a quantidade de meses que distribuídos que ficarão guardados no sistema. Isso se deve ao fato de que o sistema não permite fazer distribuições de valores de meses anteriores.

**Distribuição de eventos por tomador via entrada de dados**

Marcando essa opção será habilitada em MOVIMENTO / FOLHA DE PAGAMENTO / ENTRADA DE DADOS (TOMADOR), onde será possível fixar um evento e valor a um determinado tomador de serviço.

**Seções**

Para utilização de tomadores do tipo cessão mão-de-obra não é necessário nenhuma parametrização no cadastro de seções, porém, para empresas que administram obras, devem existir cadastradas seções que permitam identificar separadamente as seções que são da área administrativa (não são obras) e as seções que são obras.

Uma empresa pode ser identificada pó CPF ou CNPJ (no caso de CPF existe um CEI que identifica a própria empresa), e cada obra é identificada por um número de CEI. Uma empresa pode ter diversos CNPJ, no caso de filiais, uma filial também pode ser administradora de obras. Dessa forma cada CNPJ deve ter identificadores que permitam a centralização dos funcionários não alocados em obras e identificadores para cada obra.

**Exemplo:**

CNPJ Matriz 21.867.387/0001-58

CNPJ Filial 21.867.387/0003-10

Obra 1, relacionada a matriz, CEI: 11.111.11.111/11

Obra 2, relacionada a filial, CEI: 22.222.22.222/22

Obra 3, relacionada a filial, CEI: 33.333.33.333/33

Para este exemplo deve existir uma quebra que identifique a mudança de CNPJ e uma quebra que identifique a centralização do administrativo e das obrasem cada CNPJ.

O cadastro de seções poderia ter a seguinte configuração:

01 – Matriz

01.001 – Administrativo matriz

01.001.01 – Departamento Administrativo

01.001.01.001 – Setor financeiro

01.001.01.002 – Setor de Pessoal

01.001.02 – Departamento operacional

01.001.02.001 – Produção

01.002 – Obra 1 (CEI 11.111.11.111/11)

01.002.01 – Coordenação

01.002.01.001 – Engenheiros

01.002.01.002 – Encarregados

02 - Filial

02.001.01 – Departamento Administrativo Filial

02.001.01.001 – Setor financeiro

02.001.01.002 – Setor de Pessoal

02.001.02 – Departamento operacional

02.001.02.001 – Produção

02.002 – Obra 2(CEI 22.222.22.222/22)

02.002.01 – Coordenação

02.002.01.001 – Engenheiros

02.002.01.002 – Encarregados

02.003 – Obra 3(CEI 33.333.33.333/33)

02.003.01 – Coordenação

02.003.01.001 – Engenheiros

02.003.01.002 – Encarregados

**Notas:**

- Os cadastros que começam com 01 são relacionados a matriz;

- Os cadastros que começam com 02 são relacionados a filial;

- Os cadastros que começam com XX.001 são relacionados ao pessoal administrativo (não alocado em obra);

- Os cadastros que tem a estrutura inicial (6 dígitos) diferentes de XX.001 são relacionadas as obras.

Em OPÇÕES / PARÂMETROS / GLOBAIS, na pasta “Seções” o cadastro deveria ser feito como:

Máscara: ##.###.##.###

Quebra de CNPJ: ??

Quebra mestre: ?????????????

Campo “Utiliza CEI” marcado

Código de quebra para CEI: ?????? (indica a alteração de dados que identificam as seções administrativas e as obras).

**Observação:**

Quando a empresa utiliza seções identificadas por CEI, no cadastro de seções que utilizam CEI o campo “CEI” deve estar preenchido e o campo “Identificação pelo CNPJ” deve estar desmarcado.

**Eventos**

No cadastro dos eventos marque o campo “Segue rateio de tomadores” para que os eventos sejam proporcionalizados por tomador.

**Observação:**

Alguns eventos não precisam ter o campo marcado. Um destes eventos é o evento de licença maternidade.

**Cadastro de funcionários**

Acesse o cadastro do funcionário que utilizará tomador de serviço e localize a pasta “Tomadores de serviço”. Informe o código do tomador ou selecione-o através da listagem apresentada. Informe também o tipo de tomador.

**Valor**

Informe a quantidade de dias que o funcionário trabalho no tomador. A soma dos dias de todos os tomadores do funcionário não pode ultrapassar 30 dias.

**Observações:**

- Um funcionário pode não ter tomadores ou pode ter vários.

- Para os funcionários que não prestam serviço em tomadores não é preciso informar o tomador em seu cadastro, pois o sistema considerará o tomador informado como global em CONFIGURAÇÕES | PARÂMETROS | PARAMETRIZADOR | FOLHA DE PAGAMENTO | FOLHA NORMAL | TOMADOR DE SERVIÇOS. Fique atento no caso de utilização de filiais, pois os funcionários da filial deverão ter o tomador que identifica a filial.

**Cálculos**

Os cálculos da folha não são efetuados por tomadores, como acontece com os cálculos por centro de custo. O cálculo de valores por tomador é feito após o cálculo da folha, e os eventos não são recalculados, apenas tem seus valores proporcionalizados conforme os dias trabalhados em cada tomador.

**Lançamentos da folha**

Quando um evento é inserido na movimentação do funcionário através das opções de: envelope de pagamento, grupo de eventos, cálculos de férias, rescisão e 13º salário, o sistema não faz nenhum tratamento quanto ao valor a ser proporcionalizado para cada tomador. A proporcionalizacão é feita a través de um módulo específico para distribuições.

**Entrada de dados por tomador**

Para habilitar a opção de entrada de dados por tomador acesse o menu CONFIGURAÇÕES | PARÂMETROS | PARAMETRIZADOR | FOLHA DE PAGAMENTO | FOLHA NORMAL | TOMADOR DE SERVIÇOS e marque a opção “Distribuição de eventos por tomador via entrada de dados”. Após ser marcado o parâmetro o sistema habilitará o menu MOVIMENTO / FOLHA DE PAGAMENTO / ENTRADA DE DADOS (TOMADOR). Através deste módulo será possível informar eventos diretamente associados aos tomadores.

**Exemplo:**

O funcionário está alocado em 2 tomadores (C00001 e C00002), porém fez horas extras apenas no tomador C00001. Através deste módulo será possível informar que as horas extras foram feitas neste tomador.

Alguns parâmetros são semelhantes aos parâmetros aos do módulo de entrada de dados já apresentado em outro módulo.

**Código do tomador a fixa**

Caso queira fixar um tomador, para evitar a digitação a cada funcionário, informe neste campo seu código.

**Tela de entrada de dados**

Esta tela é semelhante a tela de entrada de dados do módulo “Entrada de dados”, porém existem alguns campos que precisam ser preenchidos.

**Tomador**

Informe o código do tomador.

**Colig. Tomador**

Informe a coligada onde o Cliente/Fornecedor está cadastrado.

**Distribuição de valores**

O módulo de distribuição tem a função de proporcionalizar os valores dos eventos de acordo com os tomadores informados nos cadastros dos funcionários.

**Exemplo:**

O funcionário tem em seu cadastro dois tomadores, como descrito abaixo.

C00001 – Tomador 1 – 10 dias

C00002 – Tomador 2 – 20 dias

Foram lançados para os funcionários os eventos abaixo (através do lançamento de grupos de eventos).

0002 – Dias Trabalhados = R$ 3000,00

0082 – Horas extras         = R$ 1500,00

Através do módulo de entrada de dados foi lançado o evento abaixo, para o mesmo funcionário, porém para o tomador C00003.

0083 – Adicional noturno = R$ 333,33

Ao ser processado o módulo de distribuição os dados dos tomadores ficarão da seguinte forma.

0002 – Dias trabalhados – C00001 = R$ 1000,00 (3000 / 30 \* 10)

0002 – Dias trabalhados – C00002 = R$ 2000,00 (3000 / 30 \* 20)

0082 – Horas extras – C00001 = R$ 500,00

0082 – Horas extras – C00002 = R$ 1000,00

0083 – Adicional noturno – C00003 = R$ 333,33

O evento 0083 não foi proporcionalizado como os outros eventos pois a sua informação ocorreu através da entrada de dados por tomador.

**Atenção:**

Caso o funcionário tenha mudado de tomador, antes de ser feita a distribuição execute a liberação de Flags.

**Liberação de competência**

Após ter sido efetuado a liberação da competência, não é possível fazer a distribuição de valores do mês anterior, portanto esteja atendo ao número de meses de distribuição que ficarão guardados (parâmetro “Meses de distribuição guardados, para geração de SEFIP em atraso”, em EM CONFIGURAÇÕES | PARÂMETROS | PARAMETRIZADOR | FOLHA DE PAGAMENTO | FOLHA NORMAL).

**Observação:**

Caso o número de meses seja muito grande e a base de dados tiver muitos funcionários, a performance do sistema pode ser mais lenta.

**Relatórios**

Após o cálculo e distribuição de valores é preciso gerar os relatórios com os dados calculados por tomadores.

**Folha analítica (gerador de relatórios)**

Para imprimir a folha analítica por tomadores é preciso acessar o menu RELATÓRIOS / GERADOR e localizar o relatório 2.001.004. Para impressão dos dados, informe no filtro, o mês e ano da distribuição e a situação dos funcionários.

**SEFIP**

A geração do SEFIP, para empresas que trabalham com tomadores, segue as mesmas regras do SEFIP, já apresentadas em outro módulo. Apresentaremos neste módulo apenas as considerações que diferem do SEFIP normal ou que têm tratamentos diferentes.

**Código de Recolhimento**

Os códigos de geração de SEFIP por tomador são o 150 (para cessão de mão-de-obra) e 155 (para construção civil). Não há necessidade de separar o pessoal do administrativo em SEFIP 115, isto deve ocorrer apenas em casos específicos, conforme determinação da CAIXA.

Os códigos de recolhimento 650 e 660 não geram informações de tomadores. Para saber mais, consulte o manual do SEFIP.

**Período**

O SEFIP é uma informação do FGTS do mês, portanto a forma correta de prestar as informações do SEFIP é utilizar os períodos todos. Caso seja selecionado um período específico os funcionários aparecerão no SEFIP com ocorrência de múltiplos vínculos.

**Atenção:**

Se um funcionário trabalhou em mais de um tomador o SEFIP considerará que sua movimentação é de múltiplos vínculos.

**Cálculo dos valores**

Clique no botão “Calcula valores” para que o sistema faça a verificação da existências de valores para tomadores e possibilite a prestação de informações de compensações, retenções, etc.

Após o cálculo o sistema habilita a pasta “Centralizadores” com os registros das empresas (matriz e filiais) e os registros de tomadores. Os registros de dados da empresa tem “Tipo de registro” 10, os tomadores tem o tipo 20.

Clique duas vezes no registro de tomador, será habilitada a pasta”Valores do centralizador XX”.

**Valores do centralizador**

**Valores I**

Nesta pasta são informados alguns dados importantes como: “Total do salário família” (pode ser para empresa ou tomador), “Ded. 13ª lic. Mat” e “Salário maternidade” (para dedução do salário maternidade, somente para empresa). Estes três campos são preenchidos automaticamente pelo sistema.

**Valores II**

Informe nesta pasta os dados de recolhimento referente às competências anteriores, caso existam, e os dados de fátuas de tomadores.

**Retenção de valores**

Os valores retidos para tomadores, em notas fiscais, devem ser informados no campo “Valor retenção (Lei 9711/98)”.

**Geração do arquivo**

Após serem informados os dados necessários ao SEFIP, clique no botão “Gerar SEFIP”, para geração do arquivo.

**ATENÇÃO:**

Caso o sistema não esteja gerando o arquivo do SEFIP, verifique se a distribuição foi feita corretamente.

**Guia de INSS**

A GPS para empresas que trabalham com tomadores do tipo cessão de mão-de-obra não existe diferenciação do INSS, porém para empresas que trabalham com tomadores do tipo construção civil, o sistema permite a geração da GPS por tomador.

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[R@RH](https://totvs.byyou.com/?space=rrh)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 4 – (Recursos Humanos)

*Publicador: Joyce Nereu*

*Código: LAB-00003*
