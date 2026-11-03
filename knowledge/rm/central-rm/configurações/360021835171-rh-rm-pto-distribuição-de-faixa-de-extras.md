---
article_id: 360021835171
category: Configurações
content_hash: 20eeae9ff94a88dbc8906469bab274eebcb2629b9451d5a50b0df18d807655c5
fetched_at: '2026-06-28T22:46:29.922821+00:00'
product: rm
section_id: 1500000835121
source: central-rm
title: RH - RM - PTO - Distribuição de Faixa de Extras
type: support-article
updated_at: '2025-02-19T00:35:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021835171-RH-RM-PTO-Distribui%C3%A7%C3%A3o-de-Faixa-de-Extras
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19409227012503) Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**Como configurar a distribuição de extras, para que a 1º Faixa de extra fique no banco e 2º Faixa de extra para movimento?

**Ambiente**RH - RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões.  
  
**Solução**Para realizar tal parametrização deverá realizar seguintes passos:

**1.** Acesse no módulo de **Automação de Ponto,**o menu **Configurações | Parametrizador** ao abrir o assistente clique em avançar e selecione o processo**08.02 - Sindicato** e edite o sindicato que terá a diferenciação das extras referente ao intervalo de ausência planejada. ![](https://centraldeatendimento.totvs.com/hc/article_attachments/19409227014039)

**2.** Avance até a etapa **Faixas de Extras, e**  preencha os campos da **1ª faixa de extras** e **2ª Faixa de extras,** com seus respectivos valores:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018509711)

**3.** Na etapa **Banco de Horas:** Deverá definir o **Tipo de banco de horas** como **Diário** e **marque** os parâmetros **Utiliza banco de horas por ocorrência** e **Considera atitude do Evento:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018509811)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018509891)

**4.** Na etapa de **Eventos**, deverão existir os eventos de 1º Faixa de Extra e 2º Faixa de Extras, vinculados ao eventos de Folha de Pagamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018509971)

**5.** Para o evento de 1º Faixa de Extra, deverá selecionar e clicar na opção de editar:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018510011)

Clique na aba, **Informações Adicionai**s deverá marcar opção **banco de horas**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018510031)

**6.** Para o evento de 2º Faixa de Extra, deverá selecionar e clicar na opção de editar:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018510071)

 Na aba **Informações Adicionais** deverá marcar opção **Movimento**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018510111)

**Observação**: Caso deseje, os dois eventos podem ser enviados para movimento ou banco de horas, e ter valores de pagamento diferentes para cada evento. Neste caso associe um evento do Folha de pagamento, com o respetivo percentual a ser aplicado.

**Saiba mais**  
Para orientações exemplificando a distribuição das faixas de extras, acesse as informações no link abaixo:  
[Faixas de Extras](https://tdn.totvs.com/display/public/LRM/Faixas+de+Extras)
