---
article_id: 360029175091
category: RH - Ponto Eletrônico
content_hash: e15fb6aa2ff3706b56c98e527ced187cd1c9d69a0c4f17608ccd65ed2353ce7c
fetched_at: '2026-06-28T22:44:58.180152+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Após efetuar a troca do turno, o cadastro do funcionário
  não é atualizado (SRA)
type: support-article
updated_at: '2026-04-23T17:49:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029175091-RH-Linha-Protheus-PON-Ap%C3%B3s-efetuar-a-troca-do-turno-o-cadastro-do-funcion%C3%A1rio-n%C3%A3o-%C3%A9-atualizado-SRA
---

**Ocorrência**  
Após efetuar a troca do turno, o cadastro do funcionário (SRA) não é atualizado.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**  
Esse incidente ocorre se a **data da Troca de Turno estiver fora do período de apontamento ativo**, ou nos casos em que o cliente utiliza apenas o SIGAGPE e não tem integração com o Ponto, existe configuração incorreta de parâmetro ou divergências na troca de turno.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Para que o sistema efetive a troca no cadastro de funcionário, a data da troca de turno deve estar dentro do seu período aberto do ponto, definido no **MV\_PONMES**. Se a troca de turno estiver fora do período, só atualizará o cadastro de funcionário após o fechamento do próximo período.

2. Se não utiliza o módulo SIGAPON, basta deixar o parâmetro **MV\_PONMES** sem conteúdo, ou seja, em **branco,** e realize a troca novamente que será atualizado no cadastro do funcionário.

3. No turno de trabalho aba informações ponto, parâmetro Turno Opc. (**R6\_TNOOPC**) deve ser informado um turno de trabalho diferente, informar o mesmo turno gera erro.

4. Quando é efetuado a troca de turno os parâmetros que devem ser alterados são os Turno Para (**PF\_TURNOPA**), Seq. Para (**PF\_SEQUEPA**) e Regra Para (**PF\_REGRAPA**). O sistema deve preservar nos parâmetros Turno De (**PF\_TURNODE**), Seq. De (**PF\_SEQUEDE**) e Regra De (**PF\_REGRADE**) o conteúdo da ultima troca efetuada.

Segue abaixo cenários possívels e o comportamento relacionado a cada um deles com atualização do cadastro de funcionário após a troca de turno fora do período atual no parâmetro **MV\_PONMES**:

-Período atual de exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5693050772503)

Quando é realizada uma troca de turno de um funcionário ou o fechamento mensal do período de apontamento o sistema irá atualizar o Turno, Regra de Apontamento e Sequencia no cadastro do funcionário, conforme as regras:

**1.** Se a troca de turno for realizada **dentro do período de apontamento** o sistema **irá atualizar automaticamente** Turno, Regra de Apontamento e Sequencia no **cadastro de funcionário**, por exemplo, temos o período de apontamento de 01/03/2022 à 31/03/2022, o funcionário foi cadastrado inicialmente no turno 001 e no dia 15/03/2022 foi realizada uma troca de turno para o turno 002. Após cadastrar a troca de turno na rotina (PONA160), o sistema irá atualizar o cadastro do funcionário para o turno 002, pois a troca foi realizada dentro do período de apontamento aberto.

**2.** Se a troca de turno for cadastrada para uma **data após o período de apontamento aberto**, o sistema **não irá atualizar o cadastro do funcionário após a inclusão** da troca de turno na rotina (PONA160). Esta **atualização será feita pela rotina de Fechamento Mensal (PONM090)**, quando for executada o Fechamento do Período em que a troca de turno se encontra. Por exemplo, período de apontamento aberto 01/03/2022 à 31/03/2022, foi incluída uma troca de turno para o dia 15/04/2022 para o turno 002, onde o funcionário foi cadastrado inicialmente com o turno 001. Ao realizar o Fechamento Mensal do mês 3, o sistema irá verificar se houve alguma troca de turno neste período, em nosso exemplo não existe a troca de turno, por isso o sistema não irá atualizar o cadastro de funcionário. Porém ao realizar o fechamento do mês 4, a troca de turno existe e com isso o sistema irá atualizar o cadastro do funcionário.

**3.** Se a troca de turno for realizada para o **primeiro dia do período futuro** o sistema **não irá realizar a atualização no cadastro do funcionário após a inclusão** da troca de turno na rotina PONA160. **Esta atualização será feita ao realizar o fechamento do período atual**. Por exemplo, período de apontamento 01/03/2022 à 31/03/2022, o funcionário foi cadastrado no turno 001 e no dia 01/04/2022 foi cadastrada uma troca de turno para o turno 002. Ao realizar o fechamento mensal do mês 3, o sistema irá atualizar o cadastro do funcionário.

**Saiba mais:**  
<https://tdn.totvs.com/pages/viewpage.action?pageId=682435996>  
[RH - Linha Protheus - PON - Período de apontamento desconfigurado. Como configurar: MV\_PAPONTA e MV\_PONMES](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015809548-RH-Linha-Protheus-PON-Per%C3%ADodo-de-apontamento-desconfigurado-Como-configurar-MV-PAPONTA-e-MV-PONMES?source=search)
