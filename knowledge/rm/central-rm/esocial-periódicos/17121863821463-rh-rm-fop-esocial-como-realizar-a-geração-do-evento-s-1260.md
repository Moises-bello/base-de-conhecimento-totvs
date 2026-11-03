---
article_id: 17121863821463
category: esocial - Periódicos
content_hash: 8c9eaf5ebee7d6dbf8a949bdc11faecc8ee6d5d19a0b1327f09cd3fb80c98881
fetched_at: '2026-06-28T22:47:09.225101+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Como realizar a geração do evento S-1260?
type: support-article
updated_at: '2026-01-22T22:03:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17121863821463-RH-RM-FOP-eSocial-Como-realizar-a-gera%C3%A7%C3%A3o-do-evento-S-1260
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17121825636503)Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como realizar a geração do evento S-1260?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões.  
  
**Solução**  
Para realizar a geração dos eventos S-1260, evento que contém as informações relativas à comercialização da produção rural prestadas pelo produtor rural pessoa física e pelo segurado especial, siga os seguintes passos:

1. Lançar a movimentação no módulo **Gestão de estoque, compras e faturamento**. Esse evento só é gerado considerando o lançamento da nota com as tributações FUNRURAL, GILRAT e SENAR atribuídas à ela;

2. Após gerar o XML no módulo **Folha de Pagamento**em **eSocial - Gerar XML**.

![](https://tdn.totvs.com/download/attachments/479829336/image2018-9-11_12-33-25.png?version=1&modificationDate=1555107095437&api=v2)

![](https://tdn.totvs.com/download/attachments/479829336/image2019-4-17_15-1-2.png?version=1&modificationDate=1555524062437&api=v2&effects=border-simple,shadow-kn)

**Importante**  
Esse evento apenas será gerado, quando a coligada respeitar as seguintes  condições:

* Possuir o parâmetro **Produtor Rural** marcado em seu cadastro;
* For identificada por **CPF**;
* Possuir **Classificação Tributária igual a 21 ou 22** nas Informações do Empregador.

**Saiba mais**  
Para mais informações acesse:

* [Cross Segmentos - TOTVS BackOffice Linha RM - TOTVS Gestão de Estoque, Compras e Faturamento - MOV - Apuração de Tributos - FUNRURAL, GILRAT, SENAR \ INSS, INSS15, INSS20, INSS25;](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003850232-Cross-Segmentos-TOTVS-BackOffice-Linha-RM-TOTVS-Gest%C3%A3o-de-Estoque-Compras-e-Faturamento-MOV-Apura%C3%A7%C3%A3o-de-Tributos-FUNRURAL-GILRAT-SENAR-INSS-INSS15-INSS20-INSS25)
* [Cadastro de Coligada;](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13606359301399-RH-RM-FOP-Cadastro-de-Coligada)
* [Mapeamento do evento](https://tdn.totvs.com/display/LRM/Evento+S-1260).
