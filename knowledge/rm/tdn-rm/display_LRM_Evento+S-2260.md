---
content_hash: 86dbb940ac464160d360c12db15ab42d1e36b6367622e82ffa14cf606d11a05f
fetched_at: '2026-06-29T00:08:56.249046+00:00'
page_id: '351376339'
product: rm
source: tdn-rm
title: Evento S-2260
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-2260
version: 5
---

LeiautesLeiaute 2.5.00

Mapeamento dos campos para o leiaute 2.5.00

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro eSocial** | **Campo eSocial** | **Tabela RM** | **Coluna RM** | **Informações do calculo** |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais   (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| ideVinculo | cpfTrab | PPESSOA | CPF |  |
| ideVinculo | nisTrab |  |  | Caso seja autônomo e FCFO.NIT   estiver preenchido, retorna FCFO.NIT, caso contrário, retorna   FCFO.CIAUTONOMO;          Caso não seja autônomo e codCateg diferente de contribuinte individual   (721, 722, 723, 731, 734, 738, 761, 771) retorna PFUNC.PISPASEP, caso   contrario, retorna PFUNC.CI |
| ideVinculo | matricula | PFUNC | MATRICULAESOCIAL |  |
| infoConvInterm | codConv | PFCONVOCACAO | CODCONVOCACAO |  |
| infoConvInterm | dtInicio | PFCONVOCACAO | DTINIPRESTSERV |  |
| infoConvInterm | dtFim | PFCONVOCACAO | DTFIMPRESTSERV |  |
| infoConvInterm | dtPrevPgto | PFCONVOCACAO | DTPREVPGTO |  |
| jornada | codHorContrat |  |  | "I" + "|" + AHORARIO.CODIGO + "|" +   AINDHOR.INDINICIOHOR |
| jornada | dscJornada | PFCONVOCACAO | DESCRICAOJORNADA |  |
| localTrab | indLocal | PFCONVOCACAO | INDLOCALPRESTACTRAB |  |
| localTrabInterm | tpLograd |  |  | Código recuperado através do campo PFCONVOCACAO.CODTIPORUA |
| localTrabInterm | dscLograd | PFCONVOCACAO | RUA |  |
| localTrabInterm | nrLograd | PFCONVOCACAO | NUMERO |  |
| localTrabInterm | complem | PFCONVOCACAO | COMPLEMENTO |  |
| localTrabInterm | bairro | PFCONVOCACAO | BAIRRO |  |
| localTrabInterm | cep | PFCONVOCACAO | CEP |  |
| localTrabInterm | codMunic |  |  | Código recuperado através dos campos PFCONVOCACAO.ESTADO e   PFCONVOCACAO.CODMUNICIPIO |
| localTrabInterm | uf | PFCONVOCACAO | ESTADO |  |
