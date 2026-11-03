---
article_id: 360037130433
category: PMS - Projetos
content_hash: 6910162d7d6bdf301abd84c0c939a8c651623110fe1feab2672eb46f6d3d7fd1
fetched_at: '2026-06-28T22:37:14.993722+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: MP - PMS - Baixa de Empenho
type: support-article
updated_at: '2021-04-29T21:12:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037130433-MP-PMS-Baixa-de-Empenho
---

**Duvida**

Para os produtos que não existem no estoque , realizamos o apontamento da Nota Fiscal de entrada na rotina de Apontamentos **PMSA300**, Como executar a baixa do empenho?  
  
 **Ambiente**

Microsiga Protheus – a partir da release 11.80.  
  
 **Solução**

Quando o empenho foi gerado através do **SIGAPMS**, o sistema empenha no projeto quando é gerado ordem de produção ou nota de entrada, isto é uma tratativa padrão do sistema.  
A baixa do empenho ocorre  quando o parâmetro **MV\_PMSBXEM**estiver como**T**, isto para notas de entrada. É exibido uma pergunta se deseja baixar o empenho.  
Caso contrario terá que zerar o empenho do projeto através do gerenciamento de execução.  
Existe também o parâmetro **MV\_PMSOPSC**onde exclui os empenhos para OP que foram estornadas./ canceladas.  
  
O empenho não significa que o material tenha sido consumido, mas, apenas que existe uma reserva para aquela tarefa.  
Tem o parâmetro **MV\_PMSBXEM**:  
Indica se exibe ou não a tela de baixa de empenhos na amarração da Nota Fiscal com o projeto.  
  
A tela de baixa de empenhos permite ao usuário selecionar o empenho que será baixado na entrada da Nota Fiscal (empenho gerado a partir de uma solicitação de compras amarrada ao projeto ou um planejamento deste).  
Este parâmetro é útil para empresas que não utilizam o controle de empenhos, facilitando a digitação da Nota Fiscal.
