---
content_hash: fa5c6205dad6572be5d1a644301e1c1fb6460fe3aa79622e206d23b78a300b22
fetched_at: '2026-06-29T00:09:49.319191+00:00'
page_id: '435105278'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Aluguel - Imóveis - Imóvel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105278
version: 29
---

## 🏢CADASTRO DE IMÓVEL

O cadastro de imóvel é responsável por permitir a inclusão, alteração ou exclusão de um bem imobiliário, que podemos utilizar em contratos de locação e administração, dentre outros.  
Através desse cadastro podemos também definir as prestadoras de serviço que atuam no imóvel, quais as Administradoras que gerenciam o contrato do imóvel, as características que este imóvel possua e seus endereços adicionais.

---

## 📋PRÉ-CONDIÇÕES

Antes de realizar o cadastro, é necessário:

* Ter selecionado o parâmetro que habilita o menu **Aluguel**.  
  O parâmetro pode ser localizado acessando:  
  **Projeto / Incorporação / Ambiente / Parâmetro / TOTVS Incorporação / Aluguel**;
* O usuário deve possuir as permissões para incluir, alterar ou excluir um imóvel dentro do menu **Aluguel**;
* Ter incluído previamente os seguintes cadastros:

  + Centro de Custo;
  + Tipo de Endereço;
  + Tipo de Logradouro;
  + Município;
  + Estado;
  + País.

---

## ➕INCLUINDO UM IMÓVEL

1️⃣ Acesse:  
**TOTVS RM / Projeto / Incorporação / Aluguel / Imóvel**

2️⃣ Clique em **Incluir Imóvel**.

3️⃣ Preencha os campos conforme desejado e clique em **Salvar**.

---

## 🆔IDENTIFICAÇÃO

* **Imóvel:** Código do Imóvel;
* **CIB:**  
  O Cadastro Imobiliário Brasileiro (CIB) é um banco de dados cadastrais que reúne dados de todos os imóveis do país – urbanos, rurais, públicos e privados e de características especiais.  
  O CIB é o componente central da política de gestão integrada das informações territoriais, consolidando dados em uma base nacional padronizada, interoperável e acessível no Sistema Nacional de Gestão de Informações Territoriais (Sinter).  
  Ele funciona como um identificador único para cada imóvel do país, similar ao CPF (para pessoas físicas) e ao CNPJ (para as empresas).  
  Sua estrutura é um código alfanumérico de 7 caracteres + dígito verificador.
* **Descrição Imóvel:** Descritivo com informações sobre o imóvel;

---

## 📌SITUAÇÃO DO IMÓVEL

Define o status em que o imóvel se encontra. A situação de um imóvel pode ser:

🟢 **Disponível para Administração**  
Situação inicial do imóvel, indicando que pode ser associado a um Contrato de Administração.

🟢 **Disponível para Locação**  
O imóvel fica nessa situação quando já está associado a um Contrato de Administração ou quando o parâmetro *“Imóvel de propriedade da administradora de imóvel?”* estiver marcado.  
Nessa situação, o imóvel pode ser associado a um Contrato de Locação.

🟡 **Reservado**  
O imóvel fica nessa situação quando já está associado a um Contrato de Locação com status **Elaboração**.  
Nessa situação, o imóvel não pode ser mais associado a um Contrato de Locação.

🔴 **Locado**  
O imóvel fica nessa situação quando já está associado a um Contrato de Locação com status **Efetivado**.  
Nessa situação, o imóvel não pode ser mais associado a um Contrato de Locação.

---

## 📐ALUGUEL POR M² – REGRAS DE SITUAÇÃO

As situações do imóvel possuem validações adicionais quando se utiliza **Aluguel por M²**:

🟢 **Disponível para Locação**  
O imóvel ficará nessa situação quando a subtração do Valor M² Disponível pelo M² Reservado for maior que zero.  
Dessa forma, o imóvel possui área disponível, podendo ser alugado em outro Contrato de Locação.

🟡 **Reservado**  
O imóvel ficará nessa situação quando a subtração do Valor M² Disponível pelo M² Reservado for igual a zero.  
Dessa forma, o imóvel não possui área disponível, não podendo ser associado a outro Contrato de Locação.

🔴 **Locado**  
O imóvel ficará nessa situação quando os campos M² Disponível e M² Reservado forem iguais a zero e o campo M² Locado for maior que zero.  
Dessa forma, o imóvel não possui área disponível.

---

## ⚙️DADOS GERAIS DO IMÓVEL

* **Tipo de Área:** Urbano ou Rural;
* **Tipo de Locação:**  
  Define como será realizada a locação do imóvel.  
  Ao associar um Contrato de Locação ao imóvel, este campo fica bloqueado.  
  Para alterá-lo, o imóvel não pode estar associado a nenhum Contrato de Locação.

  **Opções disponíveis:**

  + **Imóvel:** O imóvel só poderá ser locado por inteiro.
  + **Áreas Fracionadas:** O imóvel poderá ser locado por m², sendo necessária a associação de áreas.
  + **Áreas Unificadas:** O imóvel será locado por inteiro, permitindo associação de áreas sem alteração dos valores.
* **Data do Cadastro:** Data em que o imóvel foi incluído no sistema;
* **Data de Aquisição:** Data em que o imóvel foi adquirido (campo informativo);
* **Tipo de Imóvel:** Permite informar o tipo do imóvel;
* **Centro de Custo:** Setores ou áreas que permitem a apuração dos gastos;
* **Realiza integração com portais externos:**  
  Disponível a partir da versão 12.1.28.  
  Ao marcar este campo, o imóvel estará disponível para integração com portais externos, como Zap Imóveis e outros;
* **Observação:**  
  Disponível a partir da versão 12.1.28.  
  Este campo será enviado na tag <Description></Description> do [.xml de integração com portais externos;](https://tdn.totvs.com/pages/viewpage.action?pageId=538492830)
* **Item Contábil / Classe de Valor:**  
  Provenientes do Protheus, disponíveis a partir da versão 12.1.24, apenas quando a integração estiver ativa. Mais informações acesse: [Imóvel - Integração RM x Protheus - Item Contábil e Classe de Valor](https://tdn.totvs.com/pages/viewpage.action?pageId=458762373)

---

## 📂DADOS COMPLEMENTARES

* **Cartório:** Campo informativo que identifica onde o registro do imóvel foi realizado;
* **Prefeitura:** Este campo possibilita informar a Prefeitura onde o imóvel está localizado. Este campo irá exibir os registros do cadastrado de Cliente/Fornecedor do módulo Gestão Financeira. Sendo assim é necessário realizar o cadastro da prefeitura como Cliente/Fornecedor para que ela seja associada ao imóvel;
* **Regularizado:** Define se o imóvel está regularizado;
* **Sub-unidade:** Preenchido automaticamente após o processo de gerar sub-unidade;
* **Localização das Chaves / Observação:** Campo livre para link de localização (ex.: Google Maps);
* **Tipo de Finalidade:** Campo utilizado para indicar a finalidade de uso do imóvel, informação necessária para os cálculos relacionados à reforma tributária e para definir se o redutor social será aplicado na base de cálculo. O redutor social incidirá apenas quando o Tipo de Finalidade for **Residencial**. As opções disponíveis são **0-Comercial**, **1-Residencial** e **2-Misto**.
* **Tipo de Imóvel – DAI (Declaração de Atividades Imobiliárias).**

---

## 📐ÁREAS E VALORES DO IMÓVEL

* **Área Privativa m²:**  
  Área privativa representa o espaço interno do imóvel, sejam eles Casas, Apartamentos e etc., incluindo as garagens;
* **Área Comum m²:**  
  A área comum representa todos os espaços comuns dentro do domínio de um imóvel. Podemos tomar como exemplo as áreas de uso comum por inquilinos, área condominial, o espaço existente dentro dos prédios e etc;
* **Área Total m²:**  
  A área total compreende a soma da área Privativa e área Comum;

false

🔎 **Observação:**  
Ao selecionar as opções **Áreas Fracionadas** ou **Áreas Unificadas** no campo **Tipo Locação**, os campos **Área Privativa m²** e **Área Comum m²** são desabilitados e seus valores zerados, visto que o controle desses valores deve ser realizado pela associação de Áreas ao Imóvel.  
O campo **Área Total m²** também é bloqueado e seu valor passa a ser o somatório das Áreas associadas ao Imóvel.

* **Valor médio do M²:**  
  O resultado deste campo é o somatório do Valor Total dividido pelo somatório total de M² das áreas vinculadas ao imóvel;
* **Fórmula do Valor médio do M²:**  
  (Somatório Valor Total das áreas / Somatório Total de M² das áreas);

false

🔎 **Observação:**  
Até as áreas com parâmetro **"Compõe Saldo de área para locação"** desmarcado são usadas no cálculo;

* **Valor de Locação:**  
  Valor que será cobrado pelo aluguel do Imóvel;

false

🔎 **Observação:**  
Ao selecionar as opções **Áreas Fracionadas** ou **Áreas Unificadas** no campo **"Tipo Locação"**, o campo **"Valor de Locação"** tem o seu nome alterado para **Valor médio m²**, pois passará a exibir o valor médio do m² das Áreas associadas ao Imóvel;

* **Valor do Condomínio:**  
  Valor cobrado em relação às taxas do condomínio;
* **Valor dos Encargos:**  
  São aquelas despesas que normalmente devem ser contabilizadas e consideradas dedutíveis do Imposto de Renda e da Contribuição Social sobre o Lucro, sem estarem com os valores totalmente definidos em termos monetários;

---

* **Imóvel de terceiros:**  
  Ao desmarcar essa opção, será exibido o campo **Percentual de Propriedade da Administradora**, permitindo definir o percentual de participação da empresa no imóvel.  
  Este campo não poderá ser alterado quando o imóvel já estiver vinculado a um contrato de administração com situação **Em Elaboração** ou **Efetivado**.
* **Percentual de Propriedade da Administradora:**  
  Define o percentual de participação da Administradora no Imóvel.  
  Se for menor que 100%, será necessária a criação de um Contrato de Administração do Imóvel, definindo quem é o proprietário do restante do imóvel.  
  Caso o valor seja igual a 100%, o imóvel não precisará de Contrato de Administração e a situação do imóvel passará a ser **Disponível para Locação**, podendo assim ser associado a um Contrato de Locação;
* **Permite negociação:**  
  Ao marcar essa opção, o sistema permitirá que o valor de locação do Imóvel no Contrato de Locação seja diferente do valor cadastrado.  
  Dessa forma, o campo **"Valor de Locação"** será habilitado para edição na associação do Imóvel ao Contrato de Locação.  
  Caso o imóvel tenha o **Tipo Locação** como **Áreas Fracionadas** ou **Áreas Unificadas**, o valor por m² das Áreas do Imóvel também poderá ser modificado.

---

## 📍ENDEREÇO

* **Tipo de Endereço:** Define a qual o tipo de endereço do imóvel. Exemplo: comercial, residencial, etc;
* **Região:** Define a região onde está localizado o imóvel;
* **CEP:** Valor numérico e único que identifica um logradouro;

  false

  **ℹ️ Observação:**  
  A partir da versão **12.1.22**, além do sistema preencher automaticamente os campos abaixo de acordo com o CEP informado, o usuário poderá clicar nos **"..."** para efetuar uma busca mais abrangente de CEPs cadastrados no banco de dados.  
  Este cadastro utiliza a busca de CEPs e precisa estar atualizado. Para mais informações, [acesse **Importação de CEPs**.](https://tdn.totvs.com/pages/viewpage.action?pageId=210046356)
* **Tipo Logradouro:** Categoria em que o logradouro se enquadra;
* **Logradouro:** Nome da Rua;
* **Número:** Número que identifica o imóvel em um logradouro;
* **Complemento:** Informações complementares do endereço;
* **Bairro:** Código do Bairro;
* **Município:** Código do Município;
* **Estado:** Código do Estado;
* **País:** Código do País;
* **Localização:** Campo livre que possibilita informar um link para localização do imóvel, como o Google Maps, por exemplo.

 Informações Complementares

---

* [Histórico de situação do imóvel](http://tdn.totvs.com/pages/viewpage.action?pageId=435104786)





* [Período de Indisponibilidade do Imóvel](http://tdn.totvs.com/pages/viewpage.action?pageId=435105363)

Como Fazer

---

* [Buscar Imóveis](http://tdn.totvs.com/pages/viewpage.action?pageId=435104818)
