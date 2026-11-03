---
article_id: 4421427553303
category: PMS - Projetos
content_hash: 5633f1a7ebe6785bc2c9d95963ce6f316dd5ff8085fa13a395ccc2e8ec419762
fetched_at: '2026-06-28T22:37:15.217087+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Gerenciamento do Empenho
  do Projeto
type: support-article
updated_at: '2024-02-26T18:34:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421427553303-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Gerenciamento-do-Empenho-do-Projeto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21628454022423) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como gerar empenho do Projeto?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as Versões  
**Solução**

O empenho significa que esse material está alocado para a tarefa, portanto, caso não haja quantidade suficiente no almoxarifado para atender o empenho, o sistema poderá gerar uma solicitação de compra, quando o material não for produzido, ou poderá ser gerada uma ordem de produção, caso o material seja produzido, empenho não significa que o material tenha sido consumido, mas, apenas que existe uma reserva para aquela tarefa.  
  
Caso queira excluir o empenho gerado é possível excluir através da rotina: Consultar em **Projetos** > **Gerenciam. Execução > Seleciona o Projeto em questão > Outras Ações > Atualizar> Posiciona na Tarefa que originou o empenho > Outras Ações** > **Gerenciam. de Execução > Gerenciam. de Empenhos do Projeto > Excluir.**

Tela de Baixa do Empenho : Existe o parâmetro **MV\_PMSBXEM**:  
Indica se exibe ou não a tela de baixa de empenhos na amarração da NFE com o projeto.  
A tela de baixa de empenhos permite ao usuário selecionar o empenho que será baixado na entrada da NF (empenho gerado a partir de uma solicitação de compras amarrada ao projeto ou um planejamento deste). Este parâmetro é útil para empresas que não utilizam o controle de empenhos, facilitando a digitação da NF.   
A baixa do empenho ocorre  quando o parâmetro **MV\_PMSBXEM** estiver como **T**, isto para notas de entrada. É exibido uma pergunta se deseja baixar o empenho.  
Caso contrario terá que zerar o empenho do projeto através do gerenciamento de execução conforme processo que evidencia em anexo.

**Saiba mais em : [Gerenciamento do Empenho do Projeto](https://tdn.totvs.com/x/GpIOFQ)**
