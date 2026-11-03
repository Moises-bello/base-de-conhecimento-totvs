---
article_id: 360045655053
category: eSocial - Tabelas/Não Periódicos
content_hash: d28f2259d8d6bed41bf3610663379043249b4d64c1e59d293b314b75ed23a075
fetched_at: '2026-06-28T22:47:10.580261+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM- eSocial - Exclusão do S-2200 em caso de desistência do empregado
type: support-article
updated_at: '2024-07-31T20:17:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045655053-RH-RM-eSocial-Exclus%C3%A3o-do-S-2200-em-caso-de-desist%C3%AAncia-do-empregado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24346862959639)Tempo aproximado para leitura:00:01:15 min**

**Dúvida**Como realizar a exclusão do cadastro de um funcionário cujo S-2200 foi enviado e aceito pelo governo, porém desistiu do emprego antes do início das atividades?  
  
 **Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para realizar a exclusão do funcionário e do S-2200, siga os passos abaixo:  
1. Acesse **Administração de Pessoal | Funcionários | Processos | Exclusão de Funcionário.** Será gerado um gatilho do S-3000 automaticamente;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062486374)

2. Acesse eSocial | Eventos eSocial , selecione o gatilho do evento S-3000, gere o XML e transmita o evento ao governo.  
  
**Importante**Antes de realizar este processo, é necessário conferir no governo a movimentação do funcionário, pois é necessário excluir qualquer evento posterior à admissão, através do S-3000, antes de excluir o funcionário.   
O processo de **Exclusão de Funcionário** poderá excluir um funcionário do cadastro desde que tenha sido admitido no mês atual e não possua movimentação lançada na Ficha Financeira, ou seja, o sistema permite a exclusão de funcionário com a situação **A - Ativo** e data de **admissão dentro da competência atual** ou a situação **Z - Admissão próximo mês** e com data de **admissão maior ou igual a competência atual**.  
  
Em casos onde ocorrer a perda do gatilho gerado automaticamente após execução do funcionário, deverá ser incluído um novo gatilho manualmente na fila, informando o **CPF** e **NIS** do funcionário. Isso é necessário pois o sistema não possui mais as informações salvas no cadastro do funcionário para geração automática dos dados.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062497054)
