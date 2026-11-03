---
article_id: 360016352771
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 88d0a1fd4188fe3146adbe1d16e35816dd1751e1688b4ff9f24c11c9fdb05b00
fetched_at: '2026-06-28T22:42:05.348391+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  como gerar o registro F100 através da rotina Demais Documentos (FISA048)
type: support-article
updated_at: '2023-11-24T17:18:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016352771-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-como-gerar-o-registro-F100-atrav%C3%A9s-da-rotina-Demais-Documentos-FISA048
---

**Dúvida**Como realizar o lançamento do Registro F100 pela rotina Demais Documentos (FISA048)?  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
1. Cadastre uma operação de **Receita** ou de **Aquisição** por meio da rotina **Demais Docs. PIS COF.** (FISA048);

2. Certifique-se de que os campos abaixo foram devidamente preenchidos:  
Tipo Regime (**CF8\_TPREG**), Ind.Oper (**CF8\_INDOPE**), Dt.Operação (**CF8\_DTOPER**), Vl.Operação (**CF8\_VLOPER**), Sit.Trib.PIS (**CF8\_CSTPIS**), Base PIS (**CF8\_BASPIS**), Aliquota PIS (**CF8\_ALQPIS**), Valor PIS (**CF8\_VALPIS**), Sit.Trib.COF (**CF8\_CSTCOF**), Base Cofins (**CF8\_BASCOF**), Aliq.COFINS (**CF8\_ALQCOF**) e Valor COFINS (**CF8\_VALCOF**).  
  
3. Verifique se a Tabela **CF8** foi alimentada com as informações lançadas;  
  
4. Realize o processamento da **Apuração** e verifique se a Tabela **CL2** foi gerada com os valores;  
  
5. Para que o valor da Receita seja considerada no **Registro 0111**, preencha o campo **CF8\_RECBRU** com a opção **1 - SIM** e após o processamento da **Apuração**, consulte a Tabela **CKU** e verifique se os valores foram gravados;  
  
6. Gere o arquivo txt do **EFD Contribuições**.

![F100_FISA048.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360012095971)

Observação: É possível também gerar o registro F100 por meio Ponto de Entrada **SPDPIS09.**

<https://tdn.totvs.com.br/pages/releaseview.action?pageId=706917378>  
  
Para contabilização on-line, segue documentação da rotina FISA048: [<https://tdn.totvs.com/pages/viewpage.action?pageId=715150877>]  
   
Caso queira customizar a inclusão de vários documentos automaticamente, segue Boletim da Rotina Automática em MVC:  
[<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051031994-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Rotina-Autom%C3%A1tica-em-MVC>]
