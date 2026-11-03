---
article_id: 360035872254
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 68b5a2f32b6c1338726f67523ed0911fc490e6a4c03f89e73077bfe1fe66dca9
fetched_at: '2026-06-28T22:42:40.827586+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Apontamentos de perdas não são apresentados
  no MATR860
type: support-article
updated_at: '2021-10-21T17:51:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035872254-Manufatura-Linha-Protheus-SIGAPCP-Apontamentos-de-perdas-n%C3%A3o-s%C3%A3o-apresentados-no-MATR860
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:10 min**  
**Dúvida**Por que os apontamentos de perdas não estão sendo apresentados no relatório **MATR860 - Relação por Ordem de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**As informações que são apresentadas no relatório **MATR860** são buscadas da tabela **SD3 - Movimentações Internas**.  
Na rotina **MATA685 - Apontamento de perda** as informações ficam gravadas na tabelas **SBC - Perda por Ordem de Produção**.  
É necessário avaliar se a configuração relacionada a perda está gravando essa quantidade na tabela **SD3**, para que seja impressa no relatório, para isso verifique se na opção **F12** na rotina **MATA685** o parâmetro **Requisita produto de Origem?** está igual a **Sim** e se o campo **BC\_CODDEST - Produto destino** não está preenchido, isto porque quando o campo **BC\_CODDEST** é preenchido a rotina realiza uma transferência de estoque, não atrelada a **OP - Ordem de Produção.**Verifique também se item informado na **perda** é o item **produzido** pela **OP**, ao informar o **PA - Produto Acabado** na **perda,** o Sistema gera uma **requisição** sem vínculo a **OP**.
