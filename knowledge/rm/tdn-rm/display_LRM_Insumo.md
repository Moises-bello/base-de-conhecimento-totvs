---
content_hash: 5655160d4710d101371ace427422db0eba3d31e51048b859408b3fa9358fb951
fetched_at: '2026-06-29T00:10:56.070961+00:00'
page_id: '590615598'
product: rm
source: tdn-rm
title: Insumo
type: documentation
url: https://tdn.totvs.com/display/LRM/Insumo
version: 14
---

Nesta visão serão apresentados os insumos cadastrados, conforme o filtro utilizado, no lado direito da tela pode-se alternar, utilizando os anexos, entre os preços do insumo, serviços ao qual o insumo foi associado ou tarefas ao qual o insumo está associado.

Quando estamos visualizando as composições nas quais o insumo está inserido, através de um clique duplo pode-se editar as mesmas e alterá-las. O campo do insumo "Valor c/ leis" sempre estará calculado independente de qual forma de aplicação de lei social estiver selecionada no parâmetro.

Os filtros para seleção dos insumos são válidos para todos os projetos. Os insumos globais podem ser editados num projeto local, mas somente alguns campos ficam disponíveis para alteração. Quando é feita a edição de um insumo, para alterar os preços do mesmo, as informações modificadas no insumo serão salvas automaticamente.

InsumoIdentificaçãoCamposCampos

**Código:** Informe o código do insumo, campo obrigatório. Este campo deve ser preenchido de acordo com a máscara definida em "Projeto | Construção & Projetos | Projetos F6 | Exibição | Mascara".

**Observação**: é recomendado que a mesma mascara aplicada aos insumos globais, seja a mesma dos insumos locais de seus projetos. Pois, se for cadastrado uma mascara "maior" para insumos globais, e "menor" para insumos locais, na pesquisa do campo código será exibido apenas a quantidade de caracteres definida na mascara do projeto.

**Tipo do Insumo:** Informe o tipo do insumo, como Normal, Derivado ou Receita.

Insumo Normal – Será tratado como um insumo comum, com hoje é tratado no sistema.

Insumo Derivado - Caso for este o tipo do insumo, uma aba chamada Insumo Derivado fica habilitada para que seja informados o tipo da derivação, a prioridade de cálculo e a regra de derivação.

Insumo Receita - Este Insumo será usado somente em associações diretas com serviço e o valor dele quando associado será considerado somente para derivação, não devendo afetar o custo do Projeto. A tarefa se comporta como se estivesse desativada. Em relatórios como a curva ABC o usuário realizará filtro por Grupo de Custo para evitar que ele apareça. O Grupo de Custo é quem informa que os insumos deste grupo são do tipo receita ou normal.

No campo  da tela de cadastro de insumos, o usuário poderá optar por um dos seguintes preenchimentos:

* Padrão
* Somente contratação
* Somente Orçamento e Planejamento

Este campo só ficará visível caso o parâmetro **"Utiliza insumos para contratação"** esteja habilitado em Totvs Obras e Projetos | Contratos |Associação de objetos | Utiliza insumos para contratação.

**Sobre os tipos de insumos para contratação:**

* Na planilha o insumo planejado não pode ser do tipo somente contratação (filho).
* Na composição o insumo da composição não pode ser do tipo somente contratação (filho).
* Se o tipo de insumo for Derivado, o tipo de insumo para contratação não pode ser definido como Somente Contratação.
* Nos contratos somente podem ser associados insumos cujo o tipo do insumo para contratação seja Padrão ou Somente contratação.

Informando as opções Derivado ou Receita, a [aba Insumo Derivado](https://tdn.totvs.com.br/pages/viewpage.action?pageId=421385445) é habilitada.

**Unidade:** Informe a unidade do insumo, campo obrigatório.

Caso a unidade do insumo seja alterada, e a nova unidade não possua uma unidade base compatível com a unidade da lista de preços, deve-se alterar a unidade da lista de preços para a unidade do insumo.

O insumo cuja unidade é percentual não poderá ter preço cadastrado, pois será calculado pelo percentual do grupo de uma composição por produção ou por custo unitário, de acordo com o que foi definido no cadastro do grupo de custo.

Quando o Insumo é definido com a unidade do tipo Percentual (%) será disponibilizado um combo box para definir o Fator de Eficiência na execução de alguns serviços que impactam diretamente no custo de um Projeto. Os Fatores são os seguintes:

* **FIC - Fator de Influência de Chuvas:** Em face de sua natureza essencialmente linear, o conhecimento das condições climáticas regionais constitui fator fundamental para o planejamento de uma obra de infraestrutura de transportes. Por meio do tratamento da série histórica de centenas de estações pluviométricas do país, o SICRO propõe a utilização de um Fator de Influência de Chuvas, o FIC, a ser aplicado sobre o custo unitário de execução dos serviços que sofram influência das chuvas em sua produção. FIC incidirá sobre o custo unitário de execução de mão de obra e equipamentos, das composições de custos principais, dos serviços auxiliares e dos transportes. Importante destacar que as atividades relacionadas à usinagem de materiais não fazem jus à aplicação do FIC.
* **FIT - Fator de Interferência do Tráfego:** Durante a execução de obras em rodovias novas ou existentes, o volume de tráfego local é fator real de redução de produção dos serviços, principalmente nas proximidades dos grandes centros. Por essa razão, o SICRO apresenta o conceito de Fator de Interferência de Tráfego, o FIT, a ser aplicado sobre o custo unitário de alguns serviços nas obras de melhoramentos, de adequação de capacidade, de restauração, de conservação e de transporte, em função do volume médio diário de tráfego. No SICRO, a aplicação do FIT incidirá sobre todos os serviços que estejam sujeitos efetivamente à interferência do tráfego, cabendo ao orçamentista sua classificação e definição em função do volume médio diário e da proximidade de centros urbanos. No caso da elaboração de projetos que envolvam segmentos com comportamento heterogêneo em termos de volume médio diário de tráfego, recomenda-se definir um fator de interferência de tráfego médio em função da ponderação dos fatores de interferência obtidos nas diferentes seções em relação à extensão total do trecho. O FIT incidirá sobre o custo unitário de execução de mão de obra, equipamentos e momento de transporte.

Ao cadastrar o insumo que tenha o fator de eficiência, é necessário que a unidade do mesmo seja "Percentual", pois o cálculo envolvendo o FIC e FIT deve considerar os insumos que pertencem aos grupos DNIT específicos, sendo assim algumas validações se fazem necessárias:

* **Insumos com FIC:**  
  o    O Grupo de Custo no qual o insumo está associado deve ter o Grupo DNIT definido como **"Nenhum"**;  
  o    O Grupo de Custo no qual o insumo está associado deve ter os Grupos DNIT sobre o percentual, definidos como **"Equipamento" e/ou "Mão de Obra"**.  
  o    Os Grupo de Custo no qual o insumo está associado deve ter os Grupos de Custo Unitário sobre o percentual, definidos como **"Equipamento" e/ou "Mão de Obra"**.
* **Insumos com FIT:**  
  o    O Grupo de Custo no qual o insumo está associado deve ter o Grupo DNIT definido como **"Nenhum"**;  
  o    O Grupo de Custo no qual o insumo está associado deve ter os Grupos DNIT sobre o percentual, definidos como **"Equipamento" e/ou "Mão de Obra" e/ou "Momento de Transporte"**.  
  o    Os Grupo de Custo no qual o insumo está associado deve ter os Grupos de Custo Unitário sobre o percentual, definidos como **"Equipamento" e/ou "Mão de Obra" e/ou "Momento de Transporte"**.

**Fator K:** Informe o valor do fator k para esse insumo. Esse campo é habilitado de acordo com o parâmetro "Fator K" em Projeto| Construção & Projetos | Projetos F6 | Cálculo| Fator K. O Fator K deve obrigatoriamente possuir um valor superior a 0 (zero).

**Condição de Pagamento:** Informe a condição de pagamento para esse insumo. Esse campo irá interferir no Cronograma de Desembolso do Projeto.

**Jornada:** Informe a jornada de trabalho para o insumo, que será considerada na alocação de recursos. Se não for informada a jornada no cadastro do insumo, será considerada a jornada de trabalho do grupo de custo. Se a jornada de trabalho não estiver informada no insumo e nem no grupo de custo, será considerada a jornada de trabalho definida "Opções | Parâmetros | RM Solum | Projetos | Diversos".

**Grupo de Custo:** Selecione o código ou a descrição do grupo de custo ao qual pertence este insumo, campo obrigatório.

**Descrição:** Informe o nome do insumo.

**Jornada de Trabalho no período (Jornada Pdo.):** Número de horas efetivamente trabalhadas no período do cronograma.

% Máximo e Mínimo de Horas Extras (% max. e % min.): Limitam o cálculo de alocação indicando quantas horas extras podem ser programadas. Neste caso é a quantidade de horas que o sistema usa para o primeiro cálculo das horas extras, que estarão dentro deste limite, antes da equalização. Depois do Insumo equalizado, estes limites poderão ser ultrapassados.

% Fixo de Horas Extras: Caso este campo seja utilizado, a equalização irá desconsiderar o % Máximo e Mínimo de Horas Extras e programar sempre o valor Mínimo informado em "% Fixo de Horas Extras".

**Exemplo:** Equalização do Comprador. No caso deste campo o valor de horas normais não deve ser diminuído. Deve ser incluída uma quantidade de horas extras que irá aumentar a quantidade total de horas.

**Valor Unitário de Hora Extra (% valor unit.):** Apesar de não influir no cálculo da equalização, será usado para calcular o valor das horas extras programadas. O custo é informado em percentual em relação ao custo original do Insumo.

**Prazo de Ressuprimento (Dias):** Esse campo controla o prazo que determinado insumo possui para ser entregue. O valor informado neste campo representa a quantidade em dias que o insumo deve ser solicitado para que chegue a tempo da tarefa ser executada na data estipulada.

**Não fracionado:** Marque essa opção se este insumo não puder ser fracionado, ou seja, não podem ser partidos em porções menores.

**Exemplo:**Insumos que não podem ser fracionados: porta, janela, torneira, elevador, vaso sanitário, pia, telefone, rolamentos, peças e outros. **Tipo de compra:**

* **Padrão:** Insumos são pedidos conforme Cronograma (Pedido de Material);
* **Não compra Fracionado:** Insumos cujo Pedido de Material não poderá ser feito em quantidade fracionada, exemplo: 1,5 sacos de cimento;
* **Compra Única:** Insumo cujo Pedido de Material será criado com a necessidade3 total do mesmo no Projeto, exemplo: Materiais fabricados em Lote, tinta, cerâmicas etc..

**Utilizado em Composição por Produção:** Informe se este insumo poderá ser utilizado também em composição por produção e escolha o grupo DNIT a que pertence este insumo.

Se o grupo DNIT escolhido for Equipamento, aparecerá a pasta Custo Horário.

Se a integração com o Suprimentos/Faturamento estiver ativa, aparecerá a pasta Produtos do Suprimentos/Faturamento.

Campo % Improdutividade: O campo Improdutividade é uma propriedade do insumo. O valor lançado neste campo será em percentual e será aplicado à quantidade do insumo quando este for utilizado em uma composição ou diretamente a uma tarefa. Na curva ABC de insumos o campo % Improdutividade será considerado. Será mostrado pelo campo Valor total. A Curva ABC de insumos foi ajustada para exibir o valor do campo % Improdutivo; Qtde.Total = QTDEIMPRODUTIVA + QUANTIDADE Valor Total = VALORIMPRODUTIVO + VALOR

Prazo de Ressuprimento

**Prazo de Ressuprimento (Dias):** Esse campo controla o prazo que determinado insumo possui para ser entregue. O valor informado neste campo representa a quantidade em dias que o insumo deve ser solicitado para que chegue a tempo da tarefa ser executada na data estipulada.

**Atenção:** Caso não seja preenchido o campo prazo de ressuprimento a entrega do insumo ira respeitar a data do cronograma. O preenchimento do campo impactara diretamente na requisição de materiais que por sua vez terá reflexo no cronograma de desembolso.

**Exemplo:** Caso seja informado à requisição do material no cronograma no 2º período (Fevereiro), na condição de pagamento do insumo estiver 30 dias e o campo prazo ressuprimento não constar informação. A compra do insumo será feita em Fevereiro e o desembolso será em Março.

Cronograma de compra  
Jan          Fev          Mar  
               x

Cronograma de desembolso  
Jan          Fev          Mar  
                               x

Seguindo o exemplo acima, porém constando informação de 30 dias no campo prazo ressuprimento. A compra do insumo será feita em janeiro e o desembolso será em fevereiro.  
Cronograma de compra  
Jan          Fev          Mar  
x

Cronograma de desembolso  
Jan          Fev          Mar  
                x

Se informado no campo prazo ressuprimento uma quantidade de dias superior ao período do cronograma, ao realizar geração de pedidos, será emitido um log informando quando deverá ser solicitado o insumo para a realização da tarefa. Devido há não existência de parâmetro para o campo prazo ressuprimento, pode-se retirar ou dar permissão através do menu cadastro - segurança - Perfis - Acesso a campo - MISM - PRAZORESSUP e desmarcar ou marcar as permissões: Pode consultar e Pode alterar.

Compra Única

**Vídeo sobre Compra Única:**

Neste caso o arredondamento ocorre na geração da requisição de material conforme a unidade de medida de compra do Produto conforme as regras descritas abaixo.

1º - A quantidade será arredondada considerando o total acumulado ( quantidade dos os itens de mesmo produto e data de entrega ) na unidade de medida de compra.

**Exemplo: Veja que a fração é permitida na unidade do planejamento do insumo KG, e como o somatório dos itens da uma quantidade total sem fração não temos arredondamento.**

2º - O arredondamento é incluído no item de tarefa, que possuir maior saldo de quantidade, para evitar superar a necessidade do projeto.

3º - Será permitido superar a necessidade do projeto, caso seja necessário arredondamento do item para a compra.

4º - Caso um pedido de algumas tarefas, tenha solicitado uma quantidade superior pelo arredondamento, ao solicitar um novo pedido para outras tarefas, esta quantidade será abatida de forma a evitar que seja superado a quantidade total planejada para o projeto.

5º - O sistema realizara este cálculo tanto no processo de geração do pedido, quanto em alterações que afetem tal calculo ou processos como a alteração do histograma resumo ou alterações em grupo.

6º - Caso uma alteração permita que seja possível realizar a compra da quantidade solicitada sem arredondamento, o arredondamento poderá ser desfeito.  

**Exemplo:**

AO ALTERAR PARA A DATA DO SEGUNDO ITEM, DE FORMA QUE OS DOIS ITENS SEJAM AGRUPADOS NA GERAÇÃO DO PEDIDO DE COMPRA, NÃO SE FAZ MAIS NECESSARIO ARREDONDAMENTO E O MESMO É REMOVIDO.

Gráficos do Insumo

**Primeiros Passos:**

- Para o correto funcionamento dos gráficos para o insumo, o ambiente do usuário deve estar corretamente parametrizado nos seguintes pontos:

* Nas configurações do Host utilizado, deve estar informada a tag referentes ao "DefaultDB". **Exemplo:**<add key="DefaultDb" value="CorporeRM" />
* Nas configurações do Host utilizado, deve estar informada a tag referente ao "HTTPort". **Exemplo:**<add key="HTTPort" value="8051" />
* Nas configurações do "config.json" localizado em "RM.Net/wwwroot/PortalTopWeb/config" deve ser informado o nome da maquina com a porta de api ou ip da maquina com a porta de api. **Exemplo:** bhn050114745:8051 ou 192.168.0.1.4:8051.

Ao acessar a edição de um insumo, serão exibidos gráficos relacionados a quantidade e ao valor do insumo.

**Detalhamento das informações:**

* ***Pedido***

No pedido o Cockpit reflete o resultado do que já foi pedido proporcionalmente ao que já foi de fato entregue.

**Pedido:** Total que foi pedido e apropriado no insumo

**Entregue:** Total do que realmente foi entregue  do insumo

* **Medição**

Neste gráfico reflete os valores do que foi contrado e medido do insumo .

* **Saldo**

Saldo da quantidade e valor do insumo selecionado.

Descrição Completa

Esta pasta possui um único campo texto destinado ao cadastramento de uma descrição detalhada do insumo. Este campo não possui limitações.

Para imprimir esse campo através do gerador de relatórios, defina o número de linhas que deseja imprimir. Para isso, clique sobre o campo com o botão direito do mouse, selecione a opção "Máximo de linhas" e informe o número de linhas desejadas.

Campos Livres

Poderão aparecer ou não 5 campos livres alfanuméricos e 5 campos livres de valor, dependendo do parâmetro (menu Opções | Parâmetros | RM Solum | Projetos | Pasta Campos Livres | Subpasta Insumos). Informe o conteúdo dos campos livres ativos. São desativados da janela de edição, automaticamente, os campos livres que não têm descrição (nome). Para desativá-los da visão, deve-se utilizar o ícone "Configurar Colunas".

Custo Horário

Esta pasta aparecerá apenas se o campo "Utilizado em Composição por Produção" na pasta Identificação estiver marcado e o grupo DNIT escolhido for o de Equipamento ou de Mão-de-obra. Ela se divide em duas subpastas:

-Planilha:

Selecione o nome da planilha eletrônica que irá calcular o valor produtivo e o valor improdutivo do equipamento ou o valor unitário da mão-de-obra.

-Célula para Valor Produtivo: Informe o endereço de célula da planilha, que após o cálculo, irá trazer o valor produtivo do insumo. Esta célula também é utilizada para retornar o valor unitário do insumo de mão-de-obra.

-Célula para Valor Improdutivo: Informe o endereço de célula da planilha, que após o cálculo, irá trazer o valor improdutivo do insumo.

-Aparecerão até 20 campos livres. As descrições destes campos são definidas no parâmetro (Menu Opções | Parâmetros | RM Solum | Projetos | Custo Horário). Informe o valor destes campos livres.

**Exemplo:** J25, onde J é a coluna e deve estar em maiúsculo e 25 é a linha na planilha selecionada.

Com estes 3 campos acima informados (obrigatoriamente), será possível fazer o cálculo do custo horário, clicando no botão "Calcular". Ao clicar no botão será mostrado na visão o Valor Calculado do insumo, com seu valor produtivo e improdutivo. Para o custo horário de mão-de-obra são solicitados apenas os campos "Nome" da planilha e "Célula para valor produtivo".  
Para incluir e ativar estes preços no insumo, após o cálculo, marque a caixa de opção "Inserir como preço ativo" e clique no botão "Salvar Preço". Todo preço calculado inserido terá sua descrição nomeada como "calculado". Se já existir um preço com a descrição "Calculado" ao clicar no botão "Inserir Preço do Insumo", o preço do insumo será substituído ao invés de inserir um novo.

Portanto, recomendamos que ao após a criação de um preço "Calculado" o mesmo tenha a sua descrição modificada.

Este cálculo pode ser feito também através da opção Calcular Custo Horário (Menu Opções), onde poderão ser calculados os valores produtivos e improdutivos de mais de um insumo (equipamento) de uma vez.

**Exemplo:** Passos para Cálculo e Impressão do Custo Horário de Equipamentos:

Inclusão das variáveis globais e das variáveis do insumo através do parâmetro (Menu Opções | Parâmetros | RM Solum | Projetos | Custo Horário).

Criação da planilha com estas variáveis e fórmulas para o cálculo dos valores produtivo e improdutivo do equipamento.

Indicação da planilha e das células dos valores produtivo e improdutivo do equipamento (Janela de Edição do Insumo).

Cálculo dos valores produtivo e improdutivo na Janela de Edição de Insumo (pasta custo horário) ou pela opção "Calcular Custo Horário" (Menu Opções).

Impressão das planilhas pela própria janela da planilha ou pela opção "Composição de Custo Horário" (Menu Relatórios).

**Exemplo:**Passos para Cálculo e Impressão do Custo Horário de Mão-de-obra:

Inclusão das variáveis globais e das variáveis do insumo através do parâmetro (Menu Opções | Parâmetros | RM Solum | Projetos | Custo Horário).

Criação da planilha com estas variáveis e fórmulas para o cálculo dos valores produtivo e improdutivo do equipamento.

Indicação da planilha e da célula do valor unitário da mão-de-obra (Janela de Edição do Insumo).

Cálculo do valor produtivo na Janela de Edição de Insumo (pasta custo horário) ou pela opção "Calcular Custo Horário" (Menu Opções).

Impressão das planilhas pela própria janela da planilha ou pela opção "Composição de Custo Horário" (Menu Relatórios).

**Atenção:** Para o funcionamento correto da planilha eletrônica utilizada pelo RM Solum, base do Custo Horário, o Windows deve estar configurado para trabalhar com as configurações regionais do Brasil. Para alterar essas configurações vá ao menu Iniciar | Painel de Controle | Configurações Regionais e mude para "Português (Brasileiro)". Se o seu Windows estiver na língua inglesa vá ao menu Start | Settings | Control Panel | Regional Settings Properties e mude para "Portuguese (Brazilian)".

Produtos de Suprimentos/Faturamento

Esta pasta aparecerá apenas se o campo "Integrado com Suprimentos/Faturamento" no menu Opções | Parâmetros | RM Solum | Projetos, na pasta Integrações estiver marcado.

Nela será possível relacionar um produto ou mais, para um insumo.

Também será possível, através dos respectivos botões, definir um produto como principal, cadastrar um novo produto  (caso o usuário tenha tal permissão no módulo de Suprimentos/Faturamento); e consultar saldo e custos do produto selecionado

OBS.: Somente produtos de último nível: Marque essa opção para definir a visualização somente dos produtos de último nível, nos campos de seleção Código, Nome Fantasia e Descrição. Caso a mesma fique desmarcada todos os produtos ficam visíveis.

Os principais campos do cadastro do produto relacionado ao insumo, ficam visíveis conforme listado a seguir:

**Código**: Informe o código do produto do RM Nucleus correspondente a este insumo.

**Nome Fantasia**: Informe o nome fantasia do produto do RM Nucleus correspondente a este insumo.

**Descrição**: Informe a descrição do produto do RM Nucleus correspondente a este insumo.

**Unidade**: Será preenchida automaticamente com a unidade do produto selecionado através do código ou da descrição do produto.

Um insumo só pode ser relacionado a um produto do RM Nucleus, depois que for gravado.

**Principal**: O número 1 indica que o produto é principal, ou seja, será o produto enviado para o RM Nucleus. Somente um produto pode ser definido como principal. Os demais produtos recebem o número 0 (zero).

**Num. do Fabricante**: Número do produto no fabricante.

**Produto Inativo**: Indica se o produto está ativo ou não no RM Suprimentos/Faturamento.

Insumos Associados

Determinados insumos sempre são acompanhados por outros, ou seja, sempre que ele for inserido como recurso de uma composição os outros insumos terão que ser inseridos. Insira nessa pasta os insumos que acompanham o insumo que está em edição. Dessa forma, ao inserir um insumo como recurso de uma composição, os insumos existentes na pasta Insumos Associados também serão inseridos como recursos da composição.

**Exemplo:** Suponha que, sempre que o insumo Motoscraper for inserido numa composição, será necessário inserir também os insumos Operador e Ajudante. Para facilitar o cadastramento das composições, no cadastro do insumo Motoscraper, nessa pasta, deve-se inserir os insumos Operador e Ajudante. Quando o insumo Motoscraper for inserido numa composição, serão inseridos, automaticamente, o Operador e o Ajudante, com quantidade igual a um.

Funções

Código: Selecione o código da função a ser associada ao insumo em edição.

Nome da Função: Selecione a descrição da função correspondente ao insumo editado.

Somente insumos que são do grupo DNIT B no grupo de custo é que podem ter uma função associada, ou seja, somente insumos do grupo de mão-de-obra. Esse campo não poderá ser modificado, se houver uma apropriação para o insumo corrente.

Campo visível somente se houver integração com o RM Labore. Se a função está inativa, ela não fica disponível para seleção. Se a função foi desativada e estava vinculada a algum insumo, ao abrir a pasta "Funções" a mesma será desvinculada automaticamente.

Bens

Código: Selecione o código do grupo de bem a ser associado ao insumo em edição.

Descrição: Selecione a descrição do grupo de bem correspondente ao insumo editado.

Somente insumos que estão em grupos de custo unitário que pertencem ao grupo DNIT A (Equipamentos) ou F (Transporte) podem ter grupos de Bens associados.  
Campo visível somente se houver integração com o RM Bonum. O grupo de bem não poderá ser modificado, se houver uma apropriação para o insumo corrente.

Integrações

**Integração EMOP** Código: Código do insumo na EMOP – Empresa de Obras Públicas do Rio de Janeiro. Esse código será verificado na importação de recursos das composições, insumos e preços, permitindo que o código do RM Solum seja alterado.

**Integração FGV** Código: Código do insumo na FGV – Fundação Getúlio Vargas do Rio de Janeiro. Esse código será verificado na importação de recursos das composições, insumos e de preços, permitindo que o código do RM Solum seja alterado.

**Pasta Campos Complementares**

São visualizados os campos complementares cadastrados no menu Cadastros | Campos Complementares. Nessa janela os dados devem ser informados. Caso tenha sido definida uma validação do campo complementar com base numa tabela dinâmica, o mesmo será validado nesse momento. Os campos complementares podem ser do tipo Data, Inteiro, Real ou Alfanumérico.
