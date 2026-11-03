---
article_id: 35829772366871
category: ' RH - Funcionários'
content_hash: ade729c36a5e17fffb59a43fb8aca325187618873a4d045633136cd1c28f787a
fetched_at: '2026-06-28T22:44:48.201393+00:00'
product: protheus
section_id: 32419218165783
source: central-protheus
title: RH - Linha Protheus - PON - Cadastro de Exceções por Período quando tem colaboradores
  afastados e de férias
type: support-article
updated_at: '2026-02-06T12:21:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35829772366871-RH-Linha-Protheus-PON-Cadastro-de-Exce%C3%A7%C3%B5es-por-Per%C3%ADodo-quando-tem-colaboradores-afastados-e-de-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35829755411991) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
No módulo do Ponto Eletrônico ao cadastrar um exceção por período filtrando por centro de custo, o sistema aplica a exceção para todos os funcionários daquele centro de custo. Porém, essa exceção é incluída também para os funcionários que estão afastados ou de Férias, gerando falta ou apontamento indevido.  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Ponto Eletrônico - Todas as versões   
  
**Causa**  
Esse incidente ocorre, pois a parametrização da rotina não havia um campo específico para informar a situação dos funcionários, para assim filtrar e não aplicar para todos.  
  
**Solução**  
Foi criado um novo campo **Situações (P2\_SITFUN)** no cadastro de exceções para selecionar as situações em que a exceção será aplicada. Em **Atualizações> Cadastro de Funcionários> Exceções por Período**, exemplo abaixo para um funcionário de férias:  
  
- Funcionário de férias do dia **01/10/2024** à **11/10/2024,** realizado o cadastro da exceção por período para os dias **11/10** e **12/10**

No novo campo **Situações**foi selecionada apenas a situação normal, isso indica que a exceção será aplicada apenas para os funcionários com a situação normal.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35829755412247)

Ao consultar em integrados em **Atualizações> Lançamentos> Integrados**, é possível verificar que o dia **11/10** foi mantido **como férias** enquanto que no dia **12/10** (em que o funcionário não está mais de férias) a exceção foi aplicada, sendo alterado o sabado para um dia trabalhado.  
  
  
Importante: Para a criação do novo campo é necessário executar o UPDDISTR com o pacote diferencial da Expedição Contínua do RH. Para mais informações referente ao campo [clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=893449392)  
  
  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)  
[RH - Linha Protheus - PON - Como cadastrar Exceção por Período para deixar o dia Não Trabalhado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006080521-RH-Linha-Protheus-PON-Como-cadastrar-Exce%C3%A7%C3%A3o-por-Per%C3%ADodo-para-deixar-o-dia-N%C3%A3o-Trabalhado?source=search)  
[RH - Linha Protheus - PON - Como tratar feriados municipais no Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058280014-RH-Linha-Protheus-PON-Como-tratar-feriados-municipais-no-Ponto-Eletr%C3%B4nico?source=search)
