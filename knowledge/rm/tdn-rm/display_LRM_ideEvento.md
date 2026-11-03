---
content_hash: b4f2b1be2537b6ff25d07f3ab3d94029ff8ed4fd2c6f4deed843c2b0167bc21c
fetched_at: '2026-06-29T00:11:26.410510+00:00'
page_id: '716359531'
product: rm
source: tdn-rm
title: ideEvento
type: documentation
url: https://tdn.totvs.com/display/LRM/ideEvento
version: 4
---

**Informações de Identificação do Evento.**

| Registro/Campo | Registro Pai | Ocorr | Tam | Descrição | Origem RM |
| --- | --- | --- | --- | --- | --- |
| ideEvento | evtServTom evtServPrest evtAssocDespRec evtAssocDespRep evtComProd evtCPRB  evtPgtosDivs  evtRetPF  evtRetPJ | 1-1 |  | Informações de Identificação do Evento |  |
| indRetif | ideEvento | 1-1 | 1 | Informe [1] para arquivo original ou [2] para arquivo de retificação. | Parâmetro de geração da rotina |
| nrRecibo | ideEvento | 0-1 | 40 | Preencher com o número do recibo do arquivo a ser retificado.  Validação: O preenchimento é obrigatório se {indRetif} = [2]. Deve ser um recibo de entrega válido, correspondente ao arquivo que está sendo retificado. |  |
| perApur | ideEvento | 1-1 | 7 | Informar o ano/mês (formato AAAA-MM) de referência das informações.  Validação: Deve ser um ano/mês, igual ou posterior ao início de vigência da EFD-Reinf. | Parâmetro de geração da rotina |
| tpAmb | ideEvento | 1-1 | 1 | Identificação do ambiente:  Valores Válidos: 1 - Produção; 2 - Produção restrita - dados reais; 3 - Produção restrita - dados fictícios. | Parâmetro de geração da rotina |
| procEmi | ideEvento | 1-1 | 1 | Processo de emissão do evento:  Valores Válidos: 1 - Aplicativo do contribuinte; 2 - Aplicativo governamental. | Texto Fixo "1" gerado pelo sistema. |
| verProc | ideEvento | 1-1 | 20 | Versão do processo de emissão do evento.  Informar a versão do aplicativo emissor do evento. | Texto Fixo gerado pelo sistema, com a versão da Biblioteca RM. |
