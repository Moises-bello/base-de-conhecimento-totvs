---
article_id: 1500007810221
category: SIGAEST - CUSTOS
content_hash: f5673fbb01008b3728fd6f710df50229fe5e9e21f6dfd83823edaf27b6e6157b
fetched_at: '2026-06-28T22:39:02.224577+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - THREAD
  ERROR - Argument #0 error, expected N->U, function str on A330TT2B2(M330JCTB.PRX)'
type: support-article
updated_at: '2022-09-26T12:53:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007810221-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-THREAD-ERROR-Argument-0-error-expected-N-U-function-str-on-A330TT2B2-M330JCTB-PRX
---

**Ocorrência**Ao executar o Recálculo do Custo Médio (MATA330), ocorre o seguinte error.log: *"THREAD ERROR - Argument #0 error, expected N->U, function str on A330TT2B2(M330JCTB.PRX)"*.  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Causa**O erro "argument #0 error, expected N->U, function str on A330TT2B2" ocorre normalmente quando a variável está esperando um valor numérico, porém está recebendo um valor nulo ou com caractere especial.   
  
**Solução**

Devido à mensagem apontar diferença de tipo de variável entre a esperada e a recebida, uma primeira análise pode ser feita nas seguintes tabelas:

- SB2 (Saldo Físico e Financeiro);

- SB6 (Poder de Terceiros);

- SB9 (Saldos Iniciais);

- SD1 (Itens das Notas de Entrada);

- SD2 (Itens das Notas de Saída) e

- SD3 (Movimentos Internos).

Avaliar se será identificado algum campo com valor nulo ou caractere especial. Caso contenha, avaliar como foi gerado este movimento e analisar internamente como efetuar o ajuste para recriação do campo sem caractere especial ou valor nulo.

**Caso não tenha nenhum problema nas tabelas com relação à valor nulo e caractere especial**

Se este for o seu cenário, avaliar qual a data do fonte M330JCTB.PRX contido no ambiente. Segue abaixo o pacote pontual deste fonte, além do pacote acumulado do Estoque/Custos contido com o mesmo fonte:

**Pacotes acumulados Estoque/Custos:**

12.1.23 - [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/748747)   **|** 12.1.25 - [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/826640)**|** 12.1.27 - [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/960571) 

**Pacote pontual M330JCTB.PRX:**

12.1.23 - [Clique aqui](https://r.totvs.io/p/1013042) **|** 12.1.25 - [Clique aqui](https://r.totvs.io/p/1013043) **|** 12.1.27 - [Clique aqui](https://r.totvs.io/p/1013044)

**Observação:** Sempre efetuar qualquer atualização primeiramente em ambiente de homologação.

**Saiba mais:**

*[MP - SIGAEST - Rotina MATA330 - Perguntas do Recálculo do Custo Médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024805291-MP-SIGAEST-Rotina-MATA330-Perguntas-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio)*

*[MP - SIGAEST - MATA330 - Error.log "DBCopyStruct - Invalid RDD CTREE on MA330PROCESS"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004750651-MP-SIGAEST-MATA330-Error-log-DBCopyStruct-Invalid-RDD-CTREE-on-MA330PROCESS-)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
