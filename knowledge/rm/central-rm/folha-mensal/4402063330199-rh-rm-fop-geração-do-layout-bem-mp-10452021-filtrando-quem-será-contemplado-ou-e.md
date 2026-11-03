---
article_id: 4402063330199
category: Folha Mensal
content_hash: 067c8bcf9d2eb83ad5579fd301c78d52f0e734cafa5631c6418ece7ca4f51e5a
fetched_at: '2026-06-28T22:46:59.391150+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP -  Geração do Layout B.E.M. MP 1.045/2021 filtrando quem será
  contemplado ou excluído (aposentados, intermitentes e admitidos após 28/04/2021)
type: support-article
updated_at: '2025-03-07T14:53:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402063330199-RH-RM-FOP-Gera%C3%A7%C3%A3o-do-Layout-B-E-M-MP-1-045-2021-filtrando-quem-ser%C3%A1-contemplado-ou-exclu%C3%ADdo-aposentados-intermitentes-e-admitidos-ap%C3%B3s-28-04-2021
---

**Dúvida**Existe alguma forma de filtrar quem poderá ou não ser levado no layout do B.E.M?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir das versões:

* 12.1.28.293
* 12.1.29.257
* 12.1.31.162
* 12.1.32.104

**Solução**Foi implementado um passo a passo com duas opções para tratar esta demanda. Uma via consulta SQL e outra usando campos do filtro:

* *Usando consulta SQL para gerar o arquivo*

1) Criar uma consulta SQL que retorna as chapas contempladas para na adesão do BEM. No exemplo abaixo selecionamos as chapas não considerando algumas situações, data de admissão após a data da publicação da MP e se o mesmo é aposentado ou tem contrato intermitente  
  
![image2020-5-6_18-19-35.png](https://tdn.totvs.com/download/attachments/545641381/image2020-5-6_18-19-35.png?version=1&modificationDate=1588799975283&api=v2) ![image2020-5-6_18-21-40.png](https://tdn.totvs.com/download/attachments/545641381/image2020-5-6_18-21-40.png?version=1&modificationDate=1588800101037&api=v2)  
  
2) No Filtro do B.E.M, selecionar o campo Chapa do Funcionário, o operador IN (SQL) e a consulta SQL criada acima. Ao executar o processo será considerado somente a chapas da consulta:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402063147543/mceclip0.png)

* *Usando Campos do Filtro*

1) Criar um filtro usando os campos disponíveis no recurso de Filtros. No exemplo abaixo foram utilizados os campos Data de admissão, data de acordo, Contrato intermitente e situação. Ao executar o processo será considerado somente a chapas retornadas pelo filtro criado:  
  
![](https://tdn.totvs.com/download/attachments/617174252/image2021-5-17_22-7-45.png?version=1&modificationDate=1621300065527&api=v2)  
  
**Observações:****Para primeiro registro de acordo não enviado para o governo:**Caso necessite de edição realizada no cadastro do acordo poderá ser informada a data de mudança do primeiro registro do acordo. Com isso, não será criado um novo registro. Consequentemente os campos atualizados serão: Tipo de Adesão, Valor Reduzido, Data de Acordo, Percentual de Jornada e/ou Dias de Duração de Acordo.  
  
**Para registros já enviado para o governo:**Para cada registro de edição realizada no cadastro do acordo é extremamente necessário que seja informada uma nova data de mudança para o registro no histórico. Para que assim seja criado um novo registro no histórico. Consequentemente os campos atualizados serão: Dias de Prorrogação,  Data do Cancelamento ou Data de Antecipação.  
  
**Para registro de Cancelamento, Antecipação ou Prorrogação não enviado para o governo:**Para cada registro de edição realizada no cadastro do acordo, poderá ser utilizada a mesma data do ultimo registro cadastrado. Assim o ultimo registro será editado e não criará um novo. Consequentemente os campos atualizados serão: Dias de Prorrogação,  Data do Cancelamento ou Data de Antecipação.  
  
**Saiba mais:** [Filtro para adesão e não adesão do B.E.M](https://tdn.totvs.com/pages/releaseview.action?pageId=617174252)
