---
content_hash: 7140efde8cb91fbc1aa099b84796a51deb638d0f29c5f053f7c18897abcf11e8
fetched_at: '2026-06-29T00:11:10.281328+00:00'
page_id: '642970490'
product: rm
source: tdn-rm
title: Envio de Métricas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=642970490
version: 6
---

O RM, em determinadas rotinas, realiza o envio de métricas relevantes ao License Server.

Aqui se encontram as métricas que são enviadas ao License Server

# Métrica

## ***reports-rm\_quantidade\_total***

**Métrica:** Quantidade de relatórios contidos na base de dados

**Frequência de envio: Mensal**

**MetricId: *reports-rm\_quantidade\_total***

**Descrição:** Essa métrica recebe a quantidade de relatórios contido na base de dados, sendo filtrada pelo nome da SubRotina, podendo ser Delphi, RMReports, ou outro gerador de relatórios pertinente

## ***reports-rm\_delphi\_executado\_mes\_total***

**Métrica:** Quantidade de relatórios Delphi executados no mês

**Frequência de envio: Mensal**

**MetricId: *reports-rm\_delphi\_executado\_mes\_total***

**Descrição:** Essa métrica recebe a quantidade de relatórios Delphi (Contidos na tabela ***RRELAT***) executados no mês solicitado. A SubRotina recebe o nome do relatório e o valor recebe a data no formato ano/mês (202110)

## **host-rm\_jobserver\_count**

**Métrica:** Status do JobServer por Alias de cada Host.Service

**MetricId: host-rm\_jobserver\_count**

**Frequência de envio: Mensal**

**Descrição:** Essa métrica recebe ao status do JobServer relacionado ao Alias, se está ativo ou não. Essa métrica é enviada uma vez para cada Alias existente em cada Host.Service rodando. Na SubRotina será preenchida as informações referentes ao ambiente, no seguinte formato ***NOME\_DA\_MAQUINA**|NOME\_DO\_SERVICO|**ALIAS*** (Lembrando que o Nome da Máquina e o Alias, por serem informações sensíveis, são hasheadas) e o valor da métrica varia entre 0 e 1, sendo que:

* Caso o **JobServer Três Camadas** e o **JobServer do alias** estejam **ativos**, enviará **1 (true)**
* Caso o **JobServer Três Camadas** esteja **desativado**, a configuração do JobServer do alias não influenciará, será enviado **0 (false)**
* Caso o **JobServer Três Camadas** esteja **ativo** e o **JobServer** do alias esteja **desativado**, será enviado **0 (false)**

## **lgpd-rm\_perfis-sem-acesso-dados-protegidos\_total**

**Métrica:** Quantidade de perfis RM que tiveram seu *Acesso à campos sensíveis* removido

**MetricId: lgpd-rm\_perfis-sem-acesso-dados-protegidos\_total**

**Frequência de envio: Quando for registrada no banco de dados pela primeira vez e então, somente quando houve atualização na** *GPERFIL* **(Tela de cadastro/edição de perfis)**

**Descrição:** Essa métrica recebe a quantidade de perfis RM que tiveram o campo *Acesso à campos sensíveis* desmarcado durante a edição/inclusão.

## **lgpd-rm\_auditar-lgpd\_count**

**Métrica:** O campo Auditar LGPD no TOTVS Audit foi marcado?

**MetricId: lgpd-rm\_auditar-lgpd\_count**

**Frequência de envio: Quando for registrada no banco de dados pela primeira vez e então, quando o TOTVS Audit for executado.**

**Descrição:** Essa métrica recebe o status o campo **Auditar LGPD** no **TOTVS Audit** (*Ativado ou Desativado*).

## **lgpd-rm\_dicionario-dados-protegidos-alterados\_total**

**Métrica:** Quantidade de alterações em relação à proteção de dados pessoais (*Configurar dicionário de Dados*)

**MetricId: lgpd-rm\_dicionario-dados-protegidos-alterados\_total**

**Frequência de envio: Quando for registrada no banco de dados pela primeira vez e então, quando o houver atualização da *GDICDATAPROTECTION* (Configurar Proteção de Dados).**

**Descrição:** Essa métrica recebe a quantidade de registros que foram alterados na GDICDATAPROTECTION, ou seja, a quantidade de campos que tiveram suas diretivas relacionadas à LGPD alteradas do padrão enviado pela TOTVS.
