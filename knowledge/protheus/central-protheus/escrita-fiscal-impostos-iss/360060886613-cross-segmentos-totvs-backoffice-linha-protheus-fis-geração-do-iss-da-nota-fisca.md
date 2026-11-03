---
article_id: 360060886613
category: Escrita Fiscal - Impostos - ISS
content_hash: 561e3bbbe3e30826fe9a8825b89fb8e548e82ed49694e6df18ff4ccd67894a9b
fetched_at: '2026-06-28T22:39:35.228627+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Geração do ISS da
  Nota Fiscal de Saída no Contas à Pagar '
type: support-article
updated_at: '2024-06-21T20:31:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060886613-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Gera%C3%A7%C3%A3o-do-ISS-da-Nota-Fiscal-de-Sa%C3%ADda-no-Contas-%C3%A0-Pagar
---

**Dúvida**Como eu faço para gerar o Imposto Sobre Serviço (ISS) no meu contas à pagar vindo do módulo faturamento?  
  
**Ambiente**Protheus – Faturamento – A partir da versão 11.80.  
  
**Solução:**

Para essa solução é importante estar ambientando a configuração padrão do ISS:

<https://tdn.totvs.com/pages/releaseview.action?pageId=6076798>

A geração do ISS no contas à pagar sendo responsável o prestador do serviço é importante deixar os campos no cliente (SA1) e pedido de venda (SC5) conforme abaixo:

A1\_RECISS = NÃO

C5\_RECISS = NÃO

Com isso o ISS será gerado na tabela SE2 e não na tabela SE1.

**Importante:**

O cálculo na Natureza (SED) deve estar configurado = Sim, como "Não" será gerado na rotina MATA954 (Apuração do ISS).

**ATENÇÃO:**

Além dos campos acima descritos, verificar o parâmetro **MV\_1DUPNAT** e seu conteúdo, pois existem dois cenários no seu preenchimento que podem afetar na criação do título do ISS no Contas a Pagar:

**MV\_1DUPNAT =** SC5->C5\_NATUREZ – O sistema irá validar as informações da Natureza preenchida no Pedido de venda;

**MV\_1DUPNAT =** SA1->A1\_NATUREZ – O sistema irá validar as informações preenchidas na Natureza atrelada ao cadastro do cliente.

Ex.: Caso o parâmetro MV\_1DUPNAT esteja preenchido como SA1->A1\_NATUREZ, ao incluir o Pedido do Venda o sistema irá puxar as informações do seguinte campo: ![](https://centraldeatendimento.totvs.com/hc/article_attachments/18059981297815)

Se a Natureza inclusa neste campo (A1\_NATUREZ) for diferente da Natureza informada ao incluir o Pedido de Venda, o sistema irá dar prioridade para a Natureza contida no cadastro do cliente, devido ao preenchimento do parâmetro MV\_1DUPNAT.

Ao alimentar o parâmetro com o termo **SC5->C5\_NATUREZ** o sistema irá validar a Natureza informada no Pedido de Venda, independente do que estiver constando no cadastro do cliente:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18059992512535)
