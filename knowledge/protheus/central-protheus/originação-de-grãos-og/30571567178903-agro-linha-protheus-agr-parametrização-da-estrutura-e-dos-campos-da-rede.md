---
article_id: 30571567178903
category: Originação de Grãos (OG)
content_hash: 8da120ef3e5188754cf34933c0ce035fce78a8d4110f15b59c9628ef447520c1
fetched_at: '2026-06-28T22:45:41.181324+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Parametrização da estrutura e dos campos da rede
type: support-article
updated_at: '2025-10-02T13:34:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30571567178903-Agro-Linha-Protheus-AGR-Parametriza%C3%A7%C3%A3o-da-estrutura-e-dos-campos-da-rede
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30571567154711) Tempo aproximado para leitura: **00:01:20 min** **Dúvida**Como testar o **Parametrização da estrutura e dos campos da rede**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agronegócio |
| **Módulo:** | Gestão de Agronegócio |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | AGRA870A | Função chamada a partir da opção alterar/incluir a rotina AGRA870 | |
| **Ponto de entrada:** | AG870AA4 |
| **País(es):** | Todos |
| **Pacote:** | 12.1.23 e superior. |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Localização:** | AGR870ASTT - Criação da tabela temporária p/ Markbrowse |
| **Programa Fonte:** | AGRA870A |
| **Função:** | Permitir parametrização da estrutura e dos campos da grade |
| Parâmetros: | | Nome | Tipo | Descrição | | --- | --- | --- | | PARAMIXB[1] | variedade | Tabela temporária p/ Markbrowse | | PARAMIXB[2] | variedade | Campos Tabela temporária p/ Markbrowse | | PARAMIXB[3] | variedade | Índice Tabela temporária | |
| **Retorno:** | |  |  | | --- | --- | | **Tipo** | **Descrição** | | caractere | Parâmetros de envio: {aMKB,acpMKB,aInd} | |

**Exemplo:**

#incluir ' [protheus.ch](http://protheus.ch/) '  
#incluir ' [parmtype.ch](http://parmtype.ch/) '

Função do usuário AG870AA4 ()

aMKB local:= PARAMIXB[1]  

AcpMKB local:= PARAMIXB[2]  

Local aInd:= PARAMIXB[3]   

aRet := {aMKB,acpMKB,aInd}  
  
Retorna aRet
