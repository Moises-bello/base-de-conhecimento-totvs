---
article_id: 35855256093207
category: SIGAEST - CUSTOS
content_hash: c558a0cad32d30f08202a12bd55686180cb1963abb83a80317fb8c9ce08a307a
fetched_at: '2026-06-28T22:39:00.921619+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Erro no calculo do
  custo _NUMSEQ duplicado
type: support-article
updated_at: '2026-04-09T16:22:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35855256093207-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Erro-no-calculo-do-custo-NUMSEQ-duplicado
---

Problemas no cálculo do custo e fechamento de saldos no módulo de estoque/custos do TOTVS Protheus podem ser causados por dados duplicados nos campos D1\_NUMSEQ, D2\_NUMSEQ, D3\_NUMSEQ, D3\_IDENT e H6\_IDENT. A duplicidade ocorre devido à configuração incorreta das chaves specialkey e checkspecialkey no License Server. O ajuste deve ser feito nas tabelas SD1, SD2, SD3 e SH6, preferencialmente com auxílio de um analista DBA, para garantir a correta ordenação dos movimentos e evitar erros futuros.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35855256084119) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Foi identificado que problemas relacionados ao calculo do custo dos produtos, e fechamento de saldos, podem ser causados por dados duplicados nos campos D1\_NUMSEQ, D2\_NUMSEQ, D3\_NUMSEQ, D3\_IDENT e H6\_IDENT, no modulo de estoque custos.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Para a correta ordenação dos movimentos é necessario ajuste interno nos campos encontrados com duplicidade.

**Explicação tecnica:**

A repetição de CAMPOS \_NUMSEQ impacta na apropriação do Custo por conta da ordenação dos movimentos, mesmo com o uso do [I\_N\_S\_D\_T\_](https://tdn.totvs.com/x/ZxedIQ) indicado nesse link <https://tdn.totvs.com/x/IsP7Og>

A configuração atual via License Server substitui o antigo [MV\_DOCSEQ](https://tdn.totvs.com/x/XgodMg) , porém, assim como antes, se o valor indicado no License Server for menor que a maior numeração \_NUMSEQ das tabelas SD1, SD2, SD3 e SH6, os movimentos feitos no sistema vão utilizar esta numeração para gravar nas tabelas SD1, SD2, SD3 e SH6, podendo ocasionar erros de duplicidade.

Os ajustes dos dados duplicados devem ser realizados nas tabelas, sempre com o valor inicial com o maior numseq entre as tabelas SD1, SD2, SD3 e SH6, configurar a chave [specialkey](https://tdn.totvs.com/x/BRY1Gg) no AppServer, assim como a chave [checkspecialkey](https://tdn.totvs.com/pages/viewpage.action?pageId=840763998#:~:text=de%20como%20ficar%C3%A1%3A-,checkspecialkey,-%3D%201%0AA%20altera%C3%A7%C3%A3o). O ajuste das chaves evita a duplicidade nos novos movimentos, ordenando corretamente nos casos em que é usado o MV\_SEQ300 e/ou a apropriação sequencial, pois o numseq sem o [I\_N\_S\_D\_T\_](https://tdn.totvs.com/x/ZxedIQ) pode trazer dados antigos.

Os casos onde a apropriação não é sequencial e não utilize o **MV\_SEQ300**, a ordenação segue outras regras (entradas, movimentos internos e saídas), **caso os movimentos com NumSeq duplicado estejam no mesmo período de fechamento, podem gerar erros no calculo do custo por inconsistência nas ordenações e, consequentemente, na apropriação do custo e fechamento.**

**Qual o motivo de possuir campos duplicados atualmente?**

Essa situação pode ocorrer em ambientes cujo as chaves [specialkey](https://tdn.totvs.com/x/BRY1Gg)e [checkspecialkey](https://tdn.totvs.com/pages/viewpage.action?pageId=840763998#:~:text=de%20como%20ficar%C3%A1%3A-,checkspecialkey,-%3D%201%0AA%20altera%C3%A7%C3%A3o)não estejam configuradas corretamente, gerando falhas ou lacunas no controle de numeração em seu ambiente.

**O controle de numeração do NumSeq depende da correta configuração do License Server na chave @@@SD2.**

* [2024 - 31/10 Parâmetro MV\_DOCSEQ](https://tdn.totvs.com/x/XgodMg)

**E como efetuar o ajuste dos sequencias duplicados?**

Sugerimos que seja validado junto a um analista DBA ou solicitação de um analista in loco (verificar detalhes a respeito de valores para alocação do analista com o gerente de contas da unidade TOTVS responsavel por seu contrato), pode ser usada, como base para a correção, a documentação dos campos e tabelas envolvidas (<https://tdn.totvs.com/x/IsP7Og>).

**Realizei os ajustes e a Sequência da Numeração ainda estão sendo criadas incorretamente. O que Fazer?**

Para esse cenário verificar se é o caso reportado na FAQ abaixo, e sugestivel que seja validado juntamente com um analista in loco.

[SIGAEST - Campos \_NUMSEQ repetidos mesmo após apagar lsnumber.val e reiniciar o License Server](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36253990471191-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Campos-NUMSEQ-repetidos-mesmo-ap%C3%B3s-apagar-lsnumber-val-e-reiniciar-o-License-Server)

Relacionados a problemas sequencias das movimentações:

[Backoffice (Linha Protheus) - SIGAEST - Alteração no tamanho de campos NUMSEQ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35278948195351-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Altera%C3%A7%C3%A3o-no-tamanho-de-campos-NUMSEQ)

*Saiba mais:*

[Clique aqui e veja mais artigos sobre Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001533821-Estoque-e-Custos-SIGAEST)
