---
article_id: 360025947072
category: Manutenção de Ativos (SIGAMNT)
content_hash: 6be1de8067361466d9c2489b3565b752773a2d8c2c17e1ef30f585280d53d551
fetched_at: '2026-06-28T22:42:34.309615+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Parametrização para gerar O.S de forma
  automática
type: support-article
updated_at: '2025-02-13T14:01:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025947072-Manufatura-Linha-Protheus-MNT-Parametriza%C3%A7%C3%A3o-para-gerar-O-S-de-forma-autom%C3%A1tica
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18591724090775)***Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como parametrizar o ambiente para que sejam geradas**ordens de serviço** automáticas?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**Esse tipo de alteração deve ser realizada através do **Configurador**.  
  
Aplicabilidade em **ordens de serviços automáticas:**  
O processo de geração de novas ordens de serviços é realizado de forma automática, por meio de contador, resposta de etapa, *check-list,* entre outros.  
Neste momento é verificado no **Plano de manutenção - STF** se para a **O.S - Ordem de Serviço** gerada automaticamente utiliza do processo de substituição, caso sim, o Sistema irá verificar se existem **O.S** para o mesmo bem, serviço e com as sequências definidas no plano de manutenção.  
Para que o processo se torne automático é necessário seguir os parâmetros, conforme a necessidade de utilização de cada ambiente.  
  
Os parâmetros relacionados são os seguintes:  
Parâmetro de consistência de ordem de serviço **Preventiva**. Será avaliado no momento de reporte de contador, *check-list,* resposta de etapa, alteração de **O.S** ou **O.S Manual.**  
  
**MV\_NGNOVOS - Quando gerar nova O.S?**1. Gerar apenas quando não existir **O.S aberta - mesmo bem + serviço + sequência**;  
2. Gerar mesmo se existir **O.S** aberta.

Parâmetro que indica será apresentado alerta de ordem de serviço **Preventiva** vencida. Será avaliado no momento de inclusão de **O.S Corretiva**, **O.S Manual**, solicitação de serviço ou *check-list.*  
  
**MV\_NGPREVE - Apresenta alerta com O.S Preventiva atrasada?**  
**1** - Apresenta alerta ao usuário na abertura de **O.S.** **Corretiva**  
**2** - Apresenta alerta ao usuário na abertura de **S.S. - Solicitação de Serviço  
3** - Apresenta alerta ao usuário na abertura de **O.S.** **Corretiva** e **S.S.**  
**N** - Não apresenta alerta ao usuário.  
Parâmetro que avaliará se o usuário será alertado na inclusão de **O.S Preventiva** automática. Será avaliado no momento da inclusão de **O.S Corretiva**, **O.S manual**, solicitação de serviço, *check-list*, abastecimento manual ou em lote, inclusão de pneus em estrutura de bens ou retorno de **O.S.**  
  
**MV\_NGGERPR - Sistema deve gerar automaticamente O.S preventiva?**  
**S** - Deve gerar ordem de serviço preventiva de maneira automática.  
**N** - Não deve gerar ordem de serviço preventiva de maneira automática.  
Parâmetro que verificará se deverá ser gerada **O.S** automática ao finalizar uma ordem de serviço por tempo. Será avaliado no momento de finalização de outra ordem de serviço nos retornos de **O.S.**  
  
**MV\_NGOSAUT - Gerar O.S** automática **ao finalizar O.S por tempo?**  
**S** - Deve ser gerada **O.S** automática.  
**N** - Não deve ser gerada **O.S** automática.  
Parâmetro que avaliará se o usuário será alertado na inclusão de **O.S preventiva** automática para bens filhos de estrutura de bens. Será avaliado no momento da inclusão de **O.S corretiva, O.S manual**, solicitação de serviço, *check-list*, abastecimento manual ou em lote, inclusão de pneus em estrutura de bem ou retornos de **O.S.**  
  
**MV\_NGOSAES - Indica se deve verificar e gerar OS automática por contador para os componentes da estrutura?**  
**S** - Verificará as ordens dos bens filhos da estrutura de bens e gerará a ordem de serviço automática para os bens filhos, sem consultar o usuário.  
**C** - Consultará o usuário por meio de uma mensagem de alerta perguntando se deverão ser geradas as ordens de serviço para os bens filhos.  
**N** - Não gerará as ordens de serviço para os bens filhos e também não consultará o usuário.  
  
**MV\_NGVEROS -****Apresenta alerta de inclusão de OS Preventiva automática?**  
**V** - Consultará uma única vez o usuário sobre a existência de ordens de serviço abertas, solicitando sua confirmação. Caso selecione **Sim** será gerada a ordem de serviço automática mesmo que possua ordem de serviço aberta para o mesmo bem, serviço e sequência. Caso selecione **Não**, não será gerada a ordem de serviço para as manutenções que já possuírem ordem de serviço aberta.  
**S** - Consultará o usuário a cada manutenção sobre a existência de ordens de serviços abertas, solicitando sua confirmação.   
**N** - Não consultará o usuário e gerará ordem de serviço automática  
mesmo com ordens de serviço em aberto.
