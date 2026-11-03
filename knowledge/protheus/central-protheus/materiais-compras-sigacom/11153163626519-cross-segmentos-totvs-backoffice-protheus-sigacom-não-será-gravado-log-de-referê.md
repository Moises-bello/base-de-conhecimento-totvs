---
article_id: 11153163626519
category: Materiais - Compras (SIGACOM)
content_hash: 20441600a4ef97e72e3233ecaae7700c9ac764c9b4c6d3f579182df21c2fdd7a
fetched_at: '2026-06-28T22:41:20.263002+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Não será gravado log
  de referência, pois a Solicitação/Item não existe.
type: support-article
updated_at: '2025-01-22T11:41:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11153163626519-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-N%C3%A3o-ser%C3%A1-gravado-log-de-refer%C3%AAncia-pois-a-Solicita%C3%A7%C3%A3o-Item-n%C3%A3o-existe
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21860567178647) Tempo aproximado para leitura: **00:01:00min****Ocorrência**Mensagem "Não será gravado log de referência, pois a Solicitação/Item não existe:" esta sendo apresentada no Protheus.  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Compras  
  
**Causa**A mensagem ocorre por conta do parâmetro MV\_HABLOG, quando o parâmetro foi habilitado quando o processo já estava iniciado.   
  
**Solução**Para solucionar a mensagem, caso NÃO utilize os log de referencia de processo, basta desabilitar o parâmetro MV\_HABLOG, assim o sistema ira parar de validar  essa questão e não tentara gravar os Log de referencia.

Ou Caso necessite deste log, solicitamos que  valide em homologação, habilitando o parâmetro e gerando o processo desde o início, pois deverá gravar o log como um todo.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
