---
content_hash: 9f147f82850c19b5cbe407968e5a7ba47beba3c95760401a01d32ccfb24e9b30
fetched_at: '2026-06-29T00:08:40.699769+00:00'
page_id: '286495023'
product: rm
source: tdn-rm
title: EDUCACIONAL01-2003 DT Parâmetro Chave de integração Saída Inteligente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286495023
version: 107
---

# PARAMETRO CHAVE DE INTEGRACAO - SAIDA INTELIGENTE

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **Totvs Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Exportação de alunos/responsáveis para a aplicação Saída Inteligente* | *Exportação de alunos/responsáveis para a aplicação Saída Inteligente* | | *Sincronização de alunos/responsáveis para a aplicação Saída Inteligente* | *Sincronização de alunos/responsáveis para a aplicação Saída Inteligente* | |
| **Cadastros Iniciais:** | * *Cadastrar um unidade de ponto* * *Cadastrar um aluno* * *Cadastrar uma turma* |
| **Parâmetro(s):** | * *Educacional | Configurações | Parâmetros | 15.05 - Integração | 15.05.11 - Saída inteligente*   + *"Utiliza integração com a Saída Inteligente"*   + *"Chave de integração - Aluno"*   + *"Chave de integração - Responsáveis"* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [EDUCACIONAL01-2009](http://jiraproducao.totvs.com.br/browse/EDUCACIONAL01-2009) |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *N/A* |
| **Tabelas Utilizadas:** | *N/A* |
| **Sistema(s) Operacional(is):** | *N/A* |

*Exportação* 

## Descrição

Foram implementados novos parâmetros, TOTVS Educacional, para que seja possível a definição da chave de integração na exportação do aluno e do responsável para a aplicação Saída Inteligente.

Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

Nos parâmetros do TOTVS Educacional foram criados dois novos parâmetros que possibilitam a definição da chave de integração que será utilizada para a criação do relacionamento entre os alunos e responsáveis do Educacional com o Saída Inteligente.

1. ***Educacional | Configurações | Parâmetros | 15.05 - Integração | 15.05.11 - Saída inteligente |** "Chave de integração - Aluno"*
2. ***Educacional | Configurações | Parâmetros | 15.05 - Integração | 15.05.11 - Saída inteligente |** "Chave de integração - Responsáveis"*

A chave de integração do aluno poderá ser definida como:

1. RA - Registro acadêmico
2. Código do usuário
3. Endereço de e-mail  
   \*\* Com isso, a tag **"ra"** do arquivo JSON, enviado para a integração, conterá a informação da chave parametrizada.

 A chave de integração do responsável poderá ser definida como

1. CPF
2. Código do usuário
3. Endereço de e-mail  
   \*\* Com isso, a tag "**id**" do arquivo JSON. enviado para a integração, conterá a informação da cave parametrizada.

Importante

É obrigatório que os responsáveis tenha um endereço de e-mail cadastrado. Caso contrário, não serão enviado para a aplicação Saída Inteligente.

**LOG DE EXPORTAÇÃO**

O log de exportação foi detalhado, para que possa informar os alunos e os responsáveis que foram exportados:

Da mesma forma, foram inclusas informações sobre os registros que não foram importados:

divs
