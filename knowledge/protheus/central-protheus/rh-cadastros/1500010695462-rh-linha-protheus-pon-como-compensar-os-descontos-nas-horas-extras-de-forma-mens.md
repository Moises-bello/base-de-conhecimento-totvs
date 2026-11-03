---
article_id: 1500010695462
category: RH - Cadastros
content_hash: b57e00acc37a2203309e2fdb6cbabfb3ecef771a32c57ebbd146d75d8f59813c
fetched_at: '2026-06-28T22:44:52.827564+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como compensar os Descontos nas Horas Extras de
  forma Mensal
type: support-article
updated_at: '2026-02-04T14:15:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010695462-RH-Linha-Protheus-PON-Como-compensar-os-Descontos-nas-Horas-Extras-de-forma-Mensal
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35353179219735) Tempo aproximado para leitura: 00:02:00 min**  
  
**Dúvida**  
Como configurar no módulo de Ponto Eletrônico para que o sistema realize a compensação mensal das faltas, atrasos e demais ocorrências nas horas extras?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Em **Atualizações - Cadastro  do Ponto -  Regra de Apontamento - aba Apontamentos**, os campos **Pg.Hrs.Norm** e **Hr.Norm.Fol** deverão estar como = **Sim:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18257718291479)

Na aba **Apuração,** as apurações deverão ser **mensais**:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407602933015)

Na aba **Horário Móvel,** o horário deverá ser **Livre**:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407602960535)

Nos **apontamentos das marcações, em Atualizações - Lançamentos - Marcações - localizar o funcionário e clicar em Atualizar - clicar com F9 para ser possível visualizar as marcações + apontamentos,** serão apontadas todas as **horas normais diariamente**, e quando ocorrer **Atraso** ou **Hora Extra** por exemplo, estes minutos/horas serão **acrescidos** na quantidade de **horas normais** do dia.

Nesse exemplo o horário padrão é das **08:00 12:00 13:00 17:00** – trabalha 08 horas diárias.

No dia 02/08/2021, funcionário realizou **01h hora extra.** Nos **apontamentos**, será gerado o evento de **horas normais** com **09h** horas, ou seja, a **soma das horas trabalhadas mais a hora extra realizada**.

No dia 03/08/2021, o funcionário atrasou 20 minutos. Nos **apontamentos,** será gerado o evento de **horas normais** com **07h40**, ou seja, **subtraindo o atraso das 08h diárias**.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407597734423)  
  
É **importante ressaltar** que quando toda a **apuração é Mensal**, o sistema **não gera os apontamentos de descontos e proventos**, ou seja, **todas as ocorrências são mostradas no evento de Horas Normais**.  
A rotina que faz a **validação** de possíveis **proventos ou descontos a serem gerados**, é o **Cálculo Mensal**, que deverá gerar a **verba** nos **Resultados do Funcionário**.  
Com isso, é **importante** também destacar que **não é possível o lançamento de qualquer tipo de Abono ou de Código Informado.**

Com os **Apontamentos** gerados no período, deverá ser feito o **Cálculo Mensal** em **Miscelânea - Cálculos - Cálculo Mensal**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14125333767575)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14125334961559)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14125336022935)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14125337201943)

Para **conferência** das **verbas geradas**, deverá acessar **Atualizações - Lançamentos - Resultados**.  
No exemplo citado, veja que foi apontado apenas **uma verba de Hora Extra com 0,66 centesimais** (em horas **Sexagesimais**, teríamos **40 min de Hora Extras,** mas cabe relembrar que na rotina de **Resultados** visualizamos os lançamentos apenas em **Centesimal** para a correta **integração** e **cálculo** da **Folha de Pagamento**):

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407605092503)  
  
**Importante:** quando o funcionário Faltar, o desconto será aplicado através do evento/verba de Saída Antecipada, e não de Falta. Como estamos trabalhando com apuração Mensal e Horário Móvel Livre, o que deixa de ser trabalhado durante o período é apontado como Saída Antecipada.

**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
