---
article_id: 29748851986071
category: SIGAEST - MOVIMENTAÇÕES
content_hash: a6ff4ae3d7ce8a66721860515092638ddec1de528af7249c8c1933cd94196c12
fetched_at: '2026-06-28T22:38:55.666410+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA103 - Por que
  o Sistema permite inserir uma Data de Emissão antiga no Documento de Entrada?
type: support-article
updated_at: '2025-04-10T20:14:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29748851986071-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA103-Por-que-o-Sistema-permite-inserir-uma-Data-de-Emiss%C3%A3o-antiga-no-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29748861527575) Tempo aproximado para leitura: **00:02:57 min** **Dúvida**Por que o Sistema permite inserir uma data Data de Emissão (D1\_EMISSAO) antiga no Documento de Entrada?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Se o usuário inserir um Documento de Entrada com uma Data de Emissão (D1\_EMISSAO) anterior ao ultimo fechamento, mesmo assim o Sistema permitirá.

O Sistema, por meio da rotina MATA103 - Documento de Entrada - compara a dDataBase com o conteúdo do MV\_ULMES pra dar ou não o help FECHTO. Ou seja, o dDatabase sempre vai olhar a data do sistema na parte superior direita (data do sistema). Ele não avalia neste momento o D1\_EMISSAO.

Algumas coisas que justificam:

- Pode acontecer do usuário digitar uma nota atrasada cuja emissão é outra data;

- Houve alguma perda de prazo e o usuário precisou digitar uma data que foi emitida no passado;

Portanto, o fonte da rotina faz o controle no arquivo SD1 pelo campo D1\_DTDIGIT que é alimentado pela data-base do Sistema, que é justamente o ponto que permite ou não passar o movimento sem dar o FECHTO.

**É possivel criar uma trava para o usuário nunca preencher o D1\_EMISSAO menor do que o MV\_ULMES?**

É possível criar validações através de pontos de entrada. Segue documentação da listagem dos pontos de entrada do fonte MATA103 para avaliar qual melhor atenderá mesta demanda: **[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Pontos de entrada do Documento de Entrada - MATA103](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006469332-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Pontos-de-entrada-do-Documento-de-Entrada-MATA103)**

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
