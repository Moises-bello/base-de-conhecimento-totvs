---
article_id: 5970867618967
category: Cadastros
content_hash: 969df9524d3315540a54442bf46299b5d43fa23f3c80136df3b2706e431236be
fetched_at: '2026-06-28T22:47:36.370592+00:00'
product: rm
section_id: 1500000834961
source: central-rm
title: RH - RM - SMT - Utilizar o campo 'Data Inicial da Continuidade de Afastamento'
  ao cadastrar o atestado
type: support-article
updated_at: '2026-06-01T14:14:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5970867618967-RH-RM-SMT-Utilizar-o-campo-Data-Inicial-da-Continuidade-de-Afastamento-ao-cadastrar-o-atestado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16035698504471) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como utilizar o campo 'Data Inicial da Continuidade de Afastamento' ao cadastrar o atestado?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional  - 12.1.XX.XX

**Solução**  
Para utilizar o campo 'Data Inicial da Continuidade de Afastamento', siga os passos abaixo:  
  
Acesse no módulo de Folha de Pagamento o menu **Configurações** | **Parametrizador** e ao abrir o assistente, selecione o processo **06.01.03 - Folha Normal** e avance até a etapa **Afastamento 1/2** e marque a parâmetro **'Habilita controle manual de continuidade de afastamentos com Atestado Médico':**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26924614762647)

Quando marcado o parâmetro é habilitado o controle manual de continuidade de afastamentos com Atestado Médico e utilizamos a continuidade do afastamento, preenchendo o campo **'Data Inicial da Continuidade de Afastamento'**.  
  
O sistema não verifica mais se o motivo do afastamento é igual nos cadastros de atestados para realizar o cálculo de dias de afastamento. **O cálculo dos dias de atestado irá somar os dias do afastamento que inicia a sequência de continuidade (registro Pai), com os dias de afastamento que possuem no campo de relacionamento a informação do registro inicial (Pai). Estes chamados de registros Filhos.**  
  
***Obs:**A soma dos dias deste relacionamento será limitada a 15 dias para a definição do período de Atestado Médico a ser pago pela Empresa ao funcionário, respeitando o intervalo informado no parametrizador da Folha de Pagamento, campo "Dias de carência para afastamento com atestado médico".*  
  
No momento do cadastro do Atestado, caso o **motivo de afastamento seja dos tipos P (Previdência), T (Acidente de Trabalho) e O (Doença Ocupacional), no campo "Data Inicial da Continuidade de Afastamento"** será permitido cadastrar uma continuidade de afastamento gerados por atestados do mesmo tipo ou tipos diferentes, inseridos anteriormente, desde que sejam com data anterior à data de início do novo atestado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26924586512663)

**Saiba mais:**  
Para mais informações, acesse: 

- [Atestados](https://tdn.totvs.com/display/public/LRM/Atestados)

- [Parametrizador - Habilita controle manual de continuidade de afastamentos com atestado médico](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719376)

- [RH - RM - SMT - Cadastrar atestado que gera afastamento no TOTVS Folha de Pagamento (RM Labore)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009848952)
