---
content_hash: b8ccf1e2c3371d7856682c975e84f9c52b60d0b49b34c1d7b6dc1018cd70c402
fetched_at: '2026-06-29T00:10:45.936499+00:00'
page_id: '553892752'
product: rm
source: tdn-rm
title: Portal da Farmácia
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553892752
version: 32
---

**ÍNDICE**

1. **Visão Geral**
2. **Painel da Farmácia**
3. **Cadastro dos Níveis de Urgência do Painel da****Farmácia**

portaldafarmaciavisaogeralVisão Geral

## **01. VISÃO GERAL**

O **Portal da Farmácia** é uma ferramenta destinada à visualização e gestão das requisições de medicamentos solicitados através do **Prontuário Eletrônico**. Também permite realizar a movimentação de estoque de forma eficiente. Através desse painel, é possível:

* Visualizar as requisições de medicamentos dos turnos atual e seguinte;
* Escolher o local de estoque para visualizar as requisições;
* Configurar o intervalo de tempo para exibição das requisições utilizando o sistema **RM**.

  O sistema é responsivo e foi projetado para ser utilizado em todos os tamanhos de tela, facilitando o uso em dispositivos diversos como computadores, tablets e celulares.

portadafarmaciadescricaoPortal da Farmácia

## **02. PORTAL DA FARMÁCIA**

portaldafarmaciadeckportaldafarmaciaconfigConfigurações

## **02.1****CONFIGURAÇÕES**

### Pré Requisitos

1. [Biblioteca RM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004987152-RM-Frame-Como-instalar-a-Biblioteca-RM);
2. [IIS](https://tdn.totvs.com/pages/viewpage.action?pageId=329024890);
3. RM Gestão Hospitalar instalado e rodando;
4. Configurar o host com [banco de dados default](https://tdn.totvs.com/display/LRM/Configurando+DefaultDB) ou [Multi Alias](https://tdn.totvs.com/pages/viewpage.action?pageId=287079669).

### Passo a passo da instalação

* Na tela TOTVS RM Portal, selecione a opção de avançar

* Aparecerá uma tela de contrato de licença
* Ao ler os termos, marcar o checkbox ''aceito os termos de contrato de licença''
* Avançar

* Aparecerá a tela **pasta de destino**
* Selecionar o destino e avançar a tela
* Se o usuário preferir trocar, pode trocar.
* **OBS:** Recomendado não trocar o destino

* Ao aparecer a tela do tipo de instalação, marcar o checkbox **personalizada**e avançar para próxima tela

* Ao abrir a tela sobre a instalação personalizada é necessário selecionar os módulos desejados, no caso, Painel Farmácia
* Avançar

* Aparecerá a tela de confirmação de instalação do programa
* Selecionar **instalar**

* Na tela seguinte, insira o local (**server and port**) do RM host do CorporeNet para poder usa-lo
* Avança

* Aparecerá a tela do Database Connection-Alias
* Escolher uma das opções que deseja utilizar e completas os campos
* Ok

* A próxima tela é referente ao processo de instalação
* Ao aparecer a mensagem, selecione **sim**

* Abrir os IIS

 

* Conferir no servidor se as pastas estão corretas

* Abrir a pasta que criou

* Abrir o arquivo config.json

* Conferir se inclui a mesma informação que foi inserida em ''servidor''
* **OBS:** A porta 8051 é a porta padrão do RM para receber requisições HTTP. Para mais informações sobre a configurações de portas do Host [clique aqui.](https://tdn.totvs.com/display/LRM/Configurando+HttpPort+e+ApiPort)
* Adicionar um usuário e senha que é o usuário utilizado para fazer a consulta das requisições

Nesse momento está finalizada a instalação do Painel da Farmácia.

portaldafarmacialoginLogin

## **02.2** **LOGIN**

A tela de login é a porta de entrada para o **Painel da Farmácia**. Nela, os usuários devem informar suas credenciais para acessar o sistema. A tela contém os seguintes elementos:

* **Logotipo da TOTVS Saúde**: Identifica o sistema e sua integração com a solução de saúde da TOTVS.
* **Título "Painel da Farmácia"**: Apresenta o nome do sistema.
* **Mensagem "Boas-vindas"**: Recepção amigável ao usuário.
* **Campo de usuário**: Para inserção do nome de usuário registrado.
* **Campo de senha**: Para inserção da senha associada ao usuário.
* **Botão "Entrar"**: Envia as credenciais para validação e acesso ao painel.
* **Ícones auxiliares**:
  + Ao lado do campo de usuário, há um ícone de ajuda para suporte.
  + No campo de senha, um ícone para mostrar/ocultar o conteúdo digitado.

A interface foi projetada para ser limpa e intuitiva, oferecendo uma experiência simples e eficiente para os usuários.

portaldafarmaciapainelPainel dispensação

## **02.3** **PAINEL DISPENSAÇÃO**

A página de **Painel de Dispensação** exibe todas as requisições organizadas em cards, divididos em categorias como **Urgente**, **Alerta** e **Em tempo**. Cada card contém:

* **Nome do paciente**;
* **Número da requisição**;
* **Unidade de atendimento**;
* **Aprazamento mais urgente**;
* **Status** da requisição ("Em separação" ou "Aguardando separação").

* **Visão Mobile:**

#### Recursos adicionais:

* **Ícone de usuário** na barra superior:

  + Permite alterar o contexto do usuário.
  + Opção de sair do sistema.
* **Botão de filtro**:

  + Localizado no canto superior direito.
  + Permite filtrar as requisições por local de estoque e turno.

Ao abrir o painel com a visão por Turno, caso o turno termine no dia posterior, será exibido as requisições dentro deste turno.  
O mesmo acontece com os itens dentro da requisição, onde serão exibidos até os itens do outro dia caso estejam dentro do tempo do turno.

portaldafarmaciasepararSeparar Requisição

## **02.4** **SEPARAR REQUISIÇÃO**

A página de **Separar Requisição** apresenta as informações detalhadas da requisição, incluindo:

* **Nome do paciente**;
* **Número da requisição**;
* **Unidade de atendimento**;
* **Médico solicitante**;
* **Aprazamento** (tempo restante para atendimento);
* **Status da requisição** ("Aguardando separação" ou "Em separação").

Além disso, exibe a lista de materiais e medicamentos que precisam ser separados, com detalhes como:

* Nome do material/medicamento;
* Quantidade necessária;
* Data e hora do aprazamento.

Para iniciar a separação, clique no botão **Iniciar Separação**. O sistema acompanhará o progresso da separação dos itens listados.

#### Após Iniciar Separação

Quando a separação é iniciada, o status da requisição muda para **Em separação** e aparecem abas adicionais para filtrar os itens:

* **Pendentes**: Lista os itens que ainda precisam ser separados. Inclui os campos:

  + **Quantidade**: Permite informar a quantidade a ser separada.
  + **Código de barras**: Campo para informar o código do produto.
  + Botão com ícone **+**: Confirma manualmente o item separado.
* **Processados**: Mostra os itens que já foram separados.
* **Cancelados**: Exibe os itens que foram cancelados durante a separação.

#### Cancelar Itens

Caso deseje cancelar algum item:

1. Expanda o card do item na aba **Pendentes** clicando na seta correspondente.
2. Clique no botão **Cancelar item**.
3. O item será movido para a aba **Cancelados** e não será mais considerado no processo de separação.

   #### Processar Itens

   Ao clicar no botão **Processar**, todos os itens confirmados na aba **Pendentes** serão movidos para a aba **Processados**. Essa ação finaliza a separação dos itens e atualiza o status da requisição.
adicionaritemportalfarmaciaAdicionar Item

## **02.5** **ADICIONAR ITEM**

É possível adicionar item do tipo material à requisição. Para adicionar item, a requisição deve estar em separação pelo usuário, que deverá clicar sobre o botão "Adicionar Item". 

Ao clicar será exibido a pagina lateral conforme na imagem:

Haverá os campos Quantidade, Código de Barras, Botão para abrir o leitor de código de barras por câmera e uma barra de pesquisa para Materiais.  
Quantidade deve ser indicada uma maior que 0, que indica a quantidade do item a ser adicionado.  
O código de barras pode ser bipado utilizando-se um leitor ou a câmera do dispositivo e digitado manualmente.

Caso o produto tenha baixa estoque A Definir a tela para selecionar a baixa estoque será exibida:

Ao adicionar o item ele será confirmado na requisição:

Confirmar Materiais

## **02.6** **CONFIRMAR MATERIAIS**

É possível confirmar itens não controlados por lote sem a utilização de código de barras. Será necessário habilitar o parâmetro em Serviços Globais>Segurança>Perfis, selecione o perfil e **Acesso a Menus>Farmácia -> Painel da Farmácia -> Permite confirmar materiais não controlados por lote, via botão Confirmar**.

Só é possível confirmar materiais, não controlados por lote, via botão.

portaldafarmaciacadastrourgenciaCadastro dos Níveis de Urgência do Painel da Farmácia

## **03. CADASTRO DO NÍVEIS DE URGÊNCIA DO PAINEL DA FARMÁCIA**

portalfarmaciacadastrodeckportaldafarmaciacadastrodeckniveisCadastro dos Níveis de Urgência

Acesse o cadastro através de  **Cadastros > Cadastros de Estoques > Níveis de Urgência do Painel da Farmácia**

portaldafarmaciadeckurgenciaAdicionar Nova Faixa de Urgência

Clique em Incluir para adicionar uma nova faixa de de urgência para uma determinando de Local de estoque.

Cada Local de Estoque pode ter apenas conjunto de níveis associado, Nã possivel um mesmo Local de estoque ter duas faxias de Nível urgente por exemplo.IMPORTANTE!

portaldafarmaciadecklocalSelecione o Local de Estoque

1. Selecione o Local de Estoque
2. Indique qual o Nível de Urgência
3. Insira o Tempo Limite (minutos) em relação ao horário em que a medicação deverá ser entregue aquele paciente. Por exemplo se uma medicação deve ser aplicada as 14hs e o nível urgente for configurado para 60 minutos a parir das 13hs ( 60 minutos antes da medicação ter que ser entregue ) o Cartão do aprazamento esta sendo indicado como urgente.

Ao cadastrar mantenha os níveis de urgência e o tempo tempo limite, respeitando a mesma hirarquia. O mais urgente deve ter o menor tempo e o menos urgente o maior tempoIMPORTANTE!

É necessário que o dispositivo utilizado para a visualização do painel tenha acesso a um navegador de internet compatível com as tecnologias HTML 5 (HTML, CSS3 e JS).IMPORTANTE!
