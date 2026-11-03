---
article_id: 360015267491
category: RH - Cálculos
content_hash: 0d95d579faeefe9acbbd332c868b4a0cd3fd0609e582153183857f11fe861c38
fetched_at: '2026-06-28T22:44:51.619609+00:00'
product: protheus
section_id: 32419138773655
source: central-protheus
title: RH - Linha Protheus - PON - Cálculo do salário do horista com base nas horas
  reais realizadas
type: support-article
updated_at: '2026-02-11T14:00:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015267491-RH-Linha-Protheus-PON-C%C3%A1lculo-do-sal%C3%A1rio-do-horista-com-base-nas-horas-reais-realizadas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34258853226903) Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
Como efetuar o cálculo do saldo de salário do horista com base nas horas reais realizadas?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para efetuar o cálculo do salário do Horista com base nas horas reais realizadas o cliente deverá seguir o procedimento abaixo:  
  
**1.** No **SIGAGPE,** acessar **Atualizações > Definições de Cálculos > Mnemônicos** e alterar os Mnemônicos como abaixo:

**P\_LDSRHRSP = .T.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31914309954071)

**P\_NDSRHORI = 3**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31914288340887)  
**P\_LDSRSALD = .T.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31914309956887)  
  
**2.** Vincular o funcionário a um **Turno de Trabalho,  Regra de Apontamento, e Sequência de Turno** acessando **Atualizações > Ponto Eletrônico >Troca de Turno,** [troca de turno](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015528671)**.**  
  
**3.** No Configurador e alterar o parâmetro MV\_DIASMES = S  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31914288344343)  
  
**4.** Verificar se o [cadastro do Turno](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410322419095) está correto. Para efeito dos cálculos das horas trabalhadas, o sistema buscará as informações da [Tabela de Horário Padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293), do campo Horas Total.  
  
**5.** Efetuar o [Cálculo Mensal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051550453-RH-Linha-Protheus-PON-Como-fazer-e-qual-a-finalidade-do-C%C3%A1lculo-Mensal)  
  
**6.** Efetuar a [Integração com a Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050379453-RH-Linha-Protheus-PON-Integra%C3%A7%C3%A3o-com-a-Folha-de-Pagamento)  
  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[MP - PON0061 - Como efetuar o cálculo do salário do Horista proporcional com base nas horas reais realizadas?](http://tdn.totvs.com/pages/viewpage.action?pageId=235321674)
