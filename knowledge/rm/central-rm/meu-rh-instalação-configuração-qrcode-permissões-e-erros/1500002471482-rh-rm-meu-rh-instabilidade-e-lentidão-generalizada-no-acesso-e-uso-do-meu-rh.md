---
article_id: 1500002471482
category: Meu RH - Instalação, configuração, qrcode, permissões e erros
content_hash: 93890b2fb02fe2662ca36c03f6935d67b98b13a9eee10b9f37db97bf87746aa1
fetched_at: '2026-06-28T22:47:29.537650+00:00'
product: rm
section_id: 1500000961062
source: central-rm
title: RH - RM - Meu RH - Instabilidade e lentidão generalizada no acesso e uso do
  Meu RH
type: support-article
updated_at: '2025-03-12T12:57:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002471482-RH-RM-Meu-RH-Instabilidade-e-lentid%C3%A3o-generalizada-no-acesso-e-uso-do-Meu-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24078468447767) Tempo aproximado para leitura: 00:04:42 min**

**Ocorrência**

 Ao acessar o Meu RH ocorrem problemas de lentidão, erros na tentativa de login e até queda no host.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir do release 12.1.27  
  
**Causa**  
Esse incidente pode ocorrer, pois o coluna  CODIGOPAI e CODIGO da tabela PSECAO , estão com o mesmo identificador, causando uma queda repentina do Host ou instabilidade / lentidão no Meu RH.  
  
**Solução**

**1º Passo -** Execute a consulta abaixo para identificar as coligadas que apresentam o problema.  
  
 SELECT CODCOLIGADA, COUNT(\*)

FROM PSECAO WHERE CODIGOPAI = CODIGO

GROUP BY CODCOLIGADA  
  
**2º Passo -** Execute a rotina "Manutenção do Cadastro de Seções" em todas  coligadas que retornaram na consulta. Acesse o menu "Executar" do RM e pesquise pela rotina "Manutenção do Cadastro de Seções"

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11123177786903)  
  
**3º Passo -** Selecione a rotina de manutenção do cadastro de seções e confira se sua execução foi realizada com sucesso.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11123182015895)  
  
Esta rotina vai realizar ajustes na coluna PSECAO.CODIGOPAI, para correção do problema de instabilidade no acesso ao Meu RH.  
  
**Importante**

A rotina "Manutenção de Seção" **não causa nenhum impacto negativo**, poderá ser sempre executada caso suspeite de instabilidades no Meu RH e preferencialmente sempre executá-la caso houver inclusão / alteração / exclusão de seções no cadastro de seções da Folha de Pagamento.
