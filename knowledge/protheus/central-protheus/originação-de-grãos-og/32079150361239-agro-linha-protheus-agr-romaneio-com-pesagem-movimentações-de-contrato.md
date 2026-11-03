---
article_id: 32079150361239
category: Originação de Grãos (OG)
content_hash: bc0a26c242fd73e21c0cdce07b8024d165eef488dc25b7ad3d0843aa3a17f53c
fetched_at: '2026-06-28T22:45:44.814019+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Romaneio com Pesagem - Movimentações de Contrato
type: support-article
updated_at: '2025-08-18T13:59:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32079150361239-Agro-Linha-Protheus-AGR-Romaneio-com-Pesagem-Movimenta%C3%A7%C3%B5es-de-Contrato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32079158615447) Tempo aproximado para leitura: **00:01:40 min** **Dúvida**O que indica a tabela **Romaneio com Pesagem - Movimentações de Contrato**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | OGA250 | Romaneio com Pesagem | |
| **Ponto de entrada:** | OGA250GRV |
| **País(es):** | Todos |
| **Versões/Lançamento:** | 11.80.19 |

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | OGA440 | Movimentações de Contrato | |
| **Ponto de entrada:** | OGA440GRV |
| **País(es):** | Todos |
| **Versões/Lançamento:** | 11.80.19 |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Descrição:** | Permite personalizar o modelo, anteriormente à gravação de dados adicionais e ao modelo de dados. |
| **Localização:** | GrvModelo |
| **Programa Fonte:** | OGA250 |
| **Função:** | OGA250GRV |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | OGA250GRV | Lógico | Definir. permite realizar uma gravação.  Parâmetros enviados: {oModel,"PosModelo","OGA250"} | NÃO | |

**Exemplo:**

#Incluir função de usuário ' [Protheus.ch](http://protheus.ch/) ' OGA250GRV ()

    Local oStruZA0 := FWFormStruct( 1, 'ZA0' )  
    Local oModel := PARAMIXB[1] // Modelo referente ao OGA250

    Local c PosModelo := PARAMIXB[2] 

    cRotina local :=  PARAMIXB[3] 

Local lRetorno := .T.

   oModel:AddFields( 'ZA0MASTER', /\*cOwner\*/, oStruZA0)  
   oModel:SetDescription( 'Modelo de dados do Autor/Interprete' )  
   oModel:GetModel( 'ZA0MASTER' ):SetDescription( 'Dados do Autor/Interprete' )

   // Personalizações abaixo // 

    Retornar .T.

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Descrição:** | Permite personalizar o modelo, anteriormente à gravação de dados adicionais e ao modelo de dados. |
| **Localização:** | GrvModelo |
| **Programa Fonte:** | OGA440 |
| **Função:** | OGA440GRV |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | OGA440GRV | Lógico | Definir. permite realizar uma gravação.  Parâmetros enviados: {oModel,"PosModelo"," OGA440 "} | NÃO | |

**Exemplo:**

#Incluir função de usuário ' [Protheus.ch](http://protheus.ch/) ' OGA440GRV ()

    Local oStruZA0 := FWFormStruct( 1, 'ZA0' )  
    Local oModel := PARAMIXB[1] // Modelo referente ao OGA440

    Local c PosModelo := PARAMIXB[2] 

    cRotina local :=  PARAMIXB[3] 

Local lRetorno := .T.

   oModel:AddFields( 'ZA0MASTER', /\*cOwner\*/, oStruZA0)  
   oModel:SetDescription( 'Modelo de dados do Autor/Interprete' )  
   oModel:GetModel( 'ZA0MASTER' ):SetDescription( 'Dados do Autor/Interprete' )

   // Personalizações abaixo // 

    Retornar .T.
