---
article_id: 19438671665815
category: RH - Cadastros
content_hash: bdac45eeb42017f71b07c97f54c98416de4dda858f43dcc5966180c11219e897
fetched_at: '2026-06-28T22:44:52.752505+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Atualização do Turno, Sequência e Regra de Apontamento
  no Cadastro do Funcionário
type: support-article
updated_at: '2025-12-10T17:02:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19438671665815-RH-Linha-Protheus-PON-Atualiza%C3%A7%C3%A3o-do-Turno-Sequ%C3%AAncia-e-Regra-de-Apontamento-no-Cadastro-do-Funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19438655525015) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como funciona a atualização do Turno, Sequência e Regra de Apontamento no Cadastro do Funcionário?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Quando é realizada uma Troca de Turno de um Funcionário ou é feito o Fechamento Mensal do período de apontamento, o sistema vai atualizar o Turno, Sequência e Regra de Apontamento no cadastro do Funcionário conforme as regras abaixo:  
  
**1º -** Se a Troca de Turno, acessando em **Atualizações > Cadastros de Funcionários > Troca de Turno**, for realizada **dentro do período de apontamento aberto,** o sistema irá atualizar automaticamente o Turno, Sequência e Regra de Apontamento no **Cadastro de Funcionário**, por exemplo: período de apontamento de 01/03/2022 à 31/03/2022 configurado no **MV\_PONMES**, o funcionário foi cadastrado inicialmente no turno 001 e no dia 15/03/2022 foi realizada uma Troca de Turno para o turno 002. Assim que o registro for gravado, o sistema vai atualizar o cadastro do Funcionário para o turno 002, pois a troca foi realizada dentro do período de apontamento aberto.  
  
**2º -** Se a Troca de Turno for cadastrada para uma data **após o período de apontamento aberto**, o sistema não irá atualizar o cadastro do funcionário após a inclusão. Esta atualização será feita após o Fechamento Mensal, período em que a Troca de Turno se encontra. Por exemplo: período de apontamento aberto de 01/03/2022 à 31/03/2022, onde o funcionário está vinculado ao turno 001. Foi incluída uma Troca de Turno no dia 15/04/2022 para o turno 002. Ao realizar o Fechamento Mensal do primeiro período, o sistema irá verificar se houve alguma Troca de Turno dentro deste período, e em nosso exemplo não existe nenhuma troca de turno, portanto, o sistema não irá atualizar o cadastro de Funcionário neste momento. Quando for feito o fechamento do segundo período, existe uma Troca de Turno dentro do período, portanto, o cadastro do Funcionário será atualizado.  
  
**3º -** Se a Troca de Turno for realizada para o **primeiro dia do período futuro,** o sistema não vai realizar a atualização no cadastro do Funcionário após a inclusão. Esta atualização será feita ao realizar o fechamento do período atual. Por exemplo: período de apontamento de 01/03/2022 à 31/03/2022, onde o Funcionário foi cadastrado no turno 001, e no dia 01/04/2022 foi cadastrada uma troca de turno para o turno 002. Ao realizar o fechamento mensal do primeiro período, o sistema irá atualizar o cadastro do Funcionário com base na troca de turno do dia 01/04/2022.  
  
  
**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como funciona a Troca de Turno dos funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015528671-RH-Linha-Protheus-PON-Como-funciona-a-Troca-de-Turno-dos-funcion%C3%A1rios)  
[RH - Linha Protheus - PON - Para que serve o campo de Turno Opcional no cadastro do Turno de Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052521873-RH-Linha-Protheus-PON-Para-que-serve-o-campo-de-Turno-Opcional-no-cadastro-do-Turno-de-Trabalho)  
[Atualização do Turno, Sequência e Regra de Apontamento no Cadastro do Funcionário](https://tdn.totvs.com/pages/releaseview.action?pageId=682435996)
