---
article_id: 33231021284631
category: SIGAEST - LEGAIS
content_hash: 458ec54a438c3f5cfa5f93be851084781b5ad9ccfc371ccbad9a197dd91ed83d
fetched_at: '2026-06-28T22:38:51.908376+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - SPEDFISCAL: erro
  na inclusão TR2 - TOP Error -19 - Invalid bind parameter size 4096'
type: support-article
updated_at: '2026-03-30T18:09:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33231021284631-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-SPEDFISCAL-erro-na-inclus%C3%A3o-TR2-TOP-Error-19-Invalid-bind-parameter-size-4096
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33231021246487) Tempo aproximado para leitura: **00:05:00min**  
  
**Ocorrência**  
Ao tentar gerar o SPEDFISCAL, o sistema apresenta erro na inclusão TR2: TOP Error -19 - Invalid bind parameter size 4096.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.2310 ou Superior.  
  
**Causa**  
Este tipo de cenário está comumente relacionado à não configuração correta do ODBC para utilização de bancos PostgreSQL. Abaixo seguem algumas validações para a solução do erro.  
  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Junto à sua equipe de TI verifique se o ambiente em questão utiliza banco PostgreSQL. Isso também é possível validar efetuando a busca do termo "TOTVS DBAccess DB" no erro gerado. Conforme a print abaixo:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/33231034718103)
2. Verifique a versão do seu banco e a versão do seu ODBC para confirmar se estão de acordo com a documentação abaixo, bem como com a observação na captura de tela.  
     
   <https://tdn.totvs.com/display/tec/DBAccess+-+Banco+de+dados>  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/33231021250967)
3. Verifique se a sua configuração do ODBC está de acordo com a documentação abaixo para o seu sistema operacional.

   [Windows - Como criar uma fonte de dados ODBC para uso com PostgreSQL](https://tdn.totvs.com/display/tec/DBAccess+-+Como+fazer+para+criar+uma+fonte+de+dados+para+uso+com+o+PostgreSQL+-+Windows)  
   [LINUX - Como criar uma fonte de dados ODBC para uso com PostgreSQL](https://tdn.totvs.com/display/tec/DBAccess+-+Como+fazer+para+criar+uma+fonte+de+dados+para+uso+com+o+PostgreSQL+-+Linux)
4. Verifique também se seu ambiente possui o fonte MATXSPED a partir da versão 04/03/2026, e caso não esteja, aplicar o patch abaixo num ambiente de homologação, conforme sua versão:  
   12.1.2310:<https://r.totvs.io/p/1241751> ;   
   12.1.2410:<https://r.totvs.io/p/1241749> ;   
   12.1.2510:<https://r.totvs.io/p/1241750> ;
5. Caso o erro persista após validar todos os passos acima, por favor, nos envie:

   - Qual a versão do  seu Banco Postgres;   
   - Qual a versão do driver está utilizando em seu ODBC;  
   - Qual seu sistema Operacional e Prints das configurações do ODBC destacando os pontos informados link do **ponto 3**  
   - Nos envie os dados do seu ambiente em nossa central de diagnósticos, conforme ([Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como enviar dados pela Central de Diagnóstico?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33711098138007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-enviar-dados-pela-Central-de-Diagn%C3%B3stico)), e nos informe o ID da central;

**Saiba mais:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Bloco K- Conceito e configurações mínimas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421126537879-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Bloco-K-Conceito-e-configura%C3%A7%C3%B5es-m%C3%ADnimas)  
[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Guia do Bloco H do SPED Fiscal no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059965954-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Guia-do-Bloco-H-do-SPED-Fiscal-no-Protheus)  
[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
