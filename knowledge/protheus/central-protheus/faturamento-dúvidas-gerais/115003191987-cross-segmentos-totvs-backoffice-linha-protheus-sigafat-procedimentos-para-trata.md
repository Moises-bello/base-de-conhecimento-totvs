---
article_id: 115003191987
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 419ec0d651e62465f90cca42587af2d7d1b3391d31f0e71ef22e60cf071c497e
fetched_at: '2026-06-28T22:38:30.028623+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Procedimentos
  para tratar Argument_error_in_function_Len()_on_CRIAVAR
type: support-article
updated_at: '2021-09-20T20:21:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115003191987-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Procedimentos-para-tratar-Argument-error-in-function-Len-on-CRIAVAR
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:01:00 min****

**Dúvida**

Procedimentos para tratar o erro**Argument\_error\_in\_function\_Len()\_on\_CRIAVAR**

**Ambiente**

Cross Segmentos- TOTVS Backoffice (Linha Protheus)-SIGAFAT- todas as versões

**Causa**

Esse retorno ocorre quando inserido no inicializador padrão de um determinado campo um conteúdo não válido com o tipo do campo.  A maioria dos casos são campos do tipo caractere que recebe um inicializa dor padrão numérico.

Exemplo:  campo A1\_BLEMAIL é um campo do tipo caracter , onde foi colocado no x3\_relação a informação 1, que como se apresenta sem aspas, o sistema entenderá que se trata de um dado numérico, gerando a inconsistência no processo.

    Field 3: X3\_ARQUIVO(C) :SA1  
    Field 4: X3\_ORDEM(C) :H8  
    Field 5: X3\_CAMPO(C) :A1\_BLEMAIL  
    **Field 6: X3\_TIPO(C) :C ---> indicação do tipo do campo como****caractere**  
    Field 7: X3\_TAMANHO(N) :1  
    Field 8: X3\_DECIMAL(N) :0  
    Field 9: X3\_TITULO(C) :Boleto Email  
    Field 10: X3\_TITSPA(C) :Boleta Email  
    Field 11: X3\_TITENG(C) :Paym. Slip    
    Field 12: X3\_DESCRIC(C) :Boleto Via Email (Cnab)    
    Field 13: X3\_DESCSPA(C) :Boleta Por E-mail (Cnab)   
    Field 14: X3\_DESCENG(C) :Pay.slip via e-mail -Cnab  
    Field 15: X3\_PICTURE(C) :@!                                            
    Field 16: X3\_VALID(C) :                                                                                                                                  
    Field 17: X3\_USADO(C) :€€€€€€€€€€€€€€   
    **Field 18: X3\_RELACAO(C) :1     ---->Causa do erro**

**Solução**

Para solucionar o problema, retire a opção do inicializador padrão, uma vez  que no dicionário padrão não há validação ou coloque a informação ***entre aspas*** (**"1"**) .
