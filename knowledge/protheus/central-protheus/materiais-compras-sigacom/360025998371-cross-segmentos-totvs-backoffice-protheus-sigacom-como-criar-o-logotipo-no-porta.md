---
article_id: 360025998371
category: Materiais - Compras (SIGACOM)
content_hash: da10d6ab644e2fb8e77b8b671a3ca9a73ebbd7924b31252d567cc04909e8f87a
fetched_at: '2026-06-28T22:41:07.594385+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como criar o Logotipo
  no Portal Fornecedor ?
type: support-article
updated_at: '2024-02-23T12:16:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025998371-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-criar-o-Logotipo-no-Portal-Fornecedor
---

**Dúvida**Como criar o Logotipo no Portal Fornecedor ?  
  
**Ambiente**  
Microsiga Protheus – Compras– A partir da versão 12.  
  
  
**Solução**1 - Crie uma pasta dentro da pasta Web e coloque o arquivo TXT junto com o logotipo que deseja apresentar no portal do fornecedor.

Ex.:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21550864257047)

Conteúdo do documento de texto .TXT

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21550879522199)

<img src="\web\logo\logo.png" alt="logotipo" height="100" width="100">

2 - Informe o **caminho do arquivo txt** no parâmetro **MV\_PORTAL1.**

Ex.:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21550879534615)

3 - Informe o **caminho do arquivo do logo** no parâmetro **MV\_PORTAL2.**

Ex.:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21550879542295)

Ao acessar o portal do fornecedor o logo será exibido no tamanho de acordo com a configuração no TXT.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13401330733463)

***Observação 1***

Para garantir que o nome do arquivo está correto, clique nele com o botão direito -> "Propriedades" -> clique na aba "Detalhes". Dessa forma, é possível ver o nome do arquivo, seu caminho e seu tipo (.TXT, .PNG, ..).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21550864302231)

***Observação 2***

Nos parâmetros MV\_PORTAL1 e MV\_PORTAL2 informamos o caminho dos arquivos a partir da pasta Protheus\_data, pois ela é a raiz do diretório. Para garantir que no seu ambiente o caminho da raiz do diretório esteja correta, por gentileza, acesse seu appserver.ini e verifique o conteúdo da clausula "PATH" do [HTTP] e [WS]

***![](https://centraldeatendimento.totvs.com/hc/article_attachments/21550879567767)***

Dessa forma, o sistema vai pegar esse caminho e completar com o que foi informado nos parâmetros MV\_PORTAL1 e MV\_PORTAL2, conforme abaixo

***![](https://centraldeatendimento.totvs.com/hc/article_attachments/21550864328855)***

***Observação 3***

Valide também que no caminho do PATH não tenha uma barra / no final pois quando o sistema juntar com o caminho do parâmetro vão ter duas barras, por exemplo C:\TOTVS\protheus\_data**\**\web\logo\logo.txt

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
