---
article_id: 360011710632
category: Materiais - Compras (SIGACOM)
content_hash: 09699f9a66dea9c9284d89c09b9696245c927c91d680f265c29b6089b397983d
fetched_at: '2026-06-28T22:41:07.631702+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é importado o
  arquivo XML através do Totvs Colaboração ?
type: support-article
updated_at: '2024-06-13T19:54:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011710632-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-importado-o-arquivo-XML-atrav%C3%A9s-do-Totvs-Colabora%C3%A7%C3%A3o
---

**Dúvida**

Como importar arquivo XML através do Totvs Colaboração ?

**Ambiente**

Protheus – Compras – A partir da versão 12.1.17  
  
**Solução**

De forma superficial, através da sua pasta system do Protheus no seu ambiente, criar a pasta NEOGRID e dentro dessa pasta criar as pastas IN, LIDOS, OUT, SENT.

Configure os parâmetros MV\_TCNEW, MV\_NGOUT, MV\_NGINN e MV\_NGLIDOS no Configurador, especificando o caminho de cada pasta.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24165926705047)

O XML é recebimento pelo portal da Neogrid através da configuração do ClientNeoGrid, via portal da NeoGrid vai acessar o botão enviar ao ERP, dessa forma o XML é apresentado na pasta IN, quando o Schedule está rodando e funcionado ao mesmo tempo o XML é jogado para pasta LIDOS. Desta forma atualiza a tabela CKOCOL aonde os XML fica sendo apresentado e quando o campo CKO\_FLAG fica com o status 2 o XML é importado corretamente no monitor do Protheus e fica armazenado para visualização na rotina COMXCOL.

***Saiba Mais :***

[TC06 - Erros (Códigos)](https://tdn.totvs.com/pages/viewpage.action?pageId=271663193)

[TOTVS Colaboração - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/releaseview.action?pageId=271661626)

[Importador XML - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/viewpage.action?pageId=485858148)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
