---
content_hash: 80a6a83c2ed509e635dcfa7edeea0cb48bcf4b4d17e29bf02ca2919ab63be18e
fetched_at: '2026-06-29T00:12:13.470506+00:00'
page_id: '960006098'
product: rm
source: tdn-rm
title: Higienização de Leitos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=960006098
version: 31
---

## **Índice**

1. **Visão Geral**
2. **Portal Higienização**
   1. **Configuração**
      1. **Parametrização**
      2. **Permissões**
   2. **Login**
   3. **Tela Principal**
   4. **Filtros**
   5. **Processos**
   6. **Leito (card)**

false11Visão Geral

# **01.** **Visão Geral**

**Kanban de Higienização de leitos** é uma ferramenta destinada à gestão e controle do processo de higienização de leitos após a alta do paciente ou manutenção. Também permite sinalizar que o leito necessita de manutenação. Através desse painel, é possível:

* Adicionar o responsável pela higienização de cada leito;
* Definir o fluxo e controle no processo de higienização;
* Saber o tempo que o leito ficou em cada status da higienização do mesmo.

  O sistema é responsivo e foi projetado para ser utilizado em todos os tamanhos de tela, facilitando o uso em dispositivos diversos como computadores, tablets e celulares.

Importante

Disponível a partir da versão 12.1.2510

É necessário que o dispositivo utilizado para a visualização do painel tenha acesso a um navegador de internet compatível com as tecnologias HTML 5 (HTML, CSS3 e JS).

# 

2Higienização de Leitos

# **02.** **Higienização de Leitos**

22.1Configuração

## **02.A CONFIGURAÇÃO**

### Pré Requisitos

1. [Biblioteca RM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004987152-RM-Frame-Como-instalar-a-Biblioteca-RM);
2. [IIS](https://tdn.totvs.com/pages/viewpage.action?pageId=329024890);
3. RM Gestão Hospitalar instalado e rodando;

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

* Ao abrir a tela sobre a instalação personalizada é necessário selecionar os módulos desejados, no caso, Higienização de leitos
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

* Abrir o arquivo config.json

* Conferir se inclui a mesma informação que foi inserida em ''servidor''
* **OBS:** A porta 8051 é a porta padrão do RM para receber requisições HTTP. Para mais informações sobre a configurações de portas do Host [clique aqui.](https://tdn.totvs.com/display/LRM/Configurando+HttpPort+e+ApiPort)
* Caso tenha mais de uma coligada deve se realizar configuração contida nessa sessão por coligada.

bash

Nesse momento está finalizada a instalação do Kanban de higienização

falseconfiguracao2.3Parametrização

## **02.A.i****PARAMETRIZAÇÃO**

## **Gestão de Leitos**

Configuração dos [parâmetros gerais](https://tdn.totvs.com/pages/releaseview.action?pageId=829293510#Painel-1906526480):

* 11.04 Registro de controle > Gestão de Leitos

**Utilizar Etapa "Em Deslocamento" no Kanban de Higienização:** Ativa uma coluna no Kanban para indicar que a equipe de higienização está a caminho do leito. Facilita o acompanhamento em tempo real e melhora a previsão de liberação do leito.

**Utilizar status "Aguardando Supervisão" na Gestão de Leitos:** Habilita uma etapa no Kanban que mostra quando o leito já foi higienizado, mas ainda aguarda validação da supervisão. Garante controle de qualidade antes da liberação final.

Atenção

Antes de desativar o parâmetro, é necessário atualizar os leitos que estão com o status 'Aguardando Supervisão'

## **Perfis profissionais**

Configuração dos [parâmetros gerais](https://tdn.totvs.com/pages/releaseview.action?pageId=829293510#Painel-1906526480):

* 11.09 Perfis Profissionais > Perfis Profissionais 2/2

**Perfil de Supervisor de Higienização:**Define qual será o perfil para os Supervisores de higienização.

**Perfil de Higienizador:**Define qual será o perfil de Higienizadores.

PermissõesPermissões

## **02.A.ii****PERMISSÕES**

Serviços Globais > Segurança > Perfis > Acesso a Menus

**Visualizar Leitos:** Permite ao perfil visualizar os leitos no kanban (obrigatório caso queira realizar qualquer uma das outras ações do kanban)

**Movimentar Leito:** Permite ao perfil movimentar leitos no kanban (avançar ou voltar)

**Aprovar leitos aguardando supervisão:** Permite ao perfil aprovar leitos que foram higienizados e passados para a coluna aguardando Supervisão. Utilizado somente se existir a coluna de Aguardando supervisão no kanban (o parâmetro "Utilizar status "Aguardando Supervisão" na Gestão de Leitos" deve estar marcado para que a coluna apareça). Recomendado permitir apenas para o perfil de Supervisor de Higienização.

**Enviar leito para manutenção:**Permite ao perfil enviar leitos para manutenção.

2.2Login

## **02.B****LOGIN**

A tela de login é a porta de entrada para o **Higienização de Leitos**. Nela, os usuários devem informar suas credenciais para acessar o sistema. A tela contém os seguintes elementos:

* **Logotipo da TOTVS Saúde**: Identifica o sistema e sua integração com a solução de saúde da TOTVS.
* **Título "Higienização de Leitos"**: Apresenta o nome do sistema.
* **Mensagem "Boas-vindas"**: Recepção amigável ao usuário.
* **Campo de usuário**: Para inserção do nome de usuário registrado.
* **Campo de senha**: Para inserção da senha associada ao usuário.
* **Campo de Alias:** Para selecionar o banco de dados que será destinado o acesso.
* **Botão "Entrar"**: Envia as credenciais para validação e acesso ao painel.
* **Ícones auxiliares**:
  + Ao lado do campo de usuário, há um ícone de ajuda para suporte.
  + No campo de senha, um ícone para mostrar/ocultar o conteúdo digitado.

A interface foi projetada para ser limpa e intuitiva, oferecendo uma experiência simples e eficiente para os usuários.

2.4Tela Principal

## **02.C****TELA PRINCIPAL**

**Após Login a seguinte tela será exibida:**

FiltrosFiltros

## **02.D****FILTROS**

**Meus** → Para exibição dos leitos onde somente o usuário seja responsável e os leitos que estão Aguardando Higienização.

**Todos os Leitos** → Pra exibição de todos os leitos. Um filtro **por Higienizador** ficará habilitado, onde o usuário pode selecionar higienizadores para que apenas o Leitos associados a eles apareçam no kanban.

**Busque por Leito** → Permite filtrar pelo número do leito.

**Filtre por Unidade**→ Permite filtrar por unidade de atendimento onde se encontra os leitos.

2.5Processos

## **02.E** **PROCESSOS**

Após clicar em processos será exibida as seguintes opções:

## **Leitura de QR Code:**

Com a leitura do QR Code é possivel avançar o status de leitos ao scannear o QR Code presente no leito.

As mesmas validações presentes no botão Avançar de cada leito (card) serão aplicadas após o escaneamento.   
Caso não tenha permissão:

Caso o leito não seja encontrado no kanban, seja por causa de dados invalidos ou por estar em um status diferente dos presentes no processo de higienização, a seguinte mensagem de erro será mostrada

**Geração do QR Code:**

O QR Code deve conter as seguintes informações em formato JSON:

| {         "companyId": 1,        "bedCode": 1  } |
| --- |

Sendo companyId o número da Coligada e bedCode o Id do Leito.

É importante ressaltar que valores presentes no JSON devem estar formatados corretamente, string entre aspas e números sem aspas. Caso contrário o QRCode não será reconhecido, apresentará alerta de erro e mostrará seu conteúdo no scanner.

Leitos movimentados apresentarão mensagem de sucesso:

## **Processo para encaminhar o leito para manutenção:**

Selecione "encaminhar p/manutenção" o seguinte modal será aberto:

É possível expandir o campo leitos e olhar todos os leitos disponíveis.

Selecione o leito, informe o motivo e clique no botão encaminhar e conclua o processo.

O leito encaminhado para manutenção é retirado do Kanban de Higienização de Leitos.

2.6Card

## **02.F LEITO (CARD)**

Cada card de leito irá conter as seguintes informações:

* Número do Leito → Número do leito presente no card.
* Localização → localização do leito presente.
* Sexo → Sexo permitido no leito.
* Responsável → Responsável pelo leito (atribuído ao usuário que avançar o leito) o mesmo estará vazio caso não tenha responsável
* Etapa → Tempo do Leito na etapa da coluna informada (inicia em 00:00 ao ser movido para etapa)
* Total → Tempo total do leito presente no Kanban de Higienização de Leitos

O leito ficará desabilitado caso o usuário não tenha permissões ou o leito tenha como responsável um usuário diferente.

Segue exemplo de um leito desabilitado e um habilitado:

Leitos sem responsável atribuido sempre estarão habilitados caso o usuário tenha permissão para Movimentar Leitos.

Os leitos na coluna de Aguardando Supervisão somente estarão habilitados para usuários que possuam permissão para aprovar leitos.

## **Voltar:**

Volta o leito para o status anterior.

## **Avançar:**

Avança o leito para o proximo status do kanban.

**Obs:** Caso esteja Em Higienização, ao clicar em Avançar será questionado se deseja confirmar a ação, pois isso implicará na **Conclusão** da higienização.

Caso exista a coluna de Aguardando Supervisão, o leito ficará disponível para o supervisor aprovar (avançar) ou rejeitar (voltar).   
Caso rejeite o leito irá voltar para o status de Aguardando Higienização, interrompendo o processo do higienizador atual e deixando-o sem higienizador associado.

## **Enviar leito para manutenção:**

No leito desejado, clicar no item, o Modal será aberto da seguinte forma:

O Leito selecionado virá preenchido sem a possibilidade de alterar, preencha o motivo e clique em encaminhar
