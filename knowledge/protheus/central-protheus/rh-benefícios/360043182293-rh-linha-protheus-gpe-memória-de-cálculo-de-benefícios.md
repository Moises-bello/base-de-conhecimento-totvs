---
article_id: 360043182293
category: RH - Benefícios
content_hash: da580746b91670a438db92e322adaa5543ad76c13065735b910d5e3c5238389f
fetched_at: '2026-06-28T22:44:04.691789+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Memória de Cálculo de Benefícios
type: support-article
updated_at: '2025-09-12T13:47:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043182293-RH-Linha-Protheus-GPE-Mem%C3%B3ria-de-C%C3%A1lculo-de-Benef%C3%ADcios
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23665342008599) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Como Consultar ou Imprimir a Memória de Cálculo dos Benefícios?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**

Para consultar e gerar o relatório de memória de cálculo realize os seguintes passos:  
  
**1.** Acessar em **Atualizações> Definições de Cálculo> Mnemônicos**.   
Altere o Mnemônico **P\_LMEMCALC** para **.T.** para que possa ser recriadas as fórmulas com o Log Ativado:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079566453)

**2.** Execute o Cálculo do Benefício normalmente.

**3.** Após o cálculo, o Log estará disponível para consulta na rotina de **Consulta de Cálculo por Funcionário** (**GPEA090 - SRC**).  Selecione o funcionário desejado no *browser* da rotina e clique na opção **Outras Ações/Consultar Memória de Cálculo**:![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078408934)

Será apresentada uma tela listando os *logs* gravados para o funcionário selecionado;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058092833)

**4.** Para impressão do **Relatório de Memória de Cálculo,** acesse a rotina **Consulta de Cálculo por Funcionário** (GPEA090 - SRC) no menu **Outras Ações**.   
Basta configurar os parâmetros para selecionar o cálculo que deseja imprimir:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078409334)

**Importante:** Toda vez que o mnemônico for alterado P\_LMEMCALC as **fórmulas serão recriadas,** portanto o mnemônico deve ser desativado após sua utilização para conferência do cálculo, pois estando habilitado durante o processamento normal das rotinas que geram memória de cálculo, acarretará a perda de performance das mesmas.

**Saiba Mais**  
[Documento Técnico - Memória de Cálculo](https://tdn.totvs.com/pages/releaseview.action?pageId=330831446)  
[Melhorias Memória de Cálculo](https://tdn.totvs.com/pages/viewpage.action?pageId=791840585)  
[RH - Linha Protheus - GPE - Como consultar o histórico de cálculo de benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042584274-RH-Linha-Protheus-GPE-Como-consultar-o-hist%C3%B3rico-de-c%C3%A1lculo-de-benef%C3%ADcios?source=search)  
[RH - Linha Protheus - GPE - Relatório de Conferência para Cálculo de Benefícios Automáticos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052106234-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-Confer%C3%AAncia-para-C%C3%A1lculo-de-Benef%C3%ADcios-Autom%C3%A1ticos?source=search)
