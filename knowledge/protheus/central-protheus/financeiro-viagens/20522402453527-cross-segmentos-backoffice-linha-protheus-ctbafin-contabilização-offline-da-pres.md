---
article_id: 20522402453527
category: Financeiro - Viagens
content_hash: 5fd28c2dcef357f5baf9250558969644f5a83ba207c0c4d02abc92cc2dfe1ba9
fetched_at: '2026-06-28T22:38:21.364020+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - CTBAFIN- Contabilização Offline
  da Prestação de Contas pelos LP 8B3, 8B4, 8B5, 8B6
type: support-article
updated_at: '2026-04-30T18:31:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20522402453527-Cross-Segmentos-Backoffice-Linha-Protheus-CTBAFIN-Contabiliza%C3%A7%C3%A3o-Offline-da-Presta%C3%A7%C3%A3o-de-Contas-pelos-LP-8B3-8B4-8B5-8B6
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20522402433431) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Como funciona a Contabilização Offline da Prestação de Contas pelos LP **8B3, 8B4, 8B5, 8B6**?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

Na **Contabilização Off-Line (CTBAFIN)** será considerado a data de emissão da **Prestação de Contas** **(FLF\_EMISSA)** para filtrar as prestações a serem contabilizadas, caso existam **títulos a pagar**/**receber** vinculados a uma prestação, estes serão considerados para contabilizar mesmo que não esteja no range de data informado na contabilização.

**Exemplo:**  
**Prestação de contas** inserida em 12/01/2024 **(FLF\_EMISSA)**

**Título a receber** gerado em 12/02/2024 **(E1\_EMIS1)**

**Contabilização Off-Line**

Para contabilizar a **prestação de contas** deverá ser informado um range de datas na rotina de **Contabilização Off-Line** que considere a **prestação de contas 12/01/2024** e não o título financeiro gerado.

**Observação:**  
Os **LP´s 8B3 e 8B5** são para contabilizar a **prestação de contas**, por este motivo a contabilização será baseada nas tabelas **FLE/FLF**e não nas tabelas **SE1/SE2**.  
  
Como nem todas as **prestações de contas** possuem geração de títulos, haveria um problema se a contabilização fosse baseada nas tabelas **SE1/SE2**.  
  
Já a contabilização da inclusão do título, sendo feita através das **LP'S 500** (**contas a receber**) e **510** (**contas a pagar**), a rotina **CTBAFIN** descarta propositalmente os títulos gerados pela **FINA677** (**Prestação** **de Contas**) da query dessas LP's, para não ocorrerem duplicidades de valores na contabilidade (já que as **LP's 8B3/8B5/500/510** podem estar todas ativas no ambiente).  
  
Caso a necessidade seja contabilizar pela data de emissão do título (**E2\_EMISSAO/E1\_EMISSAO**), a sugestão é utilizar as **LP's 500/510** e utilizar os pontos de entrada **F370E2F** e **F370E1F**. Eles possibilitam manipular as querys de títulos no **CTBAFIN**, assim podendo retirar o filtro que descarta quando o campo **E2\_ORIGEM** for "**FINA677**".  
  
**Importante**  
**Segue documentação dos pontos de entrada:**  
[F370E1F - Filtrar registros do SE1 da rotina CTBAFIN](https://tdn.totvs.com.br/display/public/PROT/F370E1F+-+Ponto+de+Entrada+para+filtrar+registros+do+SE1+da+rotina+CTBAFIN)  
[F370E2F - Filtrar registros do SE2 da rotina CTBAFIN](https://tdn.totvs.com/pages/releaseview.action?pageId=635744423)

**Exemplo de utilização de ponto de entrada**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25842526781975)

**Saiba mais**

[Viagens - LP´S](https://tdn.totvs.com/display/PROT/Viagens+-+LPs)

[Contabilização Offline - CTBAFIN - Financeiro - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=497932563)

[Viagens - Financeiro - P12](https://tdn.totvs.com/display/public/PROT/Viagens+-+Financeiro+-+P12)
