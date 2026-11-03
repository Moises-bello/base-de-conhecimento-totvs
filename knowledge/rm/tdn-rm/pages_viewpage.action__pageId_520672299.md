---
content_hash: 4108d7278b708054a327cabd85b09fef146f235bef9c40aaeb7348d2ecc6ccb1
fetched_at: '2026-06-29T00:10:31.165898+00:00'
page_id: '520672299'
product: rm
source: tdn-rm
title: Guias de Autorização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520672299
version: 22
---

## **CONTEÚDO**

2CONTEÚDO

## **01. Visão Geral**

Essa rotina é responsável por informar quais foram os itens necessários de **Autorização** junto a **Operadora**. Essa rotina é acessada através da aba **Autorização** na tela do **Registro de Atendimento.**

## **02. Incluíndo uma Autorização**

Após salvar o registro de atendimento é possível incluir a **Autorização** através da sua respectiva aba.

Na inclusão/edição de uma guia é possível selecionar os seguintes tipos:

**Guias para atendimentos Externos** 

1. 1. Guia de Consulta
   2. Guia de SP/SADT
   3. Guia de Outras Despesas

**Guias para atendimentos Internos**

1. 1. Guia de Honorário Individual
   2. Guia de Resumo de Internação
   3. Guia de Solicitação de Internação

A inclusão/edição de uma guia não permite a seleção de parciais canceladas, ou seja, no campo Parcial só serão exibidas as parciais com o status Elaboração.

Os campos em negrito são de preenchimento obrigatório, mas é possível que os campos opcionais passem a ser de preenchimento obrigatório, no próximo tópico será explicado mais em detalhes sobre os parâmetros.

Para facilitar a inclusão de múltiplas autorizações na mesma guia, a tela mantém uma cópia das dos principais campos que foram digitadas na guia anterior. Desta forma, é necessário preencher apenas o novo item a ser autorizado.

Importante!

Caso a tela seja fechada, a cópia será perdida.

## **03. Dados do****Cabeçalho da Guia de Autorização**

Uma vez que incluída uma guia, um cabeçalho é criado automaticamente permitindo preencher informações adicionais conforme a tela abaixo:

Esta tela é acessada através do botão da guia de autorização e os seguintes campos estão disponiveis em tela:

* + **Campo Indicação Clínica**: é habilitado para os seguintes tipos de guia:  
    - Guia de SP/SADT
    - Solicitação de Internação

* + **Observação**: é habilitado para os seguintes tipos de guia:
    - Guia de Consulta
    - Guia de SP/SADT
    - Guia de Solicitação de Internação
    - Guia de Resumo de Internação
    - Guia de Honorário Individual
  + **Guia Principal**: é habilitado para os seguintes tipos de guia:
    - Guia de SP/SADT
  + **Guia Solicitação de Internação**: é habilitado para os seguintes tipos de guia:
    - Guia de Resumo de Internação - para que o número da guia de solicitação seja preenchida no XML é necessário preencher o campo abaixo.
    - Guia de Honorário Individual

* + **Tipo de acomodação**: é habilitado para os seguintes tipos de guia:
    - Guia de Honorário Individual
    - Guia de Resumo de Internação
  + **Guia prestador**: é habilitado quando o parâmetro "Permite Alterar" estiver marcado e o parâmetro "Guia Prestador: Mesmo número da guia operadora" estiver desmarcado
* + **Data da Solicitação**: está sempre habilitado para todas as guias, enquanto a guia estiver com o status pendente. Este campo é preenchido automaticamente ao efetuar a solicitação de procedimento utilizando o WebService TISS. Depois de enviado para a operadora, o campo não permitirá mais alterações, exibindo uma mensagem.
* + **Contratado Solicitante**: está sempre habilitado para todas as guias. Se não preenchido, será utilizado o prestador principal da Unidade de Faturamento do Atendimento. Caso haja necessidade que seja um prestador especifo, o mesmo deverá ser preenchido.

## **04.** **Configurando o WebSerives (T****ISS ONLINE)**

Nosso sistema está preparado para trabalhar com o Web Services no padrão TISS e Orizon.

Utilizando esse serviço, será possível através do nosso sistema realizar a comunicação diretamente com a Operadora, sem a necessidade de entrar no seu portal e digitar os dados do paciente e seus procedimentos. 

Os seguintes serviços estão disponíveis:

* + Solicitação de Elegibilidade
  + Solicitação de Autorização
  + Solicitação de Cancelamento da Guia
  + Solicitação de Status da Autorização

Importante!

O serviço de Elegibilidade não está disponível na Orizon.

Para que o sistema faça a comunicação online das autorizações, será necessária a configuração dos endereços de cada serviço.

Existem duas maneiras de realizar a autenticação:

* + Através da utilização de um certificado digital emitido por uma empresa certificadora.
  + Através de um usuário e senha que a operadora disponibilizou para o prestador.

Somente uma das formas deverá ser utilizada, caso a autenticação seja feita através do usuário e senha, os respectivos campos devem ser preenchidos em tela

Após a configuração do Web Service, os seguintes serviços podem ser utilizados:

* + **Elegibilidade** é executado após o preenchimento da carterinha do paciente durante o **Registro do Atendimento**.
  + **Solicitação de Autorização** pode ser executado pelo usuário após salvar um novo item na **Autorização**, para que seja solicitada a autorização com a operadora.
  + **Solicitação de Status da Autorização** pode ser executado quando o Status de um item estiver **Em Analise**, nesse momento o sistema irá comunicar com a operadora, pedindo um novo status para aquele item.
  + **Solicitação de Cancelamento da Guia** pode ser executado para cancelamento integral da Guia junto a operadora.

Durante essa comunicação, alguns dados serão retornados pela **Operadora**, tais dados são gravados no cabeçalho da autorização ou no próprio item, como por exemplo, **Status, Número da Guia da Operadora, Senha, Validade da Senha**, etc.

Na aba Históricos, ficam registradas todas as comunicações com a **Operadora**, assim como o **Motivo da Glosa** para os itens que não foram autorizados.

## **05.** **Lançamento Automático da Guia de Solicitação de Internação**

Ao incluir uma guia de Resumo de Internação, o sistema deve verificar se existe uma guia de solicitação de internação com o mesmo número de guia. Caso não exista, o sistema deve incluir automaticamente com os mesmo dados da guia de resumo.

## **06. Parâmetros**

O sistema possui diversos parâmetros para serem utilizados no momento da **Autorização**, para saber mais como configurar esses parâmetros consultar nossa documentação

## **07.** **Inclusão do Item na Parcial de Paciente Externo**

Ao incluir um item na guia/autorização, para que ocorra a cobrança automática do mesmo na parcial do paciente, deve-se atentar à seguinte parametrização (Parâmetros Gerais):

* + Cobrança automática a partir da Autorização/Guia de paciente externo
    - Consultas
    - Clínica Geral
    - Exames
    - Pacotes

Caso o item esteja em alguma dessas faixas no padrão de faturamento e codificação, o sistema fará a cobrança com o respectivo centro de custo parametrizado. Como a cobrança só ocorrem nessas faixas, então o sistema só lança honorários, exames e serviços do tipo pacote.

Para que ocorra o lançamento corretamente é necessário que o médico responsável pelo atendimento esteja informado, pois o mesmo será o médico executante no lançamento.

A data a ser considerada no lançamento do item segue o seguinte critério:

* + Caso a data da guia esteja preenchido, considera a data da guia
  + Caso a data da guia for maior que a data de saída (data da alta) utiliza a data de saída do atendimento
  + Caso a data da guia não esteja preenchido utiliza a data de entrada do atendimento

Todos os lançamentos serão vinculados ao número da guia informado durante a inclusão.

* + **Exclusão de item da guia**

O sistema não permite excluir um item da guia, nas seguintes condições:

* + Parcial com status de cancelada, faturada ou liberada para faturamento

* + Guia de  SP/SADT ou de consulta, com status de Em análise ou autorizada, para convênio que utiliza webservice. Neste caso é necessário solicitar o cancelamento da guia junta a operadora.
  + Se o item for um exame e o mesmo estiver associado a um pedido de exame e o status esteja como inicial, em digitação ou saiu para coleta

Caso nenhuma das condições acima sejam verdadeiras, o sistema realiza o estorno do item na conta do paciente. Se for via pedido de exames, o item é cancelado do pedido e estorno da conta.

* + Alteração

Não é permitida a alteração do **Tipo da Guia**, se foi gravado errado, a guia deverá ser excluída e uma nova incluída.

Caso o **Núm Guia / Comprovante** seja alterado, esse número será atualizado no seu respectivo item em que será cobrado na **Elaboração de Contas**.

* + Impressão da Guia

Para a correta impressão das guias é necessário a importação dos relatórios através do menu Gestão, botão RM Reports. Executar o processo Importar Estrutura de Relatórios e selecionar o arquivo TotvsReport desejado.

Uma vez que você tenha os relatórios das guias instalado é necessário configurar, qual relatório será exibido para cada tipo de guia da versão TISS correspondente.

Acessar Cadastros > Uso Geral > TISS > Versão TISS na MDI antiga e selecionar a versão da tiss que deseja e informar o relatório para cada tipo de guia do novo gerador.

Além disso, é possível definir uma impressora padrão para a estação de trabalho corrente. Ela será selecionada sempre que um novo relatório for exibido para impressão. Isto facilita na hora de enviar suas guias para a impressora.

Para imprimir uma guia, basta acessar, através do atendimento a aba  Autorização, selecionar a guia que deseja imprimir e executar o processo de impressão no menu Processos > Imprimir.

O sistema irá abrir uma pré-visualização da Guia de Autorização permitindo a conferência das informações da mesma.

A partir desta tela você pode enviar a guia para impressão, através do botão de impressão rápida ou ainda alterando as configurações de impressão antes de finalizar seu trabalho. 

### **Validações**

A impressão da guia será realizada pela nova MDI mediante algumas condições:

* + O relatório da guia para a versão tiss usada pelo convênio foi configurada para usar o novo gerador, caso esteja configurado para o gerador antigo exibirá a mensagem:

**TISS 3.0X.0X configurada para versão antiga dos relatórios das guias. Configurar para nova versão em Cadastros > Uso Geral > TISS > Versão TISS.**

* + A parcial da Guia não pode estar cancelada, caso esteja irá exibir a mensagem:

**Não é permitida a impressão do relatório em uma parcial** **cancelada.**

* + A Guia deve ter um número, caso não tenha será exibido a mensagem:

**Para impressão das guias de solicitação, o número da guia deverá ser preenchida****.**

* + O atendimento deve ter informações TISS vinculadas a ele, caso não tenha será exibida a mensagem:

**Faltam informações exigidas pelo padrão TISS - ANS que serão necessárias para este processo. Informe através da opção Informações ANS - TISS no menu lateral.**

* + A guia deve ser de solicitação de autorização (Guia de Solicitação de SP/SADT,  Guia de Solicitação de Internação, ), Caso não seja desses tipos será apresentada a mensagem:

**Função permitida somente para os tipos de guias de solicitação de autorização.**

* + O convênio da parcial  deverá estar configurado para versão TISS igual ou posterior a 3.00.00, caso não esteja será apresentada a mensagem:

**Impressão de guias de solicitação permitida somente para versão TISS 3.00.00 ou superiores.**
