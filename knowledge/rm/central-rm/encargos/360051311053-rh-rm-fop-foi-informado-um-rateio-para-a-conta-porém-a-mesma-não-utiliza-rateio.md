---
article_id: 360051311053
category: Encargos
content_hash: 956ad09ee6f17afaa069da990760902a6f177d51e25733b9db3b73c789300c1a
fetched_at: '2026-06-28T22:46:53.311783+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Foi informado um rateio para a Conta, porém a mesma não utiliza
  rateio
type: support-article
updated_at: '2025-03-12T13:53:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051311053-RH-RM-FOP-Foi-informado-um-rateio-para-a-Conta-por%C3%A9m-a-mesma-n%C3%A3o-utiliza-rateio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:03:45 min****Dúvida**Como corrigir o erro **Foi informado um rateio para a Conta, porém a mesma não utiliza rateio** ao executar o processo de Contabilização?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Este erro acontece quando o evento ou o encargo que está sendo contabilizado tem alguma conta gerencial informada, mas a conta contábil referenciada não tem rateio. Veja o exemplo a seguir:  
  
1. O evento abaixo tem uma conta gerencial informada a débito. Sendo assim, a conta contábil, que é a conta informada no erro, será rateada para a conta gerencial, 111 na imagem abaixo.   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078700613/mceclip0.png)  
  
Neste exemplo, a conta gerencial é identificada pelo código 1.1.1.1.001:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078704393/mceclip1.png)  
  
Portanto, identifique o cadastro da conta contábil a ser ajustada.  
  
2. O que ocorre é que no cadastro da conta 1.1.1.1.001 (em Encargos | Cadastros | Contas Contábeis | Plano de Contas (Gestão Contábil), o flag de Rateio não está marcado, ou seja, entende-se que a conta não possui rateio:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078704813/mceclip2.png)  
  
3. Via de regra, se for informada alguma conta gerencial em algum encargo ou evento, a conta contábil referenciada deve possuir rateio.   
Perceba que o campo **Rateio** na imagem acima encontra-se desmarcado e inativo. Isso acontece pois ele não pode ser marcado diretamente. Para parametriza-lo resultando em sua marcação, deve-se acessar **Processos | Alteração do campo "Tem Distribuição Gerencial"**:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077561814/mceclip3.png)  
  
A visualização deste processo se dá mediante de permissão do usuário no módulo Gestão Contábil.  
  
4. No processo que se abrirá, basta informar que a conta passará a ter distribuição gerencial.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078705413/mceclip4.png)  
  
Na tela seguinte, busque a(s) conta(s) gerencial(is) desejada(s), informe o rateio e posteriormente clique em **Incluir**. A(s) conta(s) aparecerá(ão) com estas informações na lista abaixo:  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078705793/mceclip5.png)  
  
5. Após a execução do processo, o campo Rateio ficará marcado no cadastro da conta, e será exibida a aba **Distribuição Gerencial**, contendo as contas gerenciais selecionadas no processo:  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077562494/mceclip6.png)  
  
Por fim, realize novamente o processo de contabilização e o erro não deverá aparecer.
