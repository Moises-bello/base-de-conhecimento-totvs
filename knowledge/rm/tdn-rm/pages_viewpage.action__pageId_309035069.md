---
content_hash: e1e4130302a4d355878d96f90168c4658548d2b73259f2368cb17911631c48ed
fetched_at: '2026-06-29T00:08:44.472025+00:00'
page_id: '309035069'
product: rm
source: tdn-rm
title: Artigo 59-B - Compensação de horas X horas extras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=309035069
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | RM |
| **Versões:** |  |
| **Ocorrência:** | Art. 59-B. O não atendimento das exigências legais para compensação de jornada, inclusive quando estabelecida mediante acordo tácito, não implica a repetição do pagamento das horas excedentes à jornada normal diária se não ultrapassada a duração máxima semanal, sendo devido apenas o respectivo adicional. Parágrafo único. A prestação de horas extras habituais não descaracteriza o acordo de compensação de jornada e o banco de horas |
| **Ambiente:** | Acordo Coletivo de Trabalho, horas extras |
| **Passo a passo:** | Para atender o artigo 59-B, foi realizado a seguinte parametrização no RM Chronus:   * Em Cadastro>Horário por intervalo> Foi Cadastrado um horário 08:00 - 12:00 - 13:00 - 17:48. Sendo que o sábado é compensado com estes 48 minutos diários        * Em Cadastros>Alteração Global>Escala de Horário e Descanso, foi associado o horário para o funcionário.        * Em Cadastro > Funcionários > Ícone espelho > é possível fazer a visualização de como o horário ficou associado:          * Em Processos>Lançamentos de horários> Foi realizado  lançamento de batidas padrão para o funcionário:        * Depois desse processo acesse o espelho do funcionário, edite uma batida para gerar hora extra e recalcule;          * Verifique que o funcionário trabalhou até as 19:00, sistema gerou a hora extra de forma correta considerando somente 01h12m hora de extra, considerando a compensação como horario trabalhado.        * Após os calculos, foi realizado o lançamento dessa hora para a folha de pagamento, pelo menu Movimento > Lançar para Folha de Pagamento:        * Após esse processo os eventos são lançados para o módulo da Folha de pagamento através do módulo > Folha Mensal > Consulta movimentação da integração:     Ao lançar a folha de pagamento pelo menu Folha mensal > Lançamentos > Grupos de eventos, o evento é incluído no envelope de pagamento do funcionário: |
| **Observações:** |  |
