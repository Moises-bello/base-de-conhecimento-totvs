---
content_hash: 497258956030b5a1932ff412277e1a4313efb8f57c9c1183727bccee5a064dd7
fetched_at: '2026-06-29T00:09:04.150509+00:00'
page_id: '382555011'
product: rm
source: tdn-rm
title: 3320278 FISCAL01-5638 DT NF-e/NFC-e - NT 2016.002 v1.60 e NT2017.001 v1.30
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=382555011
version: 88
---

# NF-e/NFC-e - NT 2016.002 v1.60 e NT2017.001 v1.30

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Emissão de NF-e/NFC-e |
| **Situação/Requisito:** | Realizar implementações da NF-e/NFC-e conforme NT 2016.002 v1.60 e NT2017.001 v1.30 |
| **Solução/Implementação:** | Foram realizados as alterações abaixo no processo de emissão da NF-e conforme NT2016.002 v1.60 e NT2017.001 v1.30   1. A TAG **vDesc** do Grupo de Faturas (**fat**) será gerado sempre com o valor zero. 2. O Grupo do opcional do **ICMS60** referente ao Valor efetivo do ICMS será gerado conforme abaixo    1. **pRedBCEfet**: Será gerado com os dados do Anexo “Dados Fiscais por UF”, considerando a UF da Filial emitente.    2. **vBCEfet**: Calculado = **Vprod** - **pRedBCEfet**    3. **pICMSEfet**: Alíquota do ICMS informada nos “Dados Fiscais por UF”, considerando a UF da Filial emitente    4. **vICMSEfet**: Calculado = **vBCEfet** \* **pICMSEfet** 3. O Grupo Parcelas (**dup**) da Fatura (**fat**) passou a ser ordenado pela data de vencimento, da menor para a maior. 4. O campo Número da Parcela (**nDup**) passou a ser gerado com valor fixo, sequencial a partir do 001. Ex: 001, 002, 003 etc. 5. Os campos **ean** e **eanTrib** passaram a gerar a literal "SEM GTIN" quando o campo estiver vazio. (em produção a alteração terá efeito somente a partir de 01/12/2018) 6. O Grupo Parcelas (**dup**) passou a ser gerado com valor zero e os meios de pagamentos foram gerados como SEM PAGAMENTO para os todas as notas do tipo ajuste e devolução independente se o pagamento foi informando ou não. |

divs
