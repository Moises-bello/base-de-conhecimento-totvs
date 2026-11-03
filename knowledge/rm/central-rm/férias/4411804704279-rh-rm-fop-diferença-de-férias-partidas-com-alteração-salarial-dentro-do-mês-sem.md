---
article_id: 4411804704279
category: Férias
content_hash: 7642f5e0b39c381e68c73931aad67010114364d1b1fae09cbf64c696b9a615ed
fetched_at: '2026-06-28T22:46:56.363538+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: RH - RM - FOP - Diferença de férias partidas com alteração salarial dentro
  do mês sem o  desconto integral de INSS
type: support-article
updated_at: '2024-10-23T22:05:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411804704279-RH-RM-FOP-Diferen%C3%A7a-de-f%C3%A9rias-partidas-com-altera%C3%A7%C3%A3o-salarial-dentro-do-m%C3%AAs-sem-o-desconto-integral-de-INSS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min****Dúvida**Como realizar diferença de férias partidas, com alteração salarial dentro da competência do cadastro das férias, sem o desconto integral de INSS, incluindo mês seguinte?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**O processo de diferença de férias é nativo do sistema ou seja ao processá-lo, o sistema realizará todos os cálculos internamente, respeitando as devidas parametrizações/configurações dos eventos. Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acesse: **Configurações | Parametrizador | Férias | Descontos.****![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9472415461783)**2. Desmarque a flag **Deduz integral (inclui mês seguinte)**, para que o desconto de INSS, não seja integral dentro do mês de cadastro das férias.  
  
 ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411795173015/mceclip1.png)  
  
3. Cadastre o período de gozo das férias do colaborador. No cadastro das férias, o período de gozo é de 30 dias, sendo 11 dias no mês de cadastro das férias e 19 dias no próximo mês. Independente das férias serem partidas, no recibo será lançada a referência e cálculo dos dias cadastrados como período de gozo. Segue exemplo abaixo com 30 dias.  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411802526359/mceclip8.png)  
  
**Detalhamento do INSS no 1º mês**

Calculando evento: 0098 - INSS FERIAS  
Código de Cálculo 82 - Prioridade 81  
  
Base de INSS:   
Proventos = 2666,67  
Descontos = 0  
Base Líquida = 2666,67  
  
Base para o 1º mês (11 dias): 977,78  
Base para o 2º mês (19 dias): 1688,89  
Férias no mês: 20/09/2021 a 19/10/2021  
Dias de férias no mês: 11  
Considerando Saldo Salário no 1º mês para 19 dias: 1266,67  
Total da Base de INSS do 1º mês: 2.244,45  
INSS: 7,5000% \* Base(977,78) = 73,33  
INSS 1o.mês: 73,33  
Valor do evento: 73,33  
  
4. Após lançamentos das férias, no envelope de pagamento das férias, serão discriminados separadamente as referências e cálculos dos dias de cada mês.  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411795335319/mceclip7.png)  
  
5. Perceba que o INSS não foi descontado integral, devido a flag **Deduz integral (inclui mês seguinte)** estar desmarcada no parametrizador, conforme a orientação do passo 2.  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411804358807/mceclip6.png)  
  
6. Após o lançamento das férias, deverá ser alterado o salário do colaborador, de acordo a porcentagem desejada, acessando: **Administração de pessoas | Alteração de salário.**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9472509898519)  
  
7. Na segunda tela, informe a porcentagem desejada.  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411795369111/mceclip9.png)  
  
8. Deverá ser processada a diferença de férias, baseada na alteração salarial cadastrada. Como a data base é  referente o mês atual, deverá ser informada nos dados do dissídio/data efeito. Caso seja outro motivo e não dissídio, basta marcar dissídio não.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9472519461143)  
  
9. Cadastramos um novo período para processar a diferença de férias. Recomendamos desta forma, por ficar mais organizado para eventual conferências e cancelamento, mais é opcional.  
  
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411804515095/mceclip11.png)  
  
O INSS da diferença de férias no mês foi lançado no código de cálculo 3.

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411804551319/mceclip12.png)

**Importante**Quando a alteração salarial e a diferença de férias, ocorrem dentro do mês que o colaborador teve férias, o desconto de INSS será efetuado no **código de cálculo 3**. Por se tratar de movimentação dentro da competência. Para o sistema a movimentação se refere ao mês.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411991725975/mceclip0.png)  
  
Ao virar a competência, o sistema lança os eventos de base, informando o valor total do saldo de 19 dias de férias , com o acumulado do valor da diferença de férias.

**Saiba Mais**[Diferença de Férias](https://tdn.totvs.com/pages/releaseview.action?pageId=452719377)  
[Descontos](https://tdn.totvs.com/display/public/LRM/Descontos)
