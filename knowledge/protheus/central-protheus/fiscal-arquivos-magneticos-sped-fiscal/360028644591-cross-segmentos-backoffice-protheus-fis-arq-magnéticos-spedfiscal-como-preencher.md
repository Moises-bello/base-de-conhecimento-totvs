---
article_id: 360028644591
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 4a3e66d703e4e104d593b8bf0e98adf41e51945630eac343358fec7e4046ec71
fetched_at: '2026-06-28T22:42:02.577108+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPEDFISCAL
  Como preencher o campo 03 DESCR_COMPL_AJ (Descrição complementar do ajuste do documento)
  no Registro C197
type: support-article
updated_at: '2025-02-11T22:04:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028644591-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPEDFISCAL-Como-preencher-o-campo-03-DESCR-COMPL-AJ-Descri%C3%A7%C3%A3o-complementar-do-ajuste-do-documento-no-Registro-C197
---

**Dúvida**

Como preencher o campo **03 - DESCR\_COMPL\_AJ** do **Registro C197** do **Sped Fiscal?**  
 **Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Para alimentar o campo **03 - DESCR\_COMPL\_AJ - Descrição complementar do ajuste do documento** no **Registro C197** do **SPED FISCAL**, o sistema busca a informação da tabela **CC6** (Item do **Pedido de Venda**)

**cCodLanc := (cAliasCC6)->CC6\_CODLAN**  
**cDescAj  := MSMM((cAliasCC6)->CC6\_DESCR2)**  
**cDescAj  := IIF(***Empty***(cDescAj),(cAliasCC6)->CC6\_DESCR,cDescAj)**  
  
Conforme trecho acima, o fonte verifica se há conteúdo no campo **CC6\_DESCR2,** caso não haja, busca a informação do campo **CC6\_DESCR**.  
O campo **CC6\_DESCR2**é preenchido por um código que busca as informações da tabela **SYP**.  
  
Exemplo:  
  
**CC6**:  
![](https://ci5.googleusercontent.com/proxy/kJ26vKaqcoOP8fM5w75x3Rv9i834bSaqopZA0o_3VTiAHN6fcHaT5JyyHPB5y-qJ3VQ5T_7MIdzhkTgU4FD7O89htEDrhdMutkfk1aG6ogCIzQC2kUz4-fX744pdDYPTPKbXHk22isTbnPIo38mSn2ePmrKpz10Lg4rZ=s0-d-e1-ft#https://totvssuporte.zendesk.com/attachments/token/Nv3PF8oltQzB0ohAGbzdUWPH5/?name=inline-1211432096.png)  
  
**SYP**:  
![](https://ci4.googleusercontent.com/proxy/4fW0ZNtPfffYfA-padzGeJErVuH0coCnTJgXiCAULx0-3TDNVaXS4wdZCDOWfBdFqpPHiPLd5-ltAXSQ06P0do79unJpy-eHViGmRuVSr0wGKo-YXTjBlPNSlgLrjQmCMqjWz1k1yCDpzPLlokZPliOKu7PgWaFvcQ=s0-d-e1-ft#https://totvssuporte.zendesk.com/attachments/token/w9iRCgZ8ScKlwvocrkXl6o97S/?name=inline484173286.png)  
  
**SPED FISCAL**:  
|C100|0|1|SA2M SP 01 02    1|55|00|001|1457||15052019|15052019|500,00|2|0|0|500,00|9|0|0|0|500,00|90,00|0|0|0|0|0|0|0|  
|C170|1|FANTA|FANTA LARANJA|100,00000|UN|500,00|0|1|0|1101||500,00|18,00|90,00|0|0|0||||500,00|0|0||0|0|0|0|0||0|0|0|0|0||0|  
|C190|0|1101|18,00|500,00|500,00|90,00|0|0|0|0|000004|  
|C195|000004|C197|  
**|C197|MG70000001|Exportação de produtos nacionais - sem saída do território brasileiro - venda para empresa sediada no exterior - atividades de pesquisa ou lavra de jazidas de petróleo e de gás natural - Art. 19 Inciso I do Decreto 7.212/2010|FANTA|500,00|18,00|90,00|0|**  
  
  
Verifique as informações nas suas tabelas e faça o ajuste conforme a necessidade; caso não seja necessário buscar as informações da tabela **SYP**, delete os registros da tabela ou o código do campo **CC6\_DESCR2** na tabela **CC6**.
