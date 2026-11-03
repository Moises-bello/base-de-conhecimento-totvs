---
article_id: 4407445890967
category: Materiais - Compras (SIGACOM)
content_hash: 4e12a447faccc2d1f4b78ded35b4242624466f23ee8fd413497f0c26b32f3102
fetched_at: '2026-06-28T22:41:18.777005+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help " AJUDA: A100VALOR
  ao utilizar a opção Retornar do Documento de Entrada'
type: support-article
updated_at: '2021-08-30T19:50:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407445890967-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-AJUDA-A100VALOR-ao-utilizar-a-op%C3%A7%C3%A3o-Retornar-do-Documento-de-Entrada
---

**Ocorrência**Ao utilizar a opção Retornar do Documento de Entrada, ocorre o Help "AJUDA: A100VALOR Valor unitário deste produto não pode ser alterado, pois este produto pertence a poder de terceiros, onde o valor unitário deve ser o mesmo da nota fiscal de remessa."  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões.  
  
**Causa**

Há duas possíveis causas para esse HELP:

1) O incidente pode ocorrer devido a quantidade de casas decimais terem sido alteradas no módulo de faturamento e não terem sido alteradas no módulo de compras, fazendo com o valor unitário fique diferente no retorno do documento de entrada.

2) O parâmetro **MV\_BLOQSB6** estar com conteúdo .T.

**Solução**Para correção desse help na opção retornar por gentileza, verificar:

**1)** Verifique se os campos de **quantidade** e **valor** das tabelas **SC6**, **SD1** e **SB6** estão com a quantidade de **decimais iguais**, conforme a documentação: **[FAT0068\_Aumento\_de\_Casas\_Decimais\_no\_ambiente\_Faturamento\_SIGAFAT](https://tdn.totvs.com/x/twEmDg)**

Todos os campos de **quantidade** devem ficar **iguais entre eles**, assim como todos os campos de **valor** também devem ter o **mesmo tamanho e decimais** entre eles.

**2)** Verificar o parâmetro ***MV\_BLOQSB6*:**

***MV\_BLOQSB6***: A finalidade desse parâmetro é impedir que seja informado um valor unitário diferente do valor unitário do campo ***B6\_PRUNIT***.  
Alterando para .F. o sistema irá permitir o retorno da nota fiscal.

Para maiores informações sobre **Devolução de Terceiros**: **[FAT0057\_Emissão\_de\_Nota\_de\_Devolução\_de\_Terceiros\_Retorno](https://tdn.totvs.com/x/nKkXDg)**

***Saiba Mais :***

[FAT0068\_Aumento\_de\_Casas\_Decimais\_no\_ambiente\_Faturamento\_SIGAFAT](https://tdn.totvs.com/x/twEmDg)

[FAT0057\_Emissão\_de\_Nota\_de\_Devolução\_de\_Terceiros\_Retorno](https://tdn.totvs.com/x/nKkXDg)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
