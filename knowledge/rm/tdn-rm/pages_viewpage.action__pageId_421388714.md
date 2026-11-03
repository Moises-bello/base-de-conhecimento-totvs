---
content_hash: 3be2e7894efa5aa5ef88166e409fa68cd34d1a8a8856e53fb34789188df6ef23
fetched_at: '2026-06-29T00:09:18.533512+00:00'
page_id: '421388714'
product: rm
source: tdn-rm
title: Sincronizador integração Educacional X Protheus  
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388714
version: 4
---

Com o objetivo de permitir a criação do De/Para para as entidades da Integração Educacional X Protheus via Stored Procedure para o novo modelo de integração que usa Mensagem Única. 

**Entidades utilizadas**

Será possível utilizar as seguintes entidades:

* Centro de Custo
* Unidade de Medida
* Cliente/Fornecedor
* Banco/Agência/Conta
* Lançamento a Receber
* Moeda
* Classe de Valor

Importante ressaltar: É necessário que Integração Educacional X BackOffice no novo modelo esteja configurado e em perfeito funcionamento.

* Fica a cargo da linha RM o envio dos registros a serem sincronizados com o Protheus.
* O Protheus deve receber a nova mensagem, consultar na base de dados o registro e retornar ao RM o status da pesquisa.
* Se encontrado na base de dados do Protheus será salvo um ID, que será registrado na tabela De/Para e enviado ao RM o ID.

**Passo a passo**

Para a sincronização das entidades necessário acessar o Totvs Integração | Ferramentas | Conversão | Converter Integração.

1. Seleção da conversão a ser utilizada: "EducacionalXProtheus Stored Procedure para Mensagem Única".
2. Seleção das entidades: Selecionar as entidades a serem convertidas de forma automática pelo processo.
3. Seleção das coligadas onde serão filtrados os registros para a conversão.
4. Seleção das filiais onde serão filtrados os registros para a conversão.

Obs1: Para conversão manual em momento posterior de alguma entidade necessário apenas deixar desmarcado a entidade.   
 Obs2: O conversor pode ser executado várias vezes, as entidades já enviadas se marcadas serão novamente transmitidas ao Protheus.

**Log do conversor de entidade**

Todos os registros enviados ao Protheus poderão ser visualizados através do Menu: Integração | Ferramentas | Conversão | Log de Conversão. Poderá ser executado pelo Id Execução.

 Informações Complementares

* [Especificação do Sincronizador](http://tdn.totvs.com/display/LRM/ER_PCREQ-7764_Sincronizador_Integracao_Educacional_Protheus)
