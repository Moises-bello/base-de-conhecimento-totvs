---
article_id: 24899919963671
category: SIGAEST - CUSTOS
content_hash: 8ffc47f9d83e3e7b99e4145e2da3fc3725050a213a43d0476fe9d813acd70b38
fetched_at: '2026-06-28T22:39:02.219393+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Tentativa
  de reservar registro no alias TRT em EOF Stack - MSRLOCK.eof
type: support-article
updated_at: '2025-03-12T12:27:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24899919963671-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Tentativa-de-reservar-registro-no-alias-TRT-em-EOF-Stack-MSRLOCK-eof
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24899928641559) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Durante o processamento da etapa de recalculo de custo médio, ocorre o erro: Tentativa de reservar registro no alias TRT em EOF Stack - MSRLOCK.eof, oque deve ser feito nessa situação?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Esse erro está relacionado à tabela TRT, que é vinculada ao parâmetro **MV\_MUDATRT**. Desde **15/05/2018**, o parâmetro **MV\_MUDATRT** foi descontinuado. então, tornou-se padrão mudar o nome das tabelas **TR's** das rotinas de Custo Médio (**MATA330**) e Virada dos Saldos (**MATA280**) para evitar conflitos de alias.

A mensagem "**EOF Stack em MSRLOCK**" indica que a rotina tentou reservar um registro para ser manipulado no processamento; mas o ponteiro da tabela estava em **FIM DE ARQUIVO (MODO EOF)** pois não localizou o dado procurado na Tabela.  
Ou seja, algum dado (relacionado a este registro que está sendo processado) está inválido / não foi localizado, apresentando quebra de integridade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24899919960343)

**Como corrigir esse problema no processamento:**

* Confirme se o parâmetro **MV\_MUDATRT** está configurado com o conteudo **.T.** caso esteja, altere para **.F.**
* O Protheus possui o parâmetro [**MV\_TTS**](https://tdn.totvs.com/pages/releaseview.action?pageId=6814812) que quando ativado garante que este processo exista nos processos críticos de transação de arquivos.
* Valide se o ambiente possui a atualização mais recente do mês vigente ([Atualizações](https://tdn.totvs.com/pages/releaseview.action?pageId=550332596#OINF0011.2-Atualiza%C3%A7%C3%B5esProtheus-Modulos)).
* Avalie se foi efetuado alguma manutenção nos tamanhos de campos das tabelas relacionas ao processo de custo medio (ex: SB1,SB2,SD1,SD2,SD3)
* Reinstale a procedure **19** e **20** do ambiente após alteração do parametro ([como reinstalar a procedure](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-e-Incompat%C3%ADvel-quais-as-diferen%C3%A7as-%C3%89-poss%C3%ADvel-utilizar-as-rotinas)).
* Reinicie os serviços, valide se os perguntes de processamento da rotina de custo médio, estão corretamente configurados de acordo sua necessidade, e então refaça o processamento da rotina novamente.

***Esse processo, pode efetuar a correção para a regravação do arquivo de processamento TR's com as novas nomenclaturas.***

**Efetuei os procedimentos, porém o erro ainda persiste durante o processamento:**

* Verifique se o arquivo **MSRLOCK.EOF** gravado na pasta **system, se** existe alguma customização no sistema que envolva o ALIAS da tabela apresentado na mensagem, caso exista, efetue um teste com a customização desativada, você pode identificar se tem uma customização no processamento, se existir uma linha iniciando com **U\_** na instrução do arquivo, então refaça o teste novamente de processamento ([Como desativar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292--Cross-Segmentos-Linha-Protheus-Como-ativar-e-desativar-customiza%C3%A7%C3%B5es-no-Protheus)).

**Nenhum procedimento surtiu efeito para o processamento:**

Nesse caso, sera necessario uma avaliação no ambiente cliente, para que acesse remotamente a sua base, visando avaliação/ debug da rotina para investigá-la e identificar a origem do problema, para tal o suporte podera prosseguir mediante a consultoria do modulo para investigação do problema apresentado em seu ambiente.

[**Guia de Relacionamentos**](https://tdn.totvs.com/x/nVi_Jg)**-** Aba: Modalidade de Atendimento > Suporte Técnico

**Saiba mais:**

*[MP - SIGAEST - Rotina MATA330 - Perguntas do Recálculo do Custo Médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024805291)*

*[MP - SIGAEST - MATR900 - Interpretando o Custo no Kardex antes e depois do Recálculo do Custo Médio (com exemplo prático)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005781102)*

*[MP - SIGAEST - Como extrair arquivo de trabalho TRB ao executar o Recálculo do Custo Médio (MATA330)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011904591-MP-SIGAEST-Como-extrair-arquivo-de-trabalho-TRB-ao-executar-o-Rec%C3%A1lculo-do-Custo-M%C3%A9dio-MATA330-)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
