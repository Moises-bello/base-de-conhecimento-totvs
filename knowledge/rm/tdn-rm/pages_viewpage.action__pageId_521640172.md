---
content_hash: 89f496dae2a09362d918733701020404b226f874e4a0786d78396cff57f3cd96
fetched_at: '2026-06-29T00:10:31.307429+00:00'
page_id: '521640172'
product: rm
source: tdn-rm
title: R-2099/R-4099 Fechamento dos Eventos Periódicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=521640172
version: 25
---

![](https://tdn.totvs.com/download/thumbnails/715830650/Retornar.png)
]]>#f5f5f5#363636noneR-2099/R-4099

## **Conteúdo**



### **01. Fechamento dos Eventos Periódicos****R-2099/R-4099****1**

Processo para realizar a transmissão do Fechamento dos Eventos Periódicos no período R-5011/9011 ou R-9015 selecionado.  
  
O processo Fechamento dos Eventos Periódicos será exibido em **RM > Gestão Fiscal > Obrigações Acessórias > SPED > REINF > Eventos Periódicos > Processos > Fechamento dos Eventos Periódicos.**

Imagem

Comportamento do processo:  Quando selecionado um ou mais Eventos R-5011/9011 ou R-9015 na visão de Eventos Periódicos, o processo será executado considerando o período de cada evento. Será gerado um Evento R-2099 para eventos do bloco 20 que são gerados a partir do R-5011/9011 e será gerado um Evento R-4099 para eventos do bloco 40 que são gerados a partir do R-9015, os eventos podem ser visualizados através do anexo Eventos. Todas as execuções deste processo serão registradas no histórico do evento e as alterações de status também serão registradas no histórico do evento.

Caso houver eventos **Pendentes R-20xx ou R-40xx** associados ao R-5011/9011 ou R-9015, o usuário poderá optar se prossegue com o processo de Fechamento ou Não; Se o usuário desejar prosseguir com o processo mesmo com pendências, um histórico com a opção desejada será persistido no evento R-5011.

### **02. Regras****2**

Poderá ser executado somente para Eventos com Status **Aberto.**

**R-2099:** O fechamento dos eventos do Bloco 20 podem ser realizados com ou sem informações no período.

**R-4099:** O fechamento dos eventos do Bloco 40 só pode ser realizado caso existam eventos enviados no período.

**Observações**

Quando houver um Evento **Inconsistente** ou **Rejeitado** o sistema irá reenviar estes eventos com um novo XML e um novo Id. da Reinf devido a validação abaixo:  
*"Código MS0037: Já existe na base de dados do Ambiente Nacional um evento com mesma identificação."*

A TAG compSemMovto não será gerada conforme a validação abaixo  
*"Código MS1217: tag compSemMovto não pode ser informada se o período de apuração é maior ou igual a 2018-11."*

A TAG evtPgtos não será gerada conforme a validação abaixo  
*"Validação: Só preencher este campo se {perApur} <= [2018-10]"*

Ao autorizar o R-2099 na versão 1.05 da REINF que exista R-2055 autorizado no período, o sistema irá exibir os **Totalizadores de** **Aquisições de Produtor Rural**
