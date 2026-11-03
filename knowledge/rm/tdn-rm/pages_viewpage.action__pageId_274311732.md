---
content_hash: 34330ba6074775f4aba180e55069e1697295c65f97a70a7364ab011674c485a8
fetched_at: '2026-06-29T00:08:33.291394+00:00'
page_id: '274311732'
product: rm
source: tdn-rm
title: Tradução do Sistema
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274311732
version: 11
---

# Índice:

---

.\*ndice:

Serviço Descontinuado

A partir da versão 12.1.2310 este serviço não estará mais disponível, dessa forma a tradução deverá ser realizada utilizando o instalador.

Mais informações,

# Objetivo:

---

       O objetivo deste documento é auxiliar o usuário na parametrização de Tradução de Idioma.

# Introdução:

---

        A tradução permite alterar o idioma dos Produtos RM. Podemos considerar como suas principais características os seguintes pontos:

* Traduz cadastros, processos eentre outras opções do sistema.
* Qualquer funcionalidade .Net pode ser traduzida.
* Vasta lista de idiomas para a tradução.
* Possibilita a gravação de pacotes de tradução.

# Configuração:

---

        Para ativar a tradução, precisamos executar algumas configurações. A seguir será apresentado exemplo de tradução para o idioma Inglês.

falseConfigurando MashupConfigurando Mashups

        O primeiro processo é configurar o Mashups. Para tal configuração, é necessário seguir os passos abaixo:

        Acessar o cadastro de coligadas e edite um registro. Selecione o menu "Processos | Mashups | Gerenciar".

        Caso ainda não possua conta no TOTVS Mashups, informe o servidor [mashups.totvs.com.br](http://mashups.totvs.com.br) e acesse o hiperlink "Criar conta do TOTVS Mashups" para preencher os dados cadastrais necessários para utilização da ferramenta. (para mais informações sobre Mashups, )

        Em seguida, realize o login no TOTVS Mashups.

        Realizado o login, selecione a adição de uma nova integração e pesquise pela palavra "Tradução". Em seguida, marque a opção retorna "Google - Tradução" e clique em selecionar.

        Salve a configuração e em seguida feche a janela do TOTVS Mashups.

Iniciando as parametrizações

        Para inciar as configurações de tradução, realize as seguintes etapas:

        Acesse o ícone "Traduzir" na barra de ferramentas do sistema, em seguida informe o idioma para tradução. Neste caso, selecionaremos a opção "English (United States)" :

        Carregada a tela de tradução de sistema, clique em "Selecionar...":

        Na seleção de sistemas, marque a opção "Serviços Globais" junto com as três ultimas "RM GLOBAIS, RM LIB e EXECUTÁVEIS" conforme exemplo abaixo:

        Depois, clique no botão "Filtrar" para que os registros referentes aos sistemas selecionados sejam carregados. Com a opção de check "Marcar/Desmarcar" habilitada, confirme a seleção dos objetos clicando em "OK":

        Aguarde até que todos os registros sejam carregados:

Executar Tradução

        Após carregada a visão, selecione os objetos que serão traduzidos clicando no [X] das caixas de seleção e inicie o processo de tradução.

        Observe que a barra de processo carregara a medida em que os componentes são traduzidos:

        Ao fim do processo será apresentada uma mensagem informando a conclusão da tradução:

        Salve as configurações e aguarde até as informações de tradução sejam concluídas:

        Após a conclusão, será apresentada a mensagem de que é necessário fechar o sistema. Clique em OK e feche o sistema

Configuração dos arquivos .Config

        Para finalizar as parametrizações, será necessário alterar algumas tags de configuração do sistema. Para isso, acesse o diretório de instalação do RM (padrão em **c:\totvs\CorporeRM\RM.Net**).

        Localize os arquivos RM.exe.config e RM.Host.Service.exe.config e edite-os.

        No procure pela tag LocalizationLanguage e altere o valor de "pt-BR" para "en-US" em ambos arquivos conforme o exemplo abaixo:

        Salva as configurações, ainda no diretório raiz do sistema, acesse o RM.Host.ServiceManager.exe e reinstale o serviço de host.

        Agora, acesse a nova MDI e observe que os textos de Serviços Globais foram traduzidos conforme as opções selecionadas no inicio do processo de tradução:

Informações adicionais

        É importante planejar quais menus serão traduzidos, pois o exemplo deste documento mostra os componentes de Globais.

        O processo para tradução deverá ser realizado uma única vez (em uma só máquina), porém para o ambiente ser traduzido (para cada máquina) deverá realizar somente a ultima etapa deste documento (Configuração dos arquivos .Config).

        Em ambiente N camadas este procedimento deverá ser realizado somente no servidor (não é necessário ser realizado em máquinas Client).

        Para DESFAZER a tradução, basta alterar novamente os arquivos .config pra "pt-BR".

        Tabelas de siglas de Language: <http://msdn.microsoft.com/en-us/library/ee825488%28v=cs.20%29.aspx>

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX e 12.01.XX

false

**Processo:** Tradução do Sistema

falsefalse

**Status:** Finalizado

false

**Data:** 11/05/2017

false

**Autores:**
