---
content_hash: bb78cfdb76bfb15a53ddda0333c17b5baea51f0839fd1921136073bd913b6cdd
fetched_at: '2026-06-29T00:09:13.505490+00:00'
page_id: '421366344'
product: rm
source: tdn-rm
title: DT Unidade de Serviço e Local de Serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421366344
version: 10
---

# UNIDADE DE SERVIÇO E LOCAL DE SERVIÇO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | **Gestão de Obras e Projetos*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Unidade de Serviço* | *Unidade de Serviço* | | *Local de Serviço* | *Local de Serviço* | |
| **Cadastros Iniciais:** | Projeto |
| **Parâmetro(s):** | *Não se aplica.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Tickets relacionados** | Informe o(s) chamado(s) relacionado(s). |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *TOPORCAPLAN001-4786 e TOPORCAPLAN001-4787.* |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | **SQL Server e Oracle.** |
| **Tabelas Utilizadas:** | **Não se aplica.** |
| **Sistema(s) Operacional(is):** | **Windows.** |
| **Pacote:** | **Não se aplica.** |

## Descrição

Criação do Cadastro de Unidade de Serviço e Cadastro de Local de Serviço.

## Procedimento para Utilização

Foi criado em Parâmetros Gerais, os Campos Unidade de Serviço e Local de Serviço, possibilitando a parametrização do nome.

Exemplo:

A **Unidade de Serviço**, pode ser utilizada para descriminar as Torres de um Prédio.

O **Local de Serviço**, pode ser utilizado para descriminar os andares de um Prédio. Os registros dessa tabela são específicos para cada unidade de serviço,

por isso deve ser identificado qual unidade ele pertence, isso porque cada unidade por ter locais distintos (ex: Torre 1 tem 20 andares, e a Torre  2 tem 10 andares).

A funcionalidade está disponível no TOTVS Obras e Projetos, Cad. Gerais, de acordo com o nome parametrizado.

Ao acessar a funcionalidade, é possível incluir uma Unidade de Serviço.

Após cadastrar a Unidade de Serviço, o cadastro de Local de Estoque fica disponível em Anexos.

Ao cadastrar códigos existentes, as seguintes validações serão exibidas:

 

Para acessar a funcionalidade, é necessário Permissão de Acesso.

* Os dados de Unidades de Serviço e Locais de Serviço também estão presentes no Backup/Restore de Projetos, nas Revisões de Projeto, tanto simples quanto múltipla;
* Para tarefas que tem associado Unidade ou Local, ao realizar Cópia de Itens, a associação será desfeita, pois o processo não copia Unidade e Local de serviço.
