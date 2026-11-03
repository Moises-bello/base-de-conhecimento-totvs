---
article_id: 360013674751
category: RH - Banco De Horas
content_hash: 40179047a769e9788ea118c21385577e2788d88609d3c7d9105915b0e25b4022
fetched_at: '2026-06-28T22:44:54.252402+00:00'
product: protheus
section_id: 32405029751063
source: central-protheus
title: RH - Linha Protheus - PON - Configuração para que as horas sejam apuradas no
  Banco de Horas
type: support-article
updated_at: '2025-09-16T13:07:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013674751-RH-Linha-Protheus-PON-Configura%C3%A7%C3%A3o-para-que-as-horas-sejam-apuradas-no-Banco-de-Horas
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34972668139415) Tempo aproximado para leitura: 00:01:30 min**Dúvida**Como configurar o sistema para que as horas sejam apuradas no **Banco de Horas?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões   
  
**Solução**Para configuração do **Banco de Horas**, siga as orientações abaixo:  
  
**1.** No Cadastro do **Funcionário,** localizado em **Atualizações > Cadastro de Funcionários > Funcionários**, aba **Relógio Registrador,** o campo **B. H. P/ Folh** (RA\_BHFOL) deve estar como **S - Sim** para que as informações do Banco de Horas apuradas para este funcionário possam ser baixadas no futuro.   
O campo **Acum. B. Horas** (RA\_ACUMBH) também deve estar como **S - Sim** para que as horas do funcionário sejam **acumuladas no Banco de Horas.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19258553661079)

**2.** No Cadastro de **Eventos,** localizado em **Atualizações > Cadastro do Ponto > Eventos**, aba de **Banco de Horas:**- o campo **Acum. B. Horas** (P9\_BHORAS) deve estar como **Sim;**  
- os campos **Horas De** (P9\_BHNDE) com **0,01** e **Horas Até** (P9\_BHNATE) com**999,99** respectivamente para definir o intervalo de início/fim do acúmulo no Banco de Horas para aquele evento;  
**-** o campo **Percentual** (P9\_BHPERC) deve ser preenchido de acordo com a **valorização da hora extra** [conforme esta documentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058922053-RH-Linha-Protheus-PON-Forma-correta-de-cadastro-para-valorizar-evento-de-Banco-de-Horas);- o campo **Agrupamento BH** (P9\_BHAGRU) **deve estar como não,** para caso ocorra do Banco de Horas do funcionário chegar em um total de 0,00 horas dentro de um mesmo período de apontamento**,** estes valores mesmo assim **sejam lançados para o funcionário para o controle do histórico;**- o campo **Tp. Apuração** (P9\_BHVAL) deve estar com a opção **T - Total** selecionada;  
- o campo **Perc. B. Horas** (P9\_PBH) deve estar como **100,00** para indicar que aquele evento em sua totalidade vai para o Banco de Horas;  
- o campo **Perc. F. Pagto.** (P9\_PFOL) deve estar **zerado.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078688054)

**3.** A rotina responsável por levar os apontamentos/eventos para o Banco de Horas, é o **Cálculo Mensal,** localizado em **Miscelânea > Cálculos > Cálculo Mensal.**   
Esta rotina também é responsável por atualizar os dados no Espelho de Ponto dos funcionários, portanto, ela **não pode deixar** de ser processada.  
  
**4.** Para realizar as conferências dos créditos e débitos, pode ser acessada a rotina **Banco de Horas,** localizada em **Atualizações > Lançamentos > Banco de Horas.**  
  
**5.** Para imprimir espelho de ponto demonstrando o banco de horas utilize a pergunta **"Imprime Banco de Horas" ?** igual à **'Sim'**, veja mais na documentação: [RH - Linha Protheus - PON - Como imprimir o Espelho de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004253171-RH-Linha-Protheus-PON-Como-imprimir-o-Espelho-de-Ponto)  
  
**Saiba Mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)[MP - PON - Como cadastrar os eventos para Folha de Pagamento ou Banco de Horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013459532-MP-PON-Como-cadastrar-os-eventos-para-Folha-de-Pagamento-ou-Banco-de-Horas?source=search)  
[MP - PON - Banco de Horas não é calculado e não grava registro na tabela](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047548594-MP-PON-Banco-de-Horas-n%C3%A3o-%C3%A9-calculado-e-n%C3%A3o-grava-registro-na-tabela)  
[RH - Linha Protheus - PON - Forma correta de cadastro para valorizar evento de Banco de Horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058922053-RH-Linha-Protheus-PON-Forma-correta-de-cadastro-para-valorizar-evento-de-Banco-de-Horas)
