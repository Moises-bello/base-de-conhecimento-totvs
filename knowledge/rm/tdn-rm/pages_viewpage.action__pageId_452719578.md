---
content_hash: 6f3b9a1cda738f75a7525daaa819c2fc18128d61a8d571b72a5ab6455efae1b7
fetched_at: '2026-06-29T00:10:08.782776+00:00'
page_id: '452719578'
product: rm
source: tdn-rm
title: Finaliza Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719578
version: 9
---

Através deste processo é realizados seguintes procedimentos:  
• Lançamento dos eventos de férias para o envelope, quando iniciadas no mês anterior e com término no mês atual;  
• Atualização da situação do funcionário para ' A-Ativo';  
• Atualização do saldo de férias do período aquisitivo aberto;  
• Mudança da 'Situação do Período' para 'Fechado', caso tenha completado os dias de direito de gozo;  
• Mudança da 'Situação das Férias' para 'Finalizadas' ou 'Finalizadas para o próximo mês', conforme o caso;  
• Abertura de novo período aquisitivo no caso de completar os dias de direito de gozo;  
• Gravação dos dados de antecipação de férias, quando o sindicato está parametrizado para permitir antecipação de férias;  
   
É possível realizar este processo para a próxima competência, para atender situação em que o funcionário é demitido para o próximo mês e não é possível liberar a competência.  
   
É recomendando a execução deste processo após a liberação da competência e antes do fechamento da folha, antes da liberação de competência, para garantir que todos os períodos de gozo finalizado no mês tenha a situação atualizada.  
   
O campo 'Situação das Férias' é preenchido conforme abaixo:  
G – Aguardando Aprovação do Gestor (quando o subordinado cadastra a sugestão de férias);  
D – Aguardando Aprovação do DP (quando o gestor aprova a sugestão e não tem permissão de marcar férias);  
M – Marcadas (quando o DP aprova ou quando o gestor tem permissão para marcar);  
P – Pagas (quando calcula as férias e as mesmas são lançadas na movimentação);  
F – Finalizadas (quando fecha o período aquisitivo e abre outro período aquisitivo, independente de ser um novo ou o mesmo);  
X - Finalizadas para o próximo mês (quando é processada a finalização de férias para a próxima competência. Na liberação de competência este campo é alterado para F – Finalizadas).

**Parâmetro: 'Considera a data atual como data final'**

Este parâmetro foi criado para que quando agendar o processo de finaliza férias, possa considerar os funcionários que estão retornando de férias até a data da execução do processo, se o retorno das mesmas for na competência da base.

*Exemplo 1*

Competência 07/2024. Processo sendo executado no dia  26/07/2024 

* Funcionário A com férias na situação pagas com data final dia 25/07/2024: As Férias serão finalizadas e o funcionário ficará como ativo
* Funcionário B com férias na situação pagas com data final dia 26/07/2024: As Férias serão finalizadas e o funcionário ficará como ativo
* Funcionário C com férias na situação pagas com data final dia 27/07/2024: As Férias não serão finalizadas e o funcionário permanecerá como a situação F

Este parâmetro não contemplará a finalização de férias próximo mês, seguindo o comportamento padrão

Quando a data da execução for maior que o ultimo dia da competência da base, mesmo com o parâmetro marcado, o processo irá considerar os funcionários que tem retorno até o ultimo dia da competência da base

*Exemplo 2*

Competência 06/2024. Processo sendo executado no dia  05/07/2024 

* Funcionário A com férias na situação pagas com data final dia 30/06/2024: As Férias serão finalizadas e o funcionário ficará como ativo
* Funcionário B com férias na situação pagas com data final dia 05/07/2024: As Férias não serão finalizadas e o funcionário permanecerá como a situação F, pois no agendamento será considerado como data final dia 30/06/2024

Se as férias começaram na competência anterior e finalizar na competência atual e a data final for igual a data da execução, as férias serão finalizadas e os valores de base serão lançados no período atual da base. Neste caso é importante verificar para que a base esteja configurada no período que deseja lançar os eventos de base.

Exemplo 3

01 - Gravação do agendamento em novembro para executar todos os dias, sendo que em novembro um funcionário tinha férias para finalizar

02 - Depois que processo foi gravado para executar todos os dias às 18:20 horas a competência foi alterada para Fevereiro com um funcionário terminando férias nesse mesmo mês

03 - Após o horário do agendamento no dia de hoje 26/02/2026 o processo foi executado automaticamente alterando o funcionário para ativo

04 - Isso pode ser acompanhado pelo Gerenciamento de JOBs

Veja que ao agendar fica criada a linha para a próxima execução

Ao terminar essa execução já cria-se a próxima linha para execução no dia seguinte

**Observação:**

Caso o parâmetro '**Não calcula Recibo de Férias**', disponível em **RH | Administração de Pessoal | Funcionários | Informações para o Cálculo | Parâmetros**, esteja 'marcado', o sistema não irá calcular o recibo de férias para o funcionário e também não serão exibidos no cadastro de férias o campo 'Data Pagamento' e os botões de 'Calcular' e 'Visualizar Recibo' de férias.

A mudança da situação do funcionário para 'Férias', continuará sendo feito pelo processo 'Lançar' férias'.

O processo 'Finalizar' férias vai mudar a situação do funcionário de 'Férias' para 'Ativo' e atualizar os dados cadastrais do período aquisitivo de férias.

O sistema não irá consistir na Liberação de Competência se constam no envelope do funcionário os códigos de cálculo específicos de férias para funcionários com o parâmetro marcado.
