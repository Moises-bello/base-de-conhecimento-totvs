---
article_id: 18894719561239
category: RH - Lançamentos
content_hash: e69397052c8e056cbdeab80f9ec3cca06b52fb2dffee3eb883375051aed02497
fetched_at: '2026-06-28T22:44:46.891597+00:00'
product: protheus
section_id: 32419271673111
source: central-protheus
title: RH - Linha Protheus - PON - Qual a funcionalidade do parâmetro MV_ADNOTHR na
  geração dos apontamentos de horas extras
type: support-article
updated_at: '2025-10-09T16:45:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18894719561239-RH-Linha-Protheus-PON-Qual-a-funcionalidade-do-par%C3%A2metro-MV-ADNOTHR-na-gera%C3%A7%C3%A3o-dos-apontamentos-de-horas-extras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18894746647831) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Qual a funcionalidade do parâmetro MV\_ADNOTHR na geração dos apontamentos de horas extras?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
 **Solução**O parâmetro **MV\_ADNOTHR** foi criado para permitir que a apuração do **horário móvel livre** seja feita através de horas corridas, sem considerar a hora reduzida como parte da jornada prevista pelo funcionário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18913743652759)

Quando o parâmetro estiver **ativado (.T.)** o sistema **não**irá considerar a hora reduzida como parte da jornada prevista do funcionário. Por exemplo: o funcionário precisa realizar 4 horas diárias. Independentemente se o horário é noturno ou diurno, se o funcionário trabalhar as 4 horas previstas não será gerado qualquer evento de Hora Extra ou Saída Antecipada, mas se caso o funcionário realizar em horário noturno as 4 horas previstas, será pago o adicional noturno normalmente, porém, sem gerar qualquer hora extra.

Quando o parâmetro estiver **desativado (.F.)** a apuração das horas será feita respeitando o conteúdo dos campos **Con.H.N.Tab** e **Con.H.N.Tb.I** existentes no cadastro do Turno de Trabalho.  
  
Abaixo exemplos de como fica o apontamento para **Horário Móvel Livre** quando o parâmetro MV\_ADNOTHR estiver habilitado (.T.) e desabilitado (.F.)

**MV\_ADNOTHR = .T.**

O sistema irá considerar horas corridas para definir se irá gerar Hora Extra ou Saída Antecipada

Tabela de Horário Padrão: 18:00 - 22:00 - 23:10 - 02:40

Considerado as horas corridas temos:  
das 18:00 às 22:00 = 04:00   
das 23:10 às 02:40 = 03:30  
Totalizando **07:30 de trabalho previstas**

Marcações realizadas pelo funcionário: 17:30 - 20:54 - 22:04 - 02:25

Considerado as horas corridas temos:  
das 17:30 às 20:54 = 03:24   
das 22:04 às 02:25 = 04:21  
Totalizando **07:45 de trabalho realizadas**

Os eventos gerados pelo sistema será:

**Hora Extra:**

Diferença entre o Horário realizado e o previsto: 07:45 - 07:30 = 00:15 como essa hora extra foi realizada em horário noturno é aplicada a hora noturna reduzida, gerando:  
**00:17  de Hora Extra Noturna**  
**00:17 de Adicional Noturno sobre Hora Extra**

**Horas Normais Trabalhadas:**

das 17:30 às 20:54 = **03:24 Horas Diurnas normais**  
das 22:04 às 02:10 (depois das 02:10 são horas extras) = 04:06 aplicando a hora noturna reduzia temos **04:41 Horas Noturnas Normais** e **04:41 de Adicional Noturno**

**MV\_ADNOTHR = .F.**

O sistema irá utilizar a Hora Noturna Reduzida para definir as horas previstas e se será gerada HE ou saída antecipada

Tabela de Horário Padrão: 18:00 - 22:00 - 23:10 - 02:40

Considerado as horas noturnas reduzidas temos:  
das 18:00 às 22:00 = 04:00   
das 23:10 às 02:40 = 03:30 → Hora Noturna → 04:00  
Totalizando **08:00 de trabalho previstas**

Marcações realizadas pelo funcionário: 17:30 - 20:54 - 22:04 - 02:25

Considerado as horas noturnas reduzidas temos:  
das 17:30 às 20:54 = 03:24   
das 22:04 às 02:25 = 04:21 → Hora Noturna → 04:58  
Totalizando **08:22 de trabalho realizadas**

Os eventos gerados pelo sistema será:

**Hora Extra:**

Diferença entre o Horário realizado e o previsto: 08:22 - 08:00 = 00:22, já está aplicada a hora noturna, gerando:  
**00:22  de Hora Extra Noturna**  
**00:22 de Adicional Noturno sobre Hora Extra**

**Horas Normais Trabalhadas:**

das 17:30 às 20:54 = **03:24 Horas Diurnas normais**  
das 22:04 às 02:05 (depois das 02:05 são horas extras) = 04:01 aplicando a hora noturna reduzia temos **04:35 Horas Noturnas Normais** e **04:35 de Adicional Noturno**

**Importante:** Por padrão, o conteúdo do parâmetro será preenchido com .T.  
  
**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download?e=1080347)
