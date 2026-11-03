---
article_id: 360029162831
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: aaba95e3f95ae8a9e4461c8f622b6290731a235ed1c75fc6e600a8525b710cff
fetched_at: '2026-06-28T22:39:36.903907+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar
  para deduzir o ICMS e não agregar o IPI na base do PIS e COFINS nas notas de entrada? '
type: support-article
updated_at: '2023-05-08T17:32:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029162831-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-para-deduzir-o-ICMS-e-n%C3%A3o-agregar-o-IPI-na-base-do-PIS-e-COFINS-nas-notas-de-entrada
---

**Dúvida**

Como configurar para deduzir o ICMS e não agregar o IPI da base do PIS e COFINS nas notas de entrada?

**Ambiente**

Protheus – Livros Fiscais– A partir da versão 11.80  
  
**Solução**

Disponibilizado a opção de configuração no fornecedor para que seja configurado se o ICMS deve ou não ser deduzido da base de PIS/COFINS nas notas de entrada.

O campo também possui validação para agregar ou não o IPI na base de cálculo do PIS e COFINS.

 Esta configuração deverá ser feita no campo **Ded.PIS/COF****(A2\_DEDBSPC).**

As opções são:

**1 - Legado**: Deduz conforme parâmetros MV\_DEDBPIS e MV\_DEDBCOF.

Ao utilizar essa opção, deverá validar primeiro como estão configurados os parâmetros MV\_DEDBPIS e MV\_DEDBCOF.

Caso os parâmetros estejam com I, somente terá a exclusão do ICMS.

Caso os parâmetros estejam com S, terá a exclusão do ICMS e pode determinar se o IPI irá agregar ou não, na base do PIS e COFINS.

Exemplo:

Para que o IPI seja **agregado**, deve configurar no TES o campo **Credita IPI (F4\_CREDIPI) = NÃO**

**Valor dos produtos - 1.000,00**

**Valor ICMS - 100,00**

**Valor IPI - 50,00**

**Base do PIS e COFINS - 1.000,00 - 100,00 + 50,00 = 950,00**

Para **não agregar** o IPI, deve configurar no TES o campo **Credita IPI (F4\_CREDIPI) = SIM**

**Valor dos produtos - 1.000,00**

**Valor ICMS - 100,00**

**Valor IPI - 50,00**

**Base do PIS e COFINS - 1.000,00 - 100,00 = 900,00**

**obs: o IPI não faz parte do custo do produto, com isso o mesmo deve ser agregado ou não agregado.**

**obs. 2: somente a opção 1 - Legado valida os parâmetros MV\_DEDBPIS e MV\_DEDBCOF, as demais opções não.**

**2 - ICMS e IPI:** Deduz ICMS e IPI.

Irá excluir ICMS e IPI da base de cálculo do PIS e COFINS.

**Valor dos produtos - 1.000,00**

**Valor ICMS - 100,00**

**Valor IPI - 50,00**

**Base do PIS e COFINS - 1.000,00 - 100,00 - 50,00 = 850,00**

**3 - ICMS:** Deduz apenas o ICMS.

Irá deduzir o ICMS e não irá agregar o IPI.

**Valor dos produtos - 1.000,00**

**Valor ICMS - 100,00**

**Valor IPI - 50,00**

**Base do PIS e COFINS - 1.000,00 - 100,00 = 900,00**

**4 - IPI:** Deduz apenas o IPI.

**Valor dos produtos - 1.000,00**

**Valor ICMS - 100,00**

**Valor IPI - 50,00**

**Base do PIS e COFINS - 1.000,00 - 50,00 = 950,00**

**5 - Nenhum**: Não deduz nem o ICMS e nem o IPI.

O ICMS não será excluído e o IPI não será agregado.

**Valor dos produtos - 1.000,00**

**Valor ICMS - 100,00**

**Valor IPI - 50,00**

**Base do PIS e COFINS = 1.000,00**

**6 - Soma IPI:**Quando configurado como 6 e não tributar o IPI, o mesmo será somado a base de PIS E COFINS.

**Valor dos produtos - 1.000,00**

**Valor ICMS - 100,00**

**Valor IPI - 50,00**

**Base do PIS e COFINS - 1.000,00 +50,00 = 1.050,00**

.
