---
article_id: 10846429625239
category: Gestão
content_hash: 6359775e510b9cdbcf72aa67b65a6525bdc6b8e1e5fa3cea9b0d3aa0af32c536
fetched_at: '2026-06-28T22:46:48.282683+00:00'
product: rm
section_id: 1500000861162
source: central-rm
title: RH - RM - FOP - Relatório sendo gerado em branco
type: support-article
updated_at: '2026-03-20T19:48:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10846429625239-RH-RM-FOP-Relat%C3%B3rio-sendo-gerado-em-branco
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:41 min****Ocorrência**No módulo Folha de Pagamento, ao realizar a geração do relatório, o mesmo está saindo em branco.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Isso ocorre quando há uma atualização do sistema e o relatório é corrompido durante a atualização, perdendo sua estrutura e informações.  
  
**Solução**Em primeiro momento, é importante ressaltar que as visões Delphi e Net encontram-se descontinuadas. Contudo, caso gere algum relatório através dessas duas opções poderá gerar inconsistências. Assim, o Suporte Totvs sugere que os relatórios sejam gerados através do RM Reports localizado em **Gestão | RM Reports**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10846169765143)  
  
Os relatórios padrão do sistema TOTVS são acessados através da ferramenta **TOTVS Compartilhamento** ou através do caminho: **C:\TOTVS\CorporeRM\ObjetosGerenciais\Relatórios**.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10846328214167)  
  
Para que o relatório seja gerado com as informações será necessário realizar a exclusão e importação do relatório seguindo os passos abaixo:  
  
1. Acesse: **Gestão | RM Reports** e exclua o relatório. Lembre-se de excluir os sub-relatórios antes de excluir o principal. Caso o relatório esteja também em outras coligadas, deverá realizar o procedimento em cada uma delas.  
  
[RH - RM - FOP - RM Reports: Exclusão de Relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411688075799-RH-RM-FOP-RM-Reports-Exclus%C3%A3o-de-Relat%C3%B3rios)  
  
2. Nesta mesma tela, acesse **Processos | Importar estrutura de relatório** e importe o relatório novamente. Caso tenha dúvidas na importação, veja o artigo abaixo:  
  
[RM - FOP - RM Reports: Importação de Relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007544951-RH-RM-FOP-RM-Reports-Importa%C3%A7%C3%A3o-de-Relat%C3%B3rios)  
  
3. Feito isso, o relatório será gerado com os dados com sucesso.  
  
**Importante**  
Caso esteja gerando um relatório que não seja padrão Totvs, ou seja, um relatório customizado, a Equipe de Suporte da Totvs não auxilia na manutenção do relatório. Para isso, será necessário verificar com a equipe DBA ou TI da empresa ou caso tenha interesse, sugerimos a Equipe de Consultoria da Totvs.
