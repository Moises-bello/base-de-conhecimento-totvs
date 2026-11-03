---
article_id: 360036988633
category: RH - Integração de Titulo
content_hash: 714a5a39a653fc49ffaf02869b0e05f520e02187c5c8640cafbe2f8c0c7d032a
fetched_at: '2026-06-28T22:43:36.529454+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar título de rescisão
type: support-article
updated_at: '2025-07-18T14:08:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036988633-RH-Linha-Protheus-GPE-Como-gerar-t%C3%ADtulo-de-rescis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33558767616151)**Tempo aproximado para leitura: 00:03:00 min

**Dúvida**Como gerar titulo de rescisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da Versão 12.  
  
**Solução**Para **configurar um título de rescisão,** de modo que a **busca de vencimento ocorra automaticamente** de acordo com a gravação do cálculo da rescisão, siga o seguinte passo a passo:   
  
1. Acesse: Miscelânea -> Títulos -> Definição:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048720753)

2. Selecione a opção **Definir título** e configure a verba de líquido de rescisão, buscando na tabela SRR e Campo Data para filtro= RR\_DATAPAG:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048720813)  
  
3. Em seguida acesse: **Outras Ações** e **Informações para busca data de vencimento**:   
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048722573)  
  
4. Em **Informações para busca da data de vencimento do título**, selecione o campo data para vencimento RG\_DATAHOM (este campo refere-se à data de recebimento da rescisão idem ao cabeçalho do cálculo (verificar no item 5):   
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047842874)  
  
5. A busca ocorrerá de acordo com o campo indicado na definição de título. Para melhor entendimento , no print abaixo, verificamos a qual campo refere-se:   
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047844854)  
  
6. Com o cálculo da rescisão efetuado, o campo de busca será apresentado da seguinte forma:   
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047847074)  
Veja que as informações de SRG\_DATAHOM e SRR\_DATAPAG são compatíveis.   
  
7. Após configuração do título e cálculo da rescisão, acesse Miscelânea -> Títulos -> Geração e ajuste os parâmetros para geração:  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047845094)  
8. Note que a data de vencimento está em branco, para que na geração busque a informação parametrizada na definição do título, no nosso caso, a data de pagamento da rescisão:  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047847294)  
Obs: A configuração realizada dessa forma permite que seja gerado mais de um título de rescisão, respeitando as datas de pagamentos diferentes.  
  
9. Acesse Miscelânea -> Títulos -> Manutenção e verifique a geração de título com a data de pagamento definida:  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047847694)  
  
**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
