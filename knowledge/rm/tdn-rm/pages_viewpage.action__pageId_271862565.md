---
content_hash: 8d359575cd0ba0b6a17f489998a3afd47fb4c85086882fd2bd6ca21fd24cecb4
fetched_at: '2026-06-29T00:08:28.849479+00:00'
page_id: '271862565'
product: rm
source: tdn-rm
title: DT ATIVIDADE FÓRMULA VISUAL CONSULTA CONTEXTO SUBSCRIBER FINANCEIRO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271862565
version: 111
---

# Atividade de Fórmula Visual que possibilita consulta do Contexto do Subscriber em execução.

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Fórmula Visual | *Fórmula Visual* | |
| **Cadastros Iniciais:** | *Cadastrar uma Nova Fórmula Visual* |
| **Parâmetro(s):** | *Permissão para incluir Fórmulas Visuais* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | FIN000272 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL e ORACLE* |
| **Tabelas Utilizadas:** | *N/A* |
| **Sistema(s) Operacional(is):** | *N/A* |

## Descrição

Disponibilizada Atividades de Fórmulas Visuais do Financeiro para Consultar Valores do Contexto de Execução em um Subscriber.

## Procedimento Exemplo para Utilização

###### Observação: Lembrando que os procedimentos abaixo são apenas ilustrativos e não significa que só irá funcionar desta maneira. É apenas um demonstrativo de como a atividade trabalha no

Acesse no RM a Aba Gestão, Fórmula Visual, Atividade, Criar as Atividades no cadastro de Atividades.

Exemplo:

Nome: Consulta Contexto de Extrato no Subscriber  
Assembly: RM.Fin.Workflow  
Classe: RM.Fin.Workflow.Subscriber.FinXCXConsultaContextSubscriberActivity

Criar uma nova Fórmula visual e nos gatilhos escolher Assinantes, "Depois de Preparar Contexto".

Busque por "FinXCX".  
Subscriber para utilizar: RM.Fin.Extrato.Alteracao.FinXCXMasterSbc  
Salve a fórmula visual.

 

Clique duas vezes na fórmula visual sobre a visão para editar o WorkFlow.

Clique e arraste a atividade de "Consulta Contexto de Extrato no Subscriber" para o Workflow.

 

Clique e arraste a atividade de "Gerar Exceção", estará será a forma de validamos que o valor do contexto está sendo carregado.

 

Na Atividade de Consultar contexto aperta F4 e preencha as propriedades:  
> Tabela com: FXCX  
> CAMPO com: CODCOLIGADA;IDXCX;VALOR;NUMERODOCUMENTO

Na Atividade de Gerar Exceção na propriedade Mensagem informe o Campo Retorno da Atividade de Consulta Valor.

Ao realizar alteração em qualquer extrato o sistema irá apresentar mensagem de erro com os campos que pediu nas propriedades da Atividade de Consulta Context.

 

Lembrando que o Resultado será apresentado em ordem alfabética dos campos. Caso a ordem no campo CAMPO estiver diferente o sistema irá reorganizá-los.

Neste caso: CODCOLIGADA (C), IDXCX (I), NUMERODOCUMENTO (N), VALOR (V),

Desta forma qualquer valor de Contexto após conclusão do serviço poderá ser consultado.

Esta funcionalidade foi disponibilizada para:

Extrato de Caixa,  
Cliente/Fornecedor,   
Dados Bancários do Cliente/Fornecedor,   
Lançamento,   
Rateio por Centro de Custo e Rateio por Departamento.

### Para isto existem as atividades:

FinCFOConsultaContextSubscriberActivity

FinDadosPGTOConsultaContextSubscriberActivity

FinXCXConsultaContextSubscriberActivity

FinLanConsultaContextSubscriberActivity

Obs: Para a Atividade de Lançamento é possível buscar dados da Tabela FLANRATCCU e FLANRATDEP, será necessário apenas modificar a propriedade TABELA, como veremos posteriormente. Para isto o campo POSIÇÃO da propriedade da atividade deve ser preenchido com a posição do item da Lista do rateio.

divs
