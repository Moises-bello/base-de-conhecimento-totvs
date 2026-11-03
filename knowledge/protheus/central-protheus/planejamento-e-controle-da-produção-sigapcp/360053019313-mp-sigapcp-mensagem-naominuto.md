---
article_id: 360053019313
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 8757c34889dbdb2a5a96c6afbfaa72966adeb66547b7c7ac6df99ac248a04c31
fetched_at: '2026-06-28T22:42:47.277978+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: MP - SIGAPCP - Mensagem NAOMINUTO
type: support-article
updated_at: '2020-08-19T14:06:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053019313-MP-SIGAPCP-Mensagem-NAOMINUTO
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:01 min**  
 **Ocorrência**Ao tentar incluir um componente **MOD - Mão de Obra** no **MATA200 - Estrutura** o Sistema apresenta a mensagem **NAOMINUTO**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084352534/mceclip0.png)

**Ambiente**Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
   
 **Causa**A mensagem ocorre porque parâmetro **MV\_TPHR - Define a unidade padrao para tempos utilizados pelo sistema de PCP e ESTOQUE. O tipo de hora pode ser N -> Normal ou C -> Centesimal**está definido como **N** e da quantidade informada na estrutura é maior que **0,5999**.  
   
 **Solução**Para que a mensagem não seja apresentada é necessário alterar o parâmetro **MV\_TPHR** para **C** ou informar a quantidade de minutos compatível com o tipo de hora utilizado.  
  
**Saiba mais**  
Para mais informações de como cadastrar **MOD** na estrutura acesse o documento: [MP - SIGAPCP - Como registrar a quantidade do MOD na estrutura do produto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024715313)
