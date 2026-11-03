---
content_hash: 60f64e75eac0aedd585aef23c294aaa21746daa29680942a2e4f1bd53e033116
fetched_at: '2026-06-29T00:11:40.480977+00:00'
page_id: '795084009'
product: rm
source: tdn-rm
title: Relatórios Fiscais (Smart View)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=795084009
version: 45
---

#FFA500#FFFACD#FFE766dashedAviso Importante:1%99%

Com o objetivo de proporcionar uma melhor experiência e alinhamento às atualizações mais recentes dos nossos produtos, informamos que os **Relatórios Fiscais****,** já disponível no Módulo Gestão Fiscal, não será mais suportado no produto **RM Liber.exe** a partir da **versão 12.1.2602**

Reforçamos que essa alteração faz parte do nosso processo de evolução tecnológica, com a descontinuidade gradual de funcionalidades no **RM** **Liber.exe**. Para garantir a continuidade do uso e acesso do Relatórios Fiscais, recomendamos que a geração seja feita diretamente no **Módulo Gestão Fiscal**.

## Conteúdo

Conteúdonone

# 1. Visão geral

Com a evolução do **SPED (Sistema Público de Escrituração Digital)**, as obrigações legais de entrega de relatórios fiscais ao governo foram substituídas, e esses relatórios agora servem como ferramenta para apoio à gestão e análise. No sistema, os relatórios fiscais podem ser gerados e visualizados através do , importados diretamente do [TOTVS Compartilhamento](https://tdn.totvs.com/pages/viewpage.action?pageId=348297816), ou criados pelos próprios usuários, conforme as necessidades da empresa. O menu de **Relatórios Fiscais (Smart View)** no Módulo Gestão Fiscal permite a visualização e gestão desses relatórios.

# 2. Relatórios

RelatóriosSmart View

No menu de **Relatórios Fiscais (Smart View)**, você pode visualizar e gerar os relatórios Integrados ao Smart View que pertencem ao Módulo Gestão Fiscal.

* **Importar Relatórios**: Relatórios pré-configurados podem ser obtidos através do [TOTVS Compartilhamento](https://tdn.totvs.com/pages/viewpage.action?pageId=348297816), facilitando a integração e a gestão de dados fiscais já formatados.
* **Criar Relatórios**: O usuário também pode criar relatórios personalizados utilizando os recursos do , selecionando os dados relevantes para a sua empresa.

Os principais **Objetos de Negócio** disponíveis para a criação de relatórios são:

* [Objeto de Negócio - Lançamentos de Entrada/Saída e Lançamentos de Ajuste](https://tdn.totvs.com/pages/viewpage.action?pageId=786545512)
* [Objeto de Negócio - EFD-REINF (Bloco 40)](https://tdn.totvs.com/pages/releaseview.action?pageId=747314339)


* [Objeto de Negócio - EFD-REINF Informe Rendimentos](https://tdn.totvs.com/display/LRM/Informe+Rendimentos+EFD-REINF)
* [Objeto de Negócio - Lançamentos fiscais CBS/IBS (nível Item)](https://tdn.totvs.com/pages/viewpage.action?pageId=1060209425)
TOTVS Reports

Alguns relatórios específicos não estão disponíveis por este menu, mas ainda podem ser acessados por meio do TOTVS Reports

* [Relatório - Apuração FUNRURAL](https://tdn.totvs.com/pages/viewpage.action?pageId=663588506)
* [Relatório de Apuração do CIDE](https://tdn.totvs.com/pages/viewpage.action?pageId=668636985)

Não existe mais supoorte ao relatório Resumo de apuração do ICMS (Fisrel0006) no RM Reports. Sua funcionalidade foi migrada para o Smartview e  já se encontra disponível através do relatório FISTRP0003 - RESUMO DE APURACAO ICMS no TOTVS Compartilhamento.

# 3. Visualizar relatórios

Para visualizar um relatório dentro do sistema, siga os passos abaixo:

1. Acesse o menu **Relatórios Fiscais (Smart View)**. Este menu está localizado em *TOTVS Gestão Fiscal > Obrigações Principais > Relatórios Fiscais (Smart View)*.
2. Na tela a seguir, selecione o recurso desejado, vá em "**Mais Ações**" e selecione a opção "**Executar no Smart View**".
3. O relatório será exibido na tela conforme os dados e filtros selecionados.

visaoMenu Relatórios Fiscais (Smart View)anexoMais AçõesrelatorioExemplo de Relatório

# 4. Filtrando apenas recursos do TOTVS Gestão Fiscal

O Menu "Relatórios Fiscais (Smart View)" irá exibir os recursos do Smart View independente de qual módulo sejam, desde que o usuário logado possua acesso à visualização dos recursos no sistema. Caso seja necessário filtrar apenas os recursos do TOTVS Gestão Fiscal, siga os passos descritos a seguir:

* Na tela de relatórios do Smart View, clique na opção "Filtros". Esta opção apenas será exibida caso nenhum recurso esteja selecionado;
* Na tela de filtros que será aberta, será exibido o campo "Código da Aplicação". Clique no ícone de lupa ao lado deste campo;
* Informe o módulo TOTVS Gestão Fiscal (Código da Aplicação = 'D', Aplicação = 'RM Liber')

Clique para expandir a interação de filtros

# 5. Importando um recurso no Smart View

Siga o passo a passo abaixo para importar o recurso no Smart View:

VisaoDeDadosPasso 1

* Ao selecionar a opção "Relatório", a próxima tela que se apresentará é ilustrada abaixo.
* Neste ponto, procederemos clicando no botão indicado no vídeo e, em seguida, navegaremos até a função de importação do relatório.

Passo 2

* Ao acionar o botão de importação do relatório, seremos direcionados à pasta que contém o arquivo do recurso a ser importado no Smart View. É relevante notar que os arquivos de importação do Smart View possuem a extensão ".TReports".

Passo 3

* Após ter importado o arquivo, exploraremos as configurações iniciais do relatório. Nesse estágio, teremos a oportunidade de examinar os campos presentes no relatório, bem como o objeto de negócio associado.

E pronto! Quando visualizar seu recurso, basta preencher os parâmetros no intervalo desejado para selecionar os dados.

# 6. Permissões

Para que um usuário possa acessar o menu **Relatórios Fiscais**, é necessário que o perfil de usuário tenha as permissões adequadas configuradas no sistema.

**Nota**: Verifique com o administrador do sistema se o seu perfil de acesso permite a visualização, criação e execução de relatórios no **Smart View**.

Imagem

# 7. Criação de relatórios

criacaorelatorioRelatóriovisaoVisão de DadostabelaTabela Dinâmica

Maiores Informações

* [Configuração dos arquivos .config](http://tdn.totvs.com/display/LRM/RM.Host)
* [Ferramenta para a integração via WebService](http://tdn.totvs.com/display/public/LRM/WebService+RM)

Maiores Informações

Para utilização do SmartView é necessário ter as configurações dos arquivos .config conforme documentação abaixo e iniciar o host como administrador:

* [Configuração dos arquivos .config](http://tdn.totvs.com/display/LRM/RM.Host)
