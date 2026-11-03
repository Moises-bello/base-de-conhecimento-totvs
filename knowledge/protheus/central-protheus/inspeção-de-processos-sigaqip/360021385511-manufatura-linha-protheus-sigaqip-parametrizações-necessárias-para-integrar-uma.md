---
article_id: 360021385511
category: Inspeção de Processos (SIGAQIP)
content_hash: 7957d10f04d438468aac73b11b04693a576dd01d0245c721f4b4afab17f379ca
fetched_at: '2026-06-28T22:42:25.902116+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Parametrizações necessárias para integrar
  uma OP ou apontamento
type: support-article
updated_at: '2026-06-12T11:27:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021385511-Manufatura-Linha-Protheus-SIGAQIP-Parametriza%C3%A7%C3%B5es-necess%C3%A1rias-para-integrar-uma-OP-ou-apontamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17144313142807)** Tempo aproximado para leitura: **00:02:23 min**  
  
**Dúvida**  
Quais são as parametrizações necessárias para uma **OP - Ordem de Produção** ou **apontamento de produção** integrarem com o módulo **SIGAQIP - Inspeção de Processos**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Todas as versões  
  
**Solução**  
Para que a **OP** ou **apontamento** sejam enviados para inspeção no **SIGAQIP**, realize os seguintes passos:  
  
1. Configure o parâmetro **MV\_QIPMAT - Indica se o módulo de Insp.de Processos está integrado com materiais** como **S - Sim**;  
  
2. Configure o parâmetro **MV\_QINSPEC - Indica, onde será realizada a Inspeção do Material quando houver integração QIP x PCP**de acordo com a necessidade, onde:

* **1 - Ordem de Produção**: ao incluir a **OP**, já é gerado o registro para inspeção na rotina **QIPA215 - Resultados**.
* **2 - Apontamento da Produção**: o registro de inspeção é gerado após o apontamento da **OP** por uma das rotinas:
  1. **MATA680 - Produção PCP Mod 1**
  2. **MATA681 - Produção PCP Mod 2**
  3. **MATA250 - Produção Simples.**

3. Na rotina **QIPA010 - Especificação de produto**, incluir uma especificação para o produto em questão.  
  
**Importante**

* Quando integrado via apontamento, o registro à ser inspecionado é gerado somente após apontamento da última operação ou encerramento da Ordem de Produção quando realizado por meio das rotinas **MATA680** e **MATA681**. Para mais detalhes consulte o artigo [Manufatura - Linha Protheus - SIGAPCP - Como validar quando é a ultima operação no apontamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027348312-Manufatura-Linha-Protheus-SIGAPCP-Como-validar-quando-%C3%A9-a-ultima-opera%C3%A7%C3%A3o-no-apontamento-)
* Inspeções a inspecionar ou certificadas:
  1. Quando o parâmetro **MV\_QINSPEC** estiver igual à 1, indicando integração por meio da OP: são geradas a inspecionar todas as inspeções, com exceção das configuradas para certificação automática ou Skip-Lote. Para mais detalhes consulte o artigo [Manufatura - Linha Protheus - SIGAQIP - Skip-lote](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049726394-Manufatura-Linha-Protheus-SIGAQIP-Skip-lote)
  2. Quando o parâmetro **MV\_QINSPEC** estiver igual à 2, indicando integração por meio do apontamento: somente apontamentos de produção destinados ao armazém **MV\_CQ - Local(Almoxarifado) Controle de Qualidade** gerarão inspeções a inspecionar na rotina **Resultados - QIPA215**. Ou seja, os apontamentos que forem destinados para outros armazéns gerarão inspeções certificadas. O parâmetro **MV\_PRAPONT - Configura prioridade no Apontamento de Produção: " 1-Tipo de Movimentação / 2-Cadastro de Produto** pode ser utilizado para definir quando o apontamento de produção será destinado para ao armazém **MV\_CQ**, consequentemente, gerando inspeções a inspecionar. Para saber mais, consulte as documentações [Manufatura - Linha Protheus - SIGAPCP - Parâmetro MV\_PRAPONT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046693993-Manufatura-Linha-Protheus-SIGAPCP-Par%C3%A2metro-MV-PRAPONT) e [MV\_PRAPONT - Prioridade no Apontamento de Produção](https://tdn.totvs.com/pages/releaseview.action?pageId=39682708).
* O apontamento realizado por meio da rotina **MATA250** gera inspeção somente quando o conteúdo do parâmetro **MV\_QIPOPEP - Define a prioridade dos dados em relação à operação o entre os ambientes QIP e PCP** for igual à **3** e quando a Especificação de Produto é simplificada tendo **somente Ensaios, sem Roteiro e sem Operação**. Para mais informações referente a utilização do parâmetro **MV\_QIPOPEP**, consulte a documentação [MV\_QIPOPEP - Informações Complementares sobre o uso do parâmetro](https://tdn.totvs.com/pages/releaseview.action?pageId=766936169).

**Observação**  
Para validar a integração entre os módulos **SIGAQIP** e **SIGAEST - Estoque** verifique o artigo: [Manufatura - Linha Protheus - SIGAQIP - Habilitar integração com SIGAEST](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15791811821591-Manufatura-Linha-Protheus-SIGAQIP-Habilitar-integra%C3%A7%C3%A3o-com-SIGAEST)
