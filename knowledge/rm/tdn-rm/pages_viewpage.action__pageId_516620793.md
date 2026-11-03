---
content_hash: 2072e1d796171f40c715f3806a6e80147dfe5866b4bb12c914dacd22d041038b
fetched_at: '2026-06-29T00:10:27.141028+00:00'
page_id: '516620793'
product: rm
source: tdn-rm
title: Cadastro Procedimento Cirúrgico NHSN
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=516620793
version: 2
---

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela inicial**
   1. **Outras Ações / Ações relacionadas**
4. **Tabelas utilizadas**

sumarioVisão Geral

## **01. VISÃO GERAL**

Não é permitida a inclusão ou exclusão de procedimentos cirúrgicos. Estes são pré-definidos com base no **NHSN, que é Sistema para monitorar eventos associados a cuidados com a saúde. O NHSN é composto por metodologias e definições médicas baseadas em pesquisas e desenvolvimentos.**   
É possível alterar apenas suas taxas IRIC de referência, seu tempo de Cutoff e informar se o procedimento pode ser realizado via vídeo na instituição de acordo com sua capacidade.   
O Cutoff é o tempo máximo esperado de ferida aberta para o procedimento. Este número é informado em minutos e deve ser informado como 75% do tempo médio dos procedimentos realizados na instituição. A taxa IRIC (vídeo, 0, 1, 2 e 3) de referência é o percentual de infecções esperadas com base no risco cirúrgico. O IRIC vídeo é usado para quando o procedimento é realizado por vídeo. Esta referência é utilizada como base para geração do comparativo de cirurgião da taxa de componente cirúrgico.

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

|  |  |
| --- | --- |
| Menu/Caminho: | Saúde/controle de infecção hospitalar/cadastros/procedimento cirúrgico |

## **03. TELA INICIAL**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Procedimento para inclusão | 1. Selecione um procedimento e clique em **Editar** (Ctrl + Enter). 2. Somente é possível editar os seguintes campos:  * + Cutoff: refere-se ao tempo de ferida aberta esperado (percentil 75%) publicado pela metodologia NHSN.   + Taxas NNISS NNISS (Sistema de Vigilância Nacional para Infecção Hospitalar).   + IRIC IRIC (Índice de Risco de Infecção Cirúrgica) - é construído a partir do somatório da pontuação das três variáveis de importância quanto à ocorrência de supuração no sítio cirúrgico: potencial de contaminação da ferida, tempo de ferida aberta (pré-operatório) e risco anestésico do paciente (ASA). M / 0-Vídeo: diferentes taxas de infecção de sítio cirúrgico esperadas.   + IRIC 0 (%): Baixo índice de infecção.   + IRIC 1 (%): Baixo para médio índice de infecção.   + IRIC 2 (%): Médio para Alto índice de infecção.   + IRIC 3 (%): Alto índice de infecção.        4. O campo **Tabela**, selecione-a indica o código da tabela de cirurgias do HIS do hospital, muitos HIS/SGH's têm várias tabelas de procedimentos cirúrgicos (Unimed, SUS, CIEFAS, TISS, etc) e cada tabela tem um código.       5. Ao selecionar a tabela, será exibido no campo **Procedimento Correspondente** às tabelas cadastradas.       6. Clique em **OK**. |

## **04. TABELAS UTILIZADAS**

* Tela de alteração do cadastro de procedimento cirúrgico
