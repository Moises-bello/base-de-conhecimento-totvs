---
article_id: 31233326925591
category: Avisos Automáticos
content_hash: 32745b4e16fcf152205c046743e1931ceb6600cba4a63155871c3f6a50b229cb
fetched_at: '2026-06-28T22:46:40.510394+00:00'
product: rm
section_id: 31224122282519
source: central-rm
title: RH - RM - FOP - Como funciona o aviso automático Tipo 2 - Término de Contrato
  de Trabalho?
type: support-article
updated_at: '2025-04-08T18:06:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31233326925591-RH-RM-FOP-Como-funciona-o-aviso-autom%C3%A1tico-Tipo-2-T%C3%A9rmino-de-Contrato-de-Trabalho
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31233326895639) Tempo aproximado para leitura: **00:03:17 min****Dúvida**Como funciona o envio de avisos automáticos do tipo Escala de Férias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**

Será enviado um aviso automático pelo TOTVS Folha de Pagamento toda vez que um ou mais funcionários estiverem com contratos a vencer, ou seja, data de término de contrato próxima.

Este aviso tem como finalidade notificar os chefes com antecedência de modo que estes possam se preparar para a contratação ou demissão do(s) funcionário(s) em questão. O número de dias de antecedência que será enviado o aviso é controlado pelo campo Nro. Dias Ref.

Este tipo de aviso, será enviado para o Funcionário que possuir o mesmo tipo da parametrização escolhida, ou poderá deixar o campo em branco para verificar todos os tipos.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31233326896535)

No cadastro do funcionário, menu **Registro**, existe a aba **Dados do Contrato** onde serão inseridas as informações.

Selecionando o contrato, informamos a Data Final do Contrato em 14/03/2025 assumindo que a data de atual é 13/03/2025 (parametrizamos com o valor 1 no campo **Nro. Dias de Referência** no cadastro do aviso)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31233380025111)

Conforme a parametrização, o e-mail foi enviado um dia antes do contrato terminar, sempre verificando a data atual com a data final do contrato.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31233380026775)

**Importante**

Para executar a rotina automaticamente, deverá ser realizado o Agendamento de Job no ambiente conforme as orientações da documentação [Como agendar a execução de um processo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005088792-Framework-Linha-RM-Frame-Como-agendar-a-execu%C3%A7%C3%A3o-de-um-processo)
