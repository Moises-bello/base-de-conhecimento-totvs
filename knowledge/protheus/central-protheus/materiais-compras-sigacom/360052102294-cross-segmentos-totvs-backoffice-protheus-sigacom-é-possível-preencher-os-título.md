---
article_id: 360052102294
category: Materiais - Compras (SIGACOM)
content_hash: 9860bd91454cf305f46cd424bb61637ec9f1881b17c947f6f7116436d246ef84
fetched_at: '2026-06-28T22:41:17.554581+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - É possível preencher
  os títulos de imposto (SE2) com base na natureza de rateio da tabela SEV e SEZ com
  múltiplas naturezas ?
type: support-article
updated_at: '2025-09-26T19:00:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052102294-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-%C3%89-poss%C3%ADvel-preencher-os-t%C3%ADtulos-de-imposto-SE2-com-base-na-natureza-de-rateio-da-tabela-SEV-e-SEZ-com-m%C3%BAltiplas-naturezas
---

**Dúvida**

É possível preencher os títulos de imposto (SE2) com base na natureza de rateio da tabela SEV e SEZ com múltiplas naturezas ?  
  
**Ambiente**

Protheus – Compras – A partir da versão 12  
  
**Solução**

Título TX a partir do Documento de Entrada Múltipla Natureza de rateio da tabela SEV e SEZ

O rateio do título de contas a pagar em múltiplas naturezas (gerado via Documento de Entrada) respeita explicitamente as perguntas das rotinas MATA103 (Documento de Entrada) e FINA050 (Contas a Pagar) a partir do F12:

* Rateia Valor?
* Gera Rateio?

**![](https://totvssuporte.zendesk.com/attachments/token/Psspj7zPkHSWw19dMPBhJKY0u/?name=inline1939433334.png)​  
  
![](https://totvssuporte.zendesk.com/attachments/token/mX8GqPKeWT5wvlg5lgEDjAaQl/?name=inline1639966169.png)​**

Com os perguntes configurados o rateio multi-natureza será também sobre os impostos do título, ou seja, os valores dos mesmos serão gravados nas tabelas SEV e SEZ com a natureza respectiva ao RATEIO (e não as naturezas dos títulos do tipo TX's caso existam), é desta forma a regra do rateio de impostos.  
  
Em **NENHUM** cenário, os títulos de impostos (Tipo TX) serão gravados na SE2 com a natureza de rateio, sempre serão gravados com a natureza dos parâmetros (**MV\_IRF, MV\_PISNAT, MV\_COFINS e MV\_CSLL**), isto porque esse dado é utilizado em auxílio à identificação dos títulos de cada imposto federal, já que o Tipo é TX e os códigos de retenção não são obrigatórios e são apenas utilizados para classificação.  
  
Dessa forma nas tabelas SEV e SEZ as naturezas preenchidas são as informações do rateio, essa guia é apresentada apenas após habilitar o parâmetro **MV\_MULNATP = .T.**

### **Exemplo 1 - Naturezas iguais**

* Natureza Duplicata - N001 (SE2)
* Natureza Rateio - N001 (SEV e SEZ)

SIGACOM > Movimentos > Documento de Entrada (**MATA103**) **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084904573)​  
  
SE2   
![](https://totvssuporte.zendesk.com/attachments/token/upZeXr8jWccIw5tHh7Rt4tlqW/?name=inline-283988451.png)​  
  
SEV  
![](https://totvssuporte.zendesk.com/attachments/token/SDamLbIwVjB5fH5UBuirIwy5p/?name=inline-232308810.png)​  
  
SEZ  
![](https://totvssuporte.zendesk.com/attachments/token/ElwzQRceIGc5vLicXly0gQ3ZI/?name=inline-436152532.png)​**

### **Exemplo 2 - Naturezas diferentes**

* Natureza Duplicata - N001 (SE2)
* Natureza Rateio - NATRRF (SEV e SEZ)

SIGACOM > Movimentos > Documento de Entrada (**MATA103**)

**![](https://totvssuporte.zendesk.com/attachments/token/zSO9KaWOE0NvGcQdN5R8IRfyH/?name=inline-1760200617.png)​**

**SE2   
![](https://totvssuporte.zendesk.com/attachments/token/VyaK284h6wfAZ6CLjOHBF6QTh/?name=inline-1795151465.png)​**

**SEV  
![](https://totvssuporte.zendesk.com/attachments/token/VlG4blOTUe9oqDHgK6R1zeA4E/?name=inline1624148816.png)**

**SEZ  
![](https://totvssuporte.zendesk.com/attachments/token/OeTYfhMEUVJw4HkEFGscAG2n4/?name=inline-1517854700.png)​**

\*Salientamos que as imagens acima são apenas exemplos de ilustração para facilitar a compreensão do processo.

Quando declaramos o **Rateio CC de "Outras Ações"**, o sistema grava essas informações na tabela **SDE**. Ele grava uma linha para cada item desse rateio, se houver 2 itens/linhas nesse rateio, serão gravados 2 registros na SDE.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20168145238295)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20168132358551)

Quando declaramos o **Rateio de Múltiplas Naturezas da aba "Duplicatas**", o sistema grava essas informações na tabela **SEV**. Ele grava uma linha para cada item desse rateio, se houver 3 itens/linhas nesse rateio, serão gravados 3 registros na SEV.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20168145261719)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20168145283607)

Quando declaramos o Rateio nas duas formas acima (**Rateio CC de "Outras Ações" E Rateio de Múltiplas Naturezas da aba "Duplicatas"**), o sistema grava essas informações na tabela **SEZ**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20168145289879)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
