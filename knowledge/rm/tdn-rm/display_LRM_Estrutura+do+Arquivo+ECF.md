---
content_hash: 960827d3c636c0ea7b341abd0ee8cfb73a49c33fa4386c5ed346520ba7ebbb3f
fetched_at: '2026-06-29T00:09:20.106110+00:00'
page_id: '422545665'
product: rm
source: tdn-rm
title: Estrutura do Arquivo ECF
type: documentation
url: https://tdn.totvs.com/display/LRM/Estrutura+do+Arquivo+ECF
version: 15
---

As informações devem ser enviadas ao validador da ECF através de arquivo texto no padrão ASCII - ISO 8859-1 com os registros organizados de maneira hierárquica e seus respectivos campos separados por "pipes".

## **01. Estrutura**

O arquivo deverá obedecer a seguinte estrutura:

| Bloco | Informação |
| --- | --- |
| **0** | Abertura e Identificação |
| **C** | Informações Recuperadas das ECD. Não gerado pelo processo da ECF. |
| **E** | Informações Recuperadas da ECF anterior e Cálculo Fiscal dos Dados Recuperados da ECD. Não gerado pelo processo da ECF. |
| **J** | Plano de Contas e Mapeamento |
| **K** | Saldos das Contas Contábeis e Referências |
| **L** | Lucro Líquidosad |
| **M** | e-LALUR e e-LACS |
| **N** | Imposto de Renda e Contribuição Social (Lucro Real) |
| **P** | Lucro Presumido |
| **T** | Lucro Arbitrado |
| **U** | Imunes ou Isentas |
| **X** | Informações Econômicas |
| **Y** | Informações Gerais |
| **9** | Encerramento do Arquivo Digital |

[Detalhes dos Blocos Gerados (ECF)](https://tdn.totvs.com/pages/viewpage.action?pageId=438289214)

---
