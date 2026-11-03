---
article_id: 360029047852
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 342923d1fc69fc2a399250775f6b57fcaa5a95cc48736dd1af826cefb2163800
fetched_at: '2026-06-28T22:42:44.721614+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Para que serve o Mapa de Divergências
type: support-article
updated_at: '2023-04-12T13:18:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029047852-Manufatura-Linha-Protheus-SIGAPCP-Para-que-serve-o-Mapa-de-Diverg%C3%AAncias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01****:30 min****Dúvida**Para que serve o **Mapa de Divergências**?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**No programa **MATA200 -  Estrutura** existe uma verificação de divergências entre a soma das quantidades dos componentes e a quantidade total do produto **pai.** A verificação é feita sempre que se confirma uma **Inclusão**, **Alteração** e/ou **Exclusão** no **MATA200**, e caso encontre algo irá exibir na tela um aviso sobre a **Divergência**.   
Este aviso contém uma lista com os produtos divergentes e a comparação da soma das quantidades obtidas pelo Sistema com a quantidade digitada.  
 Neste momento o usuário pode **corrigir a estrutura** ou **confirmar o processo**.   
Caso se confirme o processo o Sistema irá gerar **MAPA.DIV**, um arquivo formato **Texto ASCII** que armazena a lista de divergências, exatamente igual a que se vê na tela, para análise posterior.  
  
**Exemplo:**   
PA01 - Quantidade Base = 5KG  
|\_\_\_\_\_\_\_\_\_MP01 - Quantidade = 3KG  
|\_\_\_\_\_\_\_\_\_MP02 - Quantidade = 3KG  
  
O arquivo **MAPA.DIV** seria criado para avisar ao usuário que existe uma divergência entre as quantidades dos dois **MPs - Matérias Primas** somados **MP01,3KG + MP02,3KG = 6KG** é diferente da quantidade base do **PA01**, que é **5KG**.  
  
**Saiba mais**Para saber como ativar o **Mapa de Divergências** no **MATA200** acesse o artigo: [Manufatura - Linha Protheus - SIGAPCP - Mapa de divergências no cadastro de Estrutura](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028816832-MP-SIGAPCP-Mapa-de-diverg%C3%AAncias-no-cadastro-de-Estrutura)  
Para saber o funcionando do **Mapa de Divergências** no **PCPA200 - Estrutura (Nova Versão)** acesse o artigo: [Manufatura - Linha Protheus - SIGAPCP - Mapa de divergências no PCPA200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9448684298903)
