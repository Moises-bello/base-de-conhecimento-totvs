---
content_hash: d4b6b0c57be05be9658791fd0a05c0d76e5bbeff6963762b4b23c765002ca7fe
fetched_at: '2026-06-29T00:06:14.394989+00:00'
page_id: '210045262'
product: rm
source: tdn-rm
title: DT_Conversor_Integracao_Educacional_Protheus
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Conversor_Integracao_Educacional_Protheus
version: 7
---

# CONVERSÃO DA INTEGRAÇÃO EDUCACIONAL x PROTHEUS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Educacional* |
| **Requisito (ISSUE):** | *PCREQ-7763/PCREQ-7764* |
| **Banco(s) de Dados:** | *SQL Server* |
| **Versões/Release:** | *12.1.8* |

## Descrição

Foram implementados os seguintes processos para utilização do novo modelo de Integração com BackOffice Protheus via Mensagem Única:

1. **Conversor:**   
     
   O processo de acerto da base RM para utilização do novo modelo de Integração via Mensagem Única, será executada no Atualizador de Base de Dados do TOTVS RM da versão 12.1.8.0. Esse processo será identificado como "Educacional (Edu): Integração Protheus", conforme abaixo:  
     
     
   Para execução desse processo é necessário que não exista saldo em conta corrente dos alunos, caso contrário deverá ser executado o assistente para "Aproveitar valores em conta corrente" no módulo **Educacional | Financeiro/Contábil | Assistentes.**
2. **Sincronizador**  

   O sincronizador de entidades deverá ser acessado através do Módulo Integração | Ferramentas | Conversão | Converter Integração. A utilização é realizada em 4 passos, sendo:

   1. Seleção da Conversão: o usuário deverá selecionar a integração, “EducacionalxProtheus Stored Procedure para Mensagem Única”  
      .
   2. Seleção das Entidades: o usuário deverá selecionar as entidades que serão criados os De/Para de forma automática, caso alguma entidade a critério do usuário seja feita de forma manual ou em outro momento, é necessário apenas deixar desmarcado a entidade.
   3. Seleção das Coligadas: o usuário deverá selecionar para quais coligadas (empresas) serão filtrados os registros para conversão.
   4. Seleção das Filiais: o usuário deverá selecionar em quais filiais serão filtrados os registros para conversão.

   Log do Conversor de Entidade

   A conversão de entidades gera log de todos os registros que foram enviados ao Protheus que pode ser acessado através do Módulo Integração | Ferramentas | Conversão | Log de Conversão. Quando executado o processo de conversão, é gerado um novo “Id Execução” que pode ser visualizado ao final do processo na tela de log do processo, o usuário deve usar esse id para filtrar os resultados na tela de log.

divs
