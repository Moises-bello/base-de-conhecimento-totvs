---
article_id: 8578656085143
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 00546aef2b93e99053e995fbd21f5af5a8aa58e5c22315f44583e46217d6fa59
fetched_at: '2026-06-28T22:42:00.871327+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS -   Arq. Magnéticos - Como gerar
  o registro E316 no Sped Fiscal?
type: support-article
updated_at: '2022-09-01T17:21:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8578656085143-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-registro-E316-no-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min**  
 **Dúvida**Como gerar o registro **E316** no **Sped Fiscal**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução**

É possível gerar o registro **E316** de duas formas a depender da situação do estado destinatário quanto à **Inscrição Estadual (IE).**

**1. Quando o contribuinte NÃO possui Inscrição Estadual (IE) no estado de destino:**

Neste cenário, o registro **E316** é gerado com base no documento fiscal. Assim, a nota fiscal de saída deve ter o cálculo do **Difal Origem e Destino**, pois é com estas informações que o sistema monta os registros  **C101** e o **E300** e Filhos.  
  
- Ao preparar o documento de saída, as perguntas abaixo devem estar como **SIM**. Dessa forma, a guia de recolhimento será gerada após o faturamento do pedido de vendas.

**Gera Guia ICM Compl. UF Dest.?**=SIM  
**Gera Guia FECP da UF Destino?**=SIM

- Através do caminho **Livros Fiscais -> NF Manual de Saída - Complementos -> Guias de Recolhimento**, realize o **Complemento (Tabela CDC)** da guia gerada com a Nota de Saída.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8579651832983/mceclip3.png)

**Importante:**

Para os casos em que no momento da preparação do documento fiscal a guia de recolhimento não tiver sido gerada siga os seguintes passos:

- Emita o relatório **FISR087-Listagem\_Doc\_fiscal\_com\_cálculo\_do\_DIFAL/FECP\_EC 87/15** com as informações de NF, Cliente, estado entre outros.

- Gere, manualmente, a **Guia do DIFAL** através da rotina **MATA960- Guia Nacional de Recolhimento ( Tabela SF6)**

- Através do caminho **Livros Fiscais -> NF Manual de Saída - Complementos -> Guias de Recolhimento**, realize o **Complemento (Tabela CDC)** da guia gerada com a Nota de Saída.

**2. Quando o contribuinte POSSUI Inscrição Estadual (IE) no estado de destino:**

Nesse caso, o registro é gerado com base na apuração do ICMS (MATA953) configurando as perguntas na *wizard* de geração conforme abaixo:

**Apuração= Mensal**  
**Período= 1º**  
**Gera Guia de Recolhimento= Sim**  
**Exclui GNR= Sim**

Para ambos os cenários, ao gerar o **Sped Fiscal**, deixe a Pergunta abaixo como **SIM**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8579509779223/mceclip0.png)
