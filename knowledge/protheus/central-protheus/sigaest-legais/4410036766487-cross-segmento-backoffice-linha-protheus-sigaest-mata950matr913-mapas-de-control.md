---
article_id: 4410036766487
category: SIGAEST - LEGAIS
content_hash: b8f3234db0ab6f101b80a80d5ca15386a1746b23b5910037aea18837031accde
fetched_at: '2026-06-28T22:38:51.724835+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA950/MATR913 -
  Mapas de Controle de Produtos Químicos - Conceito e Configurações Mínimas
type: support-article
updated_at: '2023-12-08T18:31:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410036766487-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA950-MATR913-Mapas-de-Controle-de-Produtos-Qu%C3%ADmicos-Conceito-e-Configura%C3%A7%C3%B5es-M%C3%ADnimas
---

**Dúvida**O que é o Mapa de Produtos Químicos e como configurar o Protheus para geração do Mapa?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Neste artigo explicaremos o que é o Mapa de Produtos Químicos e demonstraremos como configurar para que seja possível a geração do Mapa (via MATA950) e do Relatório dos Mapas (MATR913).

**O que é o Mapa de Controle de Produtos Químicos?**

Trata-se de uma *Instrução Normativa* que deve ser apresentada à **Polícia Federal** mensalmente, com o objetivo de mapear as movimentações de produtos químicos sujeitos à controle e fiscalização por possuírem o potencial de serem empregados, direta ou indiretamente , na produção de substâncias entorpecentes. Maiores detalhes sobre quais produtos estão sujeitos à fiscalização e demais informações poderão ser obtidos através da [Portaria nº 240, de 12 de Março de 2019](http://www.pf.gov.br/servicos-pf/produtos-quimicos/legislacao/portaria-240.pdf).

Conforme disposto na [Portaria nº 10, de 16 de Abril de 2019](http://www.pf.gov.br/servicos-pf/produtos-quimicos/legislacao/portaria10-dou.pdf), o **Siproquim 2**, o sistema da Polícia Federal pelo qual a empresa autorizada poderá declarar os mapas de controle, entrará em funcionamento no dia 01 de Setembro de 2019, mesma data em que a nova legislação entrará em vigor, conforme disposto na [Portaria nº 577, de 05 de Junho de 2019](http://www.pf.gov.br/servicos-pf/produtos-quimicos/legislacao/portaria577.pdf). Este sistema, da mesma forma que sua versão anterior, apresentará a possibilidade de declaração dos mapas de controle por meio da importação de um arquivo texto gerado por um sistema externo.

No *ERP Microsiga Protheus®,* este arquivo texto poderá ser gerado através da rotina de *Instruções Normativas* (**MATA950**), havendo também a opção da emissão de um relatório de conferência através do *Relatório de Produtos Químicos* (**MATR913)**. Este artigo descreverá todos os passos necessários para configuração do ambiente e os procedimentos cobertos pela rotina para geração do arquivo texto e do relatório de conferência.

**Mapas - Configurações mínimas de ambiente**

Para conseguir gerar o Mapa e consultar o Relatório, vamos descrever abaixo em passos o que será necessário:

1° - Para a execução da rotina *Instruções Normativas* (**MATA950**), mesmo no novo layout, será necessário possuir o arquivo **MAPAS.INI**na pasta **StartPath**(geralmente nomeada de *System*) de seu ambiente *Protheus.* **O arquivo estará em anexo ao final do artigo**.

2° - Certificar-se da existência do campo B5\_PRODPF (ou criá-lo) com as informações abaixo:

|  |  |
| --- | --- |
| **Campo** | B5\_PRODPF |
| **Tipo** | 1 - Caracter |
| **Tamanho** | 1 |
| **Contexto** | @! |
| **Propriedade** | 1 - Real |
| **Título** | 1 - Alterar |
| **Descrição** | Produto Controlado PF |
| **Help** | Indica se este produto é um Produto Químico Controlado para geração dos Mapas de Controle da Polícia Federal |
| **Lista de Opções** | S=Sim; N=Não |

**Observação**: O nome do campo apresentado aqui é apenas uma sugestão e poderá ser diferente conforme necessidade do cliente.

3° - Pesquise pelo parâmetro **MV\_PRODPF** (se necessário, crie-o como tipo 1 - Caracter)

* Preencha seu valor com o nome do campo criado anteriormente e clique em *Salvar*

*![CONFIGINIC7.gif](https://tdn.totvs.com/download/attachments/506790632/CONFIGINIC7.gif?version=1&modificationDate=1565637136060&api=v2)*

4° - Criação do campo para o código do Produto Químico conforme estabelecido pelo sistema *Siproquim 2* da Polícia Federal.

|  |  |
| --- | --- |
| **Campo** | B5\_CODMAPA |
| **Tipo** | 1 - Caracter |
| **Tamanho** | 11 |
| **Contexto** | @! |
| **Propriedade** | 1 - Real |
| **Título** | 1 - Alterar |
| **Título** | Cód.MAPAS |
| **Descrição** | Código do Produto Químico |
| **Help** | Código do Produto Químico conforme estabelecido pelo sistema Siproquim 2 da Polícia Federal |

5° -Pesquise pelo parâmetro **MV\_CODMAPA**(se necessário, crie-o como tipo *1 - Caracter*), e preencha seu valor **com o nome do campo criado anteriormente** e clique em *Salvar*

**Atenção**

*Para consultar os códigos dos produtos químicos estabelecidos pelo sistema **Siproquim 2** da Polícia Federal, consulte o arquivo disponível em <https://www.gov.br/pf/pt-br/assuntos/produtos-quimicos/arquivos-siproquim2/arquivo-txt>, no item "**Tabela de produtos**".*

6° - Criação do Grupo de Perguntas MAPASV2

* No *menu* do módulo **Configurador**, acesse: Base de Dados > Dicionário > Bases de Dados

![](https://tdn.totvs.com/download/attachments/506790632/configinic1.gif?version=1&modificationDate=1565637146460&api=v2)

* À esquerda, clique em *Perguntas*e em seguida clique em *Incluir*

*![](https://tdn.totvs.com/download/attachments/506790632/configinic8.gif?version=1&modificationDate=1565637135007&api=v2)*

* Nomeie o novo Grupo como **MAPASV2**e preencha a tabela de perguntas conforme abaixo:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Ordem** | **Pergunta** | **Tipo** | **Tamanho** | **Consulta Padrão** | **Formato** | **Help** |
| 1 | Do Grupo? | Caracter | 4 | SBM - Grupo de Produtos |  |  |
| 2 | Até o Grupo? | Caracter | 4 | SBM - Grupo de Produtos |  |  |
| 3 | Do Produto? | Caracter | 15 | SB1 - Produtos |  |  |
| 4 | Até Produto? | Caracter | 15 | SB1 - Produtos |  |  |
| 5 | Declarar Mapas: | Caracter | 8 |  | @E 99999999 | Mapas a serem declarados no SIPROQUIM 2 para montagem do cabeçalho EM. Exemplo: 10101100 Posição 1: Movimentações Nacionais Posição 2: Movimentações Internacionais Posição 3: Produção Posição 4: Transformação Posição 5: Consumo Posição 6: Fabricação Posição 7: Transporte Posição 8: Armazenagem |

**Observação**: O tamanho das perguntas 1 e 2 devem ser iguais ao tamanho do campo **BM\_GRUPO**da tabela de *Grupos de Produtos* (**SBM**), assim como o tamanho das perguntas 3 e 4 devem ser iguais ao tamanho do campo **B1\_COD** da tabela de *Produtos* (**SB1**).

7° - Criação do Grupo de Perguntas MTR913V2:

* No *menu* do módulo **Configurador**, acesse: Base de Dados > Dicionário > Bases de Dados

![](https://tdn.totvs.com/download/attachments/506790632/configinic1.gif?version=1&modificationDate=1565637146460&api=v2)

* À esquerda, clique em *Perguntas*e em seguida clique em *Incluir*

![](https://tdn.totvs.com/download/attachments/506790632/configinic8.gif?version=1&modificationDate=1565637135007&api=v2)

* Nomeie o novo Grupo como **MTR913V2**e preencha a tabela de perguntas como se segue:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Ordem** | **Pergunta** | **Tipo** | **Tamanho** | **Consulta Padrão** | **Formato** | **Help** |
| 1 | Da data? | Data | 8 |  |  |  |
| 2 | Até a data? | Data | 8 |  |  |  |
| 3 | Do Grupo? | Caracter | 4 | SBM - Grupo de Produtos |  |  |
| 4 | Até o Grupo? | Caracter | 4 | SBM - Grupo de Produtos |  |  |
| 5 | Do Produto? | Caracter | 15 | SB1 - Produtos |  |  |
| 6 | Até o Produto? | Caracter | 15 | SB1 - Produtos |  |  |
| 7 | Declarar Mapas: | Caracter | 8 |  | @E 99999999 | Mapas a serem declarados no SIPROQUIM 2 para montagem do cabeçalho EM. Exemplo: 10101100 Posição 1: Movimentações Nacionais Posição 2: Movimentações Internacionais Posição 3: Produção Posição 4: Transformação Posição 5: Consumo Posição 6: Fabricação Posição 7: Transporte Posição 8: Armazenagem |

**Observação**: O tamanho das perguntas 3 e 4 devem ser iguais ao tamanho do campo **BM\_GRUPO**da tabela de *Grupos de Produtos* (**SBM**), assim como o tamanho das perguntas 5 e 6 devem ser iguais ao tamanho do campo **B1\_COD** da tabela de *Produtos* (**SB1**).

* Clique em *Confirmar*para salvar as alterações.

**IMPORTANTE:** A partir de Outubro de 2023 foram criados mais perguntas no relatório MATR913. Veja no link abaixo as instruções e configurações necessárias para criação das perguntas:

<https://tdn.totvs.com/pages/releaseview.action?pageId=723813044> 

Saiba Mais:

[Clique aqui e veja mais artigos sobre LEGAIS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
