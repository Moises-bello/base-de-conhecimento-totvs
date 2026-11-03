---
article_id: 360024947114
category: Treinamento
content_hash: a953b222b4441747041869986c7543f0ee89d4741d570a2b7e1b44122df0a01b
fetched_at: '2026-06-28T22:47:26.012664+00:00'
product: rm
section_id: 1500000861342
source: central-rm
title: RH - RM - RHU -  Gerar abonos de treinamento
type: support-article
updated_at: '2025-09-25T14:50:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024947114-RH-RM-RHU-Gerar-abonos-de-treinamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15864231753239) Tempo aproximado para leitura: 00:01:30 min  
  
Dúvida**Como gerar abonos de treinamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - Todas as versões  
  
**Solução**

Para resolução da dúvida, siga os passos a seguir:

- Em **Configurações** | **Parametrizador** | **Treinamentos** e preencha o campo **'*Tipo de abono para treinamento'*** que deverá ser considerado para geração do abono no RM Chronus (Automação de Ponto).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35193431001111)

- Acesse **Desenvolvimento** | **Turmas** | **Anexos** | **Aula** e marque a opção **'*Gerar Abono?'***, caso a aula em questão tenha que gerar abonos para os participantes.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35193431003543)

**Importante**Se qualquer participante da turma tiver registro de ausência na aba Controle de ausência, que se encontra no cadastro da aula, não será gerado o abono para este participante para o período em que ocorreu a ausência.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039300353)

- Ao realizar o fechamento da turma, o sistema automaticamente irá gerar os abonos para os participantes da turma para cada período de aula (data de treinamento e duração do treinamento) existente na turma.

**Atenção**Para que os abonos sejam gerados para os participantes, será sempre verificado:

* Se o participante desistiu do treinamento: neste caso, não serão gerados os abonos a partir da data de desistência;
* Se o participante ausentou de alguma aula do treinamento: neste caso, não serão gerados os abonos para as estas aulas.

O abono será visualizado no espelho ao efetuar o recálculo do ponto no Totvs Automação do Ponto ( RM Chronus).

**Saiba Mais**

Para maiores informações, acesse:

- [Aulas](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719643)

- [Parametrizador - Treinamento](https://tdn.totvs.com.br/display/public/LRM/Treinamento)
