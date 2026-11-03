---
article_id: 360018402631
category: SIGAEST - CUSTOS
content_hash: 635ea2bdb9e2c142ab107e72ff357fe0ef198bad25cf897498829ea84d19c4dc
fetched_at: '2026-06-28T22:39:00.450250+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Recursividade no processamento
  do recalculo do custo médio - MATA330
type: support-article
updated_at: '2026-06-16T18:13:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018402631-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Recursividade-no-processamento-do-recalculo-do-custo-m%C3%A9dio-MATA330
---

Durante o Recalculo do Custo Médio no TOTVS Protheus, ao ativar "Gera Estrutura Pela Movimentação = SIM", pode ocorrer erro de recursividade se um produto for requisitado para produzir ele mesmo, comprometendo o cálculo. O relatório MATR331 ajuda a identificar esses casos, que devem ser corrigidos para evitar falhas. Para cenários complexos, recomenda-se suporte especializado da TOTVS.

**Dúvida**  
Mensagem de Recursividade do Produto durante o Recalculo do Custo Médio. O que fazer?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Quando você executa o Recalculo do Custo Médio, configurando o parâmetro **Gera Estrutura Pela Movimentação = SIM**, e a rotina irá gerará uma estrutura temporária com base nas movimentações realizadas para valorização do custo de seus produtos.

Porém, caso em seu processo tenha ocorrido situações nas quais **um produto é requisitado para produção dele mesmo**, o sistema apresentará a mensagem de **"Recursividade na estrutura, Deseja prosseguir o Recalculo do custo medio?"** e não processará o cálculo dos níveis da maneira correta, comprometendo todo o recálculo de custo. Com ou sem a utilização de procedures.

Para avaliar quais produtos estão nessa situação, você poderá emitir o relatório de Recursividade Por Movimentação (**MATR331**).

Emite uma lista das movimentações que geram recursividade no processamento do Recálculo do Custo Médio. Essas movimentações baseiam-se nos movimentos internos (requisições) vinculados às Ordens de Produção.

Neste caso, a recursividade refere-se à pesquisa de movimentações que podem chamar a mesma OP. Além disso, ela também pode ser usada quando a estrutura do produto não foi cadastrada corretamente.

Para identificar a situação, **sugerimos** analisar em cada OP qual foi o problema de recursividade apontado no relatorio.

**Por exemplo**, a recursividade ocorre quando um produto é requisitado para produção dele mesmo, mas as vezes esse processo não é direto.

Veja o exemplo abaixo: Estrutura:   
|-PA   
|-PI1   
|-PI2   
|-MP

Supondo que você tenha produzido o PA conforme estrutura acima, posteriormente por alguma necessidade de seu processo, você acaba requisitando este material na produção de uma OP do PI1.

O recálculo do custo médio, ao tentar montar a estrutura por movimentação, acusará recursividade, pois o produto você está utilizando para produzir um PI1 para produzir o PA mas também utilizando um PA para produzir o PI1, o que impede a montagem da estrutura.

Esse processo não pode acontecer, pois comprometerá todo seu cálculo de custo, portanto você deverá analisar todas as OPs apontadas e corrigir esse tipo de situação.

**Importante:** O relatorio MATR331- analise de recursividade, foi concebido para analisar as recursividades dentro da filial em que esta sendo executado, Tanto que não é possivel nem selecionar uma filial, e não herda as recursividades apontadas no recalculo.  
Já o recalculo permite ser executado combinando as filiais devido ao custo que se interage entre as filiais, e as recursividades que ocorrem entre as filiais podem ser detectadas.

Caso possua cenários com essa questão, **ou cenários onde apresentem problema recursivo, identificado com ou não sob a analise de OPs**, o suporte padrão sugere solicitar a visita de um representante TOTVS especialista no módulo Estoque/Custos para que seja possível auxiliá-lo neste tipo de avaliação e correção.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001602842-Materiais-Estoque-e-Custos-SIGAEST-)
