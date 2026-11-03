---
article_id: 360045235754
category: MDT - EPI
content_hash: 69b3a1c958eaddcefb25b5a93b874af1dc48d0f1e1a157c27227ac7ec4e8d670
fetched_at: '2026-06-28T22:44:25.371123+00:00'
product: protheus
section_id: 360010945554
source: central-protheus
title: RH - Linha Protheus - MDT - Como realizar a Impressão do recibo de devolução
  do Equipamento de Proteção Individual (EPI)
type: support-article
updated_at: '2024-02-26T10:42:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045235754-RH-Linha-Protheus-MDT-Como-realizar-a-Impress%C3%A3o-do-recibo-de-devolu%C3%A7%C3%A3o-do-Equipamento-de-Prote%C3%A7%C3%A3o-Individual-EPI
---

**Dúvida**Como realizar a Impressão do recibo de devolução do Equipamento de Proteção Individual (EPI)?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
 **Solução**Esta ocorrência está relacionada a ativação de um parâmetro, e a configuração necessária no cadastro do fornecedor x epi. **1º** Acesse o configurador no caminho : **Ambiente > Cadastro > Parâmetros**  
Localize o parâmetro  **MV\_NG2RECI**, ajuste seu conteúdo para 1.  
  
**2º** Na sequencia acesse o módulo Medicina e Segurança do Trabalho ( 35) no caminho:  
**Atualizações > Epi > Fornecedor x Epi** rotina (MDTA630)Certifique-se que o campo **Indica Devolução** ( TN3\_INDEVO)  esta com seu conteúdo = SIM  
Imagem do campo em destaque abaixo.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21576989023127)

É importante avaliar na rotina Epi x Funcionário rotina ( MDTA695) no caminho:   
**Atualizações > Epi > Epi x Funcionário** Localize a matricula em questão  e clique em EPI  
Observe o campo **DATA EMISSÃO**( TNF\_DTRECI), sem essa informação o sistema realmente não irá imprimir o recibo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21576942090135)

Oriento a executar a rotina emissão do recibo de epis já entregues para preenchimento automático, acessando no caminho:  
**Relatório > EPI > Recibo de Entrega Epi** rotina ( MDTR805)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21576989043095)  
  
Após executadas estas ações em uma devolução de EPI o sistema emitirá seu recibo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21576942090135)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062872354)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21576942099095)  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
