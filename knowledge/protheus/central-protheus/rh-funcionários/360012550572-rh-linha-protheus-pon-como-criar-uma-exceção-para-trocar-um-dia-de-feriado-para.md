---
article_id: 360012550572
category: ' RH - Funcionários'
content_hash: 53223a8b20e3de231babf68ffdd26ee32d643a4667a83bd05a96d360ce43c7d3
fetched_at: '2026-06-28T22:44:48.218454+00:00'
product: protheus
section_id: 32419218165783
source: central-protheus
title: RH - Linha Protheus - PON - Como criar uma exceção para trocar um dia de feriado
  para trabalhado
type: support-article
updated_at: '2025-07-16T19:35:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012550572-RH-Linha-Protheus-PON-Como-criar-uma-exce%C3%A7%C3%A3o-para-trocar-um-dia-de-feriado-para-trabalhado
---

**Dúvida**Como criar uma exceção para trocar um dia de feriado para trabalhado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Primeiramente, verifique se o feriado está cadastrado:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097799974)  
  
O cadastro para alterar o tipo de dia pode ser a Exceção por Funcionário ou por Período, ambas tem a mesma funcionalidade.  
Neste exemplo, vamos utilizar a Exceção por Funcionário em **Atualizações> Cadastro de Funcionários> Exceção Por Funcionários**, para alterar o tipo do dia de apenas uma matrícula específica.  
  
Veja abaixo que eu informo que o dia 18 é um dia Trabalhado e informo a Observação (Importante: a observação cadastrada ficará visível no Espelho de Ponto do funcionário). Não informarei um código de Turno de Trabalho pois vou inserir os horários de forma manual:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097800214)  
  
Na aba Horário, defina o horário que deverá ser praticado no dia:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097800254)  
  
Por fim, na aba Intervalos, se o funcionário tiver o descanso neste dia, defina o campo 1ª saída Intervalo como Sim:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100071993)  
  
Acessando a rotina de Intervalo, veremos que a legenda do calendário acusa o cadastro da Exceção no dia 18 e gerando as marcações, não é calculada hora extra:  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097800414)
