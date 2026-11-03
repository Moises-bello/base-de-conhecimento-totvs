---
article_id: 360010388591
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: f4d29fdab71fc3e5fb9bc71c93fcf983d6c7e14891e39e8090fb26fa7c54d463
fetched_at: '2026-06-28T22:42:02.546593+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPEDFISCAL
  - Registro C130, C140, C141, C160 e C165
type: support-article
updated_at: '2025-02-11T21:44:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010388591-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPEDFISCAL-Registro-C130-C140-C141-C160-e-C165
---

**Duvida**

Geração dos registros C130, C140, C141, C160 e C165 do Sped Fiscal

**Produto**

Protheus - Livros Fiscais  - A partir da 12.1.17

**Solução**

#### **REGISTRO C130: ISSQN, IRRF e Previdência Social**

Este registro é gerado a partir do livro fiscal, e é composto por notas fiscais dos seguintes modelos:

* Nota Fiscal Modelo 1 ou 1-A – Espécie “NF ou NFE”
* Nota Fiscal de Produtor, Modelo 4

#### **REGISTRO C140: Fatura (Código 01)**

Este registro é gerado a partir do livro fiscal quando há uma fatura para este documento (SE1/SE2), e é composto de notas fiscais dos seguintes modelos:

* Nota Fiscal Modelo 1 ou 1-A – Espécie “NF ou NFE”

#### **REGISTRO C141: Vencimento da Fatura (Código 01)**

É gerado um registro C141 para cada C140, contendo informações complementares da fatura (valor, data do vencimento), e é composto de notas fiscais dos seguintes modelos:

* Nota Fiscal Modelo 1 ou 1-A – Espécie “NF ou NFE”

**Importante**

Disponibilizado o **Ponto de Entrada SPDFIS09** para gravar informações nos **Registros C140 e C141**. Para mais detalhes sobre este ponto de entrada, acesse: [SPDFIS09 - Grava informações nos Registros C140 e C141](http://tdn.totvs.com/pages/releaseview.action?pageId=6077180)

#### **REGISTRO C160: Volumes Transportados (Código 01 e 04) - Exceto Combustíveis**

Este registro identifica a natureza e volume das mercadorias transportadas na operação, sendo gerado apenas para **documentos de saída modelo 01 ou 04**, e é composto de notas fiscais dos seguintes modelos:

* Nota Fiscal Modelo 1 ou 1-A – Espécie “NF ou NFE”
* Nota Fiscal de Produtor, Modelo 4 - Espécie="NFP"

#### **REGISTRO C165: Operações com Combustíveis (Código 01)**

Este registro é gerado para documentos com movimentações de combustíveis, essa informação é tratada no **Complemento de Combustíveis (CD6)**, e é composto de notas fiscais dos seguintes modelos:

* Nota Fiscal Modelo 1 ou 1-A – Espécie “NF ou NFE

Para mais informações sobre o Sped Fiscal acessar:  
<http://tdn.totvs.com/pages/releaseview.action?pageId=238035285>
