---
content_hash: 92606b5f1d4ac041c334143f6e6a84f0443e5eaca3a9283e4116017f9ef996dd
fetched_at: '2026-06-29T00:08:32.465650+00:00'
page_id: '273986882'
product: rm
source: tdn-rm
title: DT_PUBLICACAO_DO_EDITAL_WF
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_PUBLICACAO_DO_EDITAL_WF
version: 6
---

# Publicação do Edital

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Educacional* |
| **Módulo:** | *Inovação, Pesquisa e Extensão* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Publicação do edital.* | *Publicação do edital* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Edital** | *Edital* | | *Envio de e-mail* | *Envio de e-mail* | | *Mensagens de Notificação* | *Mensagens de Notificação* | |
| **Cadastros Iniciais:** | *Edital*  *Pesquisador/Extensionista*  *Mensagens de Notificação* |
| **Parâmetro(s):** | *N/A* |
| **Requisito (ISSUE):** | *PCREQ-5446* |
| **País(es):** | *Brasil* |
| **Tabelas utilizadas:** | *SPROJEDITAL* |
| **Versões/Release:** | *12.1.15* |

## Descrição

A publicação do edital de pesquisa ou do edital de extensão pode acontecer tanto pelo TOTVS Educacional quanto pelo FLUIG. O edital só estará disponível para publicação se estiver devidamente cadastrado no TOTVS Educacional e marcado como "Edital liberado".

Somente pessoas associadas ao papel de "Aprovador de Edital" poderão realizar a publicação do edital.

Ao publicar o edital, será enviado um e-mail para todos os pesquisadores cadastrados, que estejam ativos, informando dessa publicação. É importante que o pesquisador tenha um e-mail válido cadastrado no TOTVS Educacional.

Pré-requisitos para utilizar a funcionalidade de publicação do edital

* Ter o FLUIG devidamente instalado e configurado conforme documentação:
  + Instalação: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409653>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409655>
* Ter o TOTVS Developer Studio (TDS) devidamente instalado e configurado.
  + Instalação: <http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7C+Developer+Studio>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=73078179>
* Criar no FLUIG os papéis necessários para a execução do fluxo de publicação do edital. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis).
  + Código = **aprov\_edital**| Descrição = **Aprovador de Edital**
* Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.
* Verificar se todos os pesquisadores cadastrados no TOTVS Educacional possuem endereço de e-mail válido.
* Configurar corretamente o TOTVS Educacional para permitir o envio de e-mail através dos parâmetros globais do sistema.
  + Configuração: <http://tdn.totvs.com/display/public/rm/Envio+de+email+-+LINHA+RM>
* Importar o fluxo de publicação de edital para a ferramenta TOTVS Developer Studio (TDS). Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em **c:\totvs\CorporeRM\ObjetosGerenciais\Fluig**
  + Configuração: [http://tdn.totvs.com/download/attachments/172300565/RM\_BT\_Montagem\_Ambiente\_Workflows\_Fluig.pdf](http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf?version=1&modificationDate=1432910252000&api=v2)
* Importar os projetos: ***\_InovacaoPesquisaExtensaoBase***e***PublicacaoDeEdital***
* Exportar para o servidor do FLUIG os datasets, diagrama, formulário e eventos do projeto de publicação de edital.  
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=189313846>
* Exportar para o servidor do FLUIG os datasets do projeto base: ***\_InovacaoPesquisaExtensaoBase***
  + **Datasets**
    - *rm\_edu\_consulta\_edital*
    - *rm\_edu\_fontedados\_usuariorm*

## Procedimento para Configuração

Para que os editais estejam disponíveis para publicação é necessário que já se encontrem cadastrados e liberados no TOTVS Educacional através da opção de menu "Atividades Acadêmicas | Pesquisa/Extensão | Edital".

**CONFIGURAÇÃO DE NOTIFICAÇÕES**

Para permitir que os pesquisadores recebam e-mail após a publicação do edital, é necessário cadastrar mensagem de notificação a ser utilizada (TOTVS Educacional | Atividades acadêmicas | Central de Notificações | Mensagem de notificação), conforme descrito abaixo: 

1. Objetivo da mensagem "**Enviar notificação aos pesquisadores sobre a divulgação do edital (pesquisa)**" para notificar pesquisadores/extensionistas de edital de "pesquisa" publicado e liberado para submeter propostas de projetos.
2. Objetivo da mensagem "**Enviar notificação aos pesquisadores sobre a divulgação do edital (extensão)**" para notificar pesquisadores/extensionistas de edital de "extensão" publicado e liberado para submeter propostas de projetos.

Publicando o edital

Após realizar a exportação do fluxo de publicação do edital para o servidor do FLUIG o usuário deve iniciar uma nova solicitação escolhendo a opção "Educacional | Inovação, Pesquisa e Extensão | Publicação de Edital | Publicação de Edital".

Será apresentado um formulário onde o usuário deverá selecionar o edital e indicar se o mesmo será "Publicado" ou "Não publicado".

Ao salvar/enviar, caso a indicação seja para "Publicado", um e-mail será enviado (conforme cadastro de mensagem de notificação) para todos os pesquisadores cadastrados, que estejam ativos, informando dessa publicação. Será realizada alteração no edital cadastrado no TOTVS Educacional para marcá-lo como publicado e informações como o número do processo do FLUIG e usuário que fez a publicação também serão gravadas.

Caso a indicação seja para "Não publicado", o usuário deverá informar uma justificativa na aba "Observações" e nenhuma alteração será realizada no edital cadastrado no TOTVS Educacional.

Após essas etapas o fluxo é encerrado.
