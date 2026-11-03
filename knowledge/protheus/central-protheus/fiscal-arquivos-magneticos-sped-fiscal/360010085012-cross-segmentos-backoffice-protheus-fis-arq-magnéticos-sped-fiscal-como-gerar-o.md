---
article_id: 360010085012
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: a5cfa8d4280c91f4e36e25f1ab2309d7bb096e01b8a75bdbda8424bf8684a925
fetched_at: '2026-06-28T22:42:02.496259+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL-
  Como gerar o registro C111 do Sped Fiscal
type: support-article
updated_at: '2025-02-13T21:43:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010085012-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-o-registro-C111-do-Sped-Fiscal
---

**Dúvida**  
Como gerar o registro **C111** do Sped Fiscal?  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão **11.80**  
   
**Solução**

O registro **C111** é gerado a partir do complemento de "Processos Referenciados", a seguir orientação de como realizar o complemento:

1. Acesse o caminho Rotina **MATA920**> Outras Ações > Complementos > Processos Referenciados;

2. Preencha o campo Núm. Processo (**CDG\_PROCES**) que se refere ao campo 02 - **NUM\_PROC** do registro **C111;**

3. Preencha o campo Tp.processo (**CDG\_TPPROC**) que se refere ao campo 03 - **IND\_PROC** do registro **C111;**

4. Salve o complemento;

5. Utilize a rotina **SPEDFISCAL** para geração do arquivo.

Ao realizar o retorno da SEFAZ o número do processo é gravado na tabela **SF3** campo **F3\_PROTOC.**![](http://tdn.totvs.com/download/attachments/238035285/image2016-7-6%2017%3A46%3A4.png?version=1&modificationDate=1467838006000&api=v2)   
  
**Importante**

Conforme portaria nº 163/2007-SEFAZ considera-se para os registros **0450**, **C100**, **C110** e **C111** o tratamento "Cancelamento extemporâneo", ou seja em caso de Cancelamento homologado fora de prazo é necessário realizar a geração dos registros a cima citados com suas devidas características como Número de Protocolo do pedido de cancelamento da NF-e fornecido pela SEFAZ  e situação do documento 08 -  Documento fiscal emitido com base em Regime Especial ou norma especifica, status “155-Cancelamento homologado fora de prazo” identificado na NT 2012/13. Sendo a geração do EFD com perfil diferente de "C".

Caso o cliente não tenha em seu dicionário de dados, o campo **F3\_PROTOC**, será considerado cancelamento normal sem a geração dos registros informado na portaria nº 163/2007-SEFAZ Art. 18 I.

**Complemento de Nota Fiscal Automático**

Utilizado para alterações automáticas nos complementos dos documentos fiscais após a emissão das Notas Fiscais.

Para informações sobre o Ponto de entrada **MATUCOMP**, acesse: [MATUCOMP - Alterações automáticas](http://tdn.totvs.com/pages/releaseview.action?pageId=6077107)

O parâmetro **MV\_ATUCOMP** deve ser configurado para que seja possível utilizar o Ponto de Entrada **MATUCOMP**,  **MV\_ATUCOMP** = T  
  
Para mais informações sobre o Sped Fiscal acessar:

<http://tdn.totvs.com/pages/releaseview.action?pageId=238035285>
