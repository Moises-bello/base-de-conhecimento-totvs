---
article_id: 360040937934
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: bd8ea01599e6ab51be8d317fa9cabc92359da017b741fa77af234ef7e58b369d
fetched_at: '2026-06-28T22:38:33.111653+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP - FAT - Descrição do Produto com grade no DANFE
type: support-article
updated_at: '2021-04-28T15:53:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040937934-MP-FAT-Descri%C3%A7%C3%A3o-do-Produto-com-grade-no-DANFE
---

**Ocorrência**No módulo Faturamento, ao inserir um produto com grade, a descrição preenchida na linha do item é a do produto principal da grade, com isso a descrição no DANFE é igual para todos os itens.  
   
 **Ambiente**Microsiga Protheus – Faturamento – A partir da versão 12  
   
 **Causa**

Ao configurar a grade de produtos, a tabela SC6 (Itens do Pedido de Venda) recebe a descrição do produto principal da grade. Conforme documentado em: <https://tdn.totvs.com/pages/releaseview.action?pageId=268578844>

O DANFE copia a descrição do produto gravada no Pedido de Vendas, esse tratamento existe porque é possível utilizar descrições diferentes para o mesmo produto quando configurada a rotina Produto x Cliente (MATA370 - SA7) / Produto x Fornecedor (SA5).

**Solução**

1. Caso necessite que na SC6 o sistema grave a descrição do produto na SB1, é necessário criar um gatilho customizado para que busque a descrição do produto na SB1 e preencha na SC6, dessa forma a descrição da SC6 será igual à da SB1, levando a descrição desejada para o DANFE;

2. Outra opção é configurar através do parâmetro MV\_NFPTER a demonstração no DANFE optando por alimentar a TAG **<xProd>** a partir da SB1 ou SA5/SA7 (detalhes [aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026075513-MP-NFE-Quais-campos-podem-ser-preenchidos-para-gerar-a-TAG-Xprod-?source=search)), neste caso, se for realizada qualquer alteração na descrição do produto na SC6, ela não será considerada no DANFE.
