---
article_id: 360011601132
category: Folha Mensal
content_hash: 0dfc0178cb2cd935fdf1959825fd0b5341e56926071cd80f449c1cac30a84ebf
fetched_at: '2026-06-28T22:47:00.306462+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Erro Retorno NIS: startIndex'
type: support-article
updated_at: '2025-03-07T14:58:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011601132-RH-RM-FOP-Erro-Retorno-NIS-startIndex
---

**Ocorrência**Ao acessar o menu **Folha Mensal | Importação | Importação Arquivo de Retorno NIS** e importar o arquivo retornado da Caixa, o erro é apresentado:  
  
**startIndex cannot be larger than length of string****Parameter name: startIndex****Ambiente**RM - Totvs Folha de Pagamento - 12.1.18 ou superiores  
  
**Causa**O erro ocorre devido a importação do layout incorreto.  
  
**Solução**Para solucionar este erro, siga os passos abaixo:  
  
**01.** Este erro ocorre devido ao arquivo importado não obedecer ao layout padrão. Caso isso ocorra, realize a geração do layout para solicitar o NIS para a caixa, acessando o menu **Folha mensal | Relatórios da folha | Cadastro NIS;**  
  
**02.** Após envio do arquivo gerado no passo **01**, será necessário enviar o arquivo para a Caixa validar e adicionar o PIS no fim do arquivo. A Caixa, então, devolve o arquivo com as informações do PIS;  
  
**03.** Com o arquivo de retorno, acesse **Folha Mensal | Importação | Importação Arquivo de Retorno NIS** e faça a importação do arquivo de retorno do NIS para que o sistema importe o número do PIS para o cadastro do funcionário;  
  
**04.** O sistema valida se o PIS foi acrescentado no arquivo conforme o CPF do funcionário;  
  
**05.** Uma vez que a importação do arquivo de retorno for realizada com sucesso, o sistema emitirá uma mensagem informando o número do PIS e a chapa do funcionário, conforme print abaixo:  
  
![nis4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008552051/nis4.png)
