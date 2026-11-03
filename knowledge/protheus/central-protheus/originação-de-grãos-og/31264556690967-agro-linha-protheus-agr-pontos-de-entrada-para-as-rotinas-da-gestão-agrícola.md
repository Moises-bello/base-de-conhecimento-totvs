---
article_id: 31264556690967
category: Originação de Grãos (OG)
content_hash: a1e021aeecda5248e394a6b8b60e69a3dbf16813d4d883e33f4ba2ff57797632
fetched_at: '2026-06-28T22:45:43.223800+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Pontos de Entrada para as rotinas da Gestão Agrícola
type: support-article
updated_at: '2025-08-07T13:20:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31264556690967-Agro-Linha-Protheus-AGR-Pontos-de-Entrada-para-as-rotinas-da-Gest%C3%A3o-Agr%C3%ADcola
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31264524526487) Tempo aproximado para leitura: **00:03:15 min** **Dúvida**Como testar o **Ponto de Entrada para rotinas da Gestão Agrícola**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | AGRA010 | Previsões de Aplicações. |  |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | AGRA040 | Cadastro de mensagens para as notas fiscais de saída e/ou documento de entrada. |  |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | AGRA100 | Inclusão de compromisso futuro. |  |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | AGRA105 | Inclusão de contratos financeiros. |  |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | AGRA200 | Inclusão de previsão de aplicação. |  |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | AGRA205 | Inclusão de retorno de aplicações. |  |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | AGRA280 | Rotina de romaneio de entrada. |  |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | AGRA045 | Manutenção de locais de estoque. | |
| **Pontos de entrada:** | AGRA010G, AGRA040IT, AGRA100DP, AGRA100PR, AGRA100RA, AGRA105E2,  AGRA105IC, AGRA105RP, AGRA200MO, AGRA200PD, AGRA205EQ, AGRA205GE,  AGRA205MO, AGRA205PD, AGRA205RA, AGRA280EX, AGRA280IN, CMA150AMNU |
| **País(es):** | Todos |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Descrição:** | Ponto de Entrada após gravação da tabela NN4. |
| **Localização:** | Rotina auxiliar para montagem da tela de cadastro. |
| **Programa Fonte:** | AGRA010 |
| **Função:** | AGRA010G |

****Exemplo:****#Incluir função de usuário  ' [Protheus.ch](http://protheus.ch/) ' AGRA010G ()

nOpcA      local := PARAMIXB[1]

    Se nOpcA == 1

        Alert("Opções escolhidas, Incluir, Alterar, Excluir")

    Outro

        Alert("Exemplo de Alerta após gravação da tabela NN4")

    FimSe

   // Personalizações abaixo // 

    Retornar

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Descrição:** | Permite a manipulação de campos para o cadastro histórico padrão. |
| **Localização:** | GetDados para cadastro de Históricos Padrão. |
| **Programa Fonte:** | AGRA040 |
| **Função:** | AGRA040IT |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **aCampos** | Variedade | Parâmetros enviados: { aCampos } | Não | |

****Exemplo:****#Incluir função de usuário  ' [Protheus.ch](http://protheus.ch/) ' AGRA040IT ()

Campos      locais  := PARAMIXB[1]

aAdd(aCampos, 'NNL\_SEQ')

    aAdd(aCampos, 'NNL\_MENS')

   // Personalizações abaixo // 

    Retornar ( aCampos) 

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Descrição:** | Ponto de entrada após g erar título no financeiro. |
| **Localização:** | Fechamento financeiro do compromisso. |
| **Programa Fonte:** | AGRA100 |
| **Função:** | AGRA100DP |

****Exemplo:****

#Incluir função de usuário  ' [Protheus.ch](http://protheus.ch/) ' AGRA100DP ()

    Alert("Exemplo de Alerta após gerar título no financeiro")

   // Personalizações abaixo // 

    Retornar

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Descrição:** | Ponto de Entrada após g erar título provisório no financeiro. |
| **Localização:** | Rotina para atualização/criação do título tipo provisório. |
| **Programa Fonte:** | AGRA100 |
| **Função:** | AGRA100PR |

****Exemplo:****#Incluir função de usuário  ' [Protheus.ch](http://protheus.ch/) ' AGRA100PR ()

    Alert("Exemplo de Alerta após gerar título provisório no financeiro")

   // Personalizações abaixo // 

    Retornar

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Descrição:** | Ponto de Entrada após a otina para inclusão de Recebimentos Antecipados. |
| **Localização:** | Rotina para inclusão de Recebimentos Antecipados. |
| **Programa Fonte:** | AGRA100 |
| **Função:** | AGRA100RA |

****Exemplo:****#Incluir função de usuário  ' [Protheus.ch](http://protheus.ch/) ' AGRA100RA ()

    Alert("Exemplo de Alerta após rotina para inclusão de coletas antecipadas.")

   // Personalizações abaixo // 

    Retornar

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Descrição:** | Ponto de entrada após a otina para gravação de dados. Geração de títulos a Pagar. |
| **Localização:** | Rotina para gravação de dados. Geração de títulos a Pagar. |
| **Programa Fonte:** | AGRA105 |
| **Função:** | AGRA105E2 |

****Exemplo:****#Incluir função de usuário  ' [Protheus.ch](http://protheus.ch/) ' AGRA105E2 ()

    Alert("Exemplo de Alerta após rotina para gravação de dados. Geração de títulos a Pagar.")

   // Personalizações abaixo // 

    Retornar

****Ponto de Entrada:****

|  |  |
| --- | --- |
| **Descrição:** | Ponto de Entrada após inclusão do contrato financeiro. |
| **Localização:** | Rotina auxiliar para montagem da tela de cadastro. |
| **Programa Fonte:** | AGRA105 |
| **Função:** | AGRA105IC |

****Exemplo:****#Incluir função de usuário  ' [Protheus.ch](http://protheus.ch/) ' AGRA105IC ()

    Alert("Exemplo de Alerta após inclusão do contrato financeiro.")

   // Personalizações abaixo // 

    Retornar

****Ponto de Entrada:****

|  |  |
| --- | --- |
| **Descrição:** | Permite determinar se deseja selecionar as parcelas a serem alteradas ou encerrar a operação. |
| **Localização:** | Seleção de parcelas a serem alteradas. |
| **Programa Fonte:** | AGRA105 |
| **Função:** | AGRA105RP |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **lRetorno** | Lógico | Sem parâmetros | Não | |

****Exemplo:****#Incluir função de usuário  ' [Protheus.ch](http://protheus.ch/) ' AGRA105RP ()

    Local lRetorno := .T.

    Local nExemp1 := 5

    Local nExemp2 := 5

If aExemp1 == aExemp2  
        Alert("Irá obrigação com a seleção de parcelas a serem alteradas")      
    Else  
        lRetorno := .F. // Não será obrigatória a seleção de parcelas a serem alteradas  
    EndIf

   // Personalizações abaixo // 

    Retornar lRetorno

****Ponto de Entrada:****

|  |  |
| --- | --- |
| **Descrição:** | Permite modificar os campos referentes à mão de obra. |
| **Localização:** | Atualização da aplicação e itens da aplicação. |
| **Programa Fonte:** | AGRA200 |
| **Função:** | AGRA200MO |
| **Retorno:** | | Nome | Tipo | Descrição | Obrigatório | | --- | --- | --- | --- | | **aCposMO** | Variedade | Parâmetros enviados: { aCposMO } | Não | |

****Exemplo:****

#Incluir função de usuário  ' [Protheus.ch](http://protheus.ch/) ' AGRA200MO ()

    aCposMO local := PARAMIXB[1]

    Se aCposMO[1] ==  'NP2\_ITEM'

aAdd(aCposMO , 'NP2\_MARCA')

    FimSe

   // Personalizações abaixo // 

    Retornar (aCposMO) 

****Ponto de Entrada:****

|  |  |
| --- | --- |
| **Descrição:** | Permite modificar os campos referentes aos produtos. |
| **Localização:** | Atualização da aplicação e itens da aplicação. |
| **Programa Fonte:** | AGRA200 |
| **Função:** | AGRA200PD |
| **Rotina:** | | Nome | Tipo | Descrição | Obrigatório | | --- | --- | --- | --- | | **umCposPD** | Variedade | Parâmetros enviados; { aCposPD } | Não | |

****Exemplo:****#Incluir função de usuário  ' [Protheus.ch](http://protheus.ch/) ' AGRA200PD ()

    aCposPD local:= PARAMIXB[1]

    Se aCposPD[1] ==  'NP2\_ITEM'

aAdd(aCposPD, 'NP2\_MARCA')

    FimSe

   // Personalizações abaixo // 

    Retorno (aCposPD) 

****Ponto de Entrada:****

|  |  |
| --- | --- |
| **Descrição:** | Permite modificar os campos referentes aos equipamentos. |
| **Localização:** | Atualização da aplicação e itens da aplicação |
| **Programa Fonte:** | AGRA205 |
| **Função:** | AGRA205EQ |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **aCposEQ** | Variedade | Parâmetros enviados: { aCposEQ } | Não | |

****Exemplo:****#Incluir função de usuário  ' [Protheus.ch](http://protheus.ch/) ' AGRA200PD ()

    aCposEQ local:= PARAMIXB[1]

    Se aCposEQ[1] ==  'NP2\_ITEM'

aAdd(aCposEQ, 'NP2\_MARCA')

    FimSe

   // Personalizações abaixo // 

    Retornar (aCposEQ) 

****Ponto de Entrada:****

|  |  |
| --- | --- |
| **Descrição:** | Permite determinar se o prazo do fechamento da aplicação será realizado ou encerrar a operação. |
| **Localização:** | Aplicar o estorno do fechamento na aplicação. |
| **Programa Fonte:** | AGRA205 |
| **Função:** | AGRA205GE |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **lAGRA205GE** | Lógico | Sem parâmetros | Não | |

****Exemplo:****#Incluir função de usuário  ' [Protheus.ch](http://protheus.ch/) ' AGRA205GE ()

    lAGRA205GE local:= .T.

    Local nExemp1 := 5

    Local nExemp2 := 5

If aExemp1 == aExemp2  
        Alert("Ira obrigação com o  estorno do fechamento na aplicação. ")        
    Else  
        lAGRA205GE:= .F. // Não haverá obrigação com  o estorno do fechamento na aplicação.  
    FimSe

   // Personalizações abaixo // 

    Retornar lAGRA205GE

****Ponto de Entrada:****

|  |  |
| --- | --- |
| **Descrição:** | Permite modificar os campos referentes à mão de obra. |
| **Localização:** | Atualização da aplicação e itens da aplicação. |
| **Programa Fonte:** | AGRA205 |
| **Função:** | AGRA205MO |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **aCposMO** | Variedade | Parâmetros enviados: { aCposMO } | Não | |

****Exemplo:****#Incluir função de usuário  ' [Protheus.ch](http://protheus.ch/) ' AGRA205MO ()

    aCposMO local := PARAMIXB[1]

    Se aCposMO[1] ==  'NP6\_ITEM'

aAdd(aCposMO , 'NP6\_VAZAO')

    FimSe

   // Personalizações abaixo // 

    Retornar (aCposMO) 

****Ponto de Entrada:****

|  |  |
| --- | --- |
| **Descrição:** | Permite modificar os campos referentes aos produtos. |
| **Localização:** | Atualização da aplicação e itens da aplicação. |
| **Programa Fonte:** | AGRA200 |
| **Função:** | AGRA200PD |
| **Rotina:** | | Nome | Tipo | Descrição | Obrigatório | | --- | --- | --- | --- | | **umCposPD** | Variedade | Parâmetros enviados; { aCposPD } | Não | |

****Exemplo:****#Incluir função de usuário  ' [Protheus.ch](http://protheus.ch/) ' AGRA200PD ()

    aCposPD local:= PARAMIXB[1]

    Se aCposPD[1] ==  'NP2\_ITEM'

aAdd(aCposPD, 'NP2\_MARCA')

    FimSe

   // Personalizações abaixo // 

    Retorno (aCposPD) 

****Ponto de Entrada:****

|  |  |
| --- | --- |
| **Descrição:** | Permite modificar os campos referentes aos equipamentos. |
| **Localização:** | Atualização da aplicação e itens da aplicação |
| **Programa Fonte:** | AGRA205 |
| **Função:** | AGRA205EQ |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **aCposEQ** | Variedade | Parâmetros enviados: { aCposEQ } | Não | |

****Exemplo:****#Incluir função de usuário  ' [Protheus.ch](http://protheus.ch/) ' AGRA200PD ()

    aCposEQ local:= PARAMIXB[1]

    Se aCposEQ[1] ==  'NP2\_ITEM'

aAdd(aCposEQ, 'NP2\_MARCA')

    FimSe

   // Personalizações abaixo // 

    Retornar (aCposEQ) 

****Ponto de Entrada:****

|  |  |
| --- | --- |
| **Descrição:** | Permite determinar se o prazo do fechamento da aplicação será realizado ou encerrar a operação. |
| **Localização:** | Aplicar o estorno do fechamento na aplicação. |
| **Programa Fonte:** | AGRA205 |
| **Função:** | AGRA205GE |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **lAGRA205GE** | Lógico | Sem parâmetros | Não | |

****Exemplo:****#Incluir função de usuário  ' [Protheus.ch](http://protheus.ch/) ' AGRA205GE ()

    lAGRA205GE local:= .T.

    Local nExemp1 := 5

    Local nExemp2 := 5

If aExemp1 == aExemp2  
        Alert("Ira obrigação com o  estorno do fechamento na aplicação. ")        
    Else  
        lAGRA205GE:= .F. // Não haverá obrigação com  o estorno do fechamento na aplicação.  
    FimSe

   // Personalizações abaixo // 

    Retornar lAGRA205GE

****Ponto de Entrada:****

|  |  |
| --- | --- |
| **Descrição:** | Permite modificar os campos referentes à mão de obra. |
| **Localização:** | Atualização da aplicação e itens da aplicação. |
| **Programa Fonte:** | AGRA205 |
| **Função:** | AGRA205MO |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **aCposMO** | Variedade | Parâmetros enviados: { aCposMO } | Não | |

****Exemplo:****#Incluir função de usuário  ' [Protheus.ch](http://protheus.ch/) ' AGRA205MO ()

    aCposMO local := PARAMIXB[1]

    Se aCposMO[1] ==  'NP6\_ITEM'

aAdd(aCposMO , 'NP6\_VAZAO')

    FimSe

   // Personalizações abaixo // 

    Retornar (aCposMO) 

****Ponto de Entrada:****

|  |  |
| --- | --- |
| **Descrição:** | Permite modificar os campos referentes aos produtos. |
| **Localização:** | Atualização da aplicação e itens da aplicação |
| **Programa Fonte:** | AGRA205 |
| **Função:** | AGRA205PD |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **umCposPD** | Variedade | Parâmetros de envio: { aCposPD } | Não | |

****Exemplo:****#Incluir função de usuário  ' [Protheus.ch](http://protheus.ch/) ' AGRA205PD ()

    aCposPD local:= PARAMIXB[1]

    Se aCposPD[1] ==  'NP6\_ITEM'

aAdd(aCposPD, 'NP6\_VAZAO')

    FimSe

   // Personalizações abaixo // 

    Retorno (aCposPD) 

****Ponto de Entrada:****

|  |  |
| --- | --- |
| **Descrição:** | Ponto de Entrada anterior à atualização dos itens do estorno. |
| **Localização:** | Grava retorno das aplicações. |
| **Programa Fonte:** | AGRA205 |
| **Função:** | AGRA205RA |

****Exemplo:****#Incluir função de usuário  ' [Protheus.ch](http://protheus.ch/) ' AGRA205RA ()

    Alert("Exemplo de Alerta anterior a atualização dos itens do estorno.")

   // Personalizações abaixo // 

    Retornar

****Ponto de Entrada:****

|  |  |
| --- | --- |
| **Descrição:** | Ponto de Entrada para o tratamento de exclusão do frete. |
| **Localização:** | Rotina auxiliar para exclusão de Romaneio de Entrada. |
| **Programa Fonte:** | AGRA280 |
| **Função:** | AGRA280EX |

****Exemplo:****#Incluir função de usuário  ' [Protheus.ch](http://protheus.ch/) ' AGRA280EX ()

    Alert("Exemplo de Alerta para o tratamento da exclusão do frete.")

   // Personalizações abaixo // 

    Retornar

****Ponto de Entrada:****

|  |  |
| --- | --- |
| **Descrição:** | Ponto de Entrada para o tratamento de inclusão do frete. |
| **Localização:** | Rotina auxiliar para inclusão de Romaneio de Entrada. |
| **Programa Fonte:** | AGRA280 |
| **Função:** | AGRA280IN |

****Exemplo:****

#Incluir função de usuário  ' [Protheus.ch](http://protheus.ch/) ' AGRA280IN ()

    Alert("Exemplo de Alerta para o tratamento da inclusão do frete.")

   // Personalizações abaixo // 

    Retornar

****Ponto de Entrada:****

|  |  |
| --- | --- |
| **Descrição:** | Permite incluir novos itens no menu "Ações Relacionadas". |
| **Localização:** | Definição de Menu |
| **Programa Fonte:** | AGRA045 |
| **Função:** | CMA150AMNU |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **aRotÁdico** | Variedade | Sem parâmetros | Não | |

****Exemplo:****

#Incluir ' [Protheus.ch](http://protheus.ch/) '

Função do usuário CMA150AMNU ()

aRotAdic local:= PARAMIXB[1]

aAdd( aRotAdic, { "TESTE PNT ENT.", "AGR750EXEMP ", 0, 4, 0, Nil } )    
Retorna (aRotAdic)
