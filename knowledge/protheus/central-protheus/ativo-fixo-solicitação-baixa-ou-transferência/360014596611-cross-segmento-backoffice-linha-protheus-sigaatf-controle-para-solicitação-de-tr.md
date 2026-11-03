---
article_id: 360014596611
category: Ativo Fixo - Solicitação Baixa ou Transferência
content_hash: f85874426c1a4fd3b3b049c552ffef5fae81d487856710e335f29757548ab839
fetched_at: '2026-06-28T22:41:49.106138+00:00'
product: protheus
section_id: 1500001547622
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF -  CONTROLE PARA SOLICITAÇÃO
  DE TRANSFERENCIA OU BAIXA DE ATIVO - ATFA125/ATFA126
type: support-article
updated_at: '2022-11-17T18:32:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014596611-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-CONTROLE-PARA-SOLICITA%C3%87%C3%83O-DE-TRANSFERENCIA-OU-BAIXA-DE-ATIVO-ATFA125-ATFA126
---

**Ocorrência**

Após realizar transferência de itens através da solicitação de baixa/transferência e aprovação movimento não é exibido no relatório de transferência (ATFR100).

**Ambiente**

**Ambiente**Cross Segmento - Backoffice Linha Protheus – Ativo fixo  – Todas as versões

**Solução**Verificar quanto a possibilidade de atualização disponível no portal.

Segue informações referente ao processo de solicitação de transferência ou baixa do ativo:

· ATFA025 – Cadastro de Locais (Cadastro que indica onde os bens estão locados)  
· ATFA125 – Solicitação de Baixa/Transferência (Inicia o workflow gerando uma solicitação para o responsável pelo ativo)  
· ATFA126 – Análise de Baixa/Transferência (Permite a aprovação ou rejeição da solicitação, encerrando o workflow). O processo de solicitação é ativado através do parâmetro MV\_ATFSOLD (1=Ativado; 2=Desativado). Quando esse parâmetro for ativado os processos normais de baixas e transferências de ativos ficarão bloqueados. O controle de workflow também pode ser ativado ou não configurando o parâmetro MV\_ATFWFM (1=Ativado; 2=Desativado), se for ativado o sistema controlará o fluxo e um email será enviado ao responsável pelo ativo  para aprovação da solicitação, se estiver desativado a aprovação deverá ser feita manualmente no sistema  
através do ATFA126.  
A melhoria permite também a geração automática de documentos fiscais para as solicitações aprovadas de baixa ou transferência.

Procedimentos para Utilização:

1. No Ativo Fixo (SIGAATF) acesse Atualizações / Cadastros / Locais (ATFA025).  
O sistema apresenta a janela de locais cadastrados.  
2. Clique no botão Incluir.  
3. Informe os dados dos novos campos:  
4. Confira os dados e confirme.  
5. Acesse Atualizações / Cadastros / Ativo (ATFA012).  
O sistema apresenta a janela de ativos cadastrados.  
6. Clique no botão Incluir.  
7. Informe os dados conforme orientação do help de campo e observe o preenchimento automático do  
novo campo presente na nova aba Localização após o preenchimento do campo  
Endereço(N1\_LOCAL):  
8. Confira os dados e confirme.  
9. Acesse Atualizações / Movimentos / Solic. Baixa/Transf. (ATFA125).  
O sistema apresenta a janela de solicitações de baixa/transferência cadastradas.  
10. Clique no botão Solic. Baixa ou selecione a opção Baixa em lote para baixa de vários itens  
simultaneamente.  
11. Informe os campos conforme help de campo.  
12. Confira os dados e confirme.

Importante  
Caso parâmetro MV\_ATFWFM possua valor igual a “T” o sistema irá enviar WorkFlow de aprovação da solicitação efetuada para o responsável pelo bem ou se não houver para o responsável padrão pelo ativo  
informado no parâmetro MV\_ATFRESP.

Links com informações em relação ao processos de solicitação de transferência

<https://tdn.totvs.com/pages/releaseview.action?pageId=190513202#WorkflowdeAprova%C3%A7%C3%A3odaSolicita%C3%A7%C3%A3odaBaixadeAtivo-MovimentandoeConsultandooProcessopeloFluig>

<https://tdn.totvs.com/pages/releaseview.action?pageId=44401528>
