---
article_id: 4411791768855
category: Férias
content_hash: 9779ad4765eb57343437cba6af9fba4fbe87f4f2fe261a98aa606983ad627a40
fetched_at: '2026-06-28T22:46:56.370161+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Férias: Diferença de férias partidas, com alteração salarial
  dentro do mês e desconto integral de INSS, incluindo mês seguinte'
type: support-article
updated_at: '2024-10-18T15:29:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411791768855-RH-RM-FOP-F%C3%A9rias-Diferen%C3%A7a-de-f%C3%A9rias-partidas-com-altera%C3%A7%C3%A3o-salarial-dentro-do-m%C3%AAs-e-desconto-integral-de-INSS-incluindo-m%C3%AAs-seguinte
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27166415690775) Tempo aproximado para leitura: **00:04:00 min****Dúvida**Como realizar diferença de férias partidas, com alteração salarial dentro da competência do cadastro das férias, com o desconto integral de INSS, incluindo mês seguinte?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**O processo de diferença de férias é nativo do sistema ou seja ao processá-lo,  o sistema realizará todos os cálculos internamente, respeitando as devidas parametrizações/configurações dos eventos.   
  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acesse: **Configurações | Parametrizador | Férias | Descontos.****![](https://centraldeatendimento.totvs.com/hc/article_attachments/27166402117399)**  
2. Marque a flag **Deduz integral (inclui mês seguinte)**, para que o desconto de INSS, seja integral dentro do mês de cadastro das férias.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27166402119959)  
  
3. Cadastre o período de gozo das férias do colaborador. No cadastro das férias, o período de gozo é de 30 dias, sendo 11 dias no mês de cadastro das férias e 19 dias no próximo mês. Independente das férias serem partidas, no recibo será lançada a referência e cálculo dos dias cadastrados como período de gozo.  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411802526359)  
  
**Detalhamento do INSS 1º mês**

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

**Detalhamento do INSS 2º mês**

Calculando evento: 0196 - INSS FERIAS PROX MES  
Código de Cálculo 130 - Prioridade 81  
  
Base de INSS:   
Proventos = 2666,67  
Descontos = 0  
Base Líquida = 2666,67  
  
Base para o 1º mês (11 dias): 977,78  
Base para o 2º mês (19 dias): 1688,89  
Parâmetro "Desconta INSS Férias integral no primeiro mês" está confirmado.  
Férias no mês: 20/09/2021 a 19/10/2021  
Dias de férias no mês: 19  
Considerando Saldo Salário no 2º mês para 11 dias: 733,33  
Total da Base de INSS do 2º mês: 2422,22  
INSS: 7,5000% \* Base(1.100,00) = 82,50  
INSS: 9,0000% \* Base(588,89) = 53,00  
INSS 2o.mês: 135,50  
Valor do evento: 135,50

4. Após lançamento das férias. No envelope de pagamento das férias, serão discriminados separadamente as referências e cálculos dos dias de cada mês.  
  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411793865367)  
  
5. Perceba que o INSS foi descontado integral no mês de cadastro das férias, devido a flag **Deduz integral (inclui mês seguinte)** marcada no parametrizador, conforme orientado no passo 2.  
  
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411802652311)  
  
6. Após o lançamento das férias, deverá ser alterado o salário do colaborador, de acordo a porcentagem desejada, acessando: **Administração de pessoas | Alteração de salário.**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27166402123031)  
  
7. Na segunda tela, informe a porcentagem para a alteração.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27166402124439)  
  
8. Deverá ser processada a diferença de férias, baseada na alteração salarial cadastrada. Como a data base é  referente o mês atual, deverá ser informada nos dados do dissídio/data efeito. Caso seja outro motivo e não dissídio, basta marcar dissídio não.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27166402128407)  
  
9. Cadastramos um novo período para processar a diferença de férias. Recomendamos desta forma, por ficar mais organizado para eventual conferências e cancelamento, porém é opcional.  
  
![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411794074007)  
  
O INSS da diferença de férias dentro mês no código de cálculo 3 e diferença de INSS próximo mês no código de cálculo 132.  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411799960343)

**Importante**Quando a alteração salarial e a diferença de férias, ocorrem dentro do mês que o colaborador teve férias, o desconto de INSS será efetuado no código de cálculo 3. É um comportamento padrão do sistema, por se tratar de um ajuste do INSS no mês, semelhante o ajuste de férias no mês, onde o  sistema ajusta o valor do INSS, quando é lançada a folha do colaborador.  
  
**Saiba Mais**[Diferença de Férias](https://tdn.totvs.com/pages/releaseview.action?pageId=452719377)  
[Descontos](https://tdn.totvs.com/display/public/LRM/Descontos)
