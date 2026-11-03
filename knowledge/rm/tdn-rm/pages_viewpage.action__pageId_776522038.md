---
content_hash: 0bb298d0319f94cbb52a79b7e4c37eac84a0e4f26199c72306631ba5191919d5
fetched_at: '2026-06-29T00:11:37.348398+00:00'
page_id: '776522038'
product: rm
source: tdn-rm
title: Painel de Documentos Eletrônicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=776522038
version: 49
---

# Conteúdo

# 1(Conteúdo)|(CONFIGURAÇÃO PARA ACESSO ÀS API's)|(Vídeo How To - Demonstração)nonenone

# 1. Visão Geral

O painel de documentos fiscais tem como objetivo trazer uma visão detalhada, através de dashboards, dos documentos fiscais eletrônicos, permitindo que o usuário filtre os documentos por tipo, filial, coligada e período. O painel apresenta as informações necessárias para uma rápida consulta de dados.

É importante salientar que o RM só terá acesso as API's do Painel de Documentos Eletrônicos após algumas configurações nos arquivos do Host:

Pré-requisitos técnicos 

**Permissões de Acesso**A funcionalidade "Painel de Documentos Eletrônicos" conta com controle de segurança, sem ele o usuário não conseguirá visualizar as informações do Painel.

Para acessar o Painel o usuário precisa das seguintes permissões:

No módulo de Gestão de Estoque:

* 01.03.01 Filial
* 04.02.01.01 Nota Fiscal Eletrônica

No módulo de Globais:

* 01.01.01 Coligadas

  
  

# 2. Vídeos de demonstração

# 

# 3. Exemplo de Utilização

O painel de Documentos Eletrônicos é acessado através do modulo "Gestão de Estoque Compras e Faturamento" > Utilitários > Painel de Documentos Eletrônicos.Menu Painel de Documentos Eletrônicos

# 

# 4. Filtros do Painel

| Ação | Descrição |
| --- | --- |
| 1 - Tipo de Documento | O campo permite que o usuário filtre as informações que serão apresentadas no dashboard pelos tipos de Documentos Fiscais Eletrônicos, sendo este um campo de seleção única. |
| 2 - Coligada | O campo permite que o usuário filtre as informações que serão apresentadas no dashboard pelas coligadas, sendo este um campo de multiseleção. |
| 3 - Filial | O campo permite que o usuário filtre as informações que serão apresentadas no dashboard pelas filiais, sendo este um campo de multiseleção. |
| 4 - Estado | O campo permite que o usuário filtre as informações que serão apresentadas no dashboard pelos Estados, sendo este um campo de multiseleção. |
| 5 - Período | O campo permite que o usuário filtre as informações que serão apresentadas no dashboard dentro de um período, sendo este um campo de intervalo de datas. |

### **Detalhes**

Filtros

# 

# 5. Componente do Gráfico

| Ação | Descrição |
| --- | --- |
| 1 - Total de Documentos | O campo traz a visualização a soma total dos documentos fiscais eletrônicos demonstrados no gráfico; |
| 2 - Valor Total | O campo traz a visualização a soma do valor total dos documentos fiscais eletrônicos demonstrados no gráfico; |
| 3 - Qtd. e Valor de cada status | O campo traz a visualização específica de cada status do gráfico, sendo possível visualiza-los ao passar o mouse em uma cor específica; |
| 4 - Legenda com as cores e os status | O espaço traz a visualização de cada status com cada cor que o representa no gráfico. |

Gráficos

# 

# 6. Widgets - Visualização por status de documento

Será apresentado na tela um widget para cada status de documento retornado.

| Ação | Descrição |
| --- | --- |
| 1 - Título do Status | O componente trará a descrição de um dos status de documento retornados, de acordo com o filtro aplicado.Sua cor será a mesma apresentada no gráfico. |
| 2 - Quantidade | Somatório da quantidade de documentos com o referido status que foi retornada pelo filtro especificado. |
| 3 - Valor | Somatório do valor dos documentos com o referido status que foi retornado pelo filtro especificado. |

Visualização por status de documento

# 

# 7. Listagem de Status por Coligada

| Ação | Descrição |
| --- | --- |
| 1 - Nome e CNPJ da coligada | O componente trará o nome da coligada, seguido pelo CNPJ logo abaixo. |
| 2 - Quantidades por status | Quantidade específica de cada status de documento daquela coligada, separado pelas mesmas coresdo widget. |
| 3 - Quantidade e Valor Total | Quantidade e Valor total dos status da respectiva coligada. |

Listagem de Status por Coligada

# 

# 8. Listagem de Status por Filial

| Ação | Descrição |
| --- | --- |
| 1 - Colunas da Tabela | O componente trará o Código da filial, o Nome da filial e os status que possuem alguma nota; |
| 2 - Itens da Tabela | O componente trará os dados especificados de cada filial da coligada correspondente; São tragos para a tabela somente 10 itens por vez; |
| 3 - Gerenciador de Colunas | O componente permite com que o usuário configure a disposição de colunas da tabela; |
| 4 - Barra de Pesquisa | Uma barra de texto que permite com que o usuário busque um item específico pelo código ou nome da filial; |
| 5 - Botão para carregar mais itens | O componente faz com que seja carregado mais 10 itens para tela, e estará habilitado para acionamento até que não haja itens a serem carregados. |

Listagem de Status por Filial

#
