---
article_id: 360010166332
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 541b09ea4fff9f79c9ecafc195b9e33556e2a50a10766aaa2621bf2b26d79b41
fetched_at: '2026-06-28T22:42:02.550616+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPEDFISCAL
  - Registro C170: Itens do Documento (Código 01, 1B, 04 e 55)'
type: support-article
updated_at: '2025-02-11T22:01:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010166332-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPEDFISCAL-Registro-C170-Itens-do-Documento-C%C3%B3digo-01-1B-04-e-55
---

**Dúvida**Como gerar o Registro **C170** do **Sped Fiscal**?

**Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80

**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
 1. Este registro é gerado a partir do Livro Fiscal e é composto de notas fiscais dos seguintes modelos:  
Nota Fiscal Modelo 1 ou 1-A – Espécie “**NF** ou **NFE**”  
Nota Fiscal Avulsa, Modelo 1B - Espécie ="**NFA**"  
Nota Fiscal de Produtor, Modelo 4 - Espécie="**NFP**"  
Nota Fiscal Eletrônica, Modelo 55 – Espécie “**SPED**”

2. Por padrão, a descrição do produto apresentada no registro **C170**é a do Cadastro de Produtos. Se for necessário buscar a descrição de outro local, customize o ponto de entrada **SPDFIS04**. Para mais detalhes sobre este ponto de entrada, acesse: [SPDFIS04 - Altera a descrição do produto](http://tdn.totvs.com/pages/releaseview.action?pageId=6077126);  
  
 3. O indicador de movimentação Física do produto (**Campo 09** do **Registro C170**) será definido da seguinte maneira:  
Caso o **TES** utilizado no documento fiscal atualize Estoque (**F4\_ESTOQUE**com opção igual a "N-Não"), este campo será gerado com opção igual a "S-Sim";  
Caso o **TES** utilizado no documento fiscal NÃO atualize Estoque, será verificado então o campo **Mov Fisica** (**F4\_MOVFIS**), se estiver preenchido com opção "N-Não", então o campo **09\_IND\_MOV** do **C170**será gerado com informação "1-Não", caso contrário será gerado com opção "0-Sim".

**TES**

![TES1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360021235311/TES1.PNG)

![TES2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360021297032/TES2.PNG)

Atenção:

Para notas de saída, somente é gerado o registro **C170** quando acompanhar o registro **C176** (**Ressarcimento de ICMS-ST**), portanto para notas sem ressarcimento não é gerado o registro **C170**.

Para mais informações sobre o **Sped Fiscal** acessar:  
 <http://tdn.totvs.com/pages/releaseview.action?pageId=238035285>
