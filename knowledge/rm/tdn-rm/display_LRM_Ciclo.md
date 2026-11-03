---
content_hash: 39fee0d4e36f1d79a666c5542fc335a0cb94b45c74daa702c225f9182e0d5d71
fetched_at: '2026-06-29T00:11:38.933292+00:00'
page_id: '786541562'
product: rm
source: tdn-rm
title: Ciclo
type: documentation
url: https://tdn.totvs.com/display/LRM/Ciclo
version: 16
---

O ciclo de transporte representará o trajeto ou percurso que os equipamentos realizarão para a retirada de resíduos, a carga e descarga de materiais e demais insumos a serem utilizados na obra, permitindo o acompanhamento entre das distâncias ou o registro do tempo gasto nessa atividade.

Após os apontamentos, essas informações são enviadas do APP Minhas Obras para o TOTVS Construção Obras e Projetos, no qual posteriormente é realizada a conciliação, manual (caso não utilize o QR code, onde a conciliação é feita de forma automática) dos apontamentos de carga e descarga e a apropriação dos custos nas respectivas tarefas.

Isto posto, para visualizar o ciclo no App Minha Obra e começar a fazer os apontamentos, é necessário primeiramente efetuar o cadastro no sistema e sincronizá-lo.

O cadastro de Ciclo de transporte encontra-se na opção de menu: Controle \ Minha Obra \  do Totvs Construção - Obra e Projetos

****Apontamento ciclo de transporte no App****

**Saiba como realizar o Apontamento de Ciclo de Transporte no APP:**

**Carga e Descarga de Ciclo de Transporte:**Para o apontamento de Ciclo de Transporte é necessário o registro da carga e descarga, porém, para o sincronismo, um não depende do outro, apenas no TOP que são necessários para realizar a conciliação dos apontamentos.

**Seleção de Ciclo para Carga:** Essa tela exibe os ciclos disponíveis para apontamento de carga que foram previamente cadastrados no TCOP:

**Apontamento de Ciclo:**Nessa tela o apontamento pode ser incluído (Carga ou Descarga dependendo da opção selecionada na tela anterior a seleção do ciclo), onde o equipamento (transporte) em questão deve ser informado. Para visualização, o equipamento deverá ter sido previamente cadastrado em Mobilidade> Equipamentos> Equipamentos associados ao projeto.

        

Quando habilitado para utilizar campos complementares nos apontamentos de ciclo de transporte, a visualização da tela ficará da seguinte forma:

Abaixo da informação de equipamento seguirá exibindo os campos complementares definidos nos parâmetros de projeto. 

No exemplo abaixo foram exibidos os campos (Atividades , Tipo\_carga e Lider\_Equipe). Veja os detalhes como parametrizar e utilizar esses campos complementares dos apontamentos de ciclo de transporte em: ,  

Quando o ciclo de transporte for do tipo distância percorrida, a tela do aplicativo irá exibir também o campo de Marcador da carga:

Quando utilizamos o parâmetro de projeto para **Informar Equipamento Responsável pela Carga** (para saber mais sobre esse parâmetro [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=662419328)), tanto no ciclo por distância Pré-Definida quanto para o ciclo de Distância Percorrida no App Minha Obra, somente nos apontamentos de **Carga** o campo **Equipamento Responsável pela Carga** será exibidopara informar o equipamento, lembrando que esse campo só busca equipamentos associados ao Projeto.

Abaixo o exemplo do campo na tela do App Minha Obra nos apontamentos dos dois tipos de ciclo.

Aqui o Campo **Equipamento Responsável pela Carga**no ciclo por **Distância Pré-Definida**:

Já aqui o Campo **Equipamento Responsável pela Carga**no ciclo por **Distância Percorrida**:

Após o sincronismo, a informação do equipamento responsável pela carga, ficará disponível nas telas de  e .

Ao salvar o apontamento, será exibido o QR Code:

Clicando em "Ver detalhes do apontamento" são exibidos os dados do apontamento; no exemplo abaixo, um apontamento de carga do tipo distância pré-definida e um do tipo distância percorrida, respectivamente::

     

Clicando no botão "Compartilhar" na tela do QR Code, o usuário será direcionado para a tela de compartilhamento do dispositivo; e por isso a tela abaixo pode variar um pouco dependendo do dispositivo em que o app está sendo usado.

     

Ao selecionar a opção de compartilhamento desejada, o usuário receberá uma imagem do comprovante com os dados do apontamento contendo o QR Code, conforme mostram os modelos abaixo:

   

Selecionando a opção de imprimir, ao salvar o apontamento, serão listados os dispositivos pareados, e o usuário poderá selecionar a impressora disponível para envio do mesmo comprovante da carga que contém o QR Code, demonstrado logo acima:

Verifique as permissões conforme documentação:

**Seleção de Ciclo para Descarga:** Essa tela exibe os ciclos disponíveis para apontamento de descarga e o procedimento manual é o mesmo realizado para carga demonstrado acima.

Uma vantangem é a possibilidade de realizar o apontamento da descarga através da leitura do QR Code gerado na carga, bastando clicar no botão QR Code:

Ao clicar no botão do QR Code, será ativada câmera do dispositivo e ao posicioná-la sobre o QR Code da carga, será realizada a sua leitura:

São exibidos os dados da carga e os campos para apontamento da descarga que será realizado. No ciclo de transporte do tipo distância percorrida, além de exibir a informação do marcador da carga, são exibidos os campos de marcador da descarga e acréscimo, que deverão ser preenchidos para o cálculo da distância:

     

No ciclo de transporte do tipo distância percorrida, ao clicar em salvar, é exibida a tela abaixo, com a distância calculada, baseada nas informações que foram preenchidas durante os apontamentos de carga e descarga (marcadores da carga, da descarga e acréscimo):

**Cálculo da Distância Calculada (Km):**

Para entender como é realizado o cálculo da distância percorrida exibida na tela acima 

Depois de salvar o apontamento, será exibida a tela abaixo, independente do tipo do ciclo, com os botões de **Ver detalhes do Apontamento**, **Compartilhar, Imprimir e Voltar para Ciclo,**assim como na carga.

Ao clicar em "Ver detalhes do Apontamento" depois de salvar o **Apontamento de Descarga**, a tela com os dados da Carga e da Descarga, nesse exemplo, carga e descarga feitos no mesmo dispositivo e sem sincronizar, para o Ciclo será mostrada, como nas imagens abaixo, para os ciclos do tipo distânca pré-definida e distância percorrida respectivamente:

     

Clicando no botão "Compartilhar" depois de salvar o **Apontamento de Descarga**, o usuário será direcionado para a tela de compartilhamento do dispositivo; e por isso a tela abaixo pode variar um pouco dependendo do dispositivo em que o App está sendo usado:

     

As imagens abaixo são exemplos de arquivos compartilhados ou impressos para a descarga dos ciclos de distância pré-definida e percorrida, respectivamente:

   

Clicando em "Voltar para Ciclo" na tela final do Apontamento do ciclo, será redirecionado para tela inicial da funcionalidade, como na imagem abaixo:

**Dica :**

Ao realizar o apontamento de ciclo de transporte e por alguma razão não tiver sido possível compartilhar os dados naquele momento, na tela "Informações do Aplicativo", são exibidos os detalhes dos apontamentos pendentes e nessa visão de Detalhes é possível também compartilhar o QRCode gerado.

Para isso deve-se clicar em cima da informação da carga, automaticamente abrirá a tela do QRcode permitindo o compartilhamento e também a visualização dos dados da carga.

O mesmo vale para apontamentos de descarga. Na tela das funcionalidades do App, acessando o ícone de Informações -> Detalhes -> pressionando sobre o apontamento da descarga. Neste caso, do apontamento da **Descarga**, será exibida a tela com "Ver detalhes do Apontamento" e "Compartilhar" para conseguir ver ou enviar novamente os dados da **Descarga**.

Abaixo estão as telas com os detalhes da descarga e um exemplo da imagem que será compartilhada:

 

**Sincronismo**

**Sincronismo (Envio e recebimento do coletor)**

* Para que o sincronismo possa ser realizado, é necessário que o WebService que receberá e enviará informações esteja ativo;
* É necessário dispor de um coletor móvel ou utilizar um emulador;
* Com a aplicação no coletor aberta, realizar o sincronismo com o usuário e senha de acesso a base de dados do TOP, ou seja, usuário definido para utilização do coletor;
* Ao término do registro de apontamentos de ciclo de transporte, carga e descarga, os mesmos podem ser enviados para o TOTVS Construção Obras e Projetos através do sincronismo e consequentemente estará visível na visão de **Apontamentos dos Coletores** nos anexos de Ciclo de Transporte. Há necessidade de realizar a conciliação, validar e apropriar. Estas funcionalidades serão tratadas posteriormente. Para sincronizar, basta acionar o botão abaixo:

**Apontamento ciclo de transporte no RM**

Após a sincronização de dados do Coletor Móvel para o TOTVS Obras e Projetos o usuário deve acessar o menu Controle | Minha Obra | Ciclos de transporte anexo . O sistema irá exibir uma visão onde é possível consultar e alterar os dados de apontamentos dos ciclos de transporte.

**Conciliar apontamentos no RM**

A conciliação de apontamentos é um processo do anexo "Apontamentos dos Coletores".

Através deste processo o sistema efetua a conciliação de registros de carga (início) e descarga (fim) do Ciclo de Transporte, que estão dispostos linha a linha separadamente, e os transforma em um único registro no anexo de "Apontamentos conciliados". Os apontamento realizados através da leitura do QR code pelo app, descritos acima, já aparecerão conciliados no TOTVS Obra e Projetos após o sincronismo.

Para maiores informações sobre o anexo de Apontamentos Conciliados .

**Apropriar custos de apontamentos**

Para entender mais sobre a apropriação do custo, dos apontamentos de ciclo de transporte no TOTVS Obras e projetos, acesse o link referente a Apropriação .

**Relatório**

Foi disponibilizado no book de relatórios, um relatório para impressão dos ciclos de transporte. Com ele é possível gerar um código QR para leitura no App Minha Obra, que irá direcionar para ciclo e facilitar os apontamentos de carga e descarga.

Clicando no ícone do código de barras na tela de carga ou descarga, é possível escanear o QR Code do ciclo:

Para visualizar o relatório e como encontrá-lo basta .
