---
article_id: 35357410638231
category: Escrita Fiscal - Configurador de Tributos
content_hash: aa06c555a3c77823e3022aef9b224c207c515300bffb62a3390b2b5df29f1175
fetched_at: '2026-06-28T22:39:17.773069+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 - Como confirmar
  se os impostos estão sendo gerados pelo Configurador de Tributos ou TES?
type: support-article
updated_at: '2025-11-25T14:14:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35357410638231-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-confirmar-se-os-impostos-est%C3%A3o-sendo-gerados-pelo-Configurador-de-Tributos-ou-TES
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35357410589207) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Como confirmar se os impostos estão sendo gerados pelo Configurador de Tributos ou TES?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - A partir da versão 12.1.2210  
  
**Como verificar:**  
Para confirmar a origem do cálculo dos impostos:

1. Acesse o Pedido de Venda e visualize a **P****lanilha Financeira** da nota fiscal em casos de nota de saída, em caso de nota de entrada, acesse a **aba Impostos** no Documento de Entada.
2. Verifique os campos de **código** e **descrição** do imposto.

#### Interpretação:

* Se estiver exibindo o código **"ICM"** com a descrição **"ICMS"**, significa que o cálculo está sendo realizado pelo **legado (TES)**.
* Caso esteja exibindo outro código e descrição (ex: definidos no Configurador de Tributos), então o imposto está sendo calculado pelo **Configurador de Tributos**.

**1. Pedido de venda:**

**1.1** Calculo realizado pelo Configurador de Tributos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35357464489111)

**1.2** Calculo realizado pela TES:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35357410591255)

**2. Documento de entrada**

**2.1** Calculo realizado pelo Configurador de Tributos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35357954734487)

**2.2** Calculo realizado pela TES:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35357464491159)

### **Gravação nas tabelas**

A gravação das informações nas tabelas permanece inalterada. No entanto, quando a nota é calculada via **Configurador de Tributos**, é gerado um identificador de tributo (**IDTRIB**) nos seguintes campos:

| Tabela | Campo |
| --- | --- |
| SD1 | D1\_IDTRIB |
| SD2 | D2\_IDTRIB |
| SFT | FT\_IDTRIB |

As demais tabelas, como **SF3, SF1, SF2, SC5 e SC6**, **não armazenam** nenhuma informação de identificação relacionada ao IDTRIB.

**OBS**: Ao utilizar o **Configurador de Tributos**, ele **sempre será a primeira fonte** de definição do cálculo fiscal.  
Somente quando não ocorre enquadramento dos perfis de validação (Perfil de Produto, Perfil de Participante, Perfil de Operação, Perfil de Origem/Destino) com as informações da nota é que o sistema recorre aos cadastros tradicionais para calcular os impostos.

**Documentações relacionadas:**

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 - Como garantir o cálculo correto do tributo na nota fiscal utilizando a Regra de Cálculo no Configurador de Tributos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35041323516183-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-garantir-o-c%C3%A1lculo-correto-do-tributo-na-nota-fiscal-utilizando-a-Regra-de-C%C3%A1lculo-no-Configurador-de-Tributos)

[CFGTRIB - Cadastro de Perfis do Configurador de Tributos - Boas Práticas](https://tdn.totvs.com/pages/viewpage.action?pageId=825324831)

[CFGTRIB - Cadastro de Regras de Cálculo no Configurador de Tributos - Boas Práticas](https://tdn.totvs.com/pages/viewpage.action?pageId=887731155)
