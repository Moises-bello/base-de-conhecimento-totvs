---
content_hash: 8031a33dd460e37bbd3758cbe65fd5d0a2d6d63d5f75ba58f31bd7d99194444c
fetched_at: '2026-06-29T00:08:28.050469+00:00'
page_id: '271655739'
product: rm
source: tdn-rm
title: ER_CPTOP002_Melhorias_Novo_TOP_Mobile
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_CPTOP002_Melhorias_Novo_TOP_Mobile
version: 17
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | TOP Mobile |
| **Segmento Executor** | Construção & Projetos | | |
| **Projeto1** | CPTOP002 | **IRM/EPIC1** |  |
| **Requisito/Story/Issue1** |  | **Subtarefa1** |  |
| **Chamado/Ticket2** |  | | |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Apresentar as melhoria desenvolvidas no TOTVS Obras e Projetos que contemplam as funcionalidades do TOP Mobile.

## Definição da Regra de Negócio

Algumas melhorias e novidades estão disponíveis no TOTVS Obras e Projetos que envolvem as funcionalidades do TOP Mobile. A seguir o detalhamento de cada uma delas.

**1) Parâmetros de imagem no sincronismo do coletor**

* Dois novos parâmetros permitem que imagens sejam trafegadas durante o sincronismo de informações entre TOTVS Obras e Projetos e Coletor Móvel (Protótipo 01):
  + **Permite enviar imagens para o coletor (Coligada e Usuários)**: Com esse parâmetro marcado as imagens presentes no cadastro da Coligada (Protótipo 02) e na pessoa que está associada diretamente ao usuário do coletor (Protótipo 03) serão enviadas para o mesmo ao sincronizar as informações e consequentemente serão exibidas no coletor (Protótipo 04);
  + **Permite registrar fotos em apontamentos no coletor**: Com esse parâmetro marcado será permitido o registro de fotos no apontamento de avanço físico (Protótipo 05) e consequentemente o envio para o TOTVS Obras e Projetos durante o sincronismo. São permitidas 6 fotos para cada apontamento .

**2) Imagens no apontamento de avanço físico**

* Após registar fotos no apontamento do avanço físico e realizar o sincronismo das informações, é possível visualizar as imagens no cadastro de folha tarefa no anexo "Edição de Apontamentos".

**3) Mapas de apontamentos**

* Durante o registro do apontamento no coletor, informações de localização (coordenadas GPS) serão coletadas e enviadas no sincronismo para o banco de dados do sistema.
* Com isso, será possível visualizar as posições dos apontamentos no sistema.
* Para habilitar a visualização de mapas é necessário configurar a chave de acesso ao Google Maps:

+ Menu: Ambiente -> Parâmetros -> Parâmetros Gerais -> Aba Google -> Chave de identificação para Google Maps
+ Como configurar a chave de acesso: <http://tdn.totvs.com/pages/viewpage.action?pageId=42043762>

* + Observação: É necessário configurar apenas a chave de acesso, não existe a necessidade de configurar o portal com IIS (Internet Information Services).

* Foi criado uma nova tela de visualização de mapas de apontamentos de equipamentos:

+ Menu: Controle -> Mobilidade -> Equipamentos -> Mapa de Apontamentos de Equipamento

* Foi criado uma permissão de acesso para a tela de mapas de equipamentos:

* Observação:

+ O aplicativo TOP Mobile deverá coletar as coordernadas GPS em intervalos de 1 minuto.
+ A precisão das coordenadas GPS será de 50 metros e deverá funcionar em ambientes abertos.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Edição da Folha Tarefa | Modificado | Controle -> Mobilidade -> Folhas Tarefa -> Aba Mapa (Filtrar apontamentos de avanço físico) | Foi criado uma aba de mapa para visualização de apontamentos de avanço físico e de mão de obra. |
| Edição de apontamento da tarefa | Modificado | Controle -> Mobilidade -> Folhas Tarefa -> Anexos -> Edição de apontamentos | Foi criado uma aba de mapa para visualização do apontamentos. |
| Edição do Ciclo de Transporte | Modificado | Controle -> Mobilidade -> Ciclo de Transporte | Foi criado uma aba de mapa para visualização do apontamentos. |
| Edição do apontamento de ciclo de transporte | Modificado | Controle -> Mobilidade -> Ciclo de Transporte -> Anexos -> Apontamentos dos Coletores | Foi criado uma aba de mapa para visualização do apontamentos. |
| Edição da equipe de mobilidade | Modificado | Controle -> Mobilidade -> Equipe de Mobilidade | Foi criado uma aba de mapa para visualização do apontamentos. |
| Tela de visualização de mapa dos apontamentos de equipamento | Criado | Controle -> Mobilidade -> Equipamentos -> Mapa de Apontamentos de Equipamentos | Mapa para visualização do apontamentos com um filtro por equipamento. |
| Edição do apontamento de equipamento | Modificado | Controle -> Mobilidade -> Equipamentos -> Apontamentos de Equipamentos | Foi criado uma aba de mapa para visualização do apontamentos. |
| Permissão de segurança para tela de mapa de equipamentos | Criado | Controle -> Mobilidade -> Equipamentos -> Mapa de Apontamentos de Equipamentos | Permissão de segurança para tela de mapa de equipamentos. |

**4) Processo QR Code para Configuração Automática do Sincronismo no TOP Mobile**

Este processo tem o objetivo de configurar de forma automática no sincronismo do TOP Mobile, as informações iniciais necessárias para seu funcionamento.

O processo tem duas etapas, e está disponível nos processos de Usuários de Coletores Móveis, na aba Controle>>Mobilidade>>Usuários de Coletores Móveis.

Na primeira etapa do processo, é gerado o QR Code para configuração automática do sincronismo do TOP Mobile.

Obs.: o botão **Copiar para área de transferência** irá disponibilizar uma cópia da imagem do QR Code na área de transferência.

Na segunda etapa, o QR Code será enviado como e-mail para os usuários de coletores móveis.  
O texto que aparece como padrão no campo Corpo do e-mail, poderá ser editado e a   
seleção dos usuários que receberão o e-mail também poderá ser alterada antes da execução do processo.

* Permissão de acesso do processo:
