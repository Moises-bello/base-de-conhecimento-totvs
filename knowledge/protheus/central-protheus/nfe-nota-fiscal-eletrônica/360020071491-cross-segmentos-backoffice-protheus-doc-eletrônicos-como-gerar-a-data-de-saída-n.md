---
article_id: 360020071491
category: NFe - Nota Fiscal Eletrônica
content_hash: 91cab4c21aadd1d76dd0466a57328eeb19fde2b06862466b631ac1cf85c09794
fetched_at: '2026-06-28T22:40:05.700541+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar a data
  de saída no DANFE TAGS dhEmi e dhSaiEnt
type: support-article
updated_at: '2025-07-03T13:15:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020071491-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-data-de-sa%C3%ADda-no-DANFE-TAGS-dhEmi-e-dhSaiEnt
---

**Dúvida**Como gerar a data de saída no DANFE TAGS dhEmi e dhSaiEnt ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**Atualmente o DANFE** mostra a informação da data de entrada/saída, pois o XML busca a data do campo F2\_EMISSAO.  
  
Existe um **parâmetro** onde você pode **deixar a data** de saída da mercadoria **em branco.**  
  
**MV\_DSAIENT**  
Descrição: Define se a data de entrada e saída da NF-e não será gerada.  
**.T.** = Não será gerada  
**.F.** = Será gerada

**Para sair uma data de saída diferente da emissão** temos**três opções de processos** a ser seguido:  
  
1- Esses casos devem ser customizados o **NFESEFAZ,** para indicar o campo **C6\_ENTREG** (ou outro campo criado manualmente na SC5 Cabeçalho do Pedido) para ser levado para a Tag <dSaiEnt>  
  
[RDMAKE](https://suporte.totvs.com/portal/p/10098/download#detail/1152113)  
  
**Rdmake disponível no link acima.**  
  
2- Segunda opção pode ser aberto melhoria na Central Colaborativa:  
  
[***Central Colaborativa TOTVS.***](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br)  
**Para saber como criar uma sugestão de melhoria clique [*AQUI.*](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics)**  
  
  
3- Para que seja atendido no padrão é necessário que a empresa tenha alguma legislação na qual informe a obrigatoriedade de gerar conforme deseja.  
  
Havendo a legislação abra um ticket no suporte e nos encaminhe que será compartilhado junto a consultoria tributária da TOTVS e posteriormente ao produto.

* **Saiba mais:**

Apenas para UF de Minas Gerais existe a transmissão de registro de saída.

Conforme o anexo abaixo:
