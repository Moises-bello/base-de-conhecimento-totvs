---
article_id: 360000589988
category: PMS - Projetos
content_hash: ac0e8b6e83c7cb1ce69f2ccc918a79af7adb718a63236a288979c4f8df6ddfd6
fetched_at: '2026-06-28T22:37:14.872485+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Baixa de Empenho
type: support-article
updated_at: '2024-02-23T12:01:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000589988-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Baixa-de-Empenho
---

**Dúvida**

Como baixar empenho de produto no Gestão de Projetos?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAPMS - A partir da versão 11.  
  
**Solução**

Quando o empenho foi gerado através do **SIGAPMS**, o sistema empenha no projeto quando é gerado ordem de produção ou nota de entrada, isto é uma tratativa padrão do sistema.

A baixa do empenho ocorre quando o parâmetro **MV\_PMSBXEM** estiver como T, isto para notas de entrada. É exibido uma pergunta se deseja baixar o empenho.   
Caso contrario terá que zerar o empenho do projeto através do gerenciamento de execução.  
Existe também o parâmetro **MV\_PMSOPSC**onde exclui os empenhos para OP que foram estornadas./ canceladas.

O empenho não significa que o material tenha sido consumido, mas, apenas que existe uma reserva para aquela tarefa. Tem o parâmetro **MV\_PMSBXEM**:  
Indica se exibe ou não a tela de baixa de empenhos na amarração da Nota Fiscal com o projeto.  
  
A tela de baixa de empenhos permite ao usuário selecionar o empenho que será baixado na entrada da Nota Fiscal (empenho gerado a partir de uma solicitação de compras amarrada ao projeto ou um planejamento deste).  
Este parâmetro é útil para empresas que não utilizam o controle de empenhos, facilitando a digitação da Nota Fiscal.

**Importante**Caso queira excluir o empenho gerado é possível excluir através da rotina: Consultar em Projetos > Gerenciam. Execução > Seleciona o Projeto em questão > Ações Relacionadas > Visualizar > Posiciona na Tarefa que originou o empenho > Ações Relacionadas > Gerenciam. de Execução > Gerenciam. de Empenhos do Projeto > Excluir.
