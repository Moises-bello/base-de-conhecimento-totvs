---
article_id: 38574207128087
category: Financeiro - Compensação entre Carteiras
content_hash: 27f3397314336a935c997cfc770cd0a6d11fb9738f67a9c9f11013d82c2c6040
fetched_at: '2026-06-28T22:37:26.983962+00:00'
product: protheus
section_id: 35058659965079
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - É possível realizar a compensação
  entre um título a receber e um título a pagar
type: support-article
updated_at: '2026-02-27T11:45:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38574207128087-Cross-Segmentos-Backoffice-Linha-Protheus-%C3%89-poss%C3%ADvel-realizar-a-compensa%C3%A7%C3%A3o-entre-um-t%C3%ADtulo-a-receber-e-um-t%C3%ADtulo-a-pagar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38574207106967) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
É possível realizar a compensação entre um título a receber e um título a pagar?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FINA450 - Todas as versões.  
  
**Solução**  
A rotina de **Compensação Entre Carteiras (FINA450)** permite a execução da compensação de títulos a pagar com títulos a receber, efetuando o encontro de contas entre fornecedor e cliente (quando a mesma entidade possui ambos os papéis).

O processo pode ser realizado de duas formas:

* **Manual:** Procedimento efetuado via rotina FINA450 com interação do usuário nas telas de marcação e parâmetros.
* **Automática:** Realizada via rotina automática (**MsExecAuto**), geralmente utilizada em customizações para que o processo ocorra sem a necessidade de interface com o usuário.

  [FINA450 - Execauto](https://tdn.totvs.com/pages/viewpage.action?pageId=516194467)

Os títulos considerados no processo são:

* **Títulos de Débito:** Ex: NF (Nota Fiscal), BOL (Boleto), etc.
* **Títulos de Crédito:** Ex: PA (Pagamento Antecipado), RA (Recebimento Antecipado) e títulos de devolução (NDF e NCC).

**Informações Técnicas Importantes:**

* A rotina utiliza uma numeração sequencial baseada no parâmetro `MV_NUMCOMP`.
* O controle é realizado pelos campos `ID_ENTREE` (tabelas **SE1**, **SE2** e **SE5**) e `IDPROC` (tabelas **FK1** e **FK2**).
* A cada operação, o sistema valida o campo `FK2_IDPROC`. Se houver duplicidade, o Protheus busca o maior número existente e segue a nova sequência para garantir a integridade dos processos.
* O parâmetro `MV_NUMCOMP` **não** deve ser configurado como exclusivo, pois o controle é sequencial e independente da filial.

**Passos**

1. Acesse o módulo **Financeiro (SIGAFIN)** e vá em **Atualizações > Contas a Pagar > Compensação entre Carteiras (FINA450)**;
2. Certifique-se de possuir um título a pagar e um título a receber (débito ou crédito) disponíveis para compensação;
3. Clique em +Compensar
4. Na tela de parametrização que será exibida, preencha as informações de filtro e defina o tipo de título, indicando se será de débito ou crédito, conforme a necessidade. Em seguida, clique em **OK**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38574207107735)

5. Serão apresentados os registros disponíveis para seleção. Após selecionar os títulos desejados, clique em **Confirmar** para realizar a compensação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38574207107991)

6. Após a compensação, os títulos serão baixados automaticamente em suas respectivas rotinas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38574230071703)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38574207109655)

**Saiba mais**

[Compensação entre carteiras - FINA450](https://tdn.totvs.com/pages/viewpage.action?pageId=516194467)

[Financeiro - Compensação entre Carteiras](https://centraldeatendimento.totvs.com/hc/pt-br/sections/35058659965079-Financeiro-Compensa%C3%A7%C3%A3o-entre-Carteiras)
