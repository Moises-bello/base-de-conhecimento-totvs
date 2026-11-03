---
article_id: 40056748897943
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 939acf4cdf5f1fa6ac943cbf3b9a960561b40864f95c1705d426ad021f7e4dbd
fetched_at: '2026-06-28T22:42:44.588053+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Não gera Estrutura a partir da Pré-Estrutura
type: support-article
updated_at: '2026-04-28T20:38:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40056748897943-Manufatura-Linha-Protheus-SIGAPCP-N%C3%A3o-gera-Estrutura-a-partir-da-Pr%C3%A9-Estrutura
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40056732803607) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Porque não gera **estrutura** a partir da **pré-estrutura** cadastrada na rotina **PCPA135 - Pré-Estrutura?**  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**  
Ao criar a **estrutura** a partir da **pré estrutura**, são realizados cálculos e validações da mesma forma que se fosse aberta uma **OP - Ordem de Produção** da quantidade base do item pai, os componentes não são levados para a estrutura pois o resultado desse cálculo é zero.  
  
**Exemplo:**

Quantidade base do produto pai: 0,01  
   
Quantidade do componente na pré-estrutura: 0,0002  
   
0,01 \* 0,0002 = 0,000002  
   
Nesse exemplo seria necessário aumentar as casas decimais dos campos numéricos para 6, para que o componente seja levado para a estrutura.
