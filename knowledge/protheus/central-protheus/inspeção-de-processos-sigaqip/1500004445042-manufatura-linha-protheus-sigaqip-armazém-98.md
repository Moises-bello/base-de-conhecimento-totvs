---
article_id: 1500004445042
category: Inspeção de Processos (SIGAQIP)
content_hash: 57ce45f727e9fb04839098aaa165e96f372444e697a0eacaff71dfd4f4aa0220
fetched_at: '2026-06-28T22:42:25.656823+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Armazém 98
type: support-article
updated_at: '2021-10-01T13:06:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004445042-Manufatura-Linha-Protheus-SIGAQIP-Armaz%C3%A9m-98
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:45 min**  
 **Dúvida**Para qual armazém é enviado o produto que possui integração com o **SIGAQIP - Inspeção de Processos**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Solução**O conceito padrão da integração entre os módulos **SIGAPCP - Planejamento e Controle da Produção** e **SIGAQIP** é que o produto sempre será gerado para o armazém **98**.  
Para que o produto seja enviado para um armazém diferente é possível utilizar o **PE - Ponto de Entrada MT680QUA**. Além disso, também é possível manipular a inclusão desta informação na tabela **SD3 - Movimentações Internas**, por meio da utilização do **PE MT680GD3**, inclusive o armazém destino.  
  
**Saiba mais**  
Para informações referente o **PE MT680QUA**, acesse o *link* [MT680QUA - Critica de envio de material ao Quality](http://tdn.totvs.com/display/public/PROT/MT680QUA+-+Critica+de+envio+de+material+ao+Quality).  
E referente ao **PE MT680GD3**, acesse o *link* [MT680GD3 - Validação do Retorno](http://tdn.totvs.com/pages/releaseview.action?pageId=330837203).
