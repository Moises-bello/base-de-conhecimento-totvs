---
article_id: 360050317953
category: RH - CNAB
content_hash: db976c4c51da262a91089fcfc15f380a4bcc023a5b6ed7691abea0e93b0e764c
fetched_at: '2026-06-28T22:43:39.366160+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE - Erro na validação do arquivo CNAB junto ao banco
  (erro no layout ou erro de linha inválido)
type: support-article
updated_at: '2021-06-07T14:24:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050317953-RH-Linha-Protheus-GPE-Erro-na-valida%C3%A7%C3%A3o-do-arquivo-CNAB-junto-ao-banco-erro-no-layout-ou-erro-de-linha-inv%C3%A1lido
---

**Ocorrência**Erro na validação do arquivo CNAB junto ao banco (erro no layout ou erro de linha inválido)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Se o arquivo CNAB já foi validado em outro envio, esse incidente pode ocorrer, devido à configuração do grupo de perguntas da rotina GPEM080 (Geração de líquidos).

**Solução**  
Exemplo de erro apresentando na validação do arquivo CNAB:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074441494/mceclip1.png)  
  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse Miscelânea ->Líquido -> Geração de Líquidos:   
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074441514/mceclip2.png)

2. Nas perguntas da rotina, verifique o campo : Linha vazia no Final do Arquivo e configure com NÃO:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074441534/mceclip3.png)  
3. Em seguida , gere o arquivo CNAB novamente e refaça a validação junto ao banco.  
  
**IMPORTANTE:** Tratando-se de layout do arquivo CNAB, caso não seja possível solucionar esse problema, é provável que seja necessário apoio para validação e configuração do arquivo, solicitando a visita de um consultor in loco para realizar tal procedimento, uma vez que para as verificações deste atendimento e validações do arquivo são realizados somente através de consultoria por um analista desenvolvedor.

**ATENÇÃO:**Muita atenção ao revalidar o arquivo gerado junto ao banco, para que não ocorra a tentativa de revalidação com o arquivo incorreto, de modo que apresente o mesmo erro.
