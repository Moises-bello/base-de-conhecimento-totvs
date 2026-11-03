---
content_hash: b633134c920ba56172d60188b9f598bf5b127b7b015e9d5e13fee3cd9a029cd0
fetched_at: '2026-06-29T00:05:55.861957+00:00'
page_id: '146965906'
product: rm
source: tdn-rm
title: Existe a possibilidade de vincular um evento a outro para realizar lançamentos
  vinculados?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=146965906
version: 1
---

| Produto | **RM** |
| --- | --- |
| **Sintoma** | **Existe a possibilidade de vincular um evento a outro para realizar lançamentos vinculados?** |
| Solução | Sim, existe a possibilidade de realizar lançamentos vinculados.  Este recurso possibilita a vinculação de um evento a outro, de modo que ao lançar o *Evento Principal* para a movimentação, o *Evento Vinculado* seja lançado automaticamente. Minimizando assim a necessidade de informar eventos nos Grupos de Eventos, Códigos Fixos, Cancelamento, Importação, etc.     Para parametrizar o evento vinculado, deverá acessar Cadastros | Eventos | Anexos | Lançamento Vínculos e o preencher Eventos Vinculados (serão lançados automaticamente). Poderão ser associados quantos eventos forem necessários.     Será possível também visualizar os ‘Eventos Principais’, ou seja, que os eventos que lançarão os eventos vinculados automaticamente.     Através do LOG de Cálculo o usuário poderá consultar quais foram os eventos lançados através da vinculação ao evento principal, deixando assim o processo mais claro e rápido. Os Eventos Vinculados serão lançados automaticamente sempre que o Evento Principal for lançado/inserido no envelope de pagamento.  Lembrando que, a funcionalidade é apenas lançar o evento, o cálculo do Evento Vinculado obedecerá à parametrização do evento.  Não será possível excluir somente o *Evento Vinculado* do envelope de pagamento, sem que o *Evento Principal* seja excluído, pois ao salvar o envelope o *Evento Vinculado* será lançado novamente na movimentação.  Sendo a única forma do *Evento Vinculado* não ser apresentado na movimentação do funcionário o não relacionamento com o *Evento Principal* ou alteração manual.  No cancelamento de movimento se o usuário cancelar um *Evento Vinculado*, o sistema irá voltar com este evento no final do cálculo do cancelamento.     **Atenção I:**  Sempre que importar ou digitar um evento que tiver *Evento Vinculado*, ao gravar o *Evento Principal* no envelope de pagamento, o sistema irá gravar também o *Evento Vinculado*.     **Atenção II:**  Sempre que nos parâmetros do RM Labore existir *Evento Vinculado* a um Evento Adicional, seja de Férias, Rescisão ou 13º Salário, ao lançar o Evento Adicional, o *Evento Vinculado* também será lançado.     Disponibilizado em Utilitários | Importação de Dados do RM Labore a importação dos Lançamentos vinculados. |
