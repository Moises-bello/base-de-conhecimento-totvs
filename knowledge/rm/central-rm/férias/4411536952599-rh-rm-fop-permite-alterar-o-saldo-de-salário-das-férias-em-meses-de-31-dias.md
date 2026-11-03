---
article_id: 4411536952599
category: Férias
content_hash: 834e66df7f2d4e877ae808a97d81abbf69cf65dfda3da4761e8013ca6c4deb7e
fetched_at: '2026-06-28T22:46:56.374562+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: RH - RM - FOP - Permite alterar o saldo de salário das férias em meses de 31
  dias
type: support-article
updated_at: '2024-09-16T18:30:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411536952599-RH-RM-FOP-Permite-alterar-o-saldo-de-sal%C3%A1rio-das-f%C3%A9rias-em-meses-de-31-dias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:43 min** **Dúvida**Qual a funcionalidade do parâmetro **Permite alterar o saldo de salário das férias em meses de 31 dias**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**O parâmetro **Permite alterar o saldo de salário das férias em meses de 31 dias** está localizado em: **Configurações | Parametrizador | Férias | Cálculo 1\2**. 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8904193306775/mceclip0.png)

Marcando este parâmetro, o sistema irá permitir que o usuário some mais um dia trabalhado ou horas normais correspondente a um dia, quando ocorrerem férias em meses de 31 dias.  
  
**Exemplo**  
Férias de 10/10 a 08/11  
Considerando mês de Outubro - Dias trabalhados = 8 dias

* **Se o parâmetro estiver marcado:** o sistema permitirá que o usuário poderá alterar os dias trabalhados para 9 que o sistema permitirá o cálculo, pois Outubro tem 31 dias.
* **Se o parâmetro estiver desmarcado:** o usuário alterar os dias trabalhados para 9 dias, ao realizar o recálculo, o sistema retornará para 8 dias trabalhados.

Quando o parâmetro estiver marcado, deverá permitir que o usuário some mais um dia trabalhado ou horas normais correspondente a um dia, quando ocorrerem férias em meses de 31 dias, na folha normal e na rescisão.  
  
**Importante**Ao marcar esse parâmetro o sistema não altera automaticamente o saldo dos dias trabalhados do colaborador no envelope . O sistema apenas autoriza o usuário alterar dentro do envelope manualmente. Caso contrário, desmarque o parâmetro, o sistema não atualiza o saldo dentro do envelope no recalculo e fica como se fosse 30 dias mesmo, somando dias trabalhado + dias de férias. Portanto, com a marcação do parâmetro, o sistema **apenas autoriza** o usuário alterar dentro do envelope manualmente. Para isso, basta efetuar o procedimento abaixo:  
  
**1.** Acesse: **Configurações | Parametrizador | Férias | Cálculo 1\2** e marque o parâmetro **'Permite alterar o saldo de salário das férias em meses de 31 dias'.**

**2.** Logo, acesse o envelope de pagamento do funcionário e altere a referência do evento.

**3.** Recalcule o envelope de pagamento.
