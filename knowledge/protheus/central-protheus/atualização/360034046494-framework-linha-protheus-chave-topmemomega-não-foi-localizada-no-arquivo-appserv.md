---
article_id: 360034046494
category: Atualização
content_hash: 64391d72dbe7968d84c9cc5f3efb707f2a1e128edfa7cb880a726c930e1da3da
fetched_at: '2026-06-28T22:42:21.310674+00:00'
product: protheus
section_id: 360000076747
source: central-protheus
title: Framework - Linha Protheus - Chave TopMemoMega não foi localizada no arquivo
  appserver.ini
type: support-article
updated_at: '2024-03-26T13:20:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034046494-Framework-Linha-Protheus-Chave-TopMemoMega-n%C3%A3o-foi-localizada-no-arquivo-appserver-ini
---

**Dúvida**Qual o motivo de aparecer a mensagem abaixo?  
Saída no final: Inconsistência no ambiente.  
Foram encontrados os seguintes erros no ambiente:  
A chave TopMemoMega não foi localizada no AppServer.ini  
   
 **Ambiente**Protheus - AppServer - A partir da versão 11  
  
**Solução**O erro, que é exibido diretamente no arquivo console.log, ocorre porque no binário versão Lobo Guará, é obrigatória a utilização da chave TopMemoMega no arquivo appserver.ini  
  
Maiores informações sobre o uso da chave no link abaixo:  
<http://tdn.totvs.com/display/tec/TOPMemoMega>
