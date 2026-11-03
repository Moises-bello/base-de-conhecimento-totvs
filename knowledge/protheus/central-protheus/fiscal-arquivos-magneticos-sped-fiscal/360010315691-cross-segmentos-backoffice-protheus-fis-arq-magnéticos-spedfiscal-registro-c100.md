---
article_id: 360010315691
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 2ac76ed7b3f33eea8062ca0bda8ff34570b3786bf951872bf38350a916ba8e3f
fetched_at: '2026-06-28T22:42:02.534427+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPEDFISCAL
  - Registro C100 Modelo 01, 1B, 04, 55 e 65
type: support-article
updated_at: '2025-02-11T21:43:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010315691-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPEDFISCAL-Registro-C100-Modelo-01-1B-04-55-e-65
---

**Dúvida**Como gerar o registro C100 para notas fiscais modelos 01, 1B, 04, 55 e 65?  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 12.1.17  
  
**Solução**

**REGISTRO C100: Nota Fiscal (Código01), Nota Fiscal Avulsa (Código1B), Nota Fiscal de Produtor (Código04), NF-e (Código55) e NFC-e (Código6****5)**

Este registro é gerado a partir do livro fiscal e é composto de notas fiscais dos seguintes modelos:

* Nota Fiscal Modelo 1 ou 1-A – Espécie “NF ou NFE”
* Nota Fiscal Avulsa, Modelo 1B - Espécie ="NFA"
* Nota Fiscal de Produtor, Modelo 4 - Espécie="NFP"
* Nota Fiscal Eletrônica, Modelo 55 – Espécie “SPED”
* Nota Fiscal Eletrônica ao Consumidor Final, Modelo 65 - Espécie="NFCE"

Para geração do registro C100 é necessário configurar os campos conforme exemplo abaixo:

**Produto**

Origem (B1\_ORIGEM) =?

**Configuração de TES**

Campos

Calcula ICMS (F4\_ICM) =?

Calcula IPI (F4\_IPI)=?

Livro ICMS, IPI = diferentes de Não -> “Deve ser configurado o campo de um dos livros com opção diferente de NÃO para geração dos valores nas tabelas SF3 e SFT”.

Sit. Trib. ICM (F4\_SITTRIB)=?

Cod. Trib. IPI (F4\_CTIPI)=?

* **Se existir cálculo de PIS COFINS:**

PIS/COFINS (F4\_PISCOF) = Ambos   
Créd. PIS/COF (F4\_PISCRED) = Debita(Saída)/Credita (Entrada)

Sit. Trib PIS (F4\_CSTPIS) = Entrada (50 a 66) / Saída (01 a 49) lembrando que as CST de credito estão no intervalo 50 a 66

Sit. Trib COFINS (F4\_CSTCOF) = Entrada (50 a 66) / Saída (01 a 49) lembrando que as CST de credito estão no intervalo 50 a 66

* **Se não existir cálculo de PIS COFINS:**

PIS/COFINS (F4\_PISCOF) = Não considera

Créd. PIS/COF (F4\_PISCRED) =Não Calcula

Sit. Trib PIS (F4\_CSTPIS) = Entrada (70) / Saída (49)

Sit. Trib COFINS (F4\_CSTCOF) = Entrada (70) / Saída (49)

**Importante:**

Cadastro de TES (SF4)

**Código da Situação tributária do ICMS (F4\_SITTRIB).**

**Código da Situação tributária do IPI (F4\_CTIPI).**

**Código da Situação tributária do PIS**, caso seja um TES que **calcule PIS(F4\_CSTPIS).**

**Código da Situação tributária do COFINS**, caso seja um TES que **calcule COFINS(F4\_CSTCOF).**

Para todos os registros no qual é necessário informar a classificação fiscal do item, com relação aos impostos ICMS, IPI, PIS e COFINS, existe a possibilidade de alterar a classificação fiscal padrão apresentada pelo sistema (composta pelo produto e pelo TES). Caso exista esta necessidade, deve-se customizar o **Ponto de Entrada SPDFIS03.**Para mais detalhes sobre este Ponto de Entrada, consulte o portal TDN: [SPDFIS03 - Altera a Situação Tributária dos Impostos ICMS, IPI, PIS e COFINS](http://tdn.totvs.com/pages/releaseview.action?pageId=6077157)

Para mais informações sobre o Sped Fiscal, acessar:

<http://tdn.totvs.com/pages/releaseview.action?pageId=238035285>
