---
article_id: 360062175194
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 8ba3ff73ab25bdcdcb7577c74f9d882c0e9220624a8ebc8ce67418ed656f00d0
fetched_at: '2026-06-28T22:42:09.230783+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Ao importar
  o arquivo da DIF - TO ocorre o erro: A inscrição estadual não localizada no cadastro
  de contribuintes'
type: support-article
updated_at: '2022-08-17T19:44:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062175194-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Ao-importar-o-arquivo-da-DIF-TO-ocorre-o-erro-A-inscri%C3%A7%C3%A3o-estadual-n%C3%A3o-localizada-no-cadastro-de-contribuintes
---

**Dúvida**  
Ao importar o arquivo da DIF - TO ocorre o erro: A inscrição estadual não localizada no cadastro de contribuintes.  
  
**Ambiente**

Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Verificar se foi realizado o cadastro de contribuinte no validador da DIF-TO em Cadastro//Contribuintes

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003756802/mceclip0.png)

Caso esteja corretamente preenchida, se faz necessário verificar no cadastro de Filial no Configurador o campo M0\_INSC deve está preenchido sem hífen e sem espaçamento conforme imagem abaixo, assim será escriturado corretamente a inscrição no arquivo, de acordo com o layout da DIF TO o campo Inscrição Estadual deve conter apenas 9 caracteres.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003807501/mceclip1.png)

**Informações adicionais:**

DIF - Documento Eletrônico de Informações Fiscais - Tocantins

<https://tdn.totvs.com/pages/releaseview.action?pageId=192107354>

Leiaute arquivo texto DIF-TO versão 2021

<http://dif.sefaz.to.gov.br/DownLoad/LeiauteDIF2021.pdf>
