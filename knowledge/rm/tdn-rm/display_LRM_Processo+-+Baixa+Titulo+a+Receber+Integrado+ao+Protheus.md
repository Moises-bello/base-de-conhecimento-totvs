---
content_hash: 081c4853b896d8b6f4547ff274b3cfb71e7ace39a8a5c007e18c7c4db7fa5730
fetched_at: '2026-06-29T00:10:51.535559+00:00'
page_id: '568930470'
product: rm
source: tdn-rm
title: Processo - Baixa Titulo a Receber Integrado ao Protheus
type: documentation
url: https://tdn.totvs.com/display/LRM/Processo+-+Baixa+Titulo+a+Receber+Integrado+ao+Protheus
version: 9
---

Os Processos descritos a seguir tem como objetivo orientar na Execução do Processo de Baixa dos Títulos a Receber para a Integração no Totvs Construção Gestão de Imóveis x Backoffice Protheus - EAI2.

**Aviso**  
Antes de seguir os passos para o processo de baixa de título a receber, é recomendado que seja verificado as configurações de parametrização de integração.  
 entrar na aba "Cadastro de Adapter" que se encontra no link, os adapters utilizados para Baixa de Títulos a Receber (FINANCING - FINA055) e (LISTOFACCOUNTRECEIVABLESETTLEMENTS - FINI070LST)

* Todo o processo de baixa de títulos a receber passa a ser efetuado no RM

RM: 

Protheus: 

**OBSERVAÇÃO:**

Em caso de baixa com data retroativa veja como configurar o Protheus = >

A mensagem utilizada na baixa e no cancelamento de baixa ( **LISTOFACCOUNTRECEIVABLESETTLEMENTS** )

O parâmetro Reajuste On-line do TCGI deverá estar marcado.

Parâmetro : NAOCONSULTATRBPRT

Para que o processo de baixa com Protheus ocorra com sucesso é necessário o procedimento abaixo.

* Caso o Protheus **não** esteja parametrizado para geração de tributos, será necessário a criação do parâmetro **NAOCONSULTATRBPRT** de integração.   
  Para criar acesse o RM →Integração → EAI 2.0 → Parâmetros de Adapter
* Caso o Protheus esteja parametrizado para geração de tributos, énecessário que o ambiente Protheus esteja atualizado com API de tributos (**EAITRIBUTOSREST**)  
  Baixe conforme a versão do seu ambiente Protheus.

  | Versão Protheus | Patch |
  | --- | --- |
  | 12.1.2310 | Clique aqui para baixar |
  | 12.1.2210 | Clique aqui para baixar |
  | 12.1.33 | Clique aqui para baixar |
  | 12.1.27 | Clique aqui para baixar |
  | 12.1.25 | Clique aqui para baixar |

  Após atualizar o ambiente Protheus é necessário reiniciar o Protheus.

**Integração | Integrações | Parâmetros adpter**
