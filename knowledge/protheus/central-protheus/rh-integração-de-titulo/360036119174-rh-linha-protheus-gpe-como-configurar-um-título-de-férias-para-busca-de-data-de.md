---
article_id: 360036119174
category: RH - Integração de Titulo
content_hash: 03784dfd1f79e0671573d0d9dd845bd7720f00d49952c0e4051843a48ac4ba71
fetched_at: '2026-06-28T22:43:36.209671+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar um título de férias para busca
  de data de vencimento automaticamente
type: support-article
updated_at: '2025-07-15T20:33:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036119174-RH-Linha-Protheus-GPE-Como-configurar-um-t%C3%ADtulo-de-f%C3%A9rias-para-busca-de-data-de-vencimento-automaticamente
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33489917447575)**Tempo aproximado para leitura: 00:03:00 min

**Dúvida**Como configurar um título de férias para busca de data de vencimento automaticamente?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**Para configurar um título de férias, de modo que a busca de vencimento ocorra automaticamente de acordo com a gravação do cálculo das férias, siga o seguinte passo a passo:   
  
  
1. Acesse: Miscelânea -> Títulos -> Definição:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13430936738967)  
  
2. Selecione a opção "Definir título" e configure a verba de líquido de férias, busca na tabela SRR e Campo Data para filtro= RR\_DATAPAG:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13430940270615)  
  
  
3. Em seguida acesse: "Outras Ações" e "Informações para busca data de vencimento":   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13431036024471)  
  
4. Em "Informações para busca da data de vencimento do título", selecione o campo data para vencimento **RR\_DATAPAG** (este campo refere-se à data de recebimento das férias):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13431082389015)  
  
5. Com o cálculo das férias efetuado, o campo de busca será apresentado da seguinte forma:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13431296363415)  
Veja que os campos **SRH\_DTRECIB** e **SRR\_DATAPAG** apresentam a mesma data.   
  
6. Após configuração do título e cálculo das férias, acesse Miscelânea -> Títulos -> Geração e ajuste os parâmetros para geração:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13431395264023)  
  
Note que a data de vencimento está em branco, para que na geração busque a informação parametrizada na definição do título que neste exrmplo é a data de pagamento das férias:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13431432981527)

Obs: A configuração realizada dessa forma permite que seja gerado mais de um título de férias, respeitando as datas de pagamentos diferentes.  
  
7. Acesse Miscelânea -> Títulos -> Manutenção e verifique a geração de título com a data de pagamento definida:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13431491211031)  
  
  
**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
