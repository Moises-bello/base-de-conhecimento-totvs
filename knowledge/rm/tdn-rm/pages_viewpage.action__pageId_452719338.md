---
content_hash: dc743196ef96d749877d2b1160171d09cc91d807610f6fdaea8cd05dbf281819
fetched_at: '2026-06-29T00:10:06.786038+00:00'
page_id: '452719338'
product: rm
source: tdn-rm
title: Parâmetros da Geração dos Lançamentos Financeiros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719338
version: 13
---

# **Geração dos Lançamentos**

É  o processo que gera os lançamentos financeiros da folha de pagamento para o sistema de gestão financeira conforme parametrização realizada em RH | Folha de Pagamento | Encargos | Financeiro | Geração dos Lançamentos.

**Quebra da** **Seção**  
Este campo influência diretamente na geração de lançamentos financeiros, ou seja, de acordo com a quebra da seção da empresa será considerada a geração do lançamento financeiro.   
   
**Competência (****Mês e Ano)**

**PONTOS IMPORTANTES:**

1. Para a geração dos lançamentos financeiros do líquido de rescisão de rescisão para próximo mês deverão ser informados o ano e o mês da competência da rescisão (próximo mês).
2. O sistema faz os lançamentos das férias cuja data de pagamento esteja dentro da competência selecionada, independente de ser ou não no próximo mês.
3. O sistema verifica a situação do funcionário no último dia do mês da competência desejada para geração dos lançamentos financeiros.
4. Sendo assim para os funcionários demitidos no mês, o sistema não gera o lançamento financeiro de "Líquido" dos períodos anteriores à rescisão, pois irá verificar a situação do funcionário no último dia do mês, e estando o funcionário com rescisão calculada será devida apenas à geração de líquido de rescisão.
5. Para os lançamentos financeiros de IRRF, o sistema não irá considerar as informações dos campos: Ano, Mês e Período de competência. Será verificando a data de pagamento dos eventos com a data de apuração informada na pasta Imposto de Renda.
6. Para a geração dos lançamentos dos tipos: 16-Pensão Folha, 17-Pensão Férias, 18-Pensão 13º e 19-Pensão Participação nos Lucros, o sistema irá buscar os valores na pasta de Movimento da Pensão no Cadastro de Funcionários.

**Período**  
O lançamento financeiro será gerado de acordo com o período escolhido entre os parâmetros Todos, Atual e Período. Sendo que para gerar lançamentos financeiros de um ou mais períodos digite no campo os períodos selecionados, separando–os por vírgula.

**Exemplo:** 1,2,3.    
   
**Data de Emissão**  
Esta data refere-se a data em que foi gerado o lançamento financeiro no RM Labore que será transferida para o campo "Data de Emissão" do Lançamento Financeiro no RM Fluxus.   
   
**Data de Vencimento**  
Esta data refere-se a data de vencimento do lançamento financeiro gerado no RM Labore que será transferida para o campo "Data de Vencimento" do Lançamento Financeiro no RM Fluxus.  
   
**Data de Previsão de Baixa**  
Será gerado o lançamento financeiro considerando a "Data Previsão de Baixa" do modulo de Geração do Lançamento Financeiro. Se:  
a) O Agrupamento for diferente de Individual por Funcionário; e  
b) Não tratar-se de Lançamento Financeiro para Liquido de Férias e Liquido de Rescisão nos quais o campo 'Usar data de pagamento para vencimento do lançamento' do Cadastro de Parâmetros para Lançamento Financeiro estiver marcado.  
   
**Conta/Caixa**  
Este campo apresentará os códigos cadastrados em Cadastros | Contas/Caixa no RM Fluxus.  
Estará desabilitado para Edição se o parâmetro "Usar Conta/Caixa do cliente/Fornecedor" estiver marcado.

**Observações:**  
1. Se não houver informação neste campo, o sistema irá buscar as informações do campo "Conta/Caixa" em dá presente rotina de Geração de Lançamentos Financeiros.  
2. Quando houver dois códigos de Conta/Caixa iguais (coligada corrente e coligada global), ao informar o código o sistema apresentará os códigos e as respectivas descrições para que o usuário possa escolher qual conta/caixa será utilizado no lançamento financeiro.

**Global**  
Este campo é informativo. Quando estiver marcado, indica que o código da Conta/Caixa é utilizado em outras coligadas da base de dados. Caso contrário, o código da Conta/Caixa é exclusivo da coligada corrente.  
   
**Usar fornecedor do funcionário**  
Com esta opção marcada, o lançamento financeiro será gerado com o fornecedor registrado no campo "Fornecedor para lançamento financeiro" em Cadastros | Funcionários | Registro.

**Gerar lanctos rateados por centro de custo**

Com esta opção ativada, o lançamento financeiro será gerado com a informação por centro de custo.  
Os centros de custos utilizados seguirão a parametrização definida no sistema:

* Se o parâmetro Configurações | Parametrizador | Folha Normal | Cálculo 2/2 | "Utiliza cálculo por Centro de Custo" estiver marcado, o sistema utilizará o centro de custo do funcionário, com base no rateio fixo configurado para ele.
* Se o parâmetro estiver desmarcado, será considerado o centro de custo da seção à qual o colaborador pertence.

**Usar Conta / Caixa do Cliente / Fornecedor**  
Estará habilitado para Edição e também Marcado se o parâmetro "Agrupamentos" estiver com a opção "Individual por funcionário" e o parâmetro "Usar fornecedor do funcionário" estiver marcado.   
Ao marcar este parâmetro o sistema gera os lançamentos financeiros com a conta caixa informados no cadastro de cliente/fornecedor. Para tal deve-se informar o fornecedor para lançamento financeiro em Cadastros | Funcionários | Registro.

**Atenção:**  
O Parâmetro acima só funcionará quando a base está integrada com o RM Fluxus. 

**Ordenação**  
Os campos abaixo só serão habilitados se na caixa Agrupamentos, o parâmetro Individual por Funcionário estiver marcado.  
   
**Nenhuma**  
A ordenação será feita na sequência numérica dos documentos gerados.  
   
**Chapa**  
Dentro da ordenação numérica dos documentos gerados será apresentada a ordenação dos nomes dos funcionários.  
   
**Nome**  
Dentro da ordenação numérica dos documentos gerados será apresentada a ordenação das chapas dos funcionários.

**AGRUPAMENTOS**  
As opções abaixo definirão a forma de agrupamento na geração dos lançamentos financeiros.  
   
**Agrupar por seção**  
Esta opção estará sempre marcada como default. O resultado será a soma dos valores de cada Código Ativo escolhido em Rotinas | Geração de Lançamentos Financeiros | pasta Lançamentos Ativos para a geração dos lançamentos financeiros dentro da quebra da seção definida pelo usuário.  
   
**Agrupar por seção e fornecedor**  
Com esta opção o sistema gera todos os lançamentos agrupando-os por Fornecedor. Ou seja, dentro da quebra da seção definida pelo usuário, o sistema irá somar em cada Lançamento Financeiro, os valores dos lançamentos de todos os seus funcionários que possuem o mesmo fornecedor.

**Atenção:** Ao habilitarmos este parâmetro a opção "Usar fornecedor do funcionário" é indicado automaticamente, mantendo-se desabilitado. Caso o fornecedor do funcionário não tenha sido informado, será considerado o fornecedor da parametrização.

**Individual por funcionário**  
Com esta opção marcada, será gerado um lançamento financeiro para cada funcionário em que o tipo de lançamento referenciado nos Códigos Ativos tenha ocorrido.  
Na visão dos lançamentos financeiros o sistema apresentará as colunas CHAPA e NOME dos funcionários para os quais foram gerados os lançamentos financeiros. Também com este parâmetro marcado o usuário poderá escolher a ordenação que melhor convier (Nenhuma ou Chapa ou Nome).

**Usar definição da parametrização**  
Com esta opção marcada, os lançamentos financeiros serão gerados baseados nas parametrizações definidas em Cadastros | Financeiro | Parametrização dos Lançamentos Financeiros.

**1- Tomador**  
Com esta opção marcada o lançamento será gerado pelo tomador principal (Cliente/Fornecedor), sem distribuição para os CEI's cadastrados no anexo Administração de Pessoal | Cliente e Fornecedor | Anexo | CEI do Cliente / Fornecedor.  
Caso contrário será gerado distribuindo nos CEI's cadastrados.

**Atenção:** Este parâmetro somente ficará habilitado para o tipo de lançamento financeiro '15-FGTS Conforme SEFIP'.

**2- Tomador/CEI**  
Com esta opção marcada o lançamento será gerado por CEI de Cliente/Fornecedor, conforme distribuição informada em Administração de Pessoal | Funcionários | Anexos | Folha de Pagamento | Rateio Tomadores.  
Caso contrário será gerado pelo tomador principal (Cliente/Fornecedor).

**Atenção:** Este parâmetro somente ficará habilitado para o tipo de lançamento financeiro 15-FGTS Conforme SEFIP.  
   
**Observação:**  
O sistema consiste lançamentos financeiros de rescisão duplicados. Este recurso funcionará somente quando os lançamentos forem gerados individualmente por funcionário. Se for identificado na movimentação dos funcionários, algum evento com os códigos de cálculo 93 (DIF. FÉRIAS PROPORCIONAIS), 96 (DIF. SALÁRIO RESCISÃO) ou 97 (DIF. 13o. SALÁRIO RESCISÃO), o sistema vai identificar que se trata de rescisão complementar e o lançamento não será bloqueado.

**Tabelas Opcionais**   
Estas tabelas serão visualizadas caso o usuário as habilite no RM Fluxus nas Tabelas Opcionais existente na parametrização.  
Se o parâmetro "Usa parametrização" estiver desmarcado, o usuário poderá optar em selecionar o Código/Descrição de cada item das Tabelas Opcionais no momento da Geração dos Lançamentos Financeiros.   
Caso contrário, o sistema buscará as informações definidas nas Tabelas Opcionais na Parametrização dos Lançamentos Financeiros.

Importante!

**Geração de Lançamento Financeiro – Tipo 24 (Total Guia FGTS Digital)**

Ao gerar o lançamento financeiro para o Tipo "24 - Total Guia FGTS Digital", e com os seguintes parâmetros configurados:

* Menu BackOffice | Gestão Financeira | Ambiente | Parâmetros | TOTVS Gestão Financeira  
     • 02.01 - Contas a Pagar |  02.01.01 - Manutenção de Lançamentos | 02.01.01.01 - Lançamento | Etapa 7 - Recursos Adicionais:  
       ◦ Parâmetro **"Rateio Centro de Custo/Natureza Orçamentária"** definido como *Centro de Custo*  
       ◦ Parâmetro **"Obrigatoriedade"** definido como *Obrigatório sempre*

* Menu RH | Folha de Pagamento | Configurações | Parametrizador | Folha Normal | Cálculo 2/2  
     • Parâmetro **"Utiliza cálculo por centro de custo"** desmarcado

O sistema passará a gerar o lançamento financeiro considerando os valores dos centros de custo cadastrados na seção.

Caso seja utilizada a quebra por CNPJ durante a geração do lançamento, e os centros de custo estejam cadastrados na seção filha, o lançamento considerará os centros de custo vinculados à seção filha.

## **Documentação**

* [Gerar lançamentos financeiros rateados por Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412577197847-RH-RM-FOP-Gerar-lan%C3%A7amentos-financeiros-rateados-por-Centro-de-Custo?source=search)

[Voltar para pagina inicial](http://tdn.totvs.com/pages/viewpage.action?pageId=452719571)
