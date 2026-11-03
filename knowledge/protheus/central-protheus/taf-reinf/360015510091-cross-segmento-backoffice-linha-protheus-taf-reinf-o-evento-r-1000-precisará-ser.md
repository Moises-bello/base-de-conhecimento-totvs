---
article_id: 360015510091
category: TAF - REINF
content_hash: d68a3429b9228fab4a792a2c7425918807bcd8a13abfaedf5d33629eead27ee8
fetched_at: '2026-06-28T22:41:33.359361+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - TAF - REINF - O Evento R-1000
  Precisará ser Enviado Todo Mês para Abrir o Período?
type: support-article
updated_at: '2023-03-30T16:53:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015510091-Cross-Segmento-Backoffice-Linha-Protheus-TAF-REINF-O-Evento-R-1000-Precisar%C3%A1-ser-Enviado-Todo-M%C3%AAs-para-Abrir-o-Per%C3%ADodo
---

**Dúvida**O evento **R-1000** precisará ser enviado todo mês para abrir o período?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) -TAF - a partir da versão 12  
   
**Solução**

O evento **R-1000** é um evento de tabela inicial, que só deve ser enviado uma única vez, quando as empresas forem entrar na obrigatoriedade da **EFD-Reinf**. Caso ocorra alterações na situação fática prestada pelo contribuinte no evento **R-1000**, deverá a empresa enviar o **R-1000** para alterar essas informações prestadas anteriormente. A abertura do movimento será feita pelo o envio do primeiro evento periódico da competência.

Evento em que são fornecidas pelo contribuinte informações cadastrais necessárias ao preenchimento e validação dos demais eventos da EFD-Reinf, inclusive para apuração das retenções e contribuições devidas.

**Prazo de envio:** A informação prestada neste evento deve ser enviada no início da utilização da EFD-Reinf e pode ser alterada no decorrer do tempo, desde que não ultrapasse o dia quinze do mês subsequente aos fatos geradores a que se refere.

**Pré-requisitos**: Este é o primeiro evento a ser transmitido pelo contribuinte.

Existe uma FAQ disponível pela Receita Federal  referente a alterações de informações fáticas no evento R-1000, conforme dispostos nos itens abaixo, compete ao responsável pela EFD REINF analisar se alterações enviadas como alteração no evento R-1000 estão inseridas no contexto apresentado na FAQ.

**2.1.1 - O registro R-1000 será enviado no início e não precisará ser enviado novamente se não houver nenhuma alteração? Ou precisará ser enviado todo mês para abrir o período?**

*O evento R-1000 é um evento de tabela inicial, que só deve ser enviado uma única vez, quando as empresas forem entrar na obrigatoriedade da EFD-Reinf. Para que não seja necessário preencher o evento R-1000 todo o mês, o contribuinte deverá deixar a "data término de validade" [fimValid] em branco, sem preenchimento.*

*Caso ocorra alterações na situação fática em alguma(s) da(s) informação(ões) prestada(s) pela empresa no evento R-1000,  a empresa deverá informar a data fim de validade no evento R-1000 anterior e enviar um novo R-1000 completo, incluindo as devidas alterações. A abertura do movimento será feita pelo o envio do primeiro evento periódico da competência.*

**2.1.5 - Considerando que já tenha sido prestada informação anteriormente e se pretende prestar informações relacionadas a um novo período com informações diferentes, é necessário enviar um evento R-1000 informando fim da validade do evento enviado anteriormente? (atualizada em 10/0-8/2020).**

*Sim, para enviar o novo evento com nova data de início da validade (campo iniValid) no bloco de "inclusao", é necessário informar a data fim de validade no evento anterior. Esse procedimento fará com que seja permitido o envio de novo evento R-1000.*

*Por exemplo: Se houver novas informações a partir de 08/2020, o evento R-1000 anterior deverá a data fim de validade de 07/2020. E, consequentemente, o novo evento R-1000 deverá ter data início de validade em 08/2020.*

O link abaixo contempla a FAQ disponível pela Receita Federal

<http://sped.rfb.gov.br/pastaperguntas/show/1497>

**Informações adicionais:**

**Eventos Reinf**

<https://tdn.totvs.com/display/public/PROT/Eventos+Reinf>
