---
content_hash: 0d0f65b15fe5e1fe4469a6cf637227b7cfba3031ffc145d6a5dd8e05a4a9747f
fetched_at: '2026-06-29T00:10:47.472605+00:00'
page_id: '557349313'
product: rm
source: tdn-rm
title: 9309492 FISCAL01-13542 DT Registro C197 - SPED Fiscal
type: documentation
url: https://tdn.totvs.com/display/LRM/9309492+FISCAL01-13542+DT+Registro+C197+-+SPED+Fiscal
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | SPED Fiscal |
| Ticket: | 9309492 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13542 |

## **02. SITUAÇÃO/REQUISITO**

1. Ao gerar a rotina do SPED Fiscal ocorre mensagem abaixo:  
   *Ocorreram erros ao calcular os registro*  
   *RegistroC197: Registro de apuração do ICMS ST não encontrado: Data: 11/06/2020 00:00:00, UF: PR*  
   *[08:40] at RM.Fis.Sped.GravadorSped`1.Add(T registro)*  
   *at RM.Fis.Sped.FisSpedModule.InsereC100(FisSpedParams spedParams, FisLancamentoFiscalCxt lanc)*  
   Esta situação já foi analisada e solucionada na Issue FISCAL01-5113 - FISCAL01-4711
2. Conforme mapeamento do Registro E210, alguns campos são gerados conforme o Código de Ajustes informado no Lançamento ou Item, valor do ICMS gerados nos Registro C197. Mas não estão sendo gerados.  
   É preciso analisar se esta situação está ocorrendo por conta do erro apresentado no Registro C100. Mesmo apresentado erro o arquivo é gerado.

## **03. SOLUÇÃO**

O problema ocorria porque a parametrização do lançamento não era adequada para geração do registro E200. O registro é gerado somente se encaixar em algum dos seguintes casos:

Os registros são gerados quando, são  Lançamento de Entrada e :

* Caso  = (Tipo Tributacao(**Tributado**) + Tipo Operacao (ST) + Soma Vlr Contabil + RetencaoIcmsSt(Substituto Tributario)) = Pegar Estado Filial
* Caso  = (Tipo Tributacao(**Tributado**) + Tipo Operacao (ST) + Soma Vlr Contabil + RetencaoIcmsSt(Não Se Aplica)) = Pegar Estado Filial
* Caso  = (Tipo Tributacao(**Tributado**) + Tipo Operacao (ST) + Soma Vlr Contabil Desmarcado + RetencaoIcmsSt(Antecipado)) = Pegar Estado Filial
* Caso  = (Tipo Tributacao(**Isento**) + Tipo Operacao (ST) + Soma Vlr Contabil Desmarcado + RetencaoIcmsSt(Antecipado))) = Pegar Estado Filial
* Caso  = (Tipo Tributacao(**Outros**) + Tipo Operacao (ST) +  Soma Vlr Contabil + Operacao Complementar (ICMSST)) = Pegar Estado Filial
* Caso  = (Tipo Tributacao(**Outros**) + Tipo Operacao (ST) +  Soma Vlr Contabil Desmarcado + RetencaoIcmsSt(Antecipado))) = Pegar Estado Filial
