---
article_id: 18450152498839
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 130e8c3305e3d20a4a17cff602385fd86afa5cdbb447e26cda2b86a561f78ab9
fetched_at: '2026-06-28T22:39:08.115311+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como configurar e
  cadastrar Opcionais?
type: support-article
updated_at: '2023-10-23T19:29:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18450152498839-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-configurar-e-cadastrar-Opcionais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18450172791831) Tempo aproximado para leitura: **00:05:30 min****Dúvida**

Como configurar e cadastrar Opcionais?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

A utilização de **Grupo de Opcionais** tem a finalidade de otimizar o processo de cadastramento, produção e estoque, permitindo a montagem de estruturas dinâmicas para produtos com opcionais.

Para ilustrar o funcionamento desta opção, vamos utilizar como exemplo uma cadeira de madeira que pode ser fabricada em quatro cores diferentes: **Preto, Azul Amarelo e Vermelho**.

Apesar das quatro cores possíveis o produto fabricado é um só: **Cadeira**, portanto só haverá um código de Produto Acabado e o Sistema atualiza o estoque desse produto independente da cor. Assim, se uma **OP - Ordem de Produção** para fabricar 20 cadeiras vermelhas é executada o Sistema atualiza o estoque de **Cadeiras** que é o Produto Acabado, somando as 20 unidades produzidas ao estoque existente. Não haverá distinção de cor ou estoques separados.

Por isso, recomenda-se que este recurso seja utilizado para venda sob encomenda, já que o produto final sempre tem o código igual.

Ao abrir uma **OP** ou um **Pedido de Venda**, é solicitado ao usuário que selecione qual dos opcionais cadastrados para o produto será considerado pelo Sistema.

Se o usuário não escolher nenhum opcional, será utilizado o opcional padrão que foi selecionado no **MATA010** > **Outras Ações** >**Opcional default**, essa informação também fica gravada no campo**B1\_OPC -****Opcional Default** no **MATA010 - Cadastro do Produtos**.

**Veja abaixo um passo a passo de exemplo:**

**- 1 -** Acessar a rotina ***Opcionais (MATA256)*** para criação do cadastro dos Opcionais desejados, no exemplo abaixo, utilizamos uma Lista de Cores;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18450479203607)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18451879780119)

**- 2 -** Na rotina ***Cadastro de Produtos** **(MATA010)*** criar 01 Produto Acabado (PA) e 01 Produto Matéria Prima (MP);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18451980001047)

**- 3 -** Na rotina ***Cadastro de Estrutura******s** **(PCPA200),*** criar a estrutura e no componente que utilizará os Opcionais, **repetir o componente** e informar o **item opcional desejado linha a linha**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18451805159703)

**- 4 -** Após as configurações acima, ao incluir um **Pedido de Vendas** ou **Ordem de Produção** para o Produto Acabado (PA) é exibido a tela de Opcionais Disponíveis para seleção, veja os prints de exemplo abaixo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18452472074135)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18452436839447)

**- 5 -** No cadastro de produtos (MATA010) definir o **Opcional Default (B1\_OPC)**, veja os passos abaixo com um exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18504640056087)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18504823390999)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18504823397655)

***Saiba Mais:***

*[Clique aqui e veja mais artigos sobre CADASTROS E CONFIGURAÇÕES GERAIS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*

[*Manufatura - Linha Protheus - SIGAPCP - Conceito de opcionais e como cadastrar*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413439228695-Manufatura-Linha-Protheus-SIGAPCP-Conceito-de-opcionais-e-como-cadastrar)
