---
content_hash: 1b57c91f7fa23f22bbaf3b5c9abd339ad9dedfcd5e397fedd6a7396198dba455
fetched_at: '2026-06-29T00:10:08.815986+00:00'
page_id: '452719585'
product: rm
source: tdn-rm
title: S-2206 – Alteração de Contrato de Trabalho
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719585
version: 10
---

Este evento registra as alterações do contrato de trabalho, tais como: remuneração e periodicidade de pagamento, duração do contrato, local, cargo ou função, jornada, etc. "S-2200 - Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador".

   
**OBSERVAÇÃO** Sempre que o usuário realizar uma alteração no cadastro de funcionário, serão verificados nos campos abaixo se foram alterados e deverá criar um gatilho considerando as datas de alterações informadas na alteração (histórico).  
Será gerado um gatilho para cada uma das datas diferentes, sendo agrupado de acordo com a data de alteração.

* + Salário
  + Horário
  + Função
  + Transferência entre Seções
  + Cargo de confiança

**ATENÇÃO:**

Ao excluir um histórico de horário por meio do cadastro do funcionário, um gatilho será gerado na fila de eventos para o evento S-2206 - Alteração de Contrato de Trabalho, com a tag <dtAlteracao> representando a data da exclusão do histórico.

Não será gerado um gatilho na fila de eventos se a data do histórico for anterior à data de obrigatoriedade do eSocial.

   
**Considerações sobre algumas tag's geradas no arquivo:**  
   
**qtdHrsSem** - A média de horas semanais pode ser calculada de acordo com a seguinte regra:

* + Se o parâmetro para considerar a jornada do funcionário estiver marcado no parametrizador do eSocial: a jornada mensal será dividida por 4.
  + Para os demais cenários a soma das horas das jornadas de trabalho do horário será dividida pelo número de dias do horário (incluindo os dias de descanso), e o resultado será multiplicado por 7 (fixo).

É importante observar que, para cada hora de adicional noturno, será aplicado no cálculo um percentual de 14,29% da Nona Hora. Certifique-se de considerar esta observação ao realizar os cálculos.

**EXEMPLO:**

1. Horário com 7 dias, sendo que 5 são jornadas trabalhadas, total de 40 horas:  (40 / 7 \* 7) = 40hs
2. Horário com 7 dias, sendo que 5 são jornadas trabalhadas, com uma hora de adicional noturno diária, total de 40 horas e 45 minutos (adicional noturno) (40.75 / 7 \*7) = 40.75 hs
3. Horário com 14 dias, sendo que 10 são jornadas trabalhadas, total de 84 horas: (84 / 14 \* 7) = 42hs
4. Horário com 3 dias, sendo que 2 são jornadas trabalhadas, total de 16 horas: (16 / 3 \* 7) = 37hs

**OBSERVAÇÃO:** 

Ao transferir um funcionário entre filiais, o sistema preencherá a tabela PESOCIALEVENTOS.ALTERACAOFILIAL seguindo a seguinte regra:

O valor 1 será registrado quando o evento (S-2206 - Alteração de Contrato de Trabalho) for gerado para uma transferência que envolva a mudança de filial.

Isso sinaliza, ao enviar o XML para o TAF, que se trata de uma alteração de filial. Dessa forma, o TAF consegue identificar o evento de admissão do funcionário (S-2200) e transferi-lo para a nova filial.

**treiCap** -  Serão considerados na geração do evento os treinamentos com data de fechamento (campo VTUAVCONH.DTFECHAMENTO) igual a data de alteração do evento e caso seja inserido o evento manual na fila será considerado a data do evento. 

**dtAlteracao** - Caso tenha um histórico do campo alterado, o sistema irá buscar a data desse histórico. Caso contrário, a data é gerada conforme a data atual.

   
[**Mapeamento das informações do evento**](http://tdn.totvs.com/display/LRM/Evento+S-2206)  
   
 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Eventos Iniciais

Gerar XML
