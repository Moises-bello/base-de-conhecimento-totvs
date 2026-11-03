---
content_hash: 74a6fdebe8681dbfaa40dafe0d4218af7fe29ddc37ff8219cb2770d43ef456ec
fetched_at: '2026-06-29T00:06:07.865317+00:00'
page_id: '201739324'
product: rm
source: tdn-rm
title: DT_Serviço_para_Extração_de_Dados_para_o_Formulário_Dinâmico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201739324
version: 3
---

# Serviço para Extração de Dados para o Formulário Dinâmico

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar - Prontuário Eletrônico do Paciente |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | GetJSON\_OBJECT e GetJSON | Serviço de extração dos dados do sistema para o formulário dinâmico |  |  | | --- | | **Rotina(s) envolvida(s)** | | PEP 2.0 | | Formulários Dinâmicos | |
| **Cadastros Iniciais:** | ConsultasSQL |
| **Requisito (ISSUE):** | [PCREQ-6799](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-6799) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Sistema(s) operacional(is):** | Windows |
| **Versões/Release:** | 12.1.7 |

## Descrição

Implementado Serviço de disponibilização dos dados do TOTVS Gestão Hospitalar para ser exibido nos Formulários Dinâmicos que é utilizado pelo Prontuário Eletrônico do Paciente (PEP 2.0).

Os serviços disponibilizam dados em um único registro e também uma lista de registros.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da BibliotecaRM versão 12.1.7.

1. Aplique o patch do chamado.
2. Instale o TOTVS BusinessConnect.
3. O arquivo wsformdinamico.asmx, deve estar na pasta base do TBC.
4. No arquivo web.config, deve existir as tags abaixo:
   1. <system.web>  
        <customErrors mode="Off"/>  
        <compilation debug="true" targetFramework="4.0" />  
        <authorization>  
             <allow users="\*" />  
        </authorization>  
       <webServices>  
          <protocols>  
      **<add name="HttpGet"/>**  
      **<add name="HttpPost"/>**  
          </protocols>  
       </webServices>

      </system.web>

## Procedimento para Utilização

1. Após a atualização da versão e instalação ou configuração do **TOTVS Business Connnect** (TBC), o serviço é inicializado.
2. Acesse a funcionalidade de **Consulta SQL** e cadastre uma sentença que envolva o paciente e/ou o atendimento.
3. Se a consulta envolver o atendimento, deve-se utilizar a tabela **SZATENDIMENTOPEP** realizando **JOIN** com a **SZATENDIMENTO**, uma vez que o código do atendimento para o **Prontuário Eletrônico do Paciente** é um outro sequencial. O campo que informado para a consulta como parâmetro é o **CODATENDIMENTOPEP**.  
   Exemplo de uso: wsformdinamico.asmx/GetJSON\_OBJECT?codSentenca=CLASS.01&codAplicacao=O&parameters=CODCOLIGADA=2;CODPACIENTE=@QUERY('mpi');CODATENDIMENTO=@QUERY('attentionId').
