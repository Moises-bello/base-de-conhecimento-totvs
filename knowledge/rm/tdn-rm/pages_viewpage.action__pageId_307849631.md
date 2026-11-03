---
content_hash: 5d2df1862b28f8e51862b2dd414028de3ed3331d8efd98290226b3eaa41cc706
fetched_at: '2026-06-29T00:08:44.382313+00:00'
page_id: '307849631'
product: rm
source: tdn-rm
title: Artigo 444 / 611 A - Item III - Empregado Diploma de Nível Superior
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=307849631
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **roduto:** | RM |
| **Ocorrência:** | **Artigo 444 / 611A – Item III**  Art. 444. ..............................  Parágrafo único. A livre estipulação a que se refere o caput deste artigo aplica-se às hipóteses previstas no art. 611-A desta Consolidação, com a mesma eficácia legal e preponderância sobre os instrumentos coletivos, no caso de empregado portador de diploma de nível superior e que perceba salário mensal igual ou superior a duas vezes o limite máximo dos benefícios do Regime Geral de Previdência Social.”(NR)    Art. 611-A. A convenção coletiva e o acordo coletivo de trabalho têm prevalência sobre a lei quando, entre outros, dispuserem sobre:  III – Intervalo intrajornada, respeitando o limite mínimo de trinta minutos para jornadas superiores a seis horas; |
| **Ambiente:** | Empregado diploma de Nível Superior |
| **Passo a passo:** | Para atender artigo 444 / 611 A - Item III, foi realizado os seguintes procedimentos:  Em Módulo RH>Automação de Ponto>Cadastros>Horários por intervalo > Foi cadastrado um horário padrão de 08:00 de jornada com um intervalo de 01:00 de refeição.       Foi associado o horário cadastrado ao funcionário:        Através do Menu>Processos>Lançamentos de Horários> Foi realizado lançamentos de batidas padrão para o funcionário no período de 01/09 a 30/09:        No dia 12/09 foi alterada a batida de refeição que era de 12:00 a 13:00 para 12:00 a 12:30, onde ao recalcular o sistema gerou 00:30 de extra para o funcionário.      Essa hora extra pode ser gerada no movimento somada às outras horas extras normais, mas também pode ser lançada em evento diferenciado, como segue abaixo:  Acessar o menu Configurações > Eventos:      Incluir evento com código de cálculo 0043 ( evento por tipo de ocorrência):      Após salvar, acessar o anexo > Evento por tipo de ocorrência e incluir o tipo de ocorrência ERA – Extra de Refeição Autorizado:      Após o processo acima, acessar o parametrizador do sindicato (Configurações> Parametrizador> Sindicato), aba Eventos e fazer a inclusão do evento criado, relacionando a ele o evento do Labore:      Em parametrizador do sindicato, acessar a etapa Extra e marcar o flag “Considera extras de refeição dentro do intervalo de ausência planejada”.    Salvar o parametrizador.  Após o recálculo da movimentação, será lançado para o movimento o evento de refeição conforme cadastrado anteriormente:      Acessar Movimento>Lançar para folha de Pagamento> Realizar lançamento dessas horas para a folha de pagamento:        Acessar módulo da folha de pagamento>Folha Mensal>Consulta movimentação da integração, lançar os eventos para folha.      Ao lançar a folha de pagamento pelo menu Folha mensal > Lançamentos > Grupos de eventos, o evento é incluído no envelope de pagamento do funcionário. |
|  |  |
| **Observações:** |  |
