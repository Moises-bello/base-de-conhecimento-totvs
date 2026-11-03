---
article_id: 18155036570391
category: Financeiro - Reinf
content_hash: f782b4bbec46f79dda98b8d4da7e41ce41b2564e7d2aecc2b1327a75ea592183
fetched_at: '2026-06-28T22:37:51.710975+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - Extrator Fiscal
  não gera os layout T154 e T158 na tabela TAFST2
type: support-article
updated_at: '2025-01-22T13:46:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18155036570391-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-Extrator-Fiscal-n%C3%A3o-gera-os-layout-T154-e-T158-na-tabela-TAFST2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18155006894231) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Extrator Fiscal não gera os layout T154 e T158 na tabela TAFST2?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.33

**Solução**

1. Para títulos oriundos das rotinas [**Documento de Entrada (MATA103)**](https://tdn.totvs.com/display/PROT/PCOM12065+-+EFD-Reinf+2.1.1+-+Documento+de+Entrada), verifique se foi preenchido a **natureza de rendimento** e gravado a tabela **FKW**.  
  
2. Para localizar o título a pagar do **Documento de Entrada** na tabela **FKW** (**Natureza Rendimento x** **Impostos**), é através do "**ID do título**" (**FKW\_IDDOC**).  
  
3. Para obter o "**ID do título**", consulte a tabela **FK7** (Tabela auxiliar onde são armazenadas as chaves de amarração entre as tabelas **SE1** e **SE2**);  
  
**Exemplo:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18154698368407)  
  
**Obs.** Se não gravar registro na **tabela FKW** e ou gravar valores incorreto, valide as informações com a equipe **Protheus Compras GCP /GCT**.  
  
4. Para titulo de origem do módulo **Financeiro.**  
5. A premissa para o título ser considerado nos layout é o vinculo com a **Natureza de Rendimento** (tabela 01 da **EFD-Reinf)**.  
  
6. Na rotina do **Contas a Pagar** (**FINA050**) há a opção **Complemento do Título**,   
que possibilita esse vínculo para títulos avulsos, preenchendo o campo "**Natureza de Rendimento**" (campo **FKF\_NATREN**), localizado na aba **REINF**.

**Importante:**  
O vínculo do "**Título x Natureza de Rendimento**" deve ser pelo **título principal** (exemplo: tipo "**BOL**") e não pelo **título do tributo** (exemplo: tipo "**TX**");  
As **naturezas de rendimento** podem ser cadastradas/consultadas através da rotina **[FINA028](https://tdn.totvs.com/pages/releaseview.action?pageId=717715456)** (tabela **FKX**)  
  
7. Após a validação acima, realize a baixa do título principal com um motivo de baixa que **movimenta banco** exemplo o Motivo de Baixa "**Debito CC**";  
**Obs.** O layout **T158** é gerado após a baixa do título principal (exemplo: título do tipo **NF, DP, BOL**, etc.). O **Extrator Fiscal** irá considerar como fato gerador do **PIS**, **COFINS**e **CSLL** o pagamento do título principal através do campo **FK2\_DATA**.  
  
8. No **Extrator Fiscal** processe o período que foi realizado a baixa do título principal para o **layout T158**.  
Para o **IRF** se estiver na **emissão** e ou **contabilização** filtrar o **período do título**.   
  
**Saiba mais**  
Os fatos geradores de cada impostos  
[**FAQ - 0016 - Quais os fatos geradores serão considerados no extrator financeiro?**](https://tdn.totvs.com/pages/viewpage.action?pageId=737543501)  
  
9. Valide se o ambiente está com o fonte **FINA989** na data igual ou superior **06/09/2023**e o**FINXREINF 17/08/2023** caso não esteja realizar aplicação do patch abaixo.  
  
**12.1.2210**:<https://suporte.totvs.com/portal/p/10098/download?e=1119309> ;  
**12.1.2310**:<https://suporte.totvs.com/portal/p/10098/download?e=1119311> ;  
**12.1.33**:<https://suporte.totvs.com/portal/p/10098/download?e=1119310> ;  
  
10. Valida se os campos do título principal**FKF\_REINF** e o **FK2\_REINF** ambos estão com **o conteúdo = 2**-**Não**, para assim realizar o processamento no **E****xtrator Fiscal**.

* **FKF\_REINF**
  + Identifica se o título a pagar/receber já foi integrado com o TAF, sendo preenchido com 1=Sim e 2=Não;
* **FK2\_REINF**
  + Identifica se a baixa do título a pagar já foi integrado com o TAF, sendo preenchido com 1=Sim e 2=Não;

11. Valide os compartilhamentos da tabelas, [**SE1, SE2, SE5,**](https://tdn.totvs.com/pages/releaseview.action?pageId=307830478) [**FKF, FKG, FKW, FKY, FI7 e FI8**](https://tdn.totvs.com/pages/releaseview.action?pageId=307830478)  
  
12. Valide se ao processar o **Extrator Fiscal** com a opção em **.TXT** ira gerar os **layouts T154 e T158**?   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18155077146135)  
  
13. Ao rodar o **Extrator Fiscal** com a opção **banco de dados** e processar a integração no **módulo do TAF** valida se foi integrado com sucesso os **layouts T154 e T158**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18155249806871)

[REINF Bloco R-4020 Extrator Fiscal BD e TAF](https://www.youtube.com/watch?v=j17JQW7kHiM)
