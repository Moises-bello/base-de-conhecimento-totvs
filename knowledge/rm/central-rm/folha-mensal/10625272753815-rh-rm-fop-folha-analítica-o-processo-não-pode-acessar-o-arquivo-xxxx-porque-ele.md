---
article_id: 10625272753815
category: Folha Mensal
content_hash: d8e4bdda34d564fd2b02692159252b5e56b17f2d39d1ff2985b7e146f6a7de9d
fetched_at: '2026-06-28T22:46:58.292740+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Folha Analítica: O processo não pode acessar o arquivo XXXX
  porque ele está sendo usado por outro processo'
type: support-article
updated_at: '2025-05-20T13:06:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10625272753815-RH-RM-FOP-Folha-Anal%C3%ADtica-O-processo-n%C3%A3o-pode-acessar-o-arquivo-XXXX-porque-ele-est%C3%A1-sendo-usado-por-outro-processo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26845374665623) Tempo aproximado para leitura: **00:01:44 min****Ocorrência**Ao gerar o relatório da folha analítica, o sistema emite a seguinte mensagem de erro: O processo não pode acessar o arquivo porque ele está sendo usado por outro processo.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10625407951255)  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**A inconsistência apresentada, geralmente ocorre por dois motivos:  
  
1. A pasta a qual esta tentando salvar o arquivo da folha analítica não esta com todas as permissões liberadas para o sistema e para seu usuário.  
  
2. o campo localizado em **Configurações | Parametrizador | Folha Normal | Geral**  não esta preenchido com o caminho da pasta que deseja salvar e com todas permissões liberadas.

**Solução**Para solucionar o erro, siga as instruções a seguir:  
  
1. Acesse **Configurações | Parametrizador | Folha Normal | Geral;**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10624696256791)**

2. Verifique se os campos acima estão preenchidos. Caso seja uma questão de permissão, realize as liberações de permissões na pasta e configure o acesso, parametrizando a pasta na tela acima juntamente com o time de TI da empresa.  
  
3. Se as permissóes já estiverem liberadas e o campo **"Diretório utilizado para processos que geram arquivos em Net. (JobServer)"** estiver em branco, faça o preenchimento do mesmo conforme o exemplo abaixo:   
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10625145312279)  
  
4. Feito isso, a mensagem de erro não será emitida e a geração da Folha Analítica poderá ser realizada.
