---
article_id: 35930886106263
category: Materiais - Compras (SIGACOM)
content_hash: 415121e66569549d04e00bd9cd8631d9b62bca417267f6a1398fde88ffb491e3
fetched_at: '2026-06-28T22:41:21.903421+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Qual o tratamento
  do parâmetro MV_PCEXCOT na exclusão do Pedido de Compra gerado na Análise da Cotação
  no NFC ?
type: support-article
updated_at: '2026-02-03T12:08:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35930886106263-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Qual-o-tratamento-do-par%C3%A2metro-MV-PCEXCOT-na-exclus%C3%A3o-do-Pedido-de-Compra-gerado-na-An%C3%A1lise-da-Cota%C3%A7%C3%A3o-no-NFC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35930886093335) Tempo aproximado para leitura: **00:08:00 min**  
  
**Dúvida**  
Qual o tratamento do parâmetro MV\_PCEXCOT na exclusão do Pedido de Compra gerado na Análise da Cotação no Novo Fluxo de Compras?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Protheus Release 12.1.2310

**Solução**

* **MV\_PCEXCOT=2**

  Após executar todo o processo de cotação (**SC -> Necessidade de Compra - Inclui Cotação -> Cotações - preenche proposta da cotação manualmente ou via formulário WF->Cotações - Analisa Cotação ->PC**), ao excluir o **PC** gerado pela **Análise de Cotação** o sistema restaura a **SC** utilizada no inicio do processo, deixando-a com status de **SC Pendente** (legenda verde). A cotação realizada até a geração do **PC** excluído não é alterada, ela continuará gravada na tabela **SC8** e aparecerá na tela de **Cotação** do NFC com legenda vermelha (**Finalizada**) apenas para fins de histórico. Com o parâmetro configurado desta forma o tratamento é o mesmo independente de uma cotação ter gerado nos **PCs**. Sendo assim é possível realizar todo o processo de cotação novamente com a **SC** que foi restaurada. Seguem GIFs abaixo com o passo a passo do processo.

  **Parte 1:**  (SC -> Necessidade de Compra - Inclui Cotação -> Cotações - preenche proposta da cotação manualmente -> Inicia a análise da cotação)

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35930886093847)

  **Parte 2:** (Finaliza análise da Cotação gerando pedido de compra -> olha o pc incluído -> valida o conteúdo do parâmetro -> valida legenda da solicitação)

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35930893939863)

  **Parte 3:** (Valida legenda da solicitação -> Exclui pedido -> Valida legenda Cotação -> Valida legenda SC)

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35930886094615)

Quando a exclusão do pedido é realizada com o parâmetro **MV\_PCEXCOT=2,** os registros são atualizados da forma abaixo:

Na tabela SC1 da Solicitação de Compras, os campos C1\_COTACAO, C1\_PEDIDO e C1\_ITEMPED (Número da Cotação, Número e item do Pedido de Compra) são limpos, ficando em branco.

Na tabela SC8 da Cotação, não ocorre nenhuma alteração. A cotação permanece no NFC como Finalizada.

Na tabela SC7 do Pedido de Compra, os registros referente o pedido excluído são marcados como excluídos.

Antes da exclusão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38125509838743)

Depois da exclusão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38125526387735)

* **MV\_PCEXCOT=1**

  Após executar todo o processo de cotação (**SC -> Necessidade de Compra - Inclui Cotação -> Cotações - preenche proposta da cotação manualmente ou via formulário WF->Cotações - Analisa Cotação ->PC**) temos dois tratamentos:

  + **A ANÁLISE GERA APENAS UM PC**: Neste caso se o **PC** for excluído a **Cotação** será reaberta e podem ser alterados os valores na tela de **Cotações no NFC** e ela pode ser reanalisada. Não é realizada nenhuma alteração da **SC** que continua indisponível para utilização;

    **Parte 1:** (SC -> Necessidade de Compra - Inclui Cotação -> Cotações - preenche proposta da cotação manualmente)

    ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35930893940631)

    **Parte 2:** (salva edição da proposta -> analisa cotação -> gera pedido -> verifica legenda pedido cotação e solicitação -> verifica conteúdo do parâmetro)

    ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35930886097303)

    **Parte 3:** (verifica conteúdo do parâmetro ->exclui pedido -> reabre cotação -> solicitação continua em processo de cotação legenda azul)

    ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35930893941015)

Quando a exclusão do pedido é realizada com o parâmetro **MV\_PCEXCOT=1,** os registros são atualizados da forma abaixo:

Na tabela SC1 da Solicitação de Compras, os campos C1\_PEDIDO e C1\_ITEMPED (Número e item do Pedido de Compra) são limpos, ficando em branco.

Na tabela SC8 da Cotação, os campos C8\_NUMPED e C8\_ITEMPED (Número e item do Pedido de Compra) são limpos, ficando em branco.

Na tabela SC7 do Pedido de Compra, os registros referente o pedido excluído são marcados como excluídos.

Antes da exclusão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38125509838743)

Depois da exclusão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38125509839767)

* **A ANÁLISE GERA MAIS DE UM PC**: Neste caso ao excluir um dos **PCs** gerados pela análise de cotação, o sistema restaura a **SC** utilizada no inicio do processo, deixando-a com status **SC Pendente** (legenda verde). A cotação realizada até a geração do PC excluído não é alterada, ela continua gravada na tabela **SC8** e aparece na tela de **Cotações** **do NFC** com legenda vermelha (**Finalizada**), apenas para fins de histórico.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
