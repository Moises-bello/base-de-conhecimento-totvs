---
content_hash: 90cf6f117c080511e686fdd67c35b37301a25458c16b5cf2c17b306c9f2f0efe
fetched_at: '2026-06-29T00:11:03.641436+00:00'
page_id: '624757370'
product: rm
source: tdn-rm
title: Configuração Inicial - App Minha Obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=624757370
version: 7
---

1. **Tela inicial do Minha Obra (SplashScreen)**
   * A tela inicial do Minha Obra mostra o aplicativo e o propósito de sua utilização, isto é, Construção e Projetos com uma imagem em background e também as quatro principais funcionalidade no qual se propõe, isto é, Avanço Físico, Mão de Obra, Equipamento e Ciclo de Transporte.
2. **Tela de configuração inicial e sincronismo do Minha Obra**
   * No aplicativo existem duas formas de se configurar os parâmetros iniciais que permitem a sincronização com o TOTVS Construção Obras e Projetos.  
                                                                 
     + **Através da leitura de QRCode:** O QRCode com as informações de Coligada, Login, Senha e WebService pode ser gerado no TOTVS Construção Obras e Projetos na opção dos processos da visão de Usuários de Coletores Móveis.
     + **Através de configuração manual:** Os dados podem ser informados manualmente. O sincronismo pode ser executado utilizando a "Url Sicronismo" comunicando com o IIS ou pela "Url API" comunicando com o Host. A prioridade de utilização é a URL de Sincronismo entretanto esta URL não é obrigatória, sendo possível a utilização de somente a URL API.

1. * + Após a definição das informações de sincronismo, o mesmo é executado e as informações sincronizadas com o TOTVS Construção Obras e Projetos.

1. * + Caso ocorra algum erro no processo de sincronismo, será possível visualizar em qual etapa ocorreu e expandir o mesmo para mais detalhes.

1. * + É possível realizar a configuração do sincronismo para que seja realizado de forma automática. O Minha Obra possibilita que seja definido o intervalo de tempo em minutos do sincronismo e o tipo de rede que será executado: Wifi, Wifi e Celular (3g).

1. * O Minha Obra possibilita a utilização de uma versão de demonstração onde informações fictícias são inseridas no banco de dados do aplicativo. Com essa versão de demonstração não é possível realizar o sincronismo. Para ativá-la, basta limpar o conteúdo do campo WebService da tela de configuração manual e clicar no botão a seguir:
