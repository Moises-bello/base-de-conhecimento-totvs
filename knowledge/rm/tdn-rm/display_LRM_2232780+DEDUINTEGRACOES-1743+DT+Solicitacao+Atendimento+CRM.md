---
content_hash: fdfb5eeffd419aa39ab27dedb9e178cb3f00ce628825d2ec3c6f7db8a57fcc01
fetched_at: '2026-06-29T00:08:51.961460+00:00'
page_id: '338373412'
product: rm
source: tdn-rm
title: 2232780 DEDUINTEGRACOES-1743 DT Solicitacao Atendimento CRM
type: documentation
url: https://tdn.totvs.com/display/LRM/2232780+DEDUINTEGRACOES-1743+DT+Solicitacao+Atendimento+CRM
version: 1
---

# SOLICITAÇÃO DE ATENDIMENTO - CRM

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Educacional* |
| **Função:** | Solicitação de atendimento - CRM |
| **Situação/Requisito:** | Ao selecionar um tipo de atendimento que esteja com o parâmetro "Substituir todos os valores atuais pelos do modelo do tipo de atendimento" selecionado, caso não exista nenhum modelo parametrizado para o tipo de atendimento no módulo CRM, a solicitação gerada não é criada com o local de entrega informado no processo. |
| **Solução/Implementação:** | Ajustes para que, na abertura de solicitação de atendimento no TOTVS Educacional, ao selecionar um tipo de atendimento que esteja com o parâmetro "Substituir todos os valores atuais pelos do modelo do tipo de atendimento" selecionado, caso não exista um modelo parametrizado no módulo CRM isso seja informado ao usuário. Caso o usuário mesmo assim decida dar sequência no processo o local de entrega selecionado será o utilizado na abertura da solicitação. Caso o modelo tenha sido corretamente parametrizado no módulo CRM o local de entrega do processo será o informado no modelo. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
