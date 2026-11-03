---
article_id: 360051318073
category: Configurações
content_hash: 8b8742a9fd0bd9e75232859d390895e0420d61c61930209f2f67fa30ccf540df
fetched_at: '2026-06-28T22:46:49.612865+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: RH - RM - FOP - Alteração da quantidade de eventos exibidos na visão
type: support-article
updated_at: '2021-11-25T14:47:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051318073-RH-RM-FOP-Altera%C3%A7%C3%A3o-da-quantidade-de-eventos-exibidos-na-vis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:30 min  
  
Dúvida**Como altero a quantidade de eventos exibidos na visão ao aplicar algum filtro que trará uma grande quantidade de cadastros?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Às vezes, precisamos alterar a quantidade máxima de cadastros exibidos na visão para melhorar o desempenho do sistema ou mostrar mais itens num só filtro. Para isso, realize os seguintes passos:  
1. Acesse**Serviços Globais | Serviços | Servidores de Aplicação**;  
2. Ao abrir esta tela, caso exista cadastro do server **FopEventoData,**edite o cadastro conforme passo 03. Caso não exista, crie um novo cadastro informando no campo ID do Server o server **FopEventoData**;  
3. No campo **Número máximo de registro**, informe o máximo de eventos desejados para serem visualizados na visão e salve:  
  
![](https://totvssuporte.zendesk.com/attachments/token/QtjCCiKeDv0Aqvz2S99hz9YRW/?name=inline1790516119.png)  
  
O número máximo de registros é o limite permitido que o sistema exibirá naquela visão quando o usuário utilizar, por exemplo, um filtro com o operador **IS NOT NULL**.
