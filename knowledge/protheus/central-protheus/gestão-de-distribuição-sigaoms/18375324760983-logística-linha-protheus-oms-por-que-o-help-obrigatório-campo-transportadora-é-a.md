---
article_id: 18375324760983
category: Gestão de Distribuição (SIGAOMS)
content_hash: 7ff19015bdd1794c29ffa3f17f622b30d87d8854ef8d4cbc028d340fe4249262
fetched_at: '2026-06-28T22:45:50.055529+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: 'Logística - Linha Protheus - OMS - Por que o Help Obrigatório: Campo Transportadora
  é apresentado na Montagem de Carga'
type: support-article
updated_at: '2023-11-03T19:18:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18375324760983-Log%C3%ADstica-Linha-Protheus-OMS-Por-que-o-Help-Obrigat%C3%B3rio-Campo-Transportadora-%C3%A9-apresentado-na-Montagem-de-Carga
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18375314440855) Tempo aproximado para leitura: **00:01:12 min** **Dúvida**Por que o *help* **Obrigatório: Campo Transportadora** é apresentado na **Montagem de Carga**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões.  
  
**Solução**Na rotina **OMSA200 - Montagem de Carga**, ao Associar Veículo, se a **Transportadora - DAK\_TRANSP** não for preenchida, será apresentado o *help*: 

![help transp obrigatorio.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18377544465815)

O *help* será apresentado quando o parâmetro **MV\_COMBUS - Grupos de produtos, separados por /, que identificam operações com combustíveis**, estiver preenchido.  
Quando o parâmetro **MV\_COMBUS** estiver preenchido, será validado se o parâmetro **MV\_TRANSP - Informar se é obrigatório a transportadora na montagem da carga**, contém algum conteúdo. O parâmetro **MV\_TRANSP** é tipo caractere, portanto qualquer informação preenchida será considerado como verdadeiro e irá apresentar o help.  
O parâmetro **MV\_TRANSP** deverá estar em branco para não obrigar o preenchimento da transportadora na rotina de Montagem de Carga, na opção Associar Veículo.  
  
**Saiba mais**Mais informações acesse os *links*abaixo:[Montagem de Carga - OMSA200](https://tdn.totvs.com/pages/viewpage.action?pageId=551446517)[Logística - Linha Protheus - OMS - Pontos de Entrada disponíveis na rotina Montagem de Carga - OMSA200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000900021-Log%C3%ADstica-Linha-Protheus-OMS-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina-Montagem-de-Carga-OMSA200)
