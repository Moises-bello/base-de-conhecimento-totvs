---
article_id: 30647143361303
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 4dc30c99d8fa8cf8b06f04a933eab3e827e81eac32f577cfaab028216c369f22
fetched_at: '2026-06-28T22:39:57.587355+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - NFE- Incluindo
  coluna no browser das rotinas
type: support-article
updated_at: '2025-05-21T19:48:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30647143361303-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-NFE-Incluindo-coluna-no-browser-das-rotinas
---

**Dúvida**  
Como incluir uma coluna personalizada no browser das rotinas SPEDNFE e/ou FISA022?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - Todas as versões   
  
**Solução** **1.** Para incluir uma coluna personalizada, dentro das rotinas, precisará acessar a engrenagem destacada e ir em 'Incluir Coluna':  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30647143351959)

**2.** Após isso, os campos abaixo deverão ser preenchidos conforme necessidade. Nesse exemplo, iremos incluir o nome do cliente do documento, ou seja, realizaremos um filtro no campo A1\_NOME e exibi-lo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30647143352343)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30647153710359)

**Título**Nome desejado da coluna que será apresentada, usamos 'Nome do Cliente' nesse exemplo. **Tipo**Utilizaremos a função POSICIONE, nativa do Protheus para posicionar e nos trazer o resultado do campo A1\_NOME.  
Documentação oficial: [clique aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=25165872) **Dados**//Retorna o valor do campo A1\_NOME com base na posição do alias SF2 e índice 1 do alias SA1  
Posicione("SA1", 1, xFilial("SA1") + SF2->F2\_CLIENTE + SF2->F2\_LOJA, **"A1\_NOME"**) **ID**Identificador de Preferência para a coluna, usamos 'NomeCli' neste exemplo.  
  
**3.** Por fim, poderá também ordenar as colunas:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30647413089303)  
  
Após configurações, a coluna criada e personalizada será devidamente apresentada:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30647413091479)
