---
article_id: 17203402479255
category: eSocial - Parametrizador
content_hash: 837d43ad89d444ffb7642dff02d50e7a223d113bf6652a81e203d81983efda50
fetched_at: '2026-06-28T22:47:06.269968+00:00'
product: rm
section_id: 1500000834501
source: central-rm
title: 'RH - RM - FOP - eSocial - Parametrizador eSocial: Configurações Gerais 6/7'
type: support-article
updated_at: '2026-04-27T17:30:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17203402479255-RH-RM-FOP-eSocial-Parametrizador-eSocial-Configura%C3%A7%C3%B5es-Gerais-6-7
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19541468102807)** Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Como configurar a etapa **Configurações Gerais 6/7** do parametrizador eSocial? **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**

Devido a instrução liberada no Manual de Orientação do eSocial do leiaute S-1.0, o recibo de férias do funcionário passa a ser apresentado no XML do S-1200. Assim, para que não houvesse duplicidade de registros, foi necessário a criação do **De/Para para substituição das verbas do envelope no XML (com exceção do evento Abono Férias, que substitui a verba do recibo).**

Para preenchimento dos campos, será necessário a criação de novas verbas considerando as orientações abaixo:

**- Evento IRRF Férias envelope (Desconto)**

Desconto, sem código de cálculo, sem incidências e com natureza da rubrica 9299 - Outros descontos não previstos nos itens anteriores

**- Evento Pensão Férias envelope (Desconto)**

Desconto, sem código de cálculo, sem incidências e com natureza da rubrica 9299 - Outros descontos não previstos nos itens anteriores

**- Evento INSS Férias Alíquota Normal envelope (Base de Cálculo)**

Base de cálculo, sem código de cálculo, sem incidências.

**- Evento INSS Férias Próximo Mês Alíquota Normal Envelope (Base de Cálculo)**

Base de cálculo, sem código de cálculo, sem incidências.

**- Evento Abono Férias envelope (Provento)**

Provento, sem código de cálculo, sem incidências

**- Evento INSS Férias envelope (Desconto)**

Desconto, sem código de cálculo e sem incidências.  
(Este evento deverá ser informado no parametrizador antes de gerar o XML S-1010, para que a incidência seja gerada corretamente)

**- Evento INSS Férias Próximo mês envelope (Desconto)**

Desconto, sem código de cálculo e sem incidências.

**Importante**  
A TOTVS não orienta qual natureza de rubrica deve ser informada nas verbas, ficando tal escolha a cargo da própria empresa. O que podemos orientar é que a natureza esteja condizente com o Anexo I do Layout eSocial utilizado.

Antes de enviar o S-1200, é necessário enviar o S-1010 das verbas criadas. Para isso, faça a edição dos gatilhos do S-1010 que serão gerados na fila de eventos do eSocial, informe no campo **Competência** um mês e ano igual ou anterior ao período de apuração do S-1200 e transmita os S-1010 para o governo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17203372363159)

**Saiba mais**  
Para maiores informações, acesse:

• [Configurações Gerais 6/7](https://tdn.totvs.com/pages/releaseview.action?pageId=540899121)  
• [S-1200 e S-1210: Recibo de Férias no leiaute S-1.0](https://tdn.totvs.com/pages/viewpage.action?pageId=627729108)  
• [Configurações Gerais 7/7](https://tdn.totvs.com/pages/releaseview.action?pageId=645896860)
