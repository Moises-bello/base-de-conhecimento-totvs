---
content_hash: 8eedab52998e0c0851cb27cecf03b9055d38e119ae4f255eb2f9574b6cf81740
fetched_at: '2026-06-29T00:09:49.520657+00:00'
page_id: '435105308'
product: rm
source: tdn-rm
title: Unidade - Anexos - Subunidade
type: documentation
url: https://tdn.totvs.com/display/LRM/Unidade+-+Anexos+-+Subunidade
version: 26
---

Para acessar as Subunidades, ao cadastrar ou editar uma Unidade, clique em Anexo e depois em Subunidade. Nesta opção de menu serão inseridas as Subunidades dos Empreendimentos que serão usados no cadastro de Vendas. Através do cadastro é possível controlar:

**Identificação**  
Ao cadastrar ou editar uma Subunidade, abrirá a janela de edição, na pasta Dados Subunidade, onde iremos cadastrar os seguintes campos:

Ao salvar a Subunidade, o sistema verificará a quantidade de Subunidades disponível na Unidade para a criação das Subunidades. Se a quantidade de Subunidades ultrapassar o número cadastrado na Unidade, o sistema não permitirá a inclusão.

Os campos *Coligada Cliente/Fornecedor do Proprietário, Cliente/Fornecedor do Proprietário e Nome do Proprietário*, são exibidos somente na visão de Empreendimentos no menu **Shopping** ou no menu **Condomínio**.

* **Empreendimento**: Este campo já estará preenchido automaticamente de acordo com o Empreendimento da Unidade selecionada para efetuar o cadastro da Subunidade.
* **Unidade**: Informe a Unidade a ser cadastrado uma Subunidade. O sistema apresentará uma lista de opções de Subunidades já previamente cadastradas no sistema RM SGI no menu Cadastro | Unidade / Subunidade, de acordo com Empreendimento selecionado no campo "Ref. Emprendimento";
* **Apto**: Código do Apartamento que é informado no momento da geração das Subunidades do bloco ou informado manualmente.
* **Descrição**: Informe uma descrição para a Subunidade.
* **Observação**: Este campo já estará preenchido automaticamente de acordo com a Unidade selecionada para efetuar o cadastro da Subunidade.
* **Sub-Unidade**: Informe o número da Subunidade;
* **Fração Ideal**: Informe a fração ideal da Subunidade. Esta informação é importante para o cálculo do IPTU;

O valor da parcela de IPTU é obtido através da fórmula:

Valor do IPTU informado \* Fração Ideal de cada sub-unidade, dividido pelo número de parcelas informado no IPTU.  
Exemplo: Valor IPTU = 1000,00 Fração Ideal = 0,1 Número de Parcelas = 1 Total = 1000\*0,1/1 = 100,00

Observação: Se o IPTU for gerado no mesmo mês da venda, o número de parcelas será sempre uma parcela a menos.

* **Peso**: Informe o peso da Subunidade. Esta informação é importante para o cálculo do Preço Base;

Se você estiver utilizando Tabela de Preço, o sistema irá utilizar este campo para calcular o preço base desta Subunidade.

O valor do Preço Base é obtido através da fórmula:

Preço Base \* Peso de cada sub-unidade.  
Exemplo: Valor do Preço Base: 10.000,00 Valor do Peso da Subunidade: 1,5 Valor Base da Subunidade: 10000 \* 1,5 = 15.000,00

* **Código Reduzido**: Informe o código reduzido para a Subunidade;
* **Custo Subunidade**: Campo calculado automaticamente pelo sistema através da fórmula: Área da Subunidade \* Custo por metro quadrado do Empreendimento;
* **Código do Imóvel**: Informe o código do Imóvel (Módulo de Locação / Aluguéis) associado à esta Subunidade. Podem ser selecionados imóveis de coligadas diferentes da do condomínio;

**Integração Contábil / Financeira:**

* **Conta Gerencial**: Informe qual a conta gerencial responsável pela distribuição contábil da Subunidade.
* **Default Contábil**: Informe os dados contábeis como Conta contábil, filial, departamento, centro de custo, percentual e histórico da desta Subunidade.
* **Rateio Centro de Custo**: Informe como será a divisão por centro de custo da Subunidade.
* **Datas:**

* + **Data da Alteração**: É informado a Data da última alteração do registro. Este campo está inabilitado para edição;
  + **Usuário**: É informado o Usuário que efetuou a última alteração do registro. Este campo está inabilitado para edição;
  + **Data do Habite-se**: Informe a data do habite-se desta Subunidade;
  + **Data de Entrega**: Informe a data de entrega desta Subunidade;

* **Descrição**: Campo livre para se digitar alguma informação relevante da Subunidade;

**Situações:**

* **Situação para Venda**: Informe a situação da Subunidade gerada para a Venda. O sistema apresentará uma lista de opções de Situações de Subunidades para a Venda já previamente cadastradas no sistema RM SGI no menu Cadastro | Tabelas Adicionais | Situação Sub-Unidade;
* **Situação para Aluguel**: Informe a situação da Subunidade gerada para o Aluguel. O sistema apresentará uma lista de opções de Situações de Subunidades para o Aluguel já previamente cadastradas no sistema RM SGI no menu Cadastro | Tabelas Adicionais | Situação Sub-Unidade;

**Contrato/Cliente**

* **Cliente Venda**: Caso a Subunidade esteja com a situação Vendido ou Reservado para Venda, o sistema irá preencher este campo com o nome do Comprador. Campo indisponível para edição;

Ao gerar Subunidade, a situação da Subunidade para a Venda, já virá preenchida automaticamente com "Disponível para Venda". Cliente Aluguel: Caso a Subunidade esteja com a situação Alugado ou Reservado para Aluguel, o sistema irá preencher este campo com o nome do Locador. Campo indisponível para edição;

**Tabela de Preço:**

* **Tabela de Preço Padrão**: Quando uma tabela de preço for associada às Subunidades, ela será exibida neste campo.
* **Preço**: Será exibido o preço da Subunidade de acordo com a tabela de preço padrão aplicada.
* **Preço por m²**: Será exibido o preço por m² da Subunidade de acordo com a tabela de preço padrão aplicada.

**Dados Adicionais:**

* **Código na Prefeitura**: Informe o código da Subunidade na prefeitura;
* **Código Reduzido na Prefeitura**: Informe o código reduzido para a Subunidade na prefeitura;
* **Número da Matrícula**: Informe o número da matrícula da Subunidade;

**Endereço:**  
Serão informados, os campos referentes à localização da Subunidade. São eles:

* **CEP**
* **Tipo de Logradouro**
* **Logradouro**
* **Número**
* **Complemento**
* **Bairro**
* **Cidade**
* **Estado**
* **País**

EFD-Pis/Cofins/DAI

* **Tipo de Imóvel DAI**  
  Neste campo será selecionado o tipo de imóvel referente a subunidade. Essa informação será enviada para a declaração DAI exclusiva do município de São Paulo.

**Integração Registradora Recebíveis:** Clique **[aqui](https://tdn.totvs.com/display/LRM/CERC+-+Subunidades)** para consultar os campos relativos à esta aba.

**Condomínio:**

**Atenção**: Os campos descritos aqui são visíveis apenas no módulo de Condomínio.

**Imóvel próprio:** Informe se o imóvel é próprio da Incorporadora ou não;  
**Cliente/Fornecedor do proprietário**: Informe o cliente/fornecedor proprietário da Subunidade. Este campo fica habilitado caso o campo Imóvel próprio estiver desmarcado;  
**Imóvel ocupado**: Informe se o imóvel está ocupado ou não;

**Dimensões / Áreas**  
Ao cadastrar ou editar uma Subunidade, na pasta Dimensões / Áreas, os campos estão divididos nos grupos Dados de Loteamento e Dados de Edificação, indicados abaixo:

**Campos de Dados de Loteamentos:**

* Dimensão Frente (m): Informe a dimensão da Frente em metros da Subunidade;
* Dimensão Fundo (m): Informe a dimensão do Fundo em metros da Subunidade;
* Dimensão Esquerdo (m): Informe a dimensão do lado esquerdo em metros da Subunidade;
* Dimensão Direito (m): Informe a dimensão do lado direito em metros da Subunidade;
* Confrontação Frente: Informe a confrontação Frente da Subunidade;
* Confrontação Fundo: Informe a confrontação Fundo da Subunidade;
* Confrontação Esquerda: Informe a confrontação esquerda da Subunidade;
* Confrontação Direita: Informe a confrontação direita da Subunidade;

**Campos de Dados de Edificação:**

* Área Privativa (m2): Informe a área privativa em metros quadrados da Subunidade;
* Área Comum (m2): Informe a área comum em metros quadrados da Subunidade;
* Área Total (m2): Informe a área total em metros quadrados da Subunidade;
* Área Garagem (m2): Informe a área da garagem em metros quadrados da Subunidade;
* Área Terraço (m2): Informe a área do terraço em metros quadrados da Subunidade;
* Área Outros (m2): Informe outras áreas em metros quadrados da Subunidade;
* Área Equivalente (m2): Informe a área equivalente em metros quadrados da Subunidade;

* **Copiar Áreas**: Ao clicar neste ícone, abrirá a janela de Copiar Áreas, onde poderemos copiar as áreas desta Subunidade para as demais Subunidades desta Unidade;
* **Descritivo do registro**: Informe o Descritivo do registro da Subunidade;
* **Modelo**: Informe o modelo de garantia a ser utilizado por essa sub unidade. O modelo de Garantia contém todas as coberturas de Problemas residenciais que essa sub unidade garante solução.

**Datas Opcionais**  
Ao cadastrar ou editar uma Subunidade, na pasta Datas Opcionais, será informado os seguintes campos:

**Datas Opcionais 1, 2, 3, 4 e 5**: Será informado as Datas opcionais do Empreendimento desta Subunidade cadastrada. Estes campos estarão indisponíveis para edição.

**Campos Complementares**  
Ao cadastrar ou editar uma Subunidade, na pasta Campos Complementares, informe os Campos Complementares cadastrados no sistema.  
O sistema apresentará na janela todos os Campos Complementares já previamente cadastradas no menu Cadastro | Campos Complementares | Subunidade.

Vagas autônomas deverão ser tratadas como Subunidades, pois temos que informar a fração ideal da mesma e ter um contrato separado para a sua comercialização. Todas as alterações desde a criação até a exclusão de uma Subunidade é monitorada por um log que criará um registro para todas as ações feitas em uma Subunidade, por exemplo, venda da Subunidade, troca de preço, etc.

**Controle IPTU**Informações pertinentes ao controle de IPTU da subunidade

* **Código Cartório**: Informar Cliente/Fornecedor criado para o cartório.
* **Código da Prefeitura**: Informar Cliente/Fornecedor criado para a prefeitura.
* **Inscrição Municipal**: Informar a Inscrição municipal.
* **Área do Terreno**: Informar a área do terreno.
* **Área Construída**: Informar a área construída.
* **Valor Venal**: Informar o valor venal.

**Despesas de IPTU**Informações pertinentes ao controle de despesas de IPTU da subunidade

* **Responsável**: Informar o responsável pelas despesas de IPTU(default) no cadastro da subunidade, onde poderão ser escolhidas duas opções: Cliente e Empresa. Essas informações são opcionais, ou seja, não precisam estar preenchidas.

  Se for escolhida a opção de Cliente, será necessário cadastrar a partir de qual momento da venda o cliente ficou como responsável com as despesas de IPTU conforme imagem abaixo:

Caso a opção escolhida seja "Data a definir", deverá ser informada uma data a partir da qual a despesa será cobrada do cliente.

OBS: No caso da responsabilidade ser do cliente, antes da data informada a responsabilidade será da empresa.

Informações Complementares

---

**Despesas**

* [Despesa de Venda](https://tdn.totvs.com/pages/viewpage.action?pageId=599367719)
* [Parcela de Despesa](https://tdn.totvs.com/display/LRM/Despesa+-+Anexo+-+Parcela+de+Despesa)
* [Parcela de Reembolso](https://tdn.totvs.com/display/LRM/Despesa+-+Anexo+-+Parcela+de+Reembolso)
