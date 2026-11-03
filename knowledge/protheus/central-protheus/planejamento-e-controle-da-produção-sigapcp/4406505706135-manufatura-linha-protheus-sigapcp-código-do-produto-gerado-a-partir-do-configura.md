---
article_id: 4406505706135
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: d1985cb905c7fde23d68b961e7bcd47278c4a4bad5f64b4029c0b94f9d06846e
fetched_at: '2026-06-28T22:42:41.051515+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Código do produto gerado a partir do
  configurador de produtos
type: support-article
updated_at: '2021-09-06T13:11:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406505706135-Manufatura-Linha-Protheus-SIGAPCP-C%C3%B3digo-do-produto-gerado-a-partir-do-configurador-de-produtos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:45 min****Dúvida**O código do produto gerado a partir do **MATA093 - Configurador de Produtos**, é uma concatenação do código da família e das opções selecionadas. É possível montar esse código de outra forma?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Sim, é possível. Para isso, siga os passos abaixo:  
1. No **MATA093**, em **BP\_CODPAD - Formação Padrão do Código**, preencha **Não**;  
2. No *browse* da rotina **MATA093**, clique em **Outras Ações** e depois em **Descrição**;  
3. Na parte superior da tela, através de uma expressão **ADVPL**, informe como o código deve ser composto, selecionado em **Variável** as características, a expressão deve conter todas as características da família.
