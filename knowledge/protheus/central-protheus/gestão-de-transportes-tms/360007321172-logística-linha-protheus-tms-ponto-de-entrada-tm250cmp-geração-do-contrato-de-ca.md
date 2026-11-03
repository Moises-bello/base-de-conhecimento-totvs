---
article_id: 360007321172
category: Gestão de Transportes (TMS)
content_hash: 3911135b5bdd2719199032b59abf995ab340e201c605421699acb13275b6c8d1
fetched_at: '2026-06-28T22:45:32.188246+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM250CMP - Geração do Contrato
  de Carreteiro
type: support-article
updated_at: '2022-05-05T14:08:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007321172-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM250CMP-Gera%C3%A7%C3%A3o-do-Contrato-de-Carreteiro
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como implementar o ponto de entrada **TM250CMP** - Geração do Contrato de Carreteiro?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - A partir da versão 11.80  
  
**Solução**O ponto de entrada **TM250CMP** está localizado após a geração do contrato de carreteiro.  
  
**Programa** **Fonte**: TMSA250.PRW  
  
**Sintaxe**: TM250CMP - Geração do Contrato de Carreteiro ( [ aDadosCTC ] ) --> NULL  
  
**Parâmetros**:

* **Nome**: aDadosCTC
* **Tipo**: *Array*
* **Descrição**: *Array* com os dados do fornecedor.

**Retorno**:  
  
**NULL**

(array\_of\_record)

**Parâmetros Enviados**: aDadosCTC **Estrutura do Array aDadosCTC**:  
  
     aDadosCTC[n,01] - Código do Fornecedor                                 
     aDadosCTC[n,02] - Loja do Fornecedor                                   
     aDadosCTC[n,03] - Tipo Fornecedor (Pessoa Física, Jurídica, ...)          
     aDadosCTC[n,04] - Contato do Fornecedor                                
     aDadosCTC[n,05] - Filial de Debito Fornecedor                          
     aDadosCTC[n,06] - Condição de Pagamento do Fornecedor                  
     aDadosCTC[n,07] - Filial de Origem                                     
     aDadosCTC[n,08] - No. da Viagem                                        
     aDadosCTC[n,09] - No. do Contrato                                      
     aDadosCTC[n,10] - Valor do Frete informado na viagem / Calculado       
     aDadosCTC[n,11] - Valor dos Adiantamentos                              
     aDadosCTC[n,12] - Credor dos Adiantamentos                             
     aDadosCTC[n,13] - Loja do Credor                                       
     aDadosCTC[n,14] - Prefixo do Titulo                                    
     aDadosCTC[n,15] - Código do Veiculo                                    
     aDadosCTC[n,16] - Valor do Pedágio                                    
     aDadosCTC[n,17] - Tipo do Titulo                                       
     aDadosCTC[n,18] - Código do Favorecido                                 
     aDadosCTC[n,19] - Loja do Favorecido                                   
     aDadosCTC[n,20] - Valor do ISS                                         
     aDadosCTC[n,21] - Natureza do Titulo                                   
     aDadosCTC[n,22] - Gera Titulo do Pedágio ? (1=Sim/2=Não)               
     aDadosCTC[n,23] - Deduz Pedágio do Valor do Frete? (1=Sim/2=Não)       
     aDadosCTC[n,24] - Valor Base para Calculo dos Impostos                 
     aDadosCTC[n,24] - Controla a Liberação do Contrato de Carreteiro?      
     aDadosCTC[n,26] - Contrato vinculado a Operadora de Frotas?            
     aDadosCTC[n,27] - Valor do INSS Retido                                 
     aDadosCTC[n,28] - Tipo de Uso - 1=Viagem;2=Carga - Frete Embarcador    
     aDadosCTC[n,29] - Identificador de Viagem ou Carga - Frete Embarcador   
     aDadosCTC[n,30] - Gera Titulo do Contrato ?(1=Sim/2=Não)
