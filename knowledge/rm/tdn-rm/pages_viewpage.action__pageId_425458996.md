---
content_hash: c72cbc6a3154fa29c8ccfc981d4f61facd7b345d718cc630b216f9afb30e99c6
fetched_at: '2026-06-29T00:09:33.365930+00:00'
page_id: '425458996'
product: rm
source: tdn-rm
title: Repasse - TOTVS Aprovações e Atendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458996
version: 3
---

**Repasse**   
No momento de efetuar o repasse de um atendimento para outro atendente o sistema efetua uma validação para confirmar se o atendente se encontra em seu horário de serviço, para que o repasse possa ser concluído sem nenhuma indagação. Como o sistema pode ter integração com o sistema de ponto eletrônico, pode ter um horário de trabalho fixo e também pode ter um horário definido por atendente onde é necessário especificar ao sistema como ele fará tal verificação.  
   
Este parâmetro é utilizado para informar ao sistema como ele irá efetuar a validação de horário de serviço do atendente para identificar se o mesmo está ou não fora de seu período de trabalho. As opções são as seguintes:  
   
**Horário de expediente fixo**  
   
O sistema irá utilizar um horário fixo definido pelo administrador e devidamente cadastrado. Esta validação irá contemplar qualquer atendente. Caso o horário fixo não esteja cadastrado então o sistema irá considerar o horário fixo das 06:00 às 18:00h, sem intervalo.   
   
   
**Horário de expediente por atendente no TOTVS Aprovações e Atendimento**  
   
A validação se realizada pelo período de trabalho do atendente que se encontra em cadastrado em "Período de Trabalho".  Caso esta opção esteja em uso e não há período de trabalho para o atendente então o sistema irá utilizar o horário fixo.   
   
   
**Horário de expediente do atendente/funcionário no RMChronus (Off-Line)**  
   
Será verificado o horário do atendente cadastrado no RMChronus. A validação será realizada para confirmar se atendente está fora do horário de trabalho.   
   
   
**Horário de expediente do atendente/funcionário no RMChronus (On-Line)**  
   
Será verificado o ponto eletrônico (RMChronus), se houve batida de entrada/saída pelo atendente/funcionário e nesta validação retornará se o atendente se encontra ou não na empresa (horário de trabalho). Tipo de informação: Valor que representa hora e minuto (hh:mm).  
   
   
**Desconsiderar tempo gasto fora do período de trabalho para o cálculo de tempo útil de permanência no histórico de repasse**   
   
Quando é executado algum repasse o sistema calcula o tempo que o atendimento ficou com o atendente e o insere este tempo útil na tabela de histórico de repasse. Este cálculo é realizado com base na data em que o atendente recebeu o atendimento (ou data de abertura do atendimento), a data que ele está repassando e o cálculo leva em consideração o horário do atendente (por atendente ou fixo observando o calendário com feriados e dias úteis).  
   
O horário de trabalho pode não ser uma coisa rígida e muitos atendentes podem trabalhar fora destes períodos. Este parâmetro informa ao sistema, no momento de efetuar tais cálculos, que é para desconsiderar os períodos (os tempos) trabalhados fora de seu horário previamente cadastrado, em outras palavras, o tempo útil é calculado observando somente os dias e os períodos de trabalho.
