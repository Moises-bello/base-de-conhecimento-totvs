---
article_id: 11631436983191
category: Anuais
content_hash: 225399b0981506aa0b9308f2d8e9765284c3dcfbe6ace3fe83b2bce1d4e0217b
fetched_at: '2026-06-28T22:46:51.051710+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: 'RH - RM - FOP - Informe de Rendimentos: relatório saindo em branco'
type: support-article
updated_at: '2025-01-24T15:19:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11631436983191-RH-RM-FOP-Informe-de-Rendimentos-relat%C3%B3rio-saindo-em-branco
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:49 min****Ocorrência**No módulo Folha de Pagamento, ao realizar a geração do Informe de Rendimentos em **Anuais | DIRF/Informe de Rendimentos,** o relatório está saindo em branco. Em outras palavras, sem as informações, conforme demonstrado na imagem abaixo.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11628093704471)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Isso ocorre quando há uma atualização do sistema e o relatório é corrompido durante a atualização, perdendo sua estrutura e informações.  
  
**Solução**

Para solucionar essa ocorrência deverá realizar a exclusão e importação do relatório seguindo os passos abaixo:  
  
1. Acesse **Gestão | RM Reports** e exclua o relatório de Informe de Rendimentos. Lembre-se de excluir os sub-relatórios antes de excluir o principal. É necessário realizar esse processo da exclusão do relatório também em outras coligadas se ele for utilizado. Portanto, deverá realizar o procedimento em cada um delas. Caso tenha dúvidas na exclusão, veja o artigo abaixo:  
[RH - RM - FOP - RM Reports: Exclusão de Relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411688075799-RH-RM-FOP-RM-Reports-Exclus%C3%A3o-de-Relat%C3%B3rios)  
  
2. Nesta mesma tela, vá em **Processos | Importar estrutura de relatório** e importe o relatório novamente. Caso tenha dúvidas na importação, veja o artigo abaixo:  
[RH - RM - FOP - RM Reports: Importação de Relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007544951-RH-RM-FOP-RM-Reports-Importa%C3%A7%C3%A3o-de-Relat%C3%B3rios)   
  
3. Gere o Informe de Rendimentos novamente pela rotina **Anuais | DIRF/Informe de Rendimentos** e informe o relatório no campo destacado na imagem abaixo.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11631096462103)

**Importante**.

Os relatórios estão disponíveis no Totvs compartilhamento, segue abaixo orientação para importação do mesmo. Lembrando que sempre deve ser importado o ultimo relatório inserido no compartilhamento, sendo assim, se atente a data de inserção do relatório.  
[RH - RM - FOP- Como fazer download de arquivos no totvs compartilhamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7781155867543-RH-RM-FOP-Como-fazer-download-de-arquivos-no-totvs-compartilhamento)
