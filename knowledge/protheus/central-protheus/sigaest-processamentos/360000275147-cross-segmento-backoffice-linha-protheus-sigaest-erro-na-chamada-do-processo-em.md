---
article_id: 360000275147
category: SIGAEST - PROCESSAMENTOS
content_hash: cc1b4b858f38c67330a4f7fc9dad6e9e98e7d84dd90ec286b136fa734e658f6e
fetched_at: '2026-06-28T22:39:04.843094+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Erro na chamada do
  processo em rotinas de Processamento
type: support-article
updated_at: '2026-06-12T15:54:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000275147-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Erro-na-chamada-do-processo-em-rotinas-de-Processamento
---

Durante o processamento de rotinas no TOTVS Protheus, pode ocorrer a mensagem "Erro na Chamada do Processo", especialmente em rotinas de estoque e custos. A solução inicial é desinstalar a procedure que gera erro, reiniciar os serviços e testar o processamento. Se o erro persistir, recomenda-se consultar a documentação específica para ambientes OnPremise ou Cloud e seguir as orientações para reinstalação ou análise detalhada.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20499020173975) **Tempo aproximado para leitura: 00:02:00 min**

**Ocorrência**

Durante o processamento de um rotina, é exibida a mensagem "**Erro na Chamada do Processo**". Por exemplo nas rotinas: Saldo Atual (MATA300), Virada de Saldos (MATA038/MATA280), Recalculo do Custo Médio (MATA330), Refaz Acumulados Empenhos (MATA215), Refaz Poder de Terceiros (MATA216) entre outras.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20501063304855)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

No vídeo abaixo demonstra um passo a passo sobre o que pode analisar para esse tipo de Erro nas PROCEDURES

**IMPORTANTE:**

**Primeiramente efetuar testes desinstalando a procedure da rotina que esta gerando o erro**, em seguida reiniciar os serviços do Protheus, acessar novamente o Protheus e processar a rotina.

Verificar se apresenta algum outro erro ou mesmo error.log. **Esse teste é essencial** para que possa identificar se o erro apresentado na PROCEDURE ocorre devido alguma inconsistência nos fontes e reflete nas PROCEDURES.

Saiba aqui quais são as procedures referente cada rotina do estoque: <https://tdn.totvs.com/x/wi3AFQ>

![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33013931342871)

Efetuando o processamento **SEM** a procedure, caso gerar um error.log nos envie para analise, caso processar sem erro, reinstale novamente a procedure, conforme a orientação desse boletim abaixo

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Procedure Desatualizada ou Incompatível](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-ou-Incompat%C3%ADvel)

Avalie a possibilidade de desativar as threads caso voce use, MV\_M330THR deixe com conteud de apenas 1.

**Se ainda o erro persistir após a reinstalação:**

Visando a melhor identificação e também o procedimento para correção do problema apresentado, centralizamos as informações de forma detalhada e separada por tópicos, dentre dois tipos de processo para clientes **OnPrimese**(Ambiente proprio hospedado) ou para cliente **CLOUD-TOTVS**.

Verifique os pontos da documentação abaixo e, após validação, retorne as informações ao time de suporte tecnico caso problema persista:

* [**Erro na chamada do Processo**](https://tdn.totvs.com/x/lEHyM)

**Saiba mais:**

[**Stored Procedures utilizadas no produto Estoque e Custos**](https://tdn.totvs.com/x/wi3AFQ)

[*Clique aqui e veja mais artigos sobre Processamentos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000275147)
