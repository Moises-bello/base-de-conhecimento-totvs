---
article_id: 360015277692
category: Administração de Pessoal
content_hash: b133087a084ce19444257e3a60da8c8b4ddb1c6f981b45455f1c9e6d46bb0c21
fetched_at: '2026-06-28T22:47:02.326385+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: 'RH - RM - FOP - Média: Sistema paga valor do último lançamento como média'
type: support-article
updated_at: '2025-01-20T21:35:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015277692-RH-RM-FOP-M%C3%A9dia-Sistema-paga-valor-do-%C3%BAltimo-lan%C3%A7amento-como-m%C3%A9dia
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:30 min  
  
Ocorrência**No módulo **Folha de pagamento**, ao tentar realizar algum **Cálculo de rotinas que tenham médias  de férias ou 13º**, o valor pago de médias não é calculado corretamente, pois um ou mais eventos estão sendo pagos com base no valor do último lançamento do evento e não na divisão parametrizada no sindicato na opção **número de meses**.  
  
O trecho do log de médias fica assim:  
*Calculando média do evento tipo D, **Último Valor**: 0002 - DIAS TRABALHADOS**Mês 09/2011: 30,00 \* 1,00 (%inc.) \* 36,666667 = 1.100,000000**TOTAL = 13.200,00***Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Esse incidente ocorre, pois no cadastro do evento calculado incorretamente no menu anexos, Eventos de média a flag **Evento último valor** está habilitada.  
  
Com a flag **Evento último valor**habilitada, o sistema buscará na movimentação do funcionário o maior valor pago referente ao evento parametrizado para médias e efetuará o pagamento deste valor.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o cadastro do evento **pago incorretamente nas médias**;  
  
2. Acesse o **menu Anexos | Eventos de média**;  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6190336448023/mceclip0.png)  
  
3. Na **aba Eventos de média**, localize a média/grupo correspondente ás médias pagas de forma incorreta;  
  
4. Edite a linha correspondente e desmarque a **flag Evento último valor**:  
  
![Sem_t_tulo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360010455112/Sem_t_tulo.png)  
  
Após desmarcar a flag acima, o sistema realizará o cálculo das médias respeitando a divisão parametrizada no sindicato na opção **Número de meses.**
