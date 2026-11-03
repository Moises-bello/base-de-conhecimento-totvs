---
article_id: 17736765600407
category: Materiais - Compras (SIGACOM)
content_hash: 9704a39acb67b1dddc6484ec5add1296e1c1e36717c32ec206d0cce9643db50e
fetched_at: '2026-06-28T22:41:24.314303+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual o Consumo de Licenças
  das rotinas responsáveis pela importação e gravação do XML ?
type: support-article
updated_at: '2024-06-13T17:40:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17736765600407-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-o-Consumo-de-Licen%C3%A7as-das-rotinas-respons%C3%A1veis-pela-importa%C3%A7%C3%A3o-e-grava%C3%A7%C3%A3o-do-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17736761647639) Tempo aproximado para leitura: **00h 02min** **Dúvida**Qual o consumo de licenças das rotinas responsáveis pela importação e gravação do XML?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - versão 12  
  
**Solução**

No Importador XML é necessário criar agendamentos das rotinas responsáveis pela importação e gravação do XML no Monitor (Protheus).

Para realizar o cadastro dos agendamentos é necessário o seguinte:

* SIGACFG -> AMBIENTE -> SCHEDULE -> SCHEDULE (Agendamento -> Cadastro):
  + Informar usuário (Ex: 000000 - Administrador)
  + Rotina (tabela abaixo)
  + Modulo: (Ex: 02 - Compras)
  + Deixar habilitado

| Agendamento | Descrição | Recorrência | Configuração | Consumo Licença |
| --- | --- | --- | --- | --- |
| COLAUTOREAD | Para importar XML's através da pasta IN (MV\_NGINN) e gravar informações na tabela CKO | 48 (00:30 min) | Configurar apenas uma filial por grupo de empresa que ocorrera a importação  Ex: T1 / D MG 01       T2 / D SP 01  Obs: Dessa forma ao importar XML será analisado se documento pertence a qualquer filial de cada grupo de empresa. | Por Empresa |
| **Mais detalhes:** [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como realizar a configuração do agendamento da rotina COLAUTOREAD dentro do novo SCHEDULE POUI?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22062101346071-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-configura%C3%A7%C3%A3o-do-agendamento-da-rotina-COLAUTOREAD-dentro-do-novo-SCHEDULE-POUI) | | | | |
| SCHEDIMPTRA | Para requisitar e ler recibos retornados do TOTVS Transmite | 144 (00:10 min) | Configurar apenas uma filial por grupo de empresa que ocorrera a importação  Ex: T1 / D MG 01       T2 / D SP 01  Obs: Dessa forma ao importar XML será analisado se documento pertence a qualquer filial de cada grupo de empresa. | Por Empresa |
| **Mais detalhes:** [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como realizar a configuração do agendamento da rotina SCHEDIMPTRA dentro do novo SCHEDULE POUI?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22062311546775-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-configura%C3%A7%C3%A3o-do-agendamento-da-rotina-SCHEDIMPTRA-dentro-do-novo-SCHEDULE-POUI) | | | | |
| SCHEDUPDTRA | Para atualizar status de documentos no TOTVS Transmite | 72 (00:20 min) | Configurar apenas uma filial por grupo de empresa que ocorrera a importação  Ex: T1 / D MG 01       T2 / D SP 01  Obs: Dessa forma ao atualiza status será analisado toda a CKO, com documentos de todos grupos e filiais importados. | Por Empresa |
| **Mais detalhes:** [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como realizar a configuração do agendamento da rotina SCHEDUPDTRA dentro do novo SCHEDULE POUI?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22062370970647-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-configura%C3%A7%C3%A3o-do-agendamento-da-rotina-SCHEDUPDTRA-dentro-do-novo-SCHEDULE-POUI) | | | | |
| SCHEDCOMCOL | Ler os XML's da CKO e importar para o monitor (SDS e SDT) | 288 (00:05 min) | Configurar TODOS os grupos e filiais que documentos possam pertencer para que sera importado para o monitor no grupo e filial correto  Ex: T1 / D MG 01        T1 / D MG 02        T2 / D SP 01        T2 / D SP 02 | Por Filial |
| **Mais detalhes:** [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como realizar a configuração do agendamento da rotina SCHEDCOMCOL dentro do novo SCHEDULE POUI?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22062559984791-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-configura%C3%A7%C3%A3o-do-agendamento-da-rotina-SCHEDCOMCOL-dentro-do-novo-SCHEDULE-POUI) | | | | |

* SIGACFG -> AMBIENTE -> SCHEDULE -> SCHEDULE (Agent -> Cadastro):
  + Incluir o Grupo de empresa/Empresa que contem configurado os agendamentos.

Para que funcione corretamente os agendamentos é necessário que após toda configuração, o **Agent e o Schedule sejam ativados**.

**IMPORTANTE.:** Para melhorar o desempenho, foram criadas as rotinas SCHEIMPTRA e SCHEDUPTRA, destinadas à integração do Importador XML com o TOTVS Transmite. Portanto, se você não estiver utilizando o Importador XML padrão ou qualquer integração, é recomendado manter a rotina **COLAUTOREAD** desativada.

Ative-as apenas se estiver utilizando a pasta INN para importar os XMLs. Essa abordagem otimizará o desempenho do sistema, ativando apenas as funcionalidades necessárias para o seu fluxo de trabalho específico.

***Saiba Mais:***

* [Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-MP-SIGACOM-Importador-XML#:~:text=No%20Importador%20de%20XML%20%C3%A9%20necess%C3%A1rio%20criar%20agendamentos,op%C3%A7%C3%B5es%20do%20menu%20Ambiente%20-%3E%20Schedule%20-%3E%20Schedule%3A)
* [Pontos de Entrada](https://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)
* [Agendamento (Schedule) - Importador XML](https://tdn.totvs.com/display/public/PROT/Agendamento+%28Schedule%29+-+Importador+XML)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
