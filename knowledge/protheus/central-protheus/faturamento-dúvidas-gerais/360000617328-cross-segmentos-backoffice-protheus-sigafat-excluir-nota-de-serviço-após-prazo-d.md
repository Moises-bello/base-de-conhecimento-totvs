---
article_id: 360000617328
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 269e78215455122464d40e0bc5476804a9b8edf015cc2480a9b1da73ecc4e26a
fetched_at: '2026-06-28T22:38:29.804004+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Excluir Nota de Serviço após
  prazo do município
type: support-article
updated_at: '2025-04-29T19:18:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000617328-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Excluir-Nota-de-Servi%C3%A7o-ap%C3%B3s-prazo-do-munic%C3%ADpio
---

**Dúvida**Como **excluir NFS - Nota Fiscal de Serviço** na rotina **MATA521** após ultrapassar o prazo do município?

É exibida a mensagem: **O prazo para exclusão de NF de serviço para o município de** Xxxxxx - XX **é de até o último dia do mês subsequente da sua emissão.** Data Limite: XX/XX/XX

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT – A partir da versão 11.80  
  
**Solução**A configuração para permissão de exclusão é realizada com base nos parâmetros:

**MV\_ESTADO** - Estado do Emitente

**MV\_TIPOPRZ** - Tipo de prazo para exclusão das notas fiscais de serviço, Sendo:

* 1=Até dia XX do mês subsequente;
* 2=XX dias após emissão

**MV\_EXCNFS** - Limite de dias para exclusão

**MV\_VLDSBT** - Validação de Nota substitua

**Para o erro ocorrer, abaixo é como precisar estar para uma das três ocorrências desse help acontecer:**  
  
1 - O campo "Tipo da nota (F3\_TIPO)" ao faturar, estiver como "S" ao mesmo tempo do campo "Estoque? (D2\_ESTOQUE)" da NF ser "N", o campo "Iss (D2\_CODISS)" preenchido e a TES usada tem que ter "ICMS ST (F4\_ISSST) = "1".  
  
2 - O "município (M0\_CODMUN)" informado na filial deve ser válido   
  
3 - O município deve ter legislação especial (ou seja, ser algum estado do item 4 a seguir)  
  
4 - Não ter as circunstâncias a seguir:  
Ter o MV\_ESTADO = BA e "município da filial (M0\_CODMUN)" com código do município de "Salvador"  
Ter o MV\_ESTADO = PR e "município da filial (M0\_CODMUN)" com código do município de "Londrina"  
Ter o MV\_ESTADO = SE e "município da filial (M0\_CODMUN)" com código do município de "Aracaju"  
Ter o MV\_ESTADO = RO e "município da filial (M0\_CODMUN)" com código do município de "Porto Velho"  
Ter o MV\_ESTADO = AL e "município da filial (M0\_CODMUN)" com código do município de "Rio Largo"  
Ter o MV\_ESTADO = RJ e "município da filial (M0\_CODMUN)" com código do município de "Rio de Janeiro"  
  
5 - O processo não ser/estar usando ExecAuto.

Juntando as ocorrências acima, ou seja, elas sendo verdade, o erro ocorre, para não ocorrer, valide se as etapas anteriores estão corretas.

**Saiba mais:**

**[FAT0150 - Exclusão Notas Serviço (MATA521A) - Processo Administrativo ISS](https://tdn.totvs.com/x/TUT2Dw)**
