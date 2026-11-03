---
article_id: 360035667093
category: RH - Lançamentos
content_hash: c12c0556bfd58eb7ce8bd03a3f9222c691a17d92ea053ca5a6a5ec2fcb6203a5
fetched_at: '2026-06-28T22:44:46.813027+00:00'
product: protheus
section_id: 32419271673111
source: central-protheus
title: RH - Linha Protheus - PON - Como gerar Hora Extra em um sábado Compensado quando
  é um Feriado
type: support-article
updated_at: '2025-08-14T19:29:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035667093-RH-Linha-Protheus-PON-Como-gerar-Hora-Extra-em-um-s%C3%A1bado-Compensado-quando-%C3%A9-um-Feriado
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34185542083863) Tempo aproximado para leitura: 00:01:00 min**  
Dúvida**Sábado Compensado quando é um Feriado, como gerar Hora Extra?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Quando a Empresa possui uma escala de jornada trabalhada de segunda à sexta e opta por compensar o sábado, distribuindo a jornada semanal dentre Segunda-feira até Sexta-feira, deixando assim o sábado como um dia compensando. Quando um feriado coincidir em um sábado, o sistema não vai gerar nenhum tipo de evento apontado, pois já consta o horário previsto configurado na tabela de horário padrão, compondo a jornada já compensando durante a semana, independente se sábado for um feriado. Ou seja, o sistema não vai entender automaticamente que para aquela semana que recaí feriado no sábado cancelaria a jornada com a compensação.  
  
Caso a empresa queira reduzir a jornada nesta semana para os funcionários exclusivamente para aquela semana não ter que compensar as horas, por conta do feriado no sábado, deverá efetuar um cadastro de exceção informando a redução da jornada do funcionário determinando aquele período. Para isto, siga o procedimento da documentação de exceção trabalhada:  
[Utilização de exceção por funcionário para escalas de trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043030894-RH-Linha-Protheus-PON-Utiliza%C3%A7%C3%A3o-de-exce%C3%A7%C3%A3o-por-funcion%C3%A1rio-para-escalas-de-trabalho)  
[Como cadastrar exceções por período](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006706652-RH-Linha-Protheus-PON-Como-cadastrar-exce%C3%A7%C3%B5es-por-per%C3%ADodo)  
  
Cabe ressaltar que se por acaso, um funcionário trabalhar nesse sábado que, consequentemente caiu como um feriado, automaticamente o Sistema traz o evento de Hora Extra de Feriado, configurado e cadastrado corretamente na rotina Tipos de Horas extras.  
  
**Saiba mais:**  
[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)  
[RH - Linha Protheus - PON - Regras importantes para o cadastro dos Tipos de Horas Extras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060489314-RH-Linha-Protheus-PON-Regras-importantes-para-o-cadastro-dos-Tipos-de-Horas-Extras)
