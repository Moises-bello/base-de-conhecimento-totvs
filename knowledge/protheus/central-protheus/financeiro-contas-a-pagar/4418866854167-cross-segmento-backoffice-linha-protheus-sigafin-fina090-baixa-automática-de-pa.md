---
article_id: 4418866854167
category: Financeiro - Contas a Pagar
content_hash: eec662a892bca478ee9dc4349c7ad22c9c105f6f0f9d9ff14cd81c0727f842dd
fetched_at: '2026-06-28T22:38:08.266276+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA090 - Baixa automática
  de PA com o campo cheque habilitado não gera número de cheque
type: support-article
updated_at: '2022-01-13T14:51:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418866854167-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA090-Baixa-autom%C3%A1tica-de-PA-com-o-campo-cheque-habilitado-n%C3%A3o-gera-n%C3%BAmero-de-cheque
---

**Ocorrência**  
Na rotina FINA090 ao baixar PA com cheque não é demonstrado o número do cheque na posição do título.  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Financeiro - FINA090 - A partir da versão 12.1.23

**Causa**

 Ao gerar o PA com **F12** selecionando **Cheque P/ Adiantamento = Não** e **Gera Mov. Banc. S/ Cheque = SIM** (nesse momento é gerada a movimentação  bancária).

No processo de baixa de **PA** da rotina **FINA090** - **Baixa automática** quando é informado um cheque para baixa não é alimentado o campo **N.cheque** na posição de título, pelo fato de não gerar cheque na tabela **SEF** para este movimento, bem como na rotina **FINA080** - **Baixa manual** não é habilitado o campo **Cheque No**., sendo este comportamento padrão do sistema .

**Solução**Trata-se de uma sugestão de melhoria no produto. A partir de agora, as melhorias não serão mais tratadas via ticket, elas devem ser incluídas diretamente no [Portal do Cliente](http://suporte.totvs.com/). Um espaço que você poderá sugerir melhorias, acompanhar a evolução das solicitações já realizadas, comentar, seguir, votar em sugestões feitas por outros clientes e muito mais!  
  
Esse espaço é a nossa [Central Colaborativa TOTVS](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics).  
Para conhecer mais sobre as suas funcionalidades clique [AQUI](https://www.youtube.com/watch?v=LTqWbDsBb6s&list=PLYQXMbUS13r-xtKThVYHMFsLK3ezvpo3q&index=13) e assista o nosso vídeo ou acesse nosso artigo [Central Colaborativa - Funcionalidades Disponíveis](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039466814-Funcionalidades-Dispon%C3%ADveis-na-Central-Colaborativa-TOTVS)​.  
  
Você pode acompanhar as suas sugestões e comentários clicando [AQUI](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br).

**Saiba mais**

**[Baixas Pagar Automática - FINA090 - Financeiro - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=271852126)**

**[Cross Segmento Protheus - Backoffice Linha Protheus - SIGAFIN - Quais os modos de inclusão de PA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004726827-Cross-Segmento-Protheus-Backoffice-Linha-Protheus-SIGAFIN-Quais-os-modos-de-inclus%C3%A3o-de-PA?source=search)**
