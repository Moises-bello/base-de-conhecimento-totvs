---
article_id: 35880226492183
category: Escrita Fiscal - Configurador de Tributos
content_hash: 518217017f84cd42fce620eecdbf6162e32be03536fd95292eee4968a5d0e54a
fetched_at: '2026-06-28T22:39:17.239468+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como configurar
  o cBenef operação isenta CST41 no fisa170?
type: support-article
updated_at: '2025-10-27T16:38:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35880226492183-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-cBenef-opera%C3%A7%C3%A3o-isenta-CST41-no-fisa170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35880201341847) Tempo aproximado para leitura: 00:10**min**  
  
**Dúvida**  
Como configurar o cBenef operação isenta CST41 no fisa170?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Segue abaixo um exemplo de configuração do cBenef para operação Isenta e pode ser usada para qualquer estado.

MV\_estado = SC

Cliente = SC

CFOP = 5927

CST = 41

Fisa170

ID tributo = ICMS

Perfil de Produtos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35880226480535)

Perfil de Operação

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35880201342231)

Perfil de Participantes

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35880201342359)

Perfil de Origem x Destino

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35880201342999)

Regra de Base de calculo

O:zero

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35880201343127)

Regra de Aliquota

O:zero

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35880226481047)

Regra de escrituração

Incidência = isento

CST = 41

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35880201344791)

Regra de Calculo Documentos Fiscais = ICMS  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35880201345687)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35880201346071)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35880201346583)

Para o código do cBenef precisa importar o código pela tabela 52 ou inserir de forma manual

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como importa a TABELA52 no Protheus para tratamento da tag cBenef](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047771974-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-importa-a-TABELA52-no-Protheus-para-tratamento-da-tag-cBenef)

Regra de Ajuste de Lançamento

SC800005

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35880226482455)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35880201347223)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35880201347351)

Base = zero

Aliquota = zero

Valor = coluna de isento

Pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35880226483607)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35880201348247)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35880226485143)
