---
article_id: 360048543893
category: SIGAEST - CUSTOS
content_hash: 7c50a19f5abd8f7a12ff68711e7ed5ce4717691d0f52236a2bce7b96b18712f1
fetched_at: '2026-06-28T22:39:02.078470+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330  - Execução
  de Schedule Custo Médio
type: support-article
updated_at: '2026-06-25T15:47:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048543893-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Execu%C3%A7%C3%A3o-de-Schedule-Custo-M%C3%A9dio
---

O artigo explica como executar a rotina MATA330 via Schedule no TOTVS Protheus para recálculo de custo médio, destacando que apenas o cálculo de custo é realizado automaticamente; a contabilização deve ser feita manualmente. Detalha o passo a passo para agendamento, configuração de parâmetros e consulta de logs no sistema.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38187275015703) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

Como executar a rotina MATA330 via Schedule?

**Ambiente**:

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

**IMPORTANTE**: Apenas a etapa de calculo de custo é efetivada via schedule, **a etapa de contabilização não é feita para utilização via Schedule e nem Execauto****,** sendo assim a etapa de contabilização tem sua funcionalidade apenas de forma sistemica via rotina.

[Cross Segmento - Backoffice Linha Protheus - ADVPL - Existe ExecAuto() para o programa MATA331](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047674113-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Existe-ExecAuto-para-o-programa-MATA331?source=search)

**Referente a função LastDay:**

Esta função retorna as informações relacionadas a data informada no parâmetro dData conforme o tipo de ação a ser executada definida através do parâmetro nTipo.

**Referente a utilização da formula DATE():**

Para que o custo médio, sempre pegue a ultima data referente a data do ambiente, pode-se utilizar a função DATE(), dessa forma os perguntes referente a data limite final, serão desconsiderados.

**Saiba mais sobre a utilização da função:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=6815100>

Abaixo vídeo exemplo:

<https://tdn.totvs.com/pages/viewpage.action?pageId=23889224>

## **Cadastrando no novo schedule passo a passo:**

### **1- Inicie os serviços, normalmente sera iniciado 3 jobs:**

```
[OnStart]
jobs=FWSCHDMANAG_ENVIRONMENT,FWSCHDQUEUE_ENVIRONMENT
RefreshRate=120

[FWSCHDMANAG_ENVIRONMENT]
Main=FWSCHDMANAG
Environment=ENVIRONMENT

[FWSCHDQUEUE_ENVIRONMENT]
Main=FWSCHDQUEUE
Environment=ENVIRONMENT
```

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38187275018519)

### **2 - Inicie o agendamento em "Novo" e digitando o codigo da rotina "MATA330" em seguida "Avançar"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38187288808855)

### 

### **3 - Informe a periodicidade do seu agendamento, conforme sua necessidade.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38187275019287)

### **4 - Configure os parametros conforme sua necessidade**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38187275019799)

Ao clicar em "Editar parametros" sera aberto os parametros para definição.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41464975042071)

A função de contabilizar **não esta disponivel**, apenas se for efetuado customização, conforme descrito no inicio do boletim, então mantenha esse pergunte assim.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41464975042839)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41464990013207)

### **5 - Confirme o agendamento**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38187275020695)

### **6- Aqui voce pode observar o agendamento, e sua finalização quando efetuar. Voce tambem pode consultar o log de processamento diretamente na tabela CV8 caso desejar.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38187275021463)

Para mais informações como quais tabelas são envolvidas do Recálculo do Custo Médio via Schedule [**clique aqui**](https://tdn.totvs.com/pages/viewpage.action?pageId=545626605)**.**

Para saber como configurar o Schedule, fazer o agendamento de outras rotinas envolvidas por gentileza [**clique aqui.**](https://tdn.totvs.com/pages/viewpage.action?pageId=271167961)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)
