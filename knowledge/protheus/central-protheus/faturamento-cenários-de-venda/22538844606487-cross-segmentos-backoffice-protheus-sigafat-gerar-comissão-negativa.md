---
article_id: 22538844606487
category: Faturamento - Cenários de Venda
content_hash: d0f82c6f7365e3286f1b4c6e66f9a1f44005a5db56ca97dcad5363e0a364adb1
fetched_at: '2026-06-28T22:38:34.015174+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Gerar comissão negativa
type: support-article
updated_at: '2026-03-26T17:20:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22538844606487-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Gerar-comiss%C3%A3o-negativa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22538813305239) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como gerar comissão negativa ao devolver uma venda?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Quando realizada uma venda, porém, o cliente devolve a nota, é possível gerar uma comissão negativa (tabela SE3) do mesmo valor para abater (zerar) a comissão gerada pela venda.

Para isso, basta habilitar o parâmetro **(MV\_COMIDEV = T)**, ao realizar a devolução de uma nota fiscal de venda, o sistema irá inserir um registro de Comissão Negativa para o vendedor na tabela de comissões (SE3).

Para geração da Comissão Negativa é necessário que os campos **E1\_VEND**(x) e **E1\_COMIS**(x) do título a receber estejam preenchidos (título a receber gerado pelo momento do faturamento da venda).

|  |
| --- |
| Assista ao vídeo explicativo para entender o fluxo de cadastro e comissão:  [How To | MP - SIGAFAT - Configuração de vendedor para comissões](https://www.youtube.com/watch?v=hxKM-ESpAKI) |

**Saiba mais:**

[FAT0052 Configuração das Comissões dos Vendedores](https://tdn.totvs.com/x/efIKDg)
