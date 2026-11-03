---
content_hash: 021a0a32b59b5c3e21c890ea0689583c6726efb9bf21b6c7dad2d759522a7993
fetched_at: '2026-06-29T00:11:13.198319+00:00'
page_id: '658407863'
product: rm
source: tdn-rm
title: Nota Orientativa nº 09/2021 - Leiaute S-1.0
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=658407863
version: 17
---

false

**A partir dos patches:**

* 12.1.32.244
* 12.1.33.183
* 12.1.34.102
* e Superiores.

Objetivo:

Em 26/11/2021 foi disponibilizada a [Nota Orientativa S-1.0. 2021.09](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-orientativa-s-1-0-09-2021-retificada.pdf), com alterações no MOS-Manual de Orientação do eSocial da versão S-1.0.

Seguem orientações referente ao produto TOTVS Folha de Pagamento para atender essa alteração:

11AtualizadorAtualizador

Após a liberação da versão será necessário executar os script's de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe.**

true2AlteraçõesAlterações

1) Disponibilizado no parametrizador a nova descrição do leiaute, conforme abaixo:

2) S-2298 - Reintegração/Outros Provimentos, incluídos os tipos de reintegração/outro provimento:

3-Reversão de Servidor Público

4-Recondução de Servidor Público

Estes tipos são utilizados no caso de haver reversão, recondução de servidor estatutário, de re-inclusão de militar, bem como de outras formas de efetivo restabelecimento de vínculo, inclusive são aplicadas as mesmas regras de reintegração, devendo ser informada com a utilização dos códigos específicos, previstos para a tag <tpReint>.

Este tipos foram incluídos na tabela dinâmica PREINTEGRA, que será visualizado no campo "Tipo de Reintegração" existente no cadastro do Funcionário na Aba "Reintegração".

 do evento S-2298 - Reintegração / Outros Provimentos.

**OBSERVAÇÃO:** A aba "Reintegração" somente é apresentada quando o Tipo de Admissão na aba "Dados do Registro" for igual à "I".

3) S-1010 - Rubrica, conforme item 15.1, verbas de devolução de tributos ou outros descontos a trabalhadores tiveram a incidência da tag <IncIRRF> alterada  de "00 - Rendimento não tributável" para "79 - Outras isenções (o nome da rubrica deve ser claro para identificação da natureza dos valores)".

O DE/PARA da tag <codIncIRRF>  está disponível no menu  Cadastros | Eventos, conforme abaixo:

4) S-2240 - Condições Ambientais do Trabalho - Agentes Nocivos, para o item 12.3 liberado no MOS conforme destacado no print abaixo, foi questionado pelas empresas de softwares junto ao comitê do eSocial se teria algum impacto enviar todos os afastamentos, mesmo os não obrigatórios, o Comitê analisou e respondeu que não haverá prejuízo para os trabalhadores afastados e descrito neste item caso a empresa envie as informações na carga Inicial do S-2240, com isso o produto não sofreu alteração continua enviando para todos os casos de afastamentos, mesmo os não obrigatórios.

5) S-2230 - Afastamento Temporário, para o item 13.1 página 203 do MOS, onde menciona "Nos casos em que os feriados não forem computados nas férias, seja por liberalidade ou por força de instrumento coletivo, a informação do período de gozo de férias deve ser prestada sem considerar a desconsideração do feriado.  O gozo do dia relativo ao feriado deve ser considerado como falta justificada e, caso a empresa deseje registrá-la, deve lançar como afastamento com o motivo 16.", também houve questionamento da empresas de softwares junto ao comitê do eSocial, e o mesmo respondeu que irá retirar esse item do MOS, continuará da maneira que é enviado atualmente.
