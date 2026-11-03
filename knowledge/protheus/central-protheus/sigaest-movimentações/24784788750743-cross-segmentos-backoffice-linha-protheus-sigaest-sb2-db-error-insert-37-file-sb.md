---
article_id: 24784788750743
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 5cefacbc00375dbcfb75f6e7db86757f3f39f85769f8a04450998474c0b3fe34
fetched_at: '2026-06-28T22:38:58.548728+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: 'Cross Segmentos - Backoffice (Linha Protheus) - SIGAEST - SB2: DB error (Insert):
  -37 File: SB2 - Error unique constraint CRIASB2'
type: support-article
updated_at: '2024-07-10T12:30:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24784788750743-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAEST-SB2-DB-error-Insert-37-File-SB2-Error-unique-constraint-CRIASB2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24784815711511) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao realizar a inclusão de uma das movimentações: Pedido de Compra / Solicitação de Compra / Documento de Entrada / Pedido de Venda / Documento de Saída, o sistema está gerando um error.log na função "CRIASB2" indicando: SB2 - Error unique constraint  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) - SIGAEST - Todas as versões  
  
**Causa**Este erro acontece quando o sistema identifica que o produto não possui um registro, para o armazém selecionado, na SB2, porém quando tenta realizar inclusão, o banco de dados identifica que o registro já existe.

Essa inconsistência pode ocorrer por alguns motivos:

* Diferença no tamanho dos campos de código do Produto: sistema faz o Seek (Pesquisa da existência do produto na SB2) a partir de três informações:
  + Filial
  + Código do Produto
  + Armazém
* Uso incorreto do Ponto de entrada "CRASB2":
  + [CRIASB2: Grava informações no registro SB2](https://tdn.totvs.com/x/GhYaDg)

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Verifique o tamanho dos campos que o sistema usa para pesquisa:
   * Principalmente os campo de Código do Produto e Código do Armazém, sempre comparando com as tabelas SB1 e SB2, os campos devem possuir o mesmo tamanho e máscara. Exemplo: se estiver incluindo um Pedido de Compras, verifique se os campos de código de produto e código do armazém da tabela SC7, estão com o mesmo tamanho e máscara dos campos das tabelas SB1 e SB2.
2. Verifique se utiliza o ponto de entrada [CRIASB2: Grava informações no registro SB2](https://tdn.totvs.com/x/GhYaDg)
   * Caso utilize, realize um teste desabilitando o ponto de entrada e verifique se o problema persiste.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
