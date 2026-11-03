---
article_id: 360047548594
category: RH - Banco De Horas
content_hash: 0cd56cfcf1a4f2bc9308b524924b22808fb7b9cef038154645392353f5c4adb6
fetched_at: '2026-06-28T22:44:54.150754+00:00'
product: protheus
section_id: 32405029751063
source: central-protheus
title: RH - Linha Protheus - PON -  Banco de Horas não é calculado e não grava registros
  na tabela
type: support-article
updated_at: '2025-11-17T11:56:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047548594-RH-Linha-Protheus-PON-Banco-de-Horas-n%C3%A3o-%C3%A9-calculado-e-n%C3%A3o-grava-registros-na-tabela
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34205596384023) Tempo aproximado para leitura: 00:01:00 min********Dúvida****Ao realizar o Cálculo Mensal do período, o sistema não leva os apontamentos para o Banco de Horas do funcionário.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
****Causa****Quando o campo **Agrupamento BH**do Cadastro de Eventos está como **SIM**, ao realizar o cálculo mensal o sistema verifica os valores de crédito/debito que serão gerado para o Banco de Horas do período de apontamento, se o saldo final for um total de 0,00 horas, o sistema não levará nenhum registro para os Lançamentos de Banco de Horas do funcionário.   
  
**Importante**: o sistema não utiliza o saldo anterior para o cálculo, ele verifica apenas o débito/crédito do intervalo de datas informado nos parâmetros do Cálculo Mensal.  
 **Solução**Para garantir o registro correto do histórico das movimentações de banco de horas do período em que estiver efetuando o cálculo, siga com o procedimento de **alteração dos eventos** de movimentações de banco de horas, mais especificamente no campo **Agrupam. B.H.**  
  
Para isto, acesse o módulo **SIGAPON**, acesse a rotina em **Atualizações → Cadastro do Ponto → Eventos.** Filtre e localize o evento de movimentação de banco de horas. Clique em **Alterar** e na aba **Banco de Horas**, altere o campo **Agrupam. B.H.** para **"N - Não".** Clique em "Salvar"  
Veja exemplo de como o cadastro de evento do BH deve ficar:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070871833)

**Atenção:**  
Repita este procedimento para todos os eventos relacionados à movimentação de banco de horas.  
Somente assim o histórico completo será registrado corretamente.  
  
**Saiba mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como utilizar o cadastro de evento do ponto eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407450836887-RH-Linha-Protheus-PON-Como-utilizar-o-cadastro-de-evento-do-ponto-eletr%C3%B4nico)  
[RH - Linha Protheus - PON - Como cadastrar os eventos para Folha de Pagamento ou Banco de Horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013459532-RH-Linha-Protheus-PON-Como-cadastrar-os-eventos-para-Folha-de-Pagamento-ou-Banco-de-Horas)
