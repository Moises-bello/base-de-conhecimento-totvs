---
article_id: 17632242681111
category: RH - Fechamentos
content_hash: 5a7716eec6f80916123b5644837754f0cc557554b42f5cf6c481ef0b99806308
fetched_at: '2026-06-28T22:44:48.912446+00:00'
product: protheus
section_id: 32419231682455
source: central-protheus
title: 'RH - Linha Protheus - PON - Mensagem no Fechamento Mensal: Já existe um período
  no cadastro de período para a filial XX'
type: support-article
updated_at: '2026-04-14T12:50:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17632242681111-RH-Linha-Protheus-PON-Mensagem-no-Fechamento-Mensal-J%C3%A1-existe-um-per%C3%ADodo-no-cadastro-de-per%C3%ADodo-para-a-filial-XX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17632210458775) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao realizar o **Fechamento Mensal**, é gerada a mensagem "Já existe um período no cadastro de período para a filial XX" no *log* de ocorrências, e o período não é fechado.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31995587631511)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as Versões.  
  
**Causa**  
A mensagem ocorre em casos que foi feita a inclusão indevidamente de um **registro** com **este período** na rotina **Período de Apontamento**, através do botão **Incluir:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31995587632407)  
  
O botão de **Incluir** não deve ser utilizado, visto que os fatores determinantes para habilitar os períodos no Ponto Eletrônico são:  
- conteúdo dos parâmetros **MV\_PAPONTA** e **MV\_PONMES**  
- **data base** do sistema  
  
Diferente da Folha de Pagamento, no modulo do Ponto Eletrônico o usuário **nunca** deve **criar/incluir** registros nessa rotina, visto que as linhas presentes nela sempre deverão mostrar períodos que já foram fechados pela rotina de **Fechamento Mensal**. Para mais informações referente ao fechamento [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004103232-RH-Linha-Protheus-PON-Como-efetuar-o-Fechamento-Mensal-do-Ponto)

É possível identificar **registros criados pelo usuário** de duas formas:  
- se a bolinha estiver com **cor verde**;  
- através da tabela **SPO**, se o campo **PO\_RESPONS** estiver como **U** de usuário.  
  
**Solução**  
Para que não seja gerada esta mensagem no *log* e o período possa ser fechado, será necessário deletar a linha com o período em questão na rotina de Período de Apontamento, em **Atualizações> Cadastro do Ponto> Períodos de Apontamentos** através de **Outras ações/excluir**. Após executar novamente a rotina de **Fechamento Mensal**.  
  
**Saiba Mais:**  
[RH - Linha Protheus - PON - Rotina Período de Apontamento - PONA290](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059188733-RH-Linha-Protheus-PON-Rotina-Per%C3%ADodo-de-Apontamento-PONA290)  
[RH - Linha Protheus - PON - Após o fechamento mensal, o sistema não alterou o período de apontamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012922731-MP-PON-Ap%C3%B3s-o-fechamento-mensal-o-sistema-n%C3%A3o-alterou-o-per%C3%ADodo-de-apontamento?source=search)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
