---
article_id: 30978972136855
category: Financeiro - Carta de Cobrança
content_hash: 99f301f8591e9a70abb5c72686f425695aea4aafe81c22a18301c513132ba2c2
fetched_at: '2026-06-28T22:37:28.977467+00:00'
product: protheus
section_id: 35058223754903
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA810 - Como criar
  um layout para a carta de cobrança?
type: support-article
updated_at: '2026-02-06T13:26:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30978972136855-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA810-Como-criar-um-layout-para-a-carta-de-cobran%C3%A7a
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30979005245335) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como criar um layout para a carta de cobrança?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Na configuração do layout da Carta de Cobrança (FINA810), tem a aba **"Dados dos Títulos", em que** é possível adicionar os campos do sistema que serão enviados na carta.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30979005245847)

Neste espaço, é possível incluir diversos campos da tabela **SE1**. Para selecioná-los, basta utilizar o duplo clique sobre o campo desejado e, em seguida, pressionar a seta para baixo para efetuar a inclusão de um novo campo.

Como exemplo, é possível adicionar o campo Número **do Título**, **Filial** e **Saldo**, conforme a necessidade.  
![FINA810.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/30979005246359)

Para que o texto do corpo do e-mail seja renderizado com as quebras de linha corretamente pela rotina **FINA810**, siga estas diretrizes de formatação no cadastro do texto:

1. **Intervalo Único:** Utilize apenas um intervalo de "Enter" (uma linha em branco) entre os parágrafos ou frases que deseja separar.
2. **Limpeza de Caracteres:** Certifique-se de que não existam **espaços em branco** ou tabulações ao final de cada linha de texto.

Conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38213972244631)

A seguir, um exemplo de como os campos configurados serão demonstrados no e-mail.

Olá Cliente

Por gentileza pague minha conta

Quebra de LINHA 1  
  
Quebra de Linha 2  
  
Quebra de Linha 3

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30978972118039)

Quebra De Linha 1  
  
Quebra de Linha 2  
  
Quebra de Linha 3

**Saiba mais**

[Carta de Cobrança](https://tdn.totvs.com/pages/releaseview.action?pageId=492706741)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Diferença entre envio da carta de cobrança FINA713 e FINA811](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17157968980247-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Diferen%C3%A7a-entre-envio-da-carta-de-cobran%C3%A7a-FINA713-e-FINA811?source=search)
