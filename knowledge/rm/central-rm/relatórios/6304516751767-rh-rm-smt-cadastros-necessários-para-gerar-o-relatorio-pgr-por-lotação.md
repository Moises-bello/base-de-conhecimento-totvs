---
article_id: 6304516751767
category: Relatórios
content_hash: dbc1c77dfed851e486aa6006b0d568f4ed9abfc6f01519b8a085a1b6db2833b3
fetched_at: '2026-06-28T22:47:43.414507+00:00'
product: rm
section_id: 1500000861522
source: central-rm
title: RH - RM - SMT - Cadastros necessários para gerar o relatorio PGR por lotação
type: support-article
updated_at: '2025-05-06T21:15:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6304516751767-RH-RM-SMT-Cadastros-necess%C3%A1rios-para-gerar-o-relatorio-PGR-por-lota%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16036169298199) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Quais os cadastros necessários para gerar o relatorio PGR por lotação?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional - **12.1.31** e **superiores.**  
  
**Solução**Siga os passos abaixo, referente aos cadastros que precisam ser realizados:

* Deve haver um avaliação de risco criada para a lotação desejada. Para realizar o cadastro acesse o meu **PPRA / PGR | Reconhecimento e avaliação de Risco**.    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/26816873855511)
* Deve ter um **Ambiente de trabalho**, cadastrado para **lotação**. Para realizar o cadastro acesse o menu **Cadastros** | **Ambiente de trabalho**:   
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/26816859097111)
* No cadastro do **Perigo**, a associação do ambiente associado deve ser por **lotação**. Para conferir acesse o menu **PPRA/PGR | Perigo** e clique na guia **Ambiente de Trabalho**:    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/26816873867543)

Para gerar o Relatorio PGR por lotação, valide os passos a seguir:

* Importe o relatorio disponível em nosso book, acessando **Gestão** | **TOTVS Compartilhamento:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26816873872151)**

Antes de baixar e importar a estrutura, avalie se estão utilizando o correspondente a base de dados que utilizam (SQL ou Oracle).

Segue documentação referente a como realizar o processo de importação:  [RH - RM - SMT - Importação de relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409650455703-TOTVS-RH-Linha-RM-SMT-Importa%C3%A7%C3%A3o-de-relat%C3%B3rios)

* É necessário ter cadastrado o Tipo Relatório PGR e ter gerado os Itens que irão conter o relatório:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26816873877399)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26816859119895)

* Caso tenha importado o relatório do nosso book, poderá gerar este itens uma única vez através do **Processo** | **Gerar modelo PGR**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26816859125911)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26816859131031)

* É necessário selecionar a **Seção e Função** que compõe a **Lotação** desejada na Identificação do Relatório:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26816859137559)

* Após isso, basta gerar o relatório na guia Gerar/Visualizar e depois clicar em Visualizar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26816873908887)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26816859148567)

**Saiba Mais:**Para maiores informações, acesse: [- Cadastros necessários para gerar o relatorio PGR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6298978683159-TOTVS-RH-Linha-RM-SMT-Cadastros-necess%C3%A1rios-para-gerar-o-relatorio-PGR)
