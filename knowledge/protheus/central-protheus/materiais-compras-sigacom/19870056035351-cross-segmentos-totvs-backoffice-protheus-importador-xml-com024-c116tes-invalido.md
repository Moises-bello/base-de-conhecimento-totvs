---
article_id: 19870056035351
category: Materiais - Compras (SIGACOM)
content_hash: d8f5f86be1ab70059cdf5623b12e19f0197b1343355ac0762415006f4bf1a191
fetched_at: '2026-06-28T22:41:12.871223+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - Importador XML - "COM024 - c116Tes
  := <--Invalido"
type: support-article
updated_at: '2024-06-11T17:36:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19870056035351-Cross-Segmentos-Totvs-Backoffice-Protheus-Importador-XML-COM024-c116Tes-Invalido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19870025450775) Tempo aproximado para leitura: **00:02min****Ocorrência**Após importar uma CTe está sendo gerado o codigo de erro COM024 - c116Tes := <--Invalido.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - versão 12  
  
**Causa**Parâmetro **MV\_XMLTECT** não configurado.  
  
**Solução**

Nesse caso, para solucionar a questão, é necessário configurar o parâmetro MV\_XMLTECT. Siga os passos abaixo:

Acesse a tela de parâmetros no sistema.

1 - Localize o parâmetro MV\_XMLTECT.Este parâmetro identifica o tipo de entrada a ser utilizado para a geração de documentos de transporte via Importador XML.

2 - Configure o parâmetro de acordo com as necessidades do processo, garantindo a correta identificação do tipo de entrada para a geração de documentos de transporte via Importador XML.

3 - Após realizar essa configuração, verifique se o problema persiste. Isso deve resolver a ocorrência relacionada à ausência de configuração do parâmetro MV\_XMLTECT.

Observação: Essa configuração é essencial para evitar a geração do código de erro COM024, permitindo a importação normal do CTe. Se necessário, é possível realizar a troca da TES durante o processo de classificação.

***Saiba Mais:***

* [Cross Segmentos - Totvs Backoffice Protheus - Totvs Colaboração / Importador XML - Como são definidos os produtos e o Tipo de Documento na importação do Documento de Frete / CTe ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027518891-Cross-Segmentos-Totvs-Backoffice-Protheus-Totvs-Colabora%C3%A7%C3%A3o-Importador-XML-Como-s%C3%A3o-definidos-os-produtos-e-o-Tipo-de-Documento-na-importa%C3%A7%C3%A3o-do-Documento-de-Frete-CTe-)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
