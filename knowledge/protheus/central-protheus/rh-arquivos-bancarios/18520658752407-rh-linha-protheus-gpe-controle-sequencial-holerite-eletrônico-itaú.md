---
article_id: 18520658752407
category: RH - Arquivos Bancarios
content_hash: 1dbddbf225a8ac51ce9ef777b82cfe6f30f33a4a6efd9dba4cb35291f7335622
fetched_at: '2026-06-28T22:43:38.286445+00:00'
product: protheus
section_id: 360004833673
source: central-protheus
title: RH - Linha Protheus - GPE - Controle sequencial holerite eletrônico Itaú.
type: support-article
updated_at: '2025-09-19T22:40:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18520658752407-RH-Linha-Protheus-GPE-Controle-sequencial-holerite-eletr%C3%B4nico-Ita%C3%BA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18520649019543) Tempo aproximado para leitura: **01:00:00 min** **Dúvida**Controle sequencial holerite eletrônico Itaú.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A cada geração do arquivo no Protheus, o sistema altera o código do Lote de Serviço.  
  
A geração do holerite eletrônico Itaú é realizada de acordo com os segmentos D, E e F, onde as posições de 04 à 07 identificam o Lote de Pagamentos.  
Segue abaixo detalhamento da Nota 3 do layout:   
   
![](https://totvssuporte.zendesk.com/attachments/token/LFmK2sBJgGfL9IlOJW9x9t2aX/?name=image.png)  
Com isto, não há especificação que todos os arquivos devem conter o mesmo código de lote de serviço "0001", mas todas as posições de 04 à 07 do arquivo devem conter o mesmo código.  
   
Caso seja necessário alterar o código de lote, no Protheus há o parâmetro MV\_SEQITU, onde é possível indicar à partir de qual numeração deve seguir o código do lote no arquivo de holerite eletrônico.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18548183179543)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18548183197591)

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Holerite Eletrônico Itaú](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12048617037975-RH-Linha-Protheus-GPE-Holerite-Eletr%C3%B4nico-Ita%C3%BA)
