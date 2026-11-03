---
article_id: 360018386511
category: Financeiro - Liquidação a Receber
content_hash: fc7aa3fd5fb914df68293521a7c5ada62fbb58a7ba07288872f9107de635dfbb
fetched_at: '2026-06-28T22:37:42.326129+00:00'
product: protheus
section_id: 33830247616663
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Pontos de Entrada FINA460
type: support-article
updated_at: '2026-05-13T20:02:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018386511-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Pontos-de-Entrada-FINA460
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22239110043031)** Tempo aproximado para leitura: **00:20 min**  
  
**Dúvida**  
Quais são os pontos de entrada da Rotina **FINA460**?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir do release 12.1.17  
  
**Solução**

Segue abaixo os pontos de entrada na rotina **FINA460**:

|  |  |  |
| --- | --- | --- |
| Ponto de entrada/Documentação | Função | Observações |
| [**FA460OUT**](https://tdn.totvs.com/x/nSdNDQ) | **A460Liquid** | Mantém funcionalidade |
| [**F460NUM**](https://tdn.totvs.com/pages/viewpage.action?pageId=640900489) | **A460Liquid** | Mantém funcionalidade |
| **F460SAID** | **A460Liquid** | Substituir por **FORMCANCEL** |
| **F460GRV** | **A460Liquid** | Substituir por **MODELCOMMITNTTS** |
| [**A460COL**](https://tdn.totvs.com/x/OqJc) | **A460Liquid** | Ponto de Entrada para a adição de colunas na GetDados da tela de geração de títulos.  Não contemplado no fonte em virtude da alteração de tecnologia de GetDados para MVC, cliente poderá criar campo da FO2, diretamente. **Descontinuado**. |
| [**F460BOT**](https://tdn.totvs.com/pages/releaseview.action?pageId=639948372) | **A460Liquid** | Substituir por **BUTTONBAR** |
| **F460CAN** | **A460Liquid** | Mantém funcionalidade |
| **F460CON** | **A460Liquid** | Mantém funcionalidade |
| **FA460LOK** | **a460OK** | Substituir por **FORMLINEPRE** |
| **A460VALLIN** | **a460OK** | Substituir por **FORMLINEPRE** |
| **F460TOK** | **a460TudoOK** | Substituir por **FORMCOMMITTTSPRE** |
| [**FA460OWN**](https://tdn.totvs.com/pages/viewpage.action?pageId=651292859) | **A460ChecF** | Mantém funcionalidade |
| **FA460FIL** | **A460ChecF** | Mantém funcionalidade |
| [**F460GerNCC**](https://tdn.totvs.com/pages/viewpage.action?pageId=640897439) | **A460Grava** | Mantém funcionalidade |
| [**F460NCC**](https://tdn.totvs.com/pages/viewpage.action?pageId=640898714) | **A460Grava** | Mantém funcionalidade |
| [**F460VAL**](https://tdn.totvs.com/pages/viewpage.action?pageId=641663360) | **A460Grava** | Mantém funcionalidade |
| [**F460SE1**](https://tdn.totvs.com/pages/viewpage.action?pageId=641466357) | **A460Grava** | Mantém funcionalidade |
| [**SE5FI460**](https://tdn.totvs.com/x/FKRc) | **A460Grava** | Mantém funcionalidade |
| [**F460GRVSEF**](https://tdn.totvs.com/pages/viewpage.action?pageId=640897758) | **A460Grava** | Mantém funcionalidade |
| **F460CTB** | **A460Grava** | Mantém funcionalidade |
| [**A460PARC**](https://tdn.totvs.com/x/O6Jc) | **A460Cond** | Mantém funcionalidade |
| **FA460con** | **A460Cond** | Substituir por **FORMPOS** |
| [**F460CANC**](https://tdn.totvs.com/pages/viewpage.action?pageId=653410106) | **FA460CAN** | Mantém funcionalidade |
| [**F460E5**](https://tdn.totvs.com/pages/viewpage.action?pageId=640895946) | **FA460CAN** | Mantém funcionalidade |
| [**FIN460E1**](https://tdn.totvs.com/x/me5bDQ) | **FA460CAN** | Mantém funcionalidade |
| [**F460JUR**](https://tdn.totvs.com/x/uYq7Hw) | **Fa460Repl** | Mantém funcionalidade |
| [**F460DES**](https://tdn.totvs.com/pages/viewpage.action?pageId=640893685) | **Fa460Repl** | Mantém funcionalidade |
| **FA460BUT** | **Fa460Bar** | Tela de seleção de títulos substituída pela **GRID** da tabela **FO1**. **Descontinuado** |
| **FA460BAD** | **Fa460Bar** | Tela de seleção de títulos substituída pela **GRID** da tabela **FO1**. **Descontinuado** |
| **F460EDIT** | **Fa460Edit** | Botão editar retirado na nova estrutura, substituído pela alteração de campos direto na tela. **Descontinuado** |
| **FI460JUR** | **Fa460Edit** | Botão editar retirado na nova estrutura, substituído pela alteração de campos direto na tela. **Descontinuado** |
| [**F460VLDE**](https://tdn.totvs.com/x/B_RbDQ) | **Fa460Edit** | Botão editar retirado na nova estrutura, substituído pela alteração de campos direto na tela. **Descontinuado** |
| [**F460OK1**](https://tdn.totvs.com/pages/viewpage.action?pageId=640901251) | **Fa460OK1** | Mantém funcionalidade |
| [**FA460CMC7**](https://tdn.totvs.com/pages/viewpage.action?pageId=653410733) | **F460CMC7** | Mantém funcionalidade |
| [**F460CMTC**](https://tdn.totvs.com/pages/viewpage.action?pageId=640889689) | **F460Cmc7Tc** | Mantém funcionalidade |
| [**FA460ROT**](https://tdn.totvs.com/x/zvFbDQ) | **MenuDef** | Mantém funcionalidade |
| [**F460LQOK**](https://tdn.totvs.com/x/f_ZbDQ) | **FA460LiqOk** | Mantém funcionalidade |
| [**F460STI**](https://tdn.totvs.com/x/tLGGHw) | **F460AIncl** | Permitirá a visualização ou bloqueio da tela de parâmetros para filtragem dos títulos a serem liquidados. |
| [**F460MNU**](https://tdn.totvs.com/x/OLKGHw) | **MenuDef** | Permitirá a inclusão de novos botões na rotina de Menudef dentro do FINA460A |
| [**F460FIL**](https://tdn.totvs.com/pages/viewpage.action?pageId=641149417) | **FINA460A** | Permitirá a inclusão de filtro personalizado para a apresentação da tela de títulos a serem liquidados e/ou simulação de liquidação. |
| [**F460PGE**](https://tdn.totvs.com/x/NBS2Hw) | **FINA460LOAD** | Permitir a manipulação das parcelas geradas. |

Atualização de dados dos clientes

Por padrão, o sistema trava o cadastro dos clientes envolvidos para atualizar algumas informações. Pode-se optar por **não fazer essa atualização dos dados do cliente** utilizando o ponto de entrada [F070TRAVA - Trava ou destrava os registros da tabela SA1](https://tdn.totvs.com/display/PROT/F070TRAVA+-+Trava+ou+destrava+os+registros+da+tabela+SA1), que também tem efeito na rotina Liquidação a receber (FINA460).

**Saiba Mais**

Acervo de pontos de entrada financeiro com modelos:

[Pontos de Entrada - Financeiro - P12](https://tdn.totvs.com/display/PROT/Pontos+de+Entrada+-+Financeiro+-+P12)  
[DT\_FINA460A\_Ponto\_Entrada\_Principal](https://tdn.totvs.com/display/PROT/DT_FINA460A_Ponto_Entrada_Principal)  
[FIN0040\_CREC\_Pontos\_de\_Entrada\_FINA460](https://tdn.totvs.com/display/PROT/FIN0040_CREC_Pontos_de_Entrada_FINA460)
