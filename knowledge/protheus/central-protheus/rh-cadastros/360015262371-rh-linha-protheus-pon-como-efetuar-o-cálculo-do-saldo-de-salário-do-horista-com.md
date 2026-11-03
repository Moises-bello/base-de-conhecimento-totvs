---
article_id: 360015262371
category: RH - Cadastros
content_hash: a9cda94093b9d87cab31ff31ddc9c1d60f5d9dfc2a80d83fdb2850897b604ba7
fetched_at: '2026-06-28T22:44:52.844275+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como efetuar o cálculo do saldo de salário do horista
  com base nas horas efetivamente realizadas
type: support-article
updated_at: '2026-02-03T17:54:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015262371-RH-Linha-Protheus-PON-Como-efetuar-o-c%C3%A1lculo-do-saldo-de-sal%C3%A1rio-do-horista-com-base-nas-horas-efetivamente-realizadas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35296114415255) Tempo aproximado para leitura: 00:01:00 min**  
  
**Dúvida**  
Como efetuar o cálculo do saldo de salário do horista com base nas horas efetivamente realizadas?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para efetuar o cálculo do saldo de salário do horista com base nas horas efetivamente realizadas:

1 - Alterar os Mnemônicos em **GPEA300 - Atualizações/Definições de Cálculos/Mnemônicos**: **LDSRHRSPON** e **LHRSPONFOL**.  
**![](http://tdn.totvs.com/download/attachments/235337720/MNEMONICO%20LDSRPON.jpg?version=1&modificationDate=1460651397000&api=v2)**  
**![](http://tdn.totvs.com/download/attachments/235337720/MNEMONICO%20LHRSPONFOL.jpg?version=1&modificationDate=1460651398000&api=v2)**

**Na versão 12, os Mnemônicos são:** P\_LDSRHRSP, P\_NDSRHORI e P\_LDSRSALD

2 - Para funcionários novos, cadastrar o funcionário a um Turno, Regra e Sequência: **GPEA010 - Atualizações/Funcionário/Funcionários**. Em caso de funcionário já cadastrado, deverá acessar e ajustar via Troca de Turno dos funcionários.

3 - Acessar o **Configurador (SIGACFG)** e acessar em **Ambiente - Cadastros - Parâmetros**, filtrar e alterar os parâmetros conforme abaixo:

* MV\_DIASMES = S
* MV\_PGCOMHR = 1
* MV\_SABDOM = S

4 - Verificar se o cadastro do Turno está correto. Para efeito dos cálculos das horas trabalhadas, o sistema buscará as informações da **Tabela de Horário Padrão**, no campo **Horas Total**. **PONA080 - Atualizações > Cadastros Ponto > Tab. Horário Padrão.**

5 - Calcular a folha.

**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[MP - PON0062 - Como efetuar o cálculo do saldo de salário do Horista com base nas horas reais realizadas?](http://tdn.totvs.com/pages/viewpage.action?pageId=235337720)
