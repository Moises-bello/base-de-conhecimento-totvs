---
article_id: 360058280014
category: RH - Cadastros
content_hash: 89766c526a527c55b056baca64fb2e9af06975fec50241748658deae10747edb
fetched_at: '2026-06-28T22:44:52.795974+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como cadastrar feriados municipais no Ponto Eletrônico
type: support-article
updated_at: '2025-12-29T13:23:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058280014-RH-Linha-Protheus-PON-Como-cadastrar-feriados-municipais-no-Ponto-Eletr%C3%B4nico
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35218106818583)****Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
Como realizar o cadastro dos feriados municipais no Ponto Eletrônico?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
O cadastro de feriados no Protheus, é validado através da tabela SP3 do Ponto Eletrônico, pode ser feito de forma exclusiva, sendo a **tabela SP3 - E E E** e, assim poderiam ter em cada filial de seu sistema um cadastro de feriado diferente.  
  
Outra possibilidade, seria cadastrar estes feriados municipais sem ser via filial como explicado acima, sendo através do **cadastro de exceções** no sistema.  
  
A exceção é uma cadastro com a finalidade de alterar um dia de tipo "Trabalhado" por exemplo, em um dia de "Feriado", e pode ser realizado para uma única matrícula, um turno ou centro de custo. Para mais detalhes [**clique aqui**.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012550572-RH-Linha-Protheus-PON-Como-criar-uma-exce%C3%A7%C3%A3o-para-trocar-um-dia-de-feriado-para-trabalhado)

Abaixo veja o exemplo, cadastro o dia 14/04 (dia normal pela tabela de horário padrão) para um dia de feriado, vinculado o turno 14, assim todos os funcionários alocados neste turno terão este dia como um feriado e não mais dia normal:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31423404646807)

**IMPORTANTE**: Para os demais funcionários de outros turnos, não sofrerão mudanças.

**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
