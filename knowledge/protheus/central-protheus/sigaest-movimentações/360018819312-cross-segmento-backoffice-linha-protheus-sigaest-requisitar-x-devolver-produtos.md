---
article_id: 360018819312
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 42b294c5a242942ff335d665021208b94336d5975264b8f2237fb93ecd2ded5b
fetched_at: '2026-06-28T22:38:54.137783+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Requisitar x Devolver  Produtos
  com Apropriação Indireta
type: support-article
updated_at: '2025-09-05T12:49:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018819312-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Requisitar-x-Devolver-Produtos-com-Apropria%C3%A7%C3%A3o-Indireta
---

**Dúvida** Como requisitar e devolver Produtos com Apropriação Indireta na prática?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Neste artigos ordenaremos em passos como fazer uma Requisição/Devolução de Produtos com Apropriação Indireta.

**1-** O produto precisar estar configurado como produto indireto (B1\_APROPRI = Indireto).

**2-** Ter cadastrado uma TM (tipo de movimentação )para movimentação de produtos com apropriação indireta conforme abaixo (MATA230):

- Tipo TM = Devolução / Valorizado (F5\_VAL) = NAO / Aprop. Indir (F5\_APROPRI) = Nao (Pois o parâmetro como "Nao" **ativa a apropriação indireta**).

- Tipo TM = Requisição / Valorizado (F5\_VAL) = NÃO / Aprop. Indir (F5\_APROPRI) = Nao (Pois o parâmetro como "Nao" **ativa a apropriação indireta**).

**3 -** Processo de **REQUISIÇÃO:**

 - Após os passos acima, acesse à rotina MATA240 ou MATA241 para realizar a movimentação;

 - Na inclusão do movimento, informe o TM de Requisição cadastrado anteriormente, o código  do produto, a quantidade a ser requisitada do armazém 01 para o armazém de processo 99.

![MATA241.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34722190051095)

![MATR900.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34722190052375)

4 - Processo de **DEVOLUÇÃO:**

- Na inclusão do movimento, informe o TM de devolução cadastrado anteriormente, o código  do produto, a quantidade a ser requisitada do armazém 99 e o armazém que irá receber a quantidade;

- Após esse procedimento, o saldo do armazém 99 será requisitado e incluso no armazém informado.

![MATA241_DEV.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34722184079511)

![MATR900_DEV.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34722190055063)

**Saiba mais:**

*[MP - SIGAEST - Conceito e usabilidade de Apropriação Indireta (MV\_LOCPROC)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020688571)*

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
