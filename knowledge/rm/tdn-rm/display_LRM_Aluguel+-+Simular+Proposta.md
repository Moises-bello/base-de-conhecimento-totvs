---
content_hash: 853a842cd44ab82a1b797863fe121cd49b18c2249f62e8f079728c1eafb6d2ce
fetched_at: '2026-06-29T00:10:57.881523+00:00'
page_id: '600297018'
product: rm
source: tdn-rm
title: Aluguel - Simular Proposta
type: documentation
url: https://tdn.totvs.com/display/LRM/Aluguel+-+Simular+Proposta
version: 40
---

#FF9900Introdução

Ao [buscar um imóvel](https://tdn.totvs.com/pages/viewpage.action?pageId=593452987) e clicar no botão "simular" de um imóvel específico, iremos para a página de simulação de proposta, onde iremos preencher as etapas necessárias para a geração de um contrato de locação. Abaixo estarão listadas mais minuciosamente estas etapas e seus respectivos cadastros obrigatórios.

O sistema irá listar, na parte esquerda da tela de simulação, as etapas obrigatórias para salvar a proposta e se estão concluídas ou não, como mostra a imagem abaixo. Dessa forma o usuário pode, facilmente, ver o que resta ser preenchido para enviar a proposta para o RM.

Abaixo teremos uma descrição mais detalhada de todos estas etapas.

#FF9900Primeira Etapa - Locatário

Aqui nesta etapa iremos realizar um cadastro de Locatário ou utilizar um Locatário já cadastrado no banco.

Para definir um locatário principal, podemos efetuar a busca por um CPF ou Nome já cadastrado no banco de dados, digitando nos campos CPF ou Nome desta seção.

Poderemos também incluir um novo locatário, clicando no botão "Cadastrar novo locatário".

Ao clicar no botão Cadastrar novo locatário, será exibido o menu lateral de Inclusão de um novo locatário caso não esteja cadastrado. Preenchendo as informações pertinentes e clicando no botão salvar, este locatário será definido como locatário principal desta proposta. O cadastro de locatário é o mesmo do prospect no Portal de Imóveis, contudo possui menos campos para preenchimento. Caso o Portal de Imóveis tenha sido configurado para consistir a obrigatoriedade de campos que não aparecem na tela do Portal de Imóveis Aluguel, então o cadastro não será possível de ser finalizado e o mesmo deverá ser feito na tela de prospect do Portal de Imóveis.

Ao clicar no controle "Acrescentar novos locatários" será possível adicionar um locatário secundário à proposta. O cadastro deste locatário secundário segue o mesmo padrão do principal. Podemos fazer uma busca por uma pessoa existente na base ou cadastrar um novo.

Estando os locatários definidos podemos seguir para a segunda etapa que é a seleção do modelo de contrato ou ainda incluir um documento que seja pertinente a proposta como exemplificado abaixo.

##### **Documentação**

---

Esta etapa não é obrigatória e permite ao corretor inserir documentos que sejam pertinentes à proposta de aluguel.

Ao clicarmos em "Anexar", teremos a exibição da tela de uploads, que possibilitará o envio do documento, associando o mesmo ao locatário:

* **Selecione um locatário:** O locatário que o documento será associado. Caso a proposta possua mais de um locatário poderemos selecioná-lo neste campo;
* **Selecione um documento:** O tipo de documento ao qual o upload será associado. Para que a opção de tipo de documento apareça, ela deve ser incluída no cadastro de documentos do Portal de Imóveis e deve ser do tipo "Prospect";
* **Arraste os arquivos aqui ou selecione os arquivos no computador:** Poderemos arrastar um documento para essa tela ou selecionar um arquivo para o upload;
* **Formatos:** Apenas PDF, JPG, DOC, DOCX, XLS e XLSX serão aceitos;
* **Limite de tamanho:** O máximo permitido é o de 10mb;
* **Data de envio:** A data de envio do documento.

Para fazer o upload, selecione o locatário e o tipo de documento associado. 

Lembrando também que, após o upload será possível excluir o documento enviado ao clicar no ícone da lixeira.

Através do botão "**Lista completa de documentos**" poderemos visualizar também os documentos que foram enviados, bem como os documentos que ainda carecem de envio, facilitando o controle da documentação.

#FF9900Segunda Etapa - Modelo de Contrato

Nesta etapa, iremos selecionar o [modelo de contrato](https://tdn.totvs.com/pages/viewpage.action?pageId=435105135) que será utilizado para compor o contrato de locação. O [modelo de contrato](https://tdn.totvs.com/pages/viewpage.action?pageId=435105135) é um cadastro do backoffice e o mesmo possui informações padrão para a geração de um contrato de aluguel. O usuário deverá selecionar um modelo nesta etapa para continuar para a etapa seguinte.

Para entender o modelo e verificar suas informações, basta o usuário clicar no botão "Informações do modelo", que irá exibir todas as informações pertinentes ao modelo escolhido.

Serão exibidas as informações abaixo:

**Identificação**

* Descrição
* Regra de vencimento
* Dia de Vencimento
* Parâmetro Financeiro
* Tipo de Locação
* Tipo de Pagamento

**Reajuste**

* Periodicidade
* Índice

**Cálculos rescisórios e****Taxas** (Locatário e Locador)

#FF9900Terceira Etapa - Dados da Locação

Neste momento iremos determinar o número do contrato e os períodos do contrato, que são compostos pelos seguintes campos:

* **Início Vigência:** Determina o inicio de vigência do Contrato de Locação. Esse campo é utilizado para validação de processos que impactam no Contrato de Locação, tais como Reajuste, Aditivos, Escalonamento, onde deveram ter a data entre a Data de Inicio e Fim de vigência;
* **Final Vigência:** Esse campo por padrão é obrigatório. Porém através do parâmetro "Permite o Contrato de Locação ter prazo indeterminado", que se encontra no caminho Parâmetros do TOTVS Incorporação >> Aluguel >> Contrato de locação, quando marcado, esse campo deixa de ser obrigatório. Ao não preencher esse campo, o Contrato passa a ter o comportamento de Contrato com Prazo Indeterminado. Esse tipo de contrato não é permitido contabilizar por Período do Contrato ou por Linearização e Efetivar aditivo de Prorrogação do Contrato;
* **Inicio da Locação:** Esse campo determina o Inicio de Locação, onde será definido as Parcelas do Contrato de Locação. Através das parcelas, serão gerados os lançamentos do Contrato;
* **1º Vencimento:**Permite ao usuário definir a data de vencimento da primeira parcela do Contrato de Locação. É importante ressaltar que a definição desta data de primeiro vencimento, que se refere a cobrança do primeiro período, impacta nas demais datas de vencimento dos períodos posteriores pois elas serão subsequentes a esta data de primeiro vencimento seguindo a regra de vencimento.
* **Fim primeiro período:** Este campo irá definir o fim da primeira competência dos períodos de locação e, com isso, os demais períodos são definidos:
  1. Inicio da locação: 16/5 Fim do 1º período: 31/5 Desta forma, a primeira competência do contrato será 16/5 a 31/5, a segunda 1/6 a 30/6, a terceira 1/7 a 31/7, e assim sucessivamente até o fim do contrato;
  2. Inicio da locação: 16/5 Fim do 1º período: 10/6 Desta forma, a primeira competência do contrato será 16/5 a 10/6, a segunda 11/6 a 10/7, a terceira 11/7 a 10/8, e assim sucessivamente até o fim do contrato.
* **Dias de carência:** Este campo irá definir o número de dias em que o primeiro período de locação será deslocado:
  1. Início da locação: 10/01/2021 Dias de carência: 31 dias Início da primeira locação: 10/02/2021;
  2. Início da locação: 10/01/2021 Dias de carência: 75 dias Início da primeira locação: 26/03/2021;

### 

##### **Garantia**

---

Esta etapa não é obrigatória e permite ao corretor anexar uma garantia à proposta de acordo com os dados informados.

Ao clicarmos em "Incluir", teremos a exibição da tela de garantia, que possibilitará o cadastro das informações da garantia, com os seguintes campos:

* **Tipo de Garantia:** O Portal de Imóveis Aluguel lista os seguintes tipos;
  + Caução
  + Carta Fiança
  + Seguro Fiança
  + Título de capitalização
  + Cessão fiduciária
* **Código da Instituição:** A Instituição responsável pela emissão da garantia;
* **Número**: Texto livre que identifica a garantia no sistema.
* **Valor da Garantia:** Os valores em reais da garantia proposta;
* **Data de Pagamento:** Data estipulada para o pagamento
* **Data Inicial e Data Final:** Período de validade da garantia;
* **Observação:** Campo texto para possíveis observações a respeito do cadastro.

Caso o usuário necessite realizar algum ajuste na garantia associada, ou excluir a mesma, poderá realizar esse procedimento através do botão "Editar" da proposta no funil de aluguel.

Somente uma garantia poderá ser associada à um contrato.

#FF9900Salvar a proposta

Após concluir as etapas acima, será possível salvar a proposta.

Esta proposta será enviada ao Backoffice na forma de um contrato de aluguel. Todos os dados como locatários, imóveis, corretores, datas do contrato, bem como escalonamentos serão associados ao contrato que será criado no status "Em Elaboração".
