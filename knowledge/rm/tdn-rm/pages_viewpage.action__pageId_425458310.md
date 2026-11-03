---
content_hash: 95cef1f29365f6767457781caf1ab8ed68bf3972d890c6a2d0d0ab93b6543e7b
fetched_at: '2026-06-29T00:09:29.845242+00:00'
page_id: '425458310'
product: rm
source: tdn-rm
title: Confirmar inscrições
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458310
version: 5
---

Este processo será executado a partir da visão de "processos seletivos". Existem quatro status possíveis para uma inscrição, são eles: Inscrito (pendente de confirmação de pagamento), Candidato (inscrição confirmada), Excedente (quando o processo seletivo utiliza controle de vagas) e Inscrição cancelada. A inscrição excedente e cancelada será ignorada na confirmação da inscrição.

Quando uma inscrição for realizada o status inicial da mesma será "Inscrito". Porém, se o valor da inscrição for zero ou a forma de inscrição aplicar 100% de desconto, o status da inscrição passará a ser "Candidato".  
Para as demais inscrições, cujo valor seja maior que zero, será necessário utilizar este processo para que as mesmas tenham seus status evoluídos de "Inscrito" para "Candidato".

*obs: O status do "Inscrito" em um processo seletivo que tenha valor maior do que R$ 0, só será atualizado para "Candidato" mediante a quitação do lançamento gerado.*

Durante o período de inscrições de um processo seletivo, os bancos conveniados com a instituição de ensino, ou seja, os que estão habilitados a receberem os boletos de pagamento de taxa de inscrição deverão enviar o arquivo CNAB. Ao receber o arquivo CNAB, a instituição deverá utilizar o módulo "RM Fluxus" para baixar os lançamentos pagos pelos candidatos.

Depois que os lançamentos forem baixados, basta executar este processo "confirmar inscrições" que todos os candidatos que estiverem com o status do lançamento igual a "Quitado" passarão a ter o status de inscrição igual a "Candidato".

Na "Inscrição de Candidato" será possível verificar o status de inscrição, para isso basta verificar o conteúdo do campo "Status da inscrição".  
  
Quando no processo seletivo está marcado a opção "Utiliza alocação automática?", ao confirmar as inscrições, o processo logo em seguida fará a alocação dos candidatos e caso ocorra alguma inconsistência na alocação dos candidatos que tiveram a inscrição confirmada. Para o correto funcionamento deste processo é necessário que o parâmetro "E-mail do remetente do processo seletivo" esteja preenchido ().

**Pré - requisitos do processo**:

* O processo seletivo para o qual o processo será executado deverá estar no período de inscrição.
* Deverão existir inscrições realizadas para o processo seletivo
