---
content_hash: e7c6343f0efd615c9479e53c48faf35cb9f67a94e5d129c8ed749d9cf4513fff
fetched_at: '2026-06-29T00:06:15.453960+00:00'
page_id: '210055925'
product: rm
source: tdn-rm
title: ER_PCREQ-6019_Upgrade_Relatorio_Planilhas_de_Tarefa
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-6019_Upgrade_Relatorio_Planilhas_de_Tarefa
version: 61
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

#### 

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão de Obras e Projetos |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP008 | **IRM1** | PCREQ-6018 |
| **Requisito1** | PCREQ-6019 | **Subtarefa1** | PDR\_CP\_TOP008-110 |
| **Chamado2** | --- | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** | não |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## 

## Objetivo

Disponibilizar os relatórios das Planilhas de Tarefa na nova MDI.

Os relatórios de composição que serão migrados do Delphi para a nova na MDI, são os seguintes:

Relatórios Baseados no Gerador: 

* 01.001-Estrutura de Tarefas
* 01.002-Estrutura de Tarefas (Totalizado por etapa e por obra)
* 01.003-Estrutura de Tarefas (Por extenso)
* 01.004-Estrutura de Tarefas (cód. serv. sem cód. obra)
* 01.006-Planilha de Preços 7o Nível (bdi sobre o projeto)
* 01.007-Planilha de Preços 7o Nível (bdi sobre os serviços)
* 01.008-Planilha de Quantidades e Preços até 3º nível
* 01.009-Planilha de Quantidades e Preços até 7º nível

Para que seja possível a importação dos relatórios na nova MDI, os relatórios serão disponibilizados através de arquivos de importação, e poderão ser importados através do RMReports.

Através da tela abaixo, os arquivos de importação dos relatórios são selecionados e importados. 

Após importados, podem ser visualizados em**Relatórios >> Tarefas >> Planilha de Tarefas.**

#### Restrições

* Estes relatórios são padrão no sistema e por questão de segurança o usuário não poderá editar ou excluí-los,   
  porém será possível duplicá-lo criando cópias, e assim editar e customizar estas cópias, de acordo com a necessidade.

#### Filtros

* Por cenário e tipo de planilha.
* Tarefa inicial e final.
* Por Disciplina

#### 

#### Parâmetro

#### 

* Parâmetros de Projetos (F6) >> Cálculo >> Outros >> Considerar quantidade de obras

#### 

#### Localização do Relatório

Interna: RM/Documentos/Prj-Projetos/Relatórios/Relatorios Migrados

Clientes: Pasta "Objetos Gerenciais" localizada no diretório de instalação do Produto.

Importante

É recomendado calcular o projeto antes de gerar os relatórios.

Os valores dos totalizadores dos relatórios, por questões de arredondamento (uma vez que os relatórios não utilizam as casas decimas definidas nos parâmetros de projeto), podem apresentar valores aceitavelmente um pouco maiores ou menores.

### Protótipos dos Relatórios

Melhorias Realizadas

Foram realizadas as melhorias abaixo:

1 - Otimização de espaço entre as linhas, fazendo com que cada página suporte mais informação, reduzindo o número de folhas utilizadas

2 - Incluído no cabeçalho a identificação de Planilha

3 - Incluído no cabeçalho a identificação de Cenário

4 - Incluído a descrição completa do projeto

5 - Incluído o código da disciplina

6 - Relatório na nova MDI 01.006, 01.007 e 01.009 passaram a exibir **todos** os níveis de código das tarefas

**Protótipo 01 - Relatório **01.001 -**Estrutura de Tarefas**

| Delphi | Nova MDI |
| --- | --- |
|  |  |

**Protótipo 02 - Relatório **01.002 -**Estrutura de Tarefas (Totalizado por etapa e por obra)**

| Delphi | Nova MDI |
| --- | --- |
|  |  |

**Protótipo 03 - Relatório **01.003 -**Estrutura de Tarefas (Por extenso)**

| Delphi | Nova MDI |
| --- | --- |
|  |  |

**Protótipo 04 - Relatório **01.004 -**Estrutura de Tarefas (cód. serv. sem cód. obra)**

| Delphi | Nova MDI |
| --- | --- |
|  |  |

**Protótipo 05 - Relatório **01.006 - Planilha de Preços 7o Nível (bdi sobre o projeto)****

| Delphi | Nova MDI |
| --- | --- |
|  |  |

**Protótipo 06 - Relatório 01.007-Planilha de Preços 7o Nível (bdi sobre os serviços)**

| Delphi | Nova MDI |
| --- | --- |
|  |  |

**Protótipo 07 - Relatório 01.008-Planilha de Quantidades e Preços até 3º nível**

| Delphi | Nova MDI |
| --- | --- |
|  |  |

**Protótipo 08 - Relatório 01.009-Planilha de Quantidades e Preços até 7º nível**

| Delphi | Nova MDI |
| --- | --- |
|  |  |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
