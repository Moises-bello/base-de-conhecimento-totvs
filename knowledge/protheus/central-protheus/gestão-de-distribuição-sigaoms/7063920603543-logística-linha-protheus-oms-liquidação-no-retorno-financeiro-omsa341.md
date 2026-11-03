---
article_id: 7063920603543
category: Gestão de Distribuição (SIGAOMS)
content_hash: 524bb3f2e5a421788e560603abc8a2b676de78f95f7721bffe9945de9de99c0d
fetched_at: '2026-06-28T22:45:49.879720+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Liquidação no Retorno Financeiro -OMSA341
type: support-article
updated_at: '2022-07-08T20:14:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7063920603543-Log%C3%ADstica-Linha-Protheus-OMS-Liquida%C3%A7%C3%A3o-no-Retorno-Financeiro-OMSA341
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:24 min****Dúvida**Como funciona a **Liquidação** do **tipo CH - Cheque** na rotina de **Retorno Financeiro - OMSA341**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Na rotina de **Retorno Financeiro - OMSA341**, temos a opção de **Liquidação**, sendo que a rotina poderá ter comportamentos diferentes conforme o preenchimento do parâmetro **MV\_GRSEFLQ.** Quando o parâmetro estiver **ativo é obrigatório informar os dados bancários.**  
  
Para solucionar essa dúvida, na **Aba Títulos**, **assinale o titulo desejado**, ao clicar em **Salvar** a **liquidação** serão analisadas as seguintes opções:

1-Se o parâmetro **MV\_GRSEFLQ** estiver como **.T.** será realizada a **liquidação** pela aba **Baixa**, **informando os dados bancários**. Caso seja de **Cheques**, informe o **Valor Recebido** e clique no botão **Cheques**, informe os dados do cheque. Esse tratamento pode ser utilizado para **Cheques à vista.**

**![omsa341__1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7065865796247/omsa341__1.png)**

Essa movimentação irá gerar dados nas seguintes tabelas:   
 **SE1 - Contas a Receber  
SEF - Cheques  
SE5 - Movimentação Bancaria  
FK1 - Baixas a Receber**2-Se o parâmetro **MV\_GRSEFLQ**estiver como **.F.**, a **liquidação** pode ser realizada pela aba **Liquidação.** Esse tratamento pode ser utilizado para **Cheques à prazo.**

**![omsa341_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7065678626071/omsa341_2.png)**

Caso não seja liquidação e os dados bancários estiverem vazios será exibida a mensagem de que o banco é obrigatório para o motivo **Normal.  
  
Importante**Quando o parâmetro **MV\_GRSEFLQ** está habilitado e a liquidação é do tipo CH - Cheque. Nas liquidações é obrigatório informar os dados bancários quando existir a geração do registro do cheque na tabela de **Cheques - SEF**. Nesse caso será necessário realizar a liquidação, utilizando a **aba Baixa**, selecionar o **motivo Liquidação** e **informar os dados bancários**.  
  
**Saiba mais**  
Maiores informações, poderão ser acessados nos *links*:   
[Logística - Linha Protheus - OMS - Quais funcionalidades compreende a rotina de Retorno Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027388152-Log%C3%ADstica-Linha-Protheus-OMS-Quais-funcionalidades-compreende-a-rotina-de-Retorno-Financeiro)  
[Logística - Linha Protheus - OMS - Cancelamento da baixa de títulos pelo OMSA341](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408150301847-Log%C3%ADstica-Linha-Protheus-OMS-Cancelamento-da-baixa-de-t%C3%ADtulos-pelo-OMSA341)  
[Logística - Linha Protheus - OMS - Pontos de Entrada disponíveis na rotina Retorno Financeiro - OMSA341](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003387081-Log%C3%ADstica-Linha-Protheus-OMS-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina-Retorno-Financeiro-OMSA341)  
[MP - SIGAFIN - FINA460 - Habilitar cheque na liquidação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016807911-MP-SIGAFIN-FINA460-Habilitar-cheque-na-liquida%C3%A7%C3%A3o-)  
[Inconsistência na rotina de retorno financeiro - OMSA341](https://tdn.totvs.com/pages/releaseview.action?pageId=657541949)
