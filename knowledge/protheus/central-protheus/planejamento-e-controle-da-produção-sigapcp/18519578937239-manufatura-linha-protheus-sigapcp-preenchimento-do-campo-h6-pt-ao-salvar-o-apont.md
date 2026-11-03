---
article_id: 18519578937239
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: bb50b4eec04bdabe8ebc7823399e75283378ce1c0f72543380f455ae62a5e753
fetched_at: '2026-06-28T22:42:45.721372+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Preenchimento do campo H6_PT ao salvar
  o apontamento
type: support-article
updated_at: '2023-10-24T12:56:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18519578937239-Manufatura-Linha-Protheus-SIGAPCP-Preenchimento-do-campo-H6-PT-ao-salvar-o-apontamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18519603843607) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Na rotina **MATA680 - Apontamento Produção Modelo I** ou **MATA681 - Apontamento Produção Modelo II**, ao preencher o campo **H6\_QTDPROD - Quantidade Produzida** ou  **H6\_QTDPERD - Quantidade Perdida** e na sequência clicar em confirmar, o campo **H6\_PT - Produção Parcial ou Total** não é atualizado.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Para que o Sistema atualize o campo **H6\_PT** ao sair do campo **H6\_QTDPROD** ou do campo **H6\_QTDPERD** e clicar em salvar, sem passar por outro campo, altere o conteúdo do parâmetro **MV\_PARTOT - Define se o campo Parcial/Total nos apontamentos de produção serão atualizados no botão Salvar** para **.T.**  
  
**Saiba Mais**No link [Preenchimento do Campo H6\_PT](https://tdn.totvs.com/pages/viewpage.action?pageId=612724395) temos a documentação sobre o preenchimento do campo **H6\_PT**.
