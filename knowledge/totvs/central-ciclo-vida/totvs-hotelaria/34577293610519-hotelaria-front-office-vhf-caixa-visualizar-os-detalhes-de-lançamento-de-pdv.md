---
article_id: 34577293610519
category: TOTVS Hotelaria
content_hash: b5bc447d3ff1fa38b929ab021146ebc2f4749e1dd38c4c427452c464069b9913
fetched_at: '2026-06-28T22:49:46.367339+00:00'
product: totvs
section_id: 1500000065542
source: central-ciclo-vida
title: Hotelaria - Front Office - VHF - Caixa - Visualizar os detalhes de lançamento
  de PDV
type: support-article
updated_at: '2025-08-30T22:39:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34577293610519-Hotelaria-Front-Office-VHF-Caixa-Visualizar-os-detalhes-de-lan%C3%A7amento-de-PDV
---

**Dúvida**  
Ao selecionar um lançamento de PDV, e clicar no botão '**Detalhes do lanç.**', o sistema apresenta uma tela sem os itens que compõem o lançamento. Como configurar para que seja apresentado?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34577293605143)

**Ambiente**  
Hotelaria - Front Office - VHF - Caixa

**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
1. No VHF o Tipo D/C correspondente ao PDV lançado, precisa estar marcado como 'PDV de A&B' e 'Lança no PDV';

Menu Cadastros > Caixa > Tipo de Débito/Crédito > Tipos de Débito/Crédito  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34577293605783)

2. No PDV Config os produtos que compõem o lançamento precisam estar associados ao PDV em questão;  
Menu Cadastros > Pontos de Venda / Associa Item a PDV

3. No PDV Config os produtos que compõem o lançamento do PDV precisam ter os campos 'Imposto' e 'Registrador Fiscal' preenchidos.

Menu Cadastros > Produtos > Itens de PDV  
Localizar o produto em questão  
Ir na guia Registrador Fiscal  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34577325259159)

Após estas ações, reinicie o VHF para que o sistema reconheça as alteações aplicadas, e repita a operação no Caixa para visualização dos Detalhes do lançamento.
