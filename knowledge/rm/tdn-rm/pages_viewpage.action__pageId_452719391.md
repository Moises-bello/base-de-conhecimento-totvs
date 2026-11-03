---
content_hash: 8ef8e9fe5ea7d267e072238a955247d6a67abea7ad253dca40be6c76d44d34f0
fetched_at: '2026-06-29T00:10:07.277744+00:00'
page_id: '452719391'
product: rm
source: tdn-rm
title: Resilição Parcial - Tipos de Resilição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719391
version: 2
---

Através deste módulo o usuário deve cadastrar os Tipos de Resilição e suas particularidades para o cálculo, vinculando aos Tipos de Desligamento da Rescisão.  
    
 **Identificação:** Informações que identificam o Tipo de Resilição

**Código:** Campo obrigatório, onde será informado um código identificador, que será utilizado no cadastro de resilição. Este campo pode ser preenchido com alfanumérico, com até 2 caracteres. Não pode existir mais de um cadastro com o mesmo código.  
    
 **Descrição:** Campo obrigatório, onde será inserido uma descrição para o tipo de resilição.   
    
 **Tipo de Demissão:** Campo obrigatório, onde é informado o tipo de demissão, ao qual será feito o cálculo da Resilição Parcial. Para este campo, só é possível informar os tipos: 2 - Inic. Empregador sem justa causa, 4 - Inic. Empregado sem justa causa e T - Término de contrato de trabalho. 

**Parametrização dos eventos:** Cadastro que permite customizações no cálculo da resilição para atender a diversas particularidades das convenções coletivas. Somente os eventos incluídos neste cadastro serão considerados no cálculo do recibo da resilição parcial. Neste módulo o usuário irá selecionar quais verbas rescisórias deverão entrar ou não no processo de resilição, bem como acrescentar novos eventos adicionais à execução.

**Código do Evento:** Campo obrigatório, onde será informado o código do evento a ser lançado na resilição parcial. No caso de eventos que não constam no grupo de verbas rescisórias calculadas pelo sistema, este será adicionado ao recibo da resilição.  
    
 **Observação**   
 Somente os eventos incluídos neste cadastro serão considerados no cálculo do recibo da resilição parcial.  
    
 **Código Fórmula:** Campo não obrigatório, onde será informado uma fórmula, caso se deseje alterar o valor calculado para o evento.  
    
 **Código Evento Folha**: Campo obrigatório, onde será informado o código do evento a ser lançado no envelope da movimentação.  
    
 **Observação**   
 O evento informando no campo Código Evento Folha deve ter o mesmo código de cálculo do evento informado no campo Código do Evento.  
 Para os códigos de cálculo 1, 2, 3 e 4, o evento informado no campo Código Evento Folha não pode ser o mesmo do campo Código do Evento, porém deve possuir o mesmo código de cálculo.   
 Para os demais códigos de cálculo, pode ser informado ou não o mesmo evento em ambos os campos, ficando opcional ao usuário.
