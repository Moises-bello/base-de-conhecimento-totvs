---
article_id: 360027654292
category: SIGAEST - CUSTOS
content_hash: b2580669b9711222cbfe584ce1cb45bc49a79a9600535b61056e75dbe4c12995
fetched_at: '2026-06-28T22:39:02.183894+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - MA320LOOP
  - Referencia Circular - Recursividade no MATA330
type: support-article
updated_at: '2025-03-12T12:22:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027654292-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-MA320LOOP-Referencia-Circular-Recursividade-no-MATA330
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30503720250775)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Ao executar o Recálculo do Custo Médio (MATA330) está apresentando "HELP: MA320LOOP - A estrutura do Produto abaixo identificado está com referencia circular". O que fazer para resolver?

**Ambiente**Protheus – Estoque/Custos – A partir da versão 11.80  
  
**Solução**

Quando é executado o Recalculo do Custo Médio, configurando o parâmetro **"Gera Estrutura Pela Movimentação = Sim"**, a rotina irá gerar uma estrutura temporária com base nas movimentações realizadas para valorização do custo de seus produtos.

Porém, caso em seu processo tenha ocorrido situações nas quais **um produto é requisitado para produção dele mesmo**, o sistema apresentará a mensagem de **Erro de Recursividade** e não processará o cálculo dos níveis da maneira correta, comprometendo todo o Recálculo de Custo, pois o PROTHEUS não efetiva o calculo de maneira recursiva.

Para avaliar quais produtos estão nessa situação, pode-se emitir o relatório Recursividade Por Movimentação (**MATR331**) ou o relatorio [Smartview ESTSV030](https://tdn.totvs.com/x/yEQpM)  Ambos relatórios listará movimentações que apresentaram problema de recursividade, **portanto todos os itens que forem citados nesse relatório estão com esse tipo de problema.**

Para identificar a situação, será necessário analisar OP por OP, qual foi o problema de recursividade apontado.

Conforme informado anteriormente, a recursividade pode ocorrer quando um produto **é requisitado para produção dele mesmo, mas as vezes esse processo não é direto. Veja o exemplo abaixo:**

 Estrutura

 |-PA

      |-PI1

          |-PI2

              |-MP

Supondo que tenhamos produzido o **PA** conforme estrutura acima e posteriormente, por alguma necessidade de seu processo, acabamos requisitando este material na produção de uma OP do **PI1**.

O Recálculo do Custo Médio, ao tentar montar a estrutura por movimentação, acusará recursividade, pois estaremos utilizando o produto **PI1 para produzir o PA** **mas também utilizando um PA para produzir o PI1, o que impede a montagem da estrutura.**

Esse processo não pode acontecer, pois comprometerá todo o cálculo de custo, portanto deve-se analisar todas as OPs apontadas e corrigir esse tipo de situação, pois o PROTHEUS não calcula movimentos RECURSIVOS.

Ao executar a rotina com o parâmetro **"Gera Estrutura pela Movimentação = Não"**, produtos requisitados para produção de um outro produto e que não estão presentes em sua estrutura **não serão considerados para valorização do custo desse produto.**

**Como ajustar o problema da Recursividade?**

Para ajuste deve-se **avaliar o resultado exibido no relatório e excluir o item da estrutura ou do movimento de consumo contra a Ordem de Produção**.

Devido à integridade de dados no sistema o procedimento de ajuste deve ser feito por profissional com conhecimento de analista em estoque custos e manufatura.

Diante da complexidade e abrangência do tema onde podemos ter cenários distintos no mesmo ambiente **e pelo fato de não existir um procedimento padrão**, nossa orientação é acionar o seu ESN (Executivo de Soluções de Negócio) TOTVS para contratação do profissional especializado, para que valide todas as situações de recursividades apresentadas para sua devida correção.

**Saiba mais;**

*[MP - SIGAEST - Recálculo do Custo Médio (MATA330) - Conceito e Informações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013945671)*

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)
