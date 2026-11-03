---
article_id: 6038704794519
category: Folha Mensal
content_hash: 1fcec062b80e6973e6c6679964ee81abe1ed3c577c5a506a8d5bb5669829c570
fetched_at: '2026-06-28T22:46:59.190470+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Mesclar Preenchimento entre números e letras no cadastro de
  código de seção
type: support-article
updated_at: '2025-03-12T20:01:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6038704794519-RH-RM-FOP-Mesclar-Preenchimento-entre-n%C3%BAmeros-e-letras-no-cadastro-de-c%C3%B3digo-de-se%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30602461848855) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como mesclar números e letras no cadastro do código de seção?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**A Máscara é uma sequência de dígitos que determinam como os dados deverão ser informados em campos pré-definidos nos Parâmetros do Sistema, como Código de Seção, Chapa, etc. Esta sequência consiste basicamente na definição do número de dígitos, bem como seus respectivos tipos, podendo ser letras, números e símbolos.  
  
A máscara é formada pelos seguintes caracteres:  
Símbolo - Significado  
  
**# - Para números****L - Para campo alfabético e de preenchimento obrigatório.****l - Para campo alfabético e de preenchimento facultativo.****A - Para campo alfanumérico e de preenchimento obrigatório.****a - Para campo alfanumérico e de preenchimento facultativo.****Q - Para qualquer caractere, menos os separadores ( : . , ; / )**Por exemplo, se a máscara de um código for L#.##, o código poderá ser: A1.01, sendo que se digitado a11, o sistema passará a letra **a**, minúsculo, para **A**, maiúsculo, e preencherá as outras casas com o número 0.  
  
Veja o exemplo abaixo de um cadastro no qual foi inserido números e letra de preenchimento obrigatório (L):

Acesse **Configurações | Parametrizador | Máscaras e Quebras**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30602478269207)  
  
No campo de Máscara código de seção, faça a alteração desejada:  
  
![](https://totvssuporte.zendesk.com/attachments/token/n6IrAcdBraMgcdBHBLComfMB2/?name=image.png)  
  
Ao realizar o cadastro de uma nova seção o sistema acatará conforme inserido nos parâmetros:  
  
![](https://totvssuporte.zendesk.com/attachments/token/fqDPHhrxaO8nBkDGRQG3vgA6j/?name=image.png)
