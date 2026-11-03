---
article_id: 360050555314
category: Financeiro - Contas a Pagar
content_hash: 3d0633141aa0a184123817fc767ea9ab0bfe0df859cdf9f7e1c606833765638e
fetched_at: '2026-06-28T22:38:08.224376+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA050 – Alterar valor
  Desdobramento
type: support-article
updated_at: '2023-08-04T17:30:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050555314-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Alterar-valor-Desdobramento
---

**Dúvida**Como alterar valor de um título com desdobramento?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12.1.17  
  
**Solução**Quando gerado o desdobramento de um título, o sistema gera um título com o valor Total (totalizador) já baixado e gera as parcelas (títulos desdobrados) em aberto, para que seja possível o rastreamento ao realizar o cancelamento do desdobramento.

O parâmetro **MV\_BLVLDES**, verificar se é permitido alterar o valor de parcelas de desdobramento.

* Se configurado como “.T.” (*true*– verdadeiro):

Bloqueia a alteração do campo valor das parcelas de desdobramento quando houver controle de rastreio (*Default*)

* Se configurado como “.F.” (*false*– Falso):

Permite que o valor das parcelas de desdobramento, sejam alteradas mesmo quando houver o controle de rastreio.

**Importante:**  
Caso não exista o parâmetro

Ir ate o **Configurador**, criar o parâmetro com a informações acima.

**Cadastros**>**Parâmetros**>  
![imagem1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078698113/imagem1.png)

Clicar em **Novo**

![imagem2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078698133/imagem2.png)

Preencha os dados.  
  
![imagem3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077554914/imagem3.png)  
  
![imagem4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077554934/imagem4.png)  
  
![imagem5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078698173/imagem5.png)

Clicar em **Salvar**.

**Procedimento:**

Caso todas as parcelas estejam em aberto:1 - Acesse a rotina **Contas a Pagar (FINA050)**;  
2 - Selecione o título original que deseja alterar o valor o desdobramento;  
3 - Clique em **Alterar** e selecione **altere o campo valor.**
