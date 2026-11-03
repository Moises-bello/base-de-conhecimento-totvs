---
article_id: 360004728072
category: SIGAEST - SALDOS
content_hash: 9ede07d3f68033552c890a4c782ab8a7993c44b0e08bc6aeec405c2dc9fafdd2
fetched_at: '2026-06-28T22:39:14.936134+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Rastreabilidade de
  Produtos por Lote SubLote
type: support-article
updated_at: '2025-03-12T12:17:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004728072-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Rastreabilidade-de-Produtos-por-Lote-SubLote
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28916771877655) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**

Rastreabilidade de Produtos, controle do lote de produtos no Protheus. Qual o conceito e quais processos são cobertos?  
(B1\_RASTRO, MV\_RASTRO, LOTECTL, MV\_FORMLOT, MV\_A390QTD)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O conceito de rastreabilidade existe para garantir que um produto tenha todo seu "caminho" dentro da empresa mapeado, desde seu recebimento ainda como Matéria Prima até a sua venda já como produto acabado. É através da rastreabilidade que as indústrias automobilísticas e farmacêuticas realizam seus 'recalls', após constatarem qualquer falha em determinado componente que comprometa a garantia do produto. Em resposta a essas questões foi criado o conceito de rastreabilidade, que trabalha baseado em normas de qualidade internacionalmente conhecidas.

**Leia mais - [Instrução completa](http://tdn.totvs.com/pages/viewpage.action?pageId=367232994)**

**Controle de lote e Nota Fiscal Eletrônica versão 4.0**

Para atender o novo Layout da nota fiscal eletronica NFE 4.0 em empresas que se enquadram no requisito será necessário seguir o procedimento indicado conforme abaixo.

Procedimentos para ativação do controle de lote

Caso seus produtos NÃO utilizem Rastreabilidade por Lote/SubLote e Deseja inciar o controle devido a obrigação da NFE 4.0 recomendamos que siga os passos abaixo:

a. Realizar um Backup Completo do Ambiente (Banco de Dados, Repositório, Dicionários, etc.)

b. Realizar um Fechamento de Estoque Completo;

c. Antes de liberar o ambiente para os usuários realizar os seguintes procedimentos

1. Alterar o parâmetro MV\_RASTRO = S

2. Alterar o parâmetro MV\_ESTNEG = N (Se for possível sua configuração)

3. Alterar o conteúdo do campo B1\_RASTRO para Lote e/ou Sublote (conforme sua escolha ), somente dos produtos que irá controlar rastreabilidade.

4. Caso tenha saldo em estoque dos produtos que irá utilizar rastreabilidade por lote é necessário definir os lotes e/ou sublote desse saldo (Utilizar a rotina "MANUTENÇÃO DE LOTES - MATA390")

d. Após os ajustes liberar o ambiente para os usuários.

Mais informações:

**[Rastreabilidade de Produtos](http://tdn.totvs.com/display/PROT/DOC0056_Complemento_medicamento_e_rastreabilidade)**

**[NF-e Implementação da versão 4.00](http://tdn.totvs.com/pages/viewpage.action?pageId=318604074)**

**Saiba mais:**

*[Documentação completa sobre controle de Rastreabilidade de Produtos no Estoque](https://tdn.totvs.com/pages/releaseview.action?pageId=367232994)*

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
