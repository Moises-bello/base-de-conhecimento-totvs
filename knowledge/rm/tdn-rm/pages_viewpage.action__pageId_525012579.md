---
content_hash: 2ae65c3284bda35e960259824f3db4e06ba4aa7485df972d0b5cea0362b7d227
fetched_at: '2026-06-29T00:10:31.915069+00:00'
page_id: '525012579'
product: rm
source: tdn-rm
title: R-2098/R-4099 Reabertura dos Eventos Periódicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=525012579
version: 15
---

![](https://tdn.totvs.com/download/thumbnails/715830650/Retornar.png)
]]>#f5f5f5#363636noneR-2098/R-4099

## **Conteúdo**



### **01. Reabertura dos Eventos Periódicos** **R-2098/R-4099****1**

Processo para executar a transmissão do Evento Período R-2098/R-4099 que é referente a Reabertura dos Eventos Periódicos no período R-5011/9011 ou R-9015 selecionado.

O processo Reabertura dos Eventos Periódicos será exibido em **RM > Gestão Fiscal > Obrigações Acessórias > SPED > REINF > Eventos Periódicos > Processos > Reabertura dos Eventos Periódicos.**

Imagem

Comportamento do processo:  Quando selecionado um ou mais R-5011/9011 ou R-9015 na visão de Eventos Periódicos, o processo será executado considerando o período de cada evento. Será gerado um Evento R-2098 para eventos do bloco 20 que são gerados a partir do R-5011/9011 e será gerado um Evento R-4099 para eventos do bloco 40 que são gerados a partir do R-9015. Todas as execuções deste processo serão registradas no histórico do Evento e as alterações de status também serão registradas no histórico do evento.

### **02. Regras****2**

Poderá ser executado somente para R-5011/9011 ou R-9015 com Status **Encerrado.**

**Observações**

Quando houver um Evento **Inconsistente** ou **Rejeitado** o sistema irá reenviar este eventos com um novo XML e um novo Id. da Reinf devido a validação abaixo:  
*"Código MS0037: Já existe na base de dados do Ambiente Nacional um evento com mesma identificação."*

Durante a transmissão podem ocorrer as seguintes situações:

* **Erro de validação do Status do Evento:** Este caso ocorrerá sempre que o processo for executado para um Evento com o status diferente de Encerrado. Neste caso o processo apresentará um log de erro e nada será salvo;
* **Erro na conexão com o TSS:** Este caso ocorrerá sempre que por diversos motivos o TSS não esteja preparado para receber a conexão com o RM. Neste caso o processo apresentará um log de erro e nada será salvo;
* **Erro de Schema:** Este caso ocorrerá quando ao Enviar o Evento ao TSS o mesmo apresentar erros de validação no schema xml do Evento. Neste caso o Evento R-2098 será salvo como inconsistente e nenhuma alteração ocorrerá no Evento R-5011;
* **Enviado com sucesso:** Este caso ocorrerá quando o RM enviar ao TSS o Evento R-2098 com sucesso. Neste caso o R-2098 será salvo com o status Pendente e o R-5011 será alterado para Pendente.
