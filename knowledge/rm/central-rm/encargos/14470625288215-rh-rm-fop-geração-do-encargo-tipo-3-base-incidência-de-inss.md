---
article_id: 14470625288215
category: Encargos
content_hash: f4265ea5eeced357ac7c3fa1cc0924dc068ece4fff10721d71279f6477960b6c
fetched_at: '2026-06-28T22:46:52.342232+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - Geração do encargo TIPO 3  Base: incidência de INSS'
type: support-article
updated_at: '2025-01-07T17:27:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14470625288215-RH-RM-FOP-Gera%C3%A7%C3%A3o-do-encargo-TIPO-3-Base-incid%C3%AAncia-de-INSS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18493191050519) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como fazer geração do encargo TIPO 3 Base: incidência de INSS ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**O encargo tipo 3 - Base: incidência de INSS é padrão do sistema, a porcentagem é habilitada para esse encargo e obrigatório o preenchimento:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14469906863895)

O Encargo Contábil com informação de rateio que o encargo segue não seguirá o Rateio Fixo definido no cadastro de funcionários e SIM, seguirá ocorrência dos eventos que foram cadastrados no Rateio por Evento para que ele seja calculado. Ele só seguirá o Rateio Fixo definido no cadastro de funcionários, se os eventos cadastrados no Rateio por Evento não existirem na movimentação do funcionário. O código do rateio é definido no cadastro de Rateio de Eventos.  
   
Preenchendo o campo **Rateio que o Encargo segue** será obrigatório preencher também o **Período para Cálculo de Rateio** com um dos os seguintes períodos:  
**1 – Mês Atual -** Rateia conforme os rateios fixos informados no cadastro do funcionário.  
**2 – Período Aquisitivo –** Rateia conforme os rateios realizados durante o período aquisitivo de Férias.  
**3 – Ano de Competência –** Rateia conforme os rateios realizados durante o ano de competência atual.  
**4 - Mês Anterior –** Rateia de acordo com o rateio por centro de custo utilizado no mês anterior, tomando como base, a ficha financeira por centro de curto. Quando essa movimentação não existir o sistema deverá buscar o centro de custo do **Rateio Fixo** do funcionário.

Verifique o código ativo associado ao encargo para no momento da geração marcar o mesmo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14470092701975)

Log da geração do encargo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14470084520343)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14470647794967)

Observando que se no cadastro do encargo estiver marcado **Aplicar Percentual FAP por filial**:  
Marcando este parâmetro o valor do encargo será acrescido do seguinte calculo:  
**Valor base do encargo** multiplicado pelo **Percentual do FAP vigente** multiplicado pelo **Percentual do SAT - agora denominado RAT**  
Onde:  
  -**Valor base do encargo**: Valor obtido pelo sistema antes da aplicação do percentual informado na parametrização do encargo.  
  -**Percentual do FAP** vigente: Percentual informado na seção centralizadora da filial em **Cadastro | Seções | Anexo FAP por Estabelecimento  Empresarial**  
  -**Percentual do SAT**: Percentual informado no cadastro da seção do funcionário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14470286365207)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14470295111063)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14470492244247)

O valor do encargo irá mudar conforme as informações preenchidas:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14470491342103)  
 Caso o percentual Fap não seja considerado, verifique executar o processo manutenção do cadastro de seção.

**Saiba mais**  
[Encargos - Folha de Pagamento](https://tdn.totvs.com/display/public/LRM/Encargos+-+Folha+de+Pagamento)

[RH - RM - FOP - Manutenção do Cadastro de Seções](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058029994-RH-RM-FOP-Manuten%C3%A7%C3%A3o-do-Cadastro-de-Se%C3%A7%C3%B5es)
