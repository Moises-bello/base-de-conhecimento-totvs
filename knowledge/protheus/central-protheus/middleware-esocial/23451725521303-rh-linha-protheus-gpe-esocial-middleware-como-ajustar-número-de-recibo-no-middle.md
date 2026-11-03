---
article_id: 23451725521303
category: MIDDLEWARE eSocial
content_hash: e156927b1a0a7a5f3d23d8b56e8a1fcf7f056d63a659855df027a2278040a3fe
fetched_at: '2026-06-28T22:43:04.953586+00:00'
product: protheus
section_id: 360005445753
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Middleware - Como ajustar número de recibo
  no Middleware
type: support-article
updated_at: '2024-05-13T19:53:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23451725521303-RH-Linha-Protheus-GPE-eSocial-Middleware-Como-ajustar-n%C3%BAmero-de-recibo-no-Middleware
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23451725470615) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como realizar o ajuste de número de recibo no Middleware?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Criada rotina para visualização de todos os registros da tabela de fila do monitor middleware.  
Para os eventos cujo o status seja **1 - Pendente de de envio** ou **3 - Evento Rejeitado será possível ajustar o recibo**, ou seja, o evento terá o número do recibo ajustado e o status alterado para **4 - Transmitido com sucesso.  
  
Primeiro passo** deve ser a **atualização do pacote de expedição continua** que será **liberado dia 20/05/2024,** através do link: **[ATUALIZACAO DE ARQUIVOS FONTES RH EXPEDICAO CONTINUA - TOPCONNECT](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/rh_expedicao_continua)**  
**Segundo passo**, após atualização será a criação da **rotina no menu** siga o exemplo abaixo:  
  
No **Configurador** (SIGACFG) acesse Ambientes/Cadastro/Menu (CFGX013). Informe a nova opção de menu do SIGAGPE, conforme instruções a seguir:

**Menu** | Miscelânea

**Submenu** | eSocial

**Submenu** | Middleware

**Nome da Rotina** | Reg. Fila Middleware

**Programa** | GPEM922A

**Módulo** | Gestão de Pessoal

**Função** | Função Protheus  
  
Exemplo de Configuração:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23451992452375)  
 **Utilização**:  
Ao acessar a rotina será apresentado um browser com todos os dados da tabela RJE. Será possivel realizar filtros, por evento, inicio de validade, entre outras opções.  
Os eventos estarão classificados pela legenda:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23451933198103)  
  
Selecione o registro que deseja realizar o ajuste de recibo, do qual deve ter a legenda Evento Pendente de Envio ou Evento Rejeitado.  
Após selecionar, clique em Ajustar Recibo:  
**![smartclient_WAgUr2YxQf.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/23451686636567)**  
Atenção, leia a mensagem emitida pelo sistema antes de realizar o ajuste e clique em Ok.  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23451686639383)**  
  
Ao confirmar o ajuste o sistema emite a seguinte mensagem:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23451725485975)  
  
No browser o registro terá seu status alterado para transmitido com sucesso e possível visualizá-lo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23451686649751)  
 **Saiba Mais**Para saber mais consulte os *links* abaixo:  
[DT Realizar ajuste de recibo do e-Social no Middleware](https://tdn.totvs.com/display/PROT/DT+Realizar+ajuste+de+recibo+do+e-Social+no+Middleware#Recibo-Uso)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
