---
article_id: 360017800931
category: NFe - Nota Fiscal Eletrônica
content_hash: d617fdab560b08a47268088e321db395aa949a269dc38924e85b7eb54e4d4693
fetched_at: '2026-06-28T22:40:03.903272+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 328 Rejeição :
  CFOP de devolução de mercadoria para NFe que não tem finalidade de devolução de
  mercadoria'
type: support-article
updated_at: '2025-10-22T23:45:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017800931-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-328-Rejei%C3%A7%C3%A3o-CFOP-de-devolu%C3%A7%C3%A3o-de-mercadoria-para-NFe-que-n%C3%A3o-tem-finalidade-de-devolu%C3%A7%C3%A3o-de-mercadoria
---

**Dúvida**Como corrigir 328 Rejeição : CFOP de devolução de mercadoria para NFe que não tem finalidade de devolução de mercadoria ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.27

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A **nota de origem precisa existir no sistema, a nota precisa ser referenciada corretamente  e o CFOP** da nota **não pode estar** no parâmetro.

Quando o **CFOP** possui a **finalidade de devolução**é necessário gerar a TAG **FINNFE = 4 (devolução)  e a TAG referenciando** o documento de origem deve ser gerada.

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em **editar e** **Retirar o CFOP** do parâmetro **MV\_DEVCFOP** caso tenha informado na NF-e.

![MV_DEVCFOP.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11572721729431)

2- Verificar se a nota foi **referenciada ao documento**de origem corretamente:

D2\_ITEMORI, D2\_SERIORI, D2\_NFORI **(nota de saída)**

![referecia_nt_saida.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11573733162263)

D1\_ITEMORI, D1\_SERIORI, D1\_NFORI **(nota de entrada)**

**![referecia_nt_entrada.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11573337997079)**

**Importante:**

Lembrando que a nota só é **referenciada no XML** caso exista no sistema.

Se a mesma for referenciada manualmente deve se preencher os campos **NF . Ori , Serie Ori e Item Ori** .   
  
Se for preenchido automaticamente pelo gatilho **F4 (Nota de saída) ou F7 (Nota entrada)** os campos são alimentados automaticamente.

3- Verificar  se o campo na TES **F4\_AJUSTE -> Ajuste CIAP = N**, pois se estiver como Sim irá gerar **FINNFE = 3.**

![f4_ajuste_n.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11573890987031)

4- Após isso, exclua a nota e gere novamente.

Se nota de **beneficiamento** deve ser verificado também:

Para notas que a nota de origem foi realizada como **beneficiamento TES** **poder de terceiro Remessa** e **no retorno** é necessário transmitir como **normal devido a TES ter poder de terceiro como devolução.**

Se nota de **remessa** deve ser verificado também:

Nota de origem **normal com TES poder de terceiro Remessa** ao r**etornar a nota é do tipo beneficiamento com Tes poder de terceiro devolução**.

**Saiba mais:**

É possível consultar a **nota técnica 2013.005\_v\_1.22** página 130 para saber quais são os CFOPs com finalidade de devolução.

<http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=tW+YMyk/50s=>

É **impossível referenciar uma nota que não está no sistema**, pois este busca os dados da nota fiscal de origem nas tabelas para referenciar no XML.

Verifique se há a possibilidade de inclusão da nota fiscal de origem com a chave correta: **Entrada (F1\_CHVNFE), saída (F2\_CHVNFE)**. 

Em caso de dúvidas na inclusão de nota de saída, abra um chamado no suporte Faturamento. **Se for nota de entrada, no suporte de Materiais.**

Se a nota não tiver que gerar movimentação (estoque, financeiro, etc.), gere-a pela rotina **NF MANUAL SAIDA/ENTRADA no módulo de Livros Fiscais.**

O sistema só realiza o processo de devolução de notas que estão em seu banco de dados. **Este processo ocorre apenas nas versões 3.10 e 4.00**, pois na versão 2.00 não existia a tag <finNfe> igual a 4, que obriga o documento a ter a finalidade de devolução, quando usado um CFOP de devolução.

Nesse caso, **é necessário ter a nota original no sistema para que possa fazer a devolução, pois não tem onde buscar as informações da nota original (série, item, modelo, chave, etc.).**

O código de **cliente e fornecedor no sistema deve ser o mesmo ao referenciar a nota**, além disso **desconhecemos a operação de devolução de complemento de nota,** ou **complemento de devolução** caso seja orientação da Sefaz enviar a consulta formal junto ao ticket.

Obs: Não é permitido gerar nota de devolução com mais de um item, quando esses itens possuem CFOP com finalidades diferentes, pois no xml so possui uma tag finnfe que define o tipo da nota.

Ex CFOP 2202 finalidade de devolução e CFOP 2949 genérico que não tem finalidade de devolução.
