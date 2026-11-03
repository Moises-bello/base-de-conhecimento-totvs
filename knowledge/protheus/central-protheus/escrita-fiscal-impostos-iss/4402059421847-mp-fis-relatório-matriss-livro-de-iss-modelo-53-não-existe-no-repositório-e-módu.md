---
article_id: 4402059421847
category: Escrita Fiscal - Impostos - ISS
content_hash: 3cd1650f99229897f440e71acb1fe528cc6a257e424c37f3969201d22a5a20d0
fetched_at: '2026-06-28T22:39:35.301557+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: MP - FIS - Relatório MATRISS (Livro de ISS Modelo 53) Não Existe no Repositório
  e Módulo 09 - Livros Fiscais
type: support-article
updated_at: '2021-06-03T19:42:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402059421847-MP-FIS-Relat%C3%B3rio-MATRISS-Livro-de-ISS-Modelo-53-N%C3%A3o-Existe-no-Reposit%C3%B3rio-e-M%C3%B3dulo-09-Livros-Fiscais
---

**Dúvida**  
Não foi possível identificar o relatório MATRISS (Livros ISS Modelo 53) pois não esta compilado no repositório e módulo Livros Fiscais.  
  
**Ambiente**

Microsiga Protheus - Livros Fiscais – A partir da versão 12

**Solução**  
O fonte MATRISS é um RDMAKE e, na versão 12 não será incluído no RPO, dessa forma, será necessário realizar a compilação do fonte que está disponível no Portal do Cliente, através da Central de Downloads.   
  
Para baixar realize a pesquisa abaixo:  
  
Busca por: RDMAKE  
Linha: Protheus  
Versão: Microsiga Protheus 12.1.\*\*\*\*  
Baixar pacote: 21-05-14-RDMAKES\_PADRAO.ZIP  
RDMAKES PADRAO COMPATIVEL DA RELEASE 12.1.23 ATE 12.1.27  
  
O link abaixo possui os RDMAKEs padrões a partir de 14/05/2021   
Na pasta Livros Fiscais contem o RDMAKE MATRISS.PRX para que possa baixar e compilar no repositório:   
  
<https://suporte.totvs.com/portal/p/10098/download?e=947505>  
  
Poderá fazer download e **compilação**normalmente, por ser livre para customizações precisará adicionar a um projeto e compilar no RPO.
