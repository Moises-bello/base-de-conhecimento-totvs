---
content_hash: 5f3ad54a173ee1da8e1b4969004876e392c4f4adac74354fd0e0a5946c011d4a
fetched_at: '2026-06-29T00:11:04.057364+00:00'
page_id: '624766184'
product: rm
source: tdn-rm
title: Ciclo de Transporte - App Minha Obra
type: documentation
url: https://tdn.totvs.com/display/LRM/Ciclo+de+Transporte+-+App+Minha+Obra
version: 58
---

Ciclo de TransporteCadastro

O ciclo de transporte representará o trajeto, percurso que os equipamentos realizarão para a retirada de resíduos ou a busca de matérias. Permitindo o acompanhamento ou medir o quesito tempo.

O cadastro de Ciclo de transporte encontra-se na opção de menu: Projetos \ Construção e Projetos \ Controle \ Mobilidade \ Ciclos de Transporte; 

* Esta informação será disponibilizada aos coletores e também será retornada ao ERP/TOP juntamente com os registros de apontamento. São através destas informações que o sistema identifica em qual ciclo ocorreu o apontamento e também obtém informações para efetuar os cálculos de apropriações;
* Permite o sincronismo de informações para o coletor móvel e o gerenciamento dos apontamentos realizados e sincronizados;
* Depende do cadastro do projeto e do cadastro do insumo;
* O ciclo será um cadastro do projeto e nele constarão as seguintes informações:
* Descrição: Descrição do ciclo de transporte;
* Insumo: O ciclo de transportes será associado a um insumo do TOP, que por sua vez contém informações de custo, bem associado ao insumo, unidade de medida, entre outras informações;
  + Distância (Km): Distância entre os lugares de carga/descarga. Sua unidade padrão será quilômetros (Km);
  + Disponível Coletor: Indica que este Ciclo estará disponível para ser enviado ao coletor associado ao projeto;
  + Considera Distância: Indica se a distância será utilizada no cálculo da apropriação;
  + Considera Capacidade do Bem: Indica se a capacidade do bem será utilizada no cálculo da apropriação;
  + Ativo: Indica se o ciclo de transporte está ativo.

**Importante:**

* + **Na inclusão do Ciclo de Transporte, os campos obrigatórios devem ser preenchidos, são eles, “Descrição” e “Insumo”;**
  + **Para a exclusão, o Ciclo de Transporte a ser deletado deve estar inativo, ou seja, o atributo “Ativo” deve estar desmarcado. Além disso, a exclusão de registros de ciclo de transporte somente poderá ser realizada caso não exista registros de apontamentos (anexo deste cadastro).**

**Capacidade do Bem**

Para que seja considerada a capacidade do Bem no cálculo da apropriação, é necessário realizar o cadastro dos campos complementares no módulo de Backoffice - Gestão Patrimonial; conforme detalhado abaixo:

No módulo de Gestão Patrimonial, acesse o menu Cadastros/Campos Complementares/Patrimônio:

E realize o cadastro dos dois campos conforme as imagens:

**Importante:**

* **É imprescindível que as colunas sejam criadas com a nomenclatura exata - CAPACIDADEPROD e CAPACIDADECODUND - caso considere a capacidade do bem na apropriação.**
* **Isso também é válido para o correto funcionamento da integração com o SIGAMNT, pois esses campos deverão ter seus valores preenchidos através do sincronismo entre os sistemas.**

Com base nos valores desses campos complementares, contidos no cadastro do patrimônio associado ao insumo informado no ciclo de transporte, que é calculada a apropriação:

Caso os campos não sejam informados, o cálculo da apropriação será realizado como se o checkbox "Considera Capacidade do Bem" não estivesse marcado.

Para saber mais sobre a apropriação do Ciclo de Transporte, navege até a aba "Apropriar Custos de Apontamento"

****Mapa de Apontamentos - Ciclos de Transporte:****

Apontamento Ciclo de Transporte - APP

**Saiba como realizar o Apontamento de Ciclo de Transporte no APP:**

**Carga e Descarga de Ciclo de Transporte:**Para o apontamento de Ciclo de Transporte é necessário o registro da carga e descarga, porém, para o sincronismo, um não depende do outro, apenas no TOP que são necessários para realizar a conciliação dos apontamentos.

**Seleção de Ciclo para Carga:** Essa tela exibe os ciclos disponíveis para apontamento de carga que foram previamente cadastrados no TCOP:

**Apontamento de Ciclo:**Nessa tela o apontamento pode ser incluído (Carga ou Descarga dependendo da opção selecionada na tela anterior a seleção do ciclo), onde o equipamento (transporte) em questão deve ser informado. Para visualização, o equipamento deverá ter sido previamente cadastrado em Mobilidade> Equipamentos> Equipamentos associados ao projeto.

        

Ao salvar o apontamento, será exibido o QR Code:

Clicando em "Ver detalhes do apontamento" são exibidos os dados do apontamento, no exemplo abaixo, um aporntamento de carga:

Clicando no botão "Compartilhar" na tela do QR Code, o usuário será direcionado para a tela de compartilhamento do dispositivo; e por isso a tela abaixo pode variar um pouco dependendo do dispositivo em que o app está sendo usado.

     

Ao selecionar a opção de compartilhamento desejada, o usuário receberá uma imagem com os dados do apontamento contendo o QR Code, conforme mostra o modelo abaixo:

Selecionando a opção de imprimir, ao salvar o apontamento, serão listados os dispositivos pareados, e o usuário poderá selecionar a impressora disponível para envio do comprovante da carga que contém o QR Code:

O comprovante impresso é o mesmo do compartilhamento.

**Seleção de Ciclo para Descarga:** Essa tela exibe os ciclos disponíveis para apontamento de descarga e o procedimento manual é o mesmo realizado para carga demonstrado acima.

Uma vantangem é a possibilidade de realizar o apontamento da descarga através da leitura do QR Code gerado na carga, bastando clicar no botão QR Code:

Ao clicar no botão, será ativada câmera do dispositivo e ao posicioná-la sobre o QR Code da carga, será realizada a sua leitura:

São exibidos os dados da carga e o apontamento da descarga que está sendo realizado:

Depois de salvar o apontamento, será exibida a tela abaixo com os botões de **Ver detalhes do Apontamento**, **Compartilhar, Imprimir e Voltar para Ciclo,**assim como na carga.

Ao clicar em "Ver detalhes do Apontamento" depois de salvar o **Apontamento de Descarga**, a tela com os dados da Carga e da Descarga, nesse exemplo, carga e descarga feitos no mesmo dispositivo e sem sincronizar, para o Ciclo será mostrada, como na imagem abaixo:

Clicando no botão "Compartilhar" depois de salvar o **Apontamento de Descarga**, o usuário será direcionado para a tela de compartilhamento do dispositivo; e por isso a tela abaixo pode variar um pouco dependendo do dispositivo em que o App está sendo usado:

     

A imagem abaixo é um exemplo do arquivo que foi compartilhado para a descarga:

Clicando em "Voltar para Ciclo" será redirecionado para tela inicial da funcionalidade, como na imagem abaixo:

**IMPORTANTE:** Ao sincronizar os apontamentos de carga e descarga, realizados através da leitura do QR Code, estes já serão exibidos no RM com status "Conciliado" e não "Pendente" como ocorre no apontamento de ciclo de transporte feito sem QR Code, demonstrados na imagem abaixo;  

**Dica :**

Ao realizar o apontamento de ciclo de transporte e por alguma razão não tiver sido possível compartilhar os dados, na tela "Informações do Aplicativo"  exibirá detalhes dos apontamentos pendentes e nessa visão de detalhes será possível também compartilhar o QRCode gerado.

Para isso deve-se clicar em cima da opção "Carga" , automaticamente abrirá a tela do QRcode permitindo o compartilhamento e também a visualização detalhada dos dados da carga.

Na tela das funcionalidades do App, acessando o ícone de Informações -> Detalhes -> pressionando sobre a descarga, neste caso somente quando tiver apenas o apontamento da **Descarga**, será exibida a tela com "Ver detalhes do Apontamento" e "Compartilhar" para conseguir ver ou enviar novamente os dados da **Descarga**.

Abaixo estão as telas com os detalhes da descarga e um exemplo da imagem que será compartilhada:

Apontamentos Ciclo de Transporte - RM

Acesse:

* Menu: Projetos \ Construção e Projetos \ Controle \ Mobilidade \ Ciclos de Transporte \ Anexo \ Apontamentos dos Coletores;

* Os apontamentos de Ciclo de transporte recebidos dos coletores são armazenados no sistema da forma que foram recebidos:
  + Registros correspondentes às cargas dos ciclos (início de ciclo);
  + Registros correspondentes às descargas dos ciclos (fim do ciclo).
* Os registros de carga e descarga poderão ser realizados em coletores distintos. Os apontamentos transmitidos ao ERP/TOP entrarão no sistema com o status “Pendente”.
* Este cadastro apresenta as seguintes informações:
  + Data Apontamento: Data e hora em que o apontamento foi realizado. A data irá também considerar os minutos e segundo (HH:mm:ss);
  + Tipo de apontamento: Indica se o apontamento é de Saída ou Entrada;
  + Carga: Indica o início do ciclo;
  + Descarga: Indica o fim do ciclo;
  + Status: Indica se o apontamento está pendente ou conciliado;

    - Pendente: Quando o registro foi exportado do coletor e está no sistema. Indica que o registro ainda não foi conciliado;
    - Conciliado: O apontamento já foi utilizado como origem/destino de um apontamento conciliado.
  + Equipamento: Equipamento em que foi realizado o apontamento;
  + Coletor: Coletor que realizou o apontamento. O coletor deverá estar associado ao mesmo projeto do apontamento;
  + Usuário: Usuário que realizou o apontamento. Este usuário deverá estar associado ao coletor em que o apontamento foi coletado;
  + Motivo Inconsistência: Campo texto para inclusão de observações sobre os apontamentos.
* Além de permitir a visualização dos apontamentos, o objetivo é permitir aos usuários realizar ajustes, identificar os emparelhamentos de cargas e descargas referentes aos equipamentos/ciclos para posteriormente efetuar a conciliação destes conjuntos para possibilitar a apropriação;
* São exibidos apontamentos pendentes e conciliados. Sendo assim, são disponibilizados filtros previamente configurados (como um botão na barra de ferramentas da visão) onde tais filtros permitem maior agilidade no gerenciamento dos registros principalmente, para localização e seleção para operação em grupo;
* Os filtros inicialmente idealizados para esta opção seriam os de “Apontamentos dos últimos 7 dias”, “Apontamentos nos último 30 dias”, “Apontamentos por data”, “Apontamentos pendentes”. Lembrando ainda das funcionalidades inerentes da visão que são a ordenação e agrupamentos por campos, capacidade de se utilizar funções de média, somatórios, etc. por campo.
Conciliar Apontamentos - RM

**Conciliar Apontamentos**

* Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Mobilidade \ Ciclos de Transporte \ Anexos \ Apontamentos dos Coletores \ Processo \ Conciliar Apontamentos;

* Realiza a conciliação de registros de carga (início) e descarga (fim), que estão dispostos linha a linha separadamente, e os transformam em um único registro que pode ser visualizado no anexo de “Apontamentos Consolidados”;
* Este processo é disparado manualmente onde será informado a data início e fim de carga. Todos os apontamentos dos equipamentos que possuírem data de carga neste período serão conciliados;
* O processamento de conciliação ocorre sempre aos pares de registros. O sistema ordena os registros de apontamentos pela data e então verifica se o primeiro registro é de carga e o próximo é de descarga, em caso afirmativo é efetuada a conciliação, atualização dos registros de origem. Em caso negativo desconsidera o primeiro registro, inclui uma mensagem explicativa no log do processo;
* Este processo será executado para todos os apontamentos resultantes do filtro de datas informado pelo usuário;
* Apesar da possibilidade de serem selecionados apontamentos de vários equipamentos distintos, o sistema efetua a conciliação por conjuntos de apontamentos de mesmos equipamentos;
* Apontamentos de um equipamento não irão ser processados junto ao conjunto de apontamentos de outro equipamento;
* Efetuada a conciliação, os registros originais ficarão marcados como “Conciliados” e não serão considerados nas próximas execuções;

Somente apontamentos com o status “Pendente” fazem parte do processo de conciliação.  
  
**IMPORTANTE:** Apontamentos de carga e descarga realizados através da leitura do QR Code, serão exibidos no RM com status "Conciliado" automaticamente após o sincronismo.

**Apontamentos Conciliados**

* **Anexo Apontamentos Conciliados**
  + Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Mobilidade \ Ciclos de Transporte \ Anexo \ Apontamentos Conciliados;

* + - Representa os registros de apontamentos já conciliados, cargas e descargas emparelhadas por ciclo/equipamento;
    - Os registros deste anexo são o “casamento” de dois registros, um de carga e outro de descarga, que originalmente estão no anexo de “Apontamentos dos coletores” e conterão as referências (identificadores) dos apontamentos que o originaram;
    - São exibidos apontamentos pendentes, validados e conciliados. Sendo assim, são disponibilizados filtros previamente configurados (como um botão na barra de ferramentas da visão) onde tais filtros permitem maior agilidade no gerenciamento dos registros, principalmente para localização e seleção para operação em grupo;
    - Os filtros inicialmente idealizados para esta opção são os de “Apontamentos dos últimos 7 dias”, “Apontamentos dos últimos 30 dias”, “Apontamentos por data”, “Apontamentos Pendentes”, “Apontamentos Validados”. Lembrando ainda das funcionalidades inerentes da visão que são a ordenação e agrupamentos por campos, capacidade de se utilizar funções de média, somatórios, etc. por campo;
    - Apresentar para o usuário os seguintes dados:
      * **Status**: Indica se o apontamento está pendente ou conciliado.
        + **Pendente**: Status inicial de um registro que foi conciliado;
        + **Validado**: Apontamento conciliado que foi validado pelo usuário. Este status indica que os dados conciliados estão corretos;
        + **Apropriado**: O apontamento conciliado teve seu custo apropriado. E um registro de apropriação foi gerado na apropriação de Serviços/Insumos.
      * **Equipamento**: Equipamento em que foi realizado o apontamento;
      * **Apontamento Início Ciclo**: Apontamento do início (saída) do ciclo de transporte.  É exibida a data e hora em que o apontamento do início do ciclo foi realizado. A data irá também considerar os minutos e segundos (HH:mm:ss);
      * **Apontamento Fim Ciclo**: Apontamento do fim (entrada) do ciclo de transporte.  É exibida a data e hora em que o apontamento do fim do ciclo foi realizado. A data irá também considerar os minutos e segundos (HH:mm:ss);
      * **Duração**: A duração do ciclo de transporte será a diferença em horas entre a data fim e a data início. Esta informação será calculada ao exibir a tela;
      * **Apropriação**: Exibe a tarefa em que o apontamento foi apropriado;
      * **Capacidade do Bem**: Exibe a capacidade do equipamento.

**Validar Apontamentos**

* Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Ciclos de Transporte \ Anexo \ Apontamentos Conciliados \ Processos \ Validar Apontamentos;
* É necessário que após a conciliação de dois apontamentos realizados pelos coletores o apontamento conciliado seja analisado e validado, com o intuído de certificar que as informações conciliadas estão corretas;
* O status Validado não possui uma forma automática que o valor, pois é uma situação onde o apontamento deve passar por uma verificação manual, uma análise pelo usuário a fim de garantir que suas informações estejam consistentes. Após esta verificação deve-se alterar o status do apontamento para “Validado";
* Através da lista de registros selecionados previamente na visão de apontamentos o sistema atualiza o STATUS de cada apontamento da lista para o valor “Validado”;
* Este processo é disparado sem a necessidade de uma interface específica em que o usuário precise informar algum dado em particular.

**Desfazer Conciliação**

* Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Ciclos de Transporte \ Anexo \ Apontamentos Conciliados \ Processos \ Desfazer conciliação;
* Este processo altera o STATUS dos apontamentos originais valorando-os como “Pendente” e exclui o registro de apontamento conciliado. Além disso, este é disparado sem a necessidade de uma interface específica em que o usuário precise informar algum dado em particular;
* Para execução deverá ser selecionado pelo menos um apontamento conciliado, porém, poderá ser executado para vários registros simultaneamente;
* Ao ser disparado somente serão desfeitas conciliações de registros com o status de “Pendente” ou “Validado”. Caso algum registro não possua algum destes status o processo executará normalmente e será incluída mensagem no final do processo informando que a conciliação não foi realizada.
Apropriar Custos de Apontamentos

**Apropriando Custos de Apontamentos**

* Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Mobilidade \ Ciclos de Transporte \ Anexo \ Apontamentos Conciliados \ Processos \ Apropriar custos de apontamentos;

* Este processo efetua a apropriação de custos para o projeto dos ciclos de transporte que foram obtidos via apontamentos de coletores móveis;
* A apropriação de custos é realizada sempre com base em uma obra/etapa/tarefa e vale lembrar que os apontamentos de ciclos de transportes coletados e exportados para o ERP/TOP, em primeira instância, não estarão associados a uma destas tarefas;
* A apropriação de custos se dará acessando o anexo de “Apontamentos conciliados”, selecionando os registros (apontamentos) que se deseja efetuar a apropriação e acionar o processo em questão;
* A apropriação não é um passo obrigatório e pode ser desabilitada via perfil e este deve ser o procedimento adotado caso deseje trabalhar somente com estatísticas (tiradas dos apontamentos dos coletores ou então dos apontamentos conciliados);
* O valor para a apropriação será calculado utilizando a distância do ciclo, preço do insumo, capacidade do bem, conforme parametrizado no cadastro do ciclo.  
  Este processo contém uma interface do tipo “WIZARD” onde a primeira tela apresentará ao usuário data e hora do último cálculo da curva ABC e a opção para cálculo da curva ABC. Caso a opção de cálculo esteja selecionada a curva ABC será recalculada;
* A segunda tela do processo exibe um controle para informar a tarefa na qual será realizada a apropriação dos apontamentos dos ciclos;
* São exibidas tarefas que possuem como recurso direto ou indiretamente o insumo informado no cadastro de ciclo de transporte. Além disso, as tarefas exibidas devem respeitar o parâmetro de projeto “Permite apropriar apenas serviço”. Se parâmetro estiver selecionado, serão exibidas apenas selecionar tarefas de último nível. Caso contrário etapas e obras também poderão ser escolhidas. Dessa forma, a primeira tela se faz necessário para garantir que a curva ABC esteja atualizada, já que as tarefas a serem exibidas no segundo passo serão obtidas a partir da curva ABC de insumos;
* Após confirmar a execução do processo o sistema efetua a apropriação somente dos apontamentos que ainda não foram apropriados. Apontamentos que tenham sido apropriados não são processados e o sistema os listará com uma mensagem explicativa ao final do processo;
* Caso algum apontamento não possa ser apropriado devido a alguma regra interna de apropriação o sistema não o processará, mas continuará o processamento do próximo registro. Estes apontamentos que apresentarem erro serão listados ao final do processo com suas respectivas mensagens de erro;
* Considerando que o apontamento é de um ciclo, que o ciclo de transporte possui a distância/quantidade e insumo, que o insumo tem seu valor por sua unidade e está associado a um bem e que o bem tem como um de seus atributos a capacidade. Então, podemos então descrever que o cálculo do valor da apropriação será: **DISTÂNCIA (QUANTIDADE DO CICLO) \* PREÇO DO INSUMO \* CAPACIDADE DO BEM**;
* O atributo “distância” do ciclo de transporte será informado no campo distância no cadastro do Ciclo de Transporte;
* A capacidade do bem/equipamento, quando integrado com SIGAMNT do PROTHEUS, está no Manutenção de Ativos e, via sincronização, será enviada ao RM/Bens (no campo complementar **CAPACIDADEPROD,** conforme utilização da capacidade, descrita na aba que detalha o cadastro de Ciclo de transporte). Qualquer alteração necessária na capacidade do bem deve ser feita no Manutenção de Ativos do Protheus e será refletida no RM;
* A forma de acompanhamento do Ciclo de Transporte pode variar, dependendo da forma como o serviço foi contratado. Sendo que, em alguns casos, a capacidade do bem ou a distância podem não serem consideradas no cálculo do valor a ser apropriado. Esta definição é feita no cadastro do Ciclo. Desta forma, o cálculo será flexível, parametrizado conforme o tipo de contratação do serviço;

  **Importante:**

  + - **Ao se excluir uma apropriação no cadastro de Apropriação de Serviços/Insumos em que está apropriação esteja associada a algum apontamento conciliado, o apontamento conciliado terá seu status modificado de “Apropriado” para “Validado”;**
    - **A data atribuída à apropriação será a data do apontamento de saída (data inicial) do equipamento no ciclo.**
Sincronismo

**Sincronismo (Envio e recebimento do coletor)**

* Para que o sincronismo possa ser realizado, é necessário que o WebService que receberá e enviará informações esteja ativo;
* É necessário dispor de um coletor móvel ou utilizar um emulador;
* Com a aplicação no coletor aberta, realizar o sincronismo com o usuário e senha de acesso a base de dados do TOP, ou seja, usuário definido para utilização do coletor;
* O apontamento é realizado por código de barras disponível no relatório de folha tarefa ou manual, selecionando a tarefa ou centro de custo, informando o motivo de improdutividade, caso exista;

1. 1. * + Ao término do registro de apontamentos de ciclo de transporte, carga e descarga, os mesmos podem ser enviados para o TOTVS Construção Obras e Projetos através do sincronismo e consequentemente estará visível na visão de **Apontamentos dos Coletores** nos anexos de Ciclo de Transporte. Há necessidade de realizar a conciliação, validar e apropriar. Estas funcionalidades serão tratadas posteriormente.
Relatório

O relatório**TOPREL0029 - Ciclos de Transporte.TotvsReport** pode ser encontrado no book de relatórios e sua geração disponibiliza os códigos de barras para serem utilizados no APP Minha Obra. A geração do relatório é através do menu Projetos \ Construção e Projetos \ Relatórios \ Mobilidade \ Ciclo de Transporte.

Deve-se selecionar o relatório e marcar os ciclos de transporte cadastrados e que serão exibidos na geração.

Informações exibidas neste relatório:

* Descrição do projeto (no cabeçalho);
* Descrição do ciclo de transporte;
* Distância (em KM) do ciclo de transporte;
* Insumo: código e descrição do insumo cadastrado no ciclo de transporte;
* Código de barras: o código de barras será formado pelo código da coligada, código do projeto e o código do ciclo de transporte.
