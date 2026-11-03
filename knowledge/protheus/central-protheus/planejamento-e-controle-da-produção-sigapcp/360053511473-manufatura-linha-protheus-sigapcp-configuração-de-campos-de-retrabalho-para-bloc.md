---
article_id: 360053511473
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 4a99b985c34dd9436cd1f734d3b4f9f2b437d4e0e5f27ce3a2b40da473554bf4
fetched_at: '2026-06-28T22:42:42.099579+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Configuração de campos de retrabalho
  para Bloco K
type: support-article
updated_at: '2021-09-30T17:01:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053511473-Manufatura-Linha-Protheus-SIGAPCP-Configura%C3%A7%C3%A3o-de-campos-de-retrabalho-para-Bloco-K
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Como configurar o **Protheus** para trabalhar com **ordens de retrabalho**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**No processo do **Bloco K** foi criada uma forma padronizada de trabalho com **ordens de retrabalho**.   
No entanto, para que este processo possa ser utilizado é preciso parametrizar o **Protheus** para que o campo **VK\_PRDORI - Prod. Orig.** seja apresentado em tela no **MATA010 - Cadastro de Produtos**. Para esta configuração é necessário acessar o **SIGACFG - Configurador** e na manutenção de parâmetros adicionar a tabela **SVK - Complemento Produto PCP** no parâmetro **MV\_CADPROD - Determina os cadastros complementares que serão apresentados no cadastro de produto**.  
  
**Saiba mais**  
A documentação do processo de ordens de retrabalho pode ser encontrada em: [Manufatura - Linha Protheus - SIGAPCP - Processo de Retrabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409765801239)
