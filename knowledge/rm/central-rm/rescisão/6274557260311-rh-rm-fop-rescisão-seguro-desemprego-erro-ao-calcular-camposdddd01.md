---
article_id: 6274557260311
category: Rescisão
content_hash: 4b07af028ea42a673ef54f9c012a5a16a409d3954afaf9c731ddf4a63b764a7c
fetched_at: '2026-06-28T22:46:54.340317+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Rescisão - Seguro Desemprego: Erro ao calcular campoSDDDD01'
type: support-article
updated_at: '2025-01-20T14:26:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6274557260311-RH-RM-FOP-Rescis%C3%A3o-Seguro-Desemprego-Erro-ao-calcular-campoSDDDD01
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:34 min****Ocorrência**  
No módulo Folha de Pagamento, ao tentar realizar a geração do Seguro Desemprego é apresentada a seguinte mensagem: **Erro ao calcular campo CampoSDDDD01- System.ArgumentOutOfRangeException: O índice e o comprimento devem se referir a um local dentro da cadeia de caracteres.** **Nome do parâmetro: length****Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**O erro retornado é referente as máscaras e quebras ou informações divergentes na parametrização realizada.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Vá em **Administração de Pessoal | Funcionários,** selecione o colaborador que deseja e clique em **Editar** para acessar o seu cadastro.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6271995423767/mceclip0.png)  
  
2. Logo após, vá em **Informações Pessoais | Endereço Principal** e verifique o telefone do funcionário no campo **Telefone**. Essa informação será necessária na parametrização.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6274178002839/mceclip1.png)  
  
3. Feito isso, será necessário parametrizar em **Configurações | Parametrizador RH - Máscaras e Quebras**, a máscara de telefone conforme o cadastro do funcionário.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6274391401495/mceclip2.png)  
  
4. Após fazer a verificação e os devidos ajustes, o erro não será mais apresentado e a geração do seguro desemprego poderá ser feita normalmente.  
  
Saiba mais

[RH - RM - FOP - Seguro Desemprego: geração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003366401-RH-RM-FOP-Seguro-Desemprego-gera%C3%A7%C3%A3o)
