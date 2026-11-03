---
article_id: 4409772507671
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 1ed08b58311101fd60baa5ae95c7126be5914c2fc4252692af6dc72afb98027a
fetched_at: '2026-06-28T22:42:43.341676+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Geração do registro K270
type: support-article
updated_at: '2021-10-01T11:52:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409772507671-Manufatura-Linha-Protheus-SIGAPCP-Gera%C3%A7%C3%A3o-do-registro-K270
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:10 min** **Dúvida**Ao gerar o **Bloco K** qual a regra para gerar o **Registro K270 - Correção de apontamentos**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O **Registro K270** tem o objetivo de escriturar correções de outros registros de períodos anteriores ao período de apuração.   
A geração desse registro é feita com base no campo **D3\_PERBLK - Período Bloco K**, através do qual é realizada a marcação do registro, indicando se o mesmo foi escriturado no **Bloco K** e em qual período essa escrituração ocorreu, portanto são levados para o **Registro K270** todos os registros dos períodos anteriores ao período de apuração, e que contenham o campo **D3\_PERBLK** em branco.  
  
**Exemplo**Supondo que em um determinado mês, para o nosso exemplo, mês **09/2021**, são realizados dois apontamentos de uma **OP - Ordem de Produção**, na inclusão do apontamento o campo **D3\_PERBLK** tem o seu conteúdo em branco.

![Imagem01.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4409825746199/Imagem01.jpg)

Ao executar a rotina **SPEDFISCAL** ou **MATR241 - Relação Bloco K** para o mês do apontamento, para este exemplo **09/2021** o registro é listado no **Bloco K230 - Itens Produzidos** e no bloco **K235 - Insumos Consumidos** e o campo **D3\_PERBLK** é preenchido com o mês e ano de processamento.

![Image02.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4409825797399/Image02.jpg)

![Image3.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4409825805975/Image3.jpg)

Se após a execução do **SPEDFISCAL** ou do **MATR241** ocorrer o estorno de um dos apontamentos, na tabela **SD3 - Movimentos Internos** é realizado o registro correspondente ao estorno e o campo **D3\_PERBLK** tem seu conteúdo em branco.

![Imagem04.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4409819422103/Imagem04.jpg)

Ao executar o **SPEDFISCAL** para o mês seguinte, no caso **10/2021**, é identificado através do campo **D3\_PERBLK** a necessidade de ajuste do apontamento referente ao estorno registrado para o mês **09/2021**, sendo assim o mesmo é listado no **K270** e o campo **D3\_PERBLK** é preenchido com o mês de processamento, no caso **10/2021.**

![image05.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4409825986711/image05.jpg)

![Imagem06.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4409826007831/Imagem06.jpg)

**Importante**Como o controle é realizado pelas rotinas **SPEDFISCAL - SPED Fiscal** e **MATR241 - Relação Bloco K**, que preenchem o campo **D3\_PERBLK**, uma vez o arquivo entregue ao **Fisco** o período não deve mais ser processado pelo **SPEDFISCAL** ou **MATR241**, pois o campo **D3\_PERBLK** será atualizado novamente podendo comprometer entregas de dados em período futuro.
