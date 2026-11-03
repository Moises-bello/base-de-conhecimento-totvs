---
article_id: 6907901652247
category: eSocial - Tabelas/Não Periódicos
content_hash: ebdd8c9b7772935a390706d2d3162fedda170a4fdb071581386ef594041c0ce7
fetched_at: '2026-06-28T22:47:10.410221+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro código 116: Código de treinamento/capacitação
  inválido'
type: support-article
updated_at: '2022-06-20T19:10:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6907901652247-RH-RM-FOP-eSocial-Erro-c%C3%B3digo-116-C%C3%B3digo-de-treinamento-capacita%C3%A7%C3%A3o-inv%C3%A1lido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao transmitir os eventos S-2200 e/ou S-2206 para o governo é retornado a inconsistência **Erro código 116: Código de treinamento/capacitação inválido. Ação Sugerida: O valor informado no campo devera existir na Tabela 29 (Treinamentos e capacitações).**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6907314398231/mceclip0.png)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Conforme mensagem apresentada, a inconsistência geralmente é apresentada quando no evento S-2200 e/ou S-2206 foi enviado um código de treinamento incorreto.   
  
**Solução**Foi liberado em 15/06/2022 a [Nota Técnica S-1.0 05/2022](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-0-05-2022.pdf) que **exclui** da **Tabela 28 - Treinamentos, Capacitações, Exercícios Simulados e Outras Anotações** todos os códigos iniciados por **37XX**:

![image.png](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AAUuIGuu8ZT0E0amuQlvgzhQq8WEbO9%2FhwWFYpenVGZQshc2zZqegqJzhAdorkam3ATa%2BOqeZ1AXiI9JECw6ZbBhcYEVEXJvg391C3WA7FDDFurFnq2%2FtsH%2Fdr8dkJ6EE3xZtBlFpmGFd50%2FJmykPfQjpHMP4jj8Nnv6%2BKB9DClZpEYqsNM0lp9kKUdVf1S62e3chqdI61bw%2FR3o9Vdk756k0Ya5VFv3X3FdBDNR33vTY8%2FidVjoWpkMBqAGjEZuKlmGK7L%2Bfdk3Jm3OpoEHpHK5Cq%2B6KisyxXPKlw8O5KLxY4d2VZ%2BDZx0DSW6MZ%2BxR2TuDDOJyth77%2FWl0HoVYV8nBHSvQbhKJS9rcUetdeWsU0gxDE9UuKxfrKokSlxszi6n68pibWnQd%2FisoP%2B9DbDjzCJwKHkiA%2Bbj6r%2BA%3D&sz=w512)

Sendo assim, para ajuste realize os passos abaixo:

1. Acesse o menu **RH | Gestão de Pessoas | Desenvolvimento | Cursos** e faça a edição do curso relacionado;  
2. No campo **Código do Treinamento eSocial** informe o código **1006** ou **1207**, que são os aceitos pelo governo a partir da **NT 05/22** e salve o cadastro;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6907479003415/mceclip1.png)

3. Após ajuste do curso, gere novamente o XML e faça a transmissão para o governo.

**Saiba mais**  
Para mais informações, acesse:  
- [Documentação Técnica](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)
