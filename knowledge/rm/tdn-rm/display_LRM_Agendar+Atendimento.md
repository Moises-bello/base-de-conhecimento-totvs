---
content_hash: 0f9a25af474448cf79c22c7986fc874e053f0bb31de94244272ce8f88fffc861
fetched_at: '2026-06-29T00:09:37.528111+00:00'
page_id: '425459632'
product: rm
source: tdn-rm
title: Agendar Atendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Agendar+Atendimento
version: 6
---

# **Agendar Atendimento**

O processo de **Agendar Atendimento** permite que o atendente informe o Prazo Limite e Data de Despertar do atendimento. Dependendo da data de Prazo Limite, o atendimento retorna efetuando um repasse para o atendente responsável pelo contato com o cliente a fim que este seja informado do prazo limite estipulado para a solução do atendimento.  
Para executar o processo, os atendimentos que serão sofrer o agendamento devem ser selecionados e o processo executado, o sistema apresentará uma interface com a lista de atendimentos que foram selecionados, juntamente com as datas de previsão para conclusão, data de despertar, o motivo do agendamento e a justificativa.  
   
O status do atendimento será  apresentado como "Agendado a Responder" se o prazo limite novo for maior que o prazo limite inicial (anterior) do atendimento e "Agendado Respondido" caso contrário (se o prazo limite novo for menor ou igual que o prazo limite inicial (anterior)).  
Se o Prazo Limite novo ou a Data de Despertar (Agendado Para) for menor que 01/01/2000 então o sistema considerará como data inválida, o processo será interrompido e enviada uma mensagem.  
Se a Data de Despertar (Agendado Para) for menor que a data atual, o processo será interrompido e enviada uma mensagem.  
Se o Prazo Limite novo for menor que a data de despertamento (Agendado Para) o processo será interrompido e enviada uma mensagem.  
Busca a descrição do motivo de agendamento e juntamente com a justificativa estas informações são gravadas no campo discussão do atendimento;  
Se o Prazo Limite novo for maior que o Prazo Limite inicial (anterior) então o status do atendimento é alterado para "Agendar a Responder" e o atendimento é repassado ao atendente que é responsável pelo contato com o cliente caso contrário o status do atendimento é alterado para "Agendado Respondido";   
Existe um botão "Automático", que ao ser pressionado irá preencher os campos: (Data de Despertar, Prazo Limite).

Processo de Agendar Atendimento , pode ser feito diretamente pela TELA do atendimento. Basta selecionar o Atendimento e em Seguida marcar opçção : Agendar e inserir os dados  e SALVAR.

# **Despertar de Atendimento**

TCGI | Cobrança | Atendimetno | Despertar de Atendimento

**Despertar de Atendimento:**  Data que o atendimento terá seu status alterado para dar andamento no atendimento.  
Para especificar o horário que o serviço de despertar será executado (recomendável para organizações que trabalham com turnos de funcionários) basta realizar configuração do parâmetro: "Utilizar data/hora do momento da execução do serviço".  
Veja maiores detalhes nos parâmetros gerais do sistema: Clique aqui.  
**Prazo limite:** Calcula qual data será o prazo limite baseado na Data de Despertar + Previsão de Horas para se realizar o atendimento (fica dentro de dados adicionais). Esse cálculo irá levar em consideração o calendário e o período de trabalho do atendente, sendo que primeiro buscará o período de trabalho por atendente, se não existir buscará o período de trabalho global do TOTVS Aprovações e Atendimento.  
Caso a hora do prazo limite seja diferente do horário de expediente ou no horário de almoço, será considerado a próxima hora útil do atendente.  
Não irá considerar sábado e domingo como dia útil, em nenhuma hipótese.  
Se o campo Dados Adicionais / Previsão de Horas não estiver preenchido, o cálculo não será realizado, e será apresentada uma mensagem informativa.  
Se não existir período de trabalho do atendente, e não estiver definido o horário de expediente nos parâmetros do TOTVS Aprovações e Atendimento, o cálculo não será realizado e será apresentada uma mensagem informativa.

Fica Registrado no Histórico o Processo de Agendamento.  
   
Verifique informações sobre o Serviço de Despertar: Clique aqui.
