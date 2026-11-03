---
article_id: 360035627974
category: Configurador
content_hash: cea7cb44ce8a2368141e6a1945ae7a6d573766bbcdd0e1c9bb3cfc78ce1b85c9
fetched_at: '2026-06-28T22:42:18.896429+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - TOTVS News não sendo exibido
type: support-article
updated_at: '2024-05-08T11:32:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035627974-Framework-Linha-Protheus-TOTVS-News-n%C3%A3o-sendo-exibido
---

**OCORRÊNCIA**Ao acessar o menu de um ou mais módulos do Protheus, o TOTVS News referente ao mesmo não é exibido.  
  
**AMBIENTE**Protheus – Framework – A partir da versão 12.1.17  
  
**CAUSA**As páginas do TOTVS News podem não ser exibidas devido a cinco cenários diferentes:

1. Bloqueio de firewall
2. LIB desatualizada e/ou Application Server desatualizado
3. Parâmetro MV\_PAISLOC com conteúdo inválido
4. Página inexistente para o módulo
5. Conteúdo da SYS\_APP\_PARAM divergente do novo padrão

**SOLUÇÃO**Segue abaixo a solução para cada um dos cinco cenários acima citados:

1. Bloqueio de firewall
   * Verifique por meio do navegador padrão se a URL <http://redirect.engpro.totvs.com.br/protheus[MOD_NAME][COUNTRY]> sendo aberta corretamente;
   * Para MOD\_NAME, insira o nome do módulo removendo o SIGA (ex: quando SIGACOM, utilize COM. Quando SIGALOJA, use LOJA);
   * Para COUNTRY, informe o valor referente ao pais corrente (ex: quando Brasil, utilize BRA)
   * Exemplo de URL: <http://redirect.engpro.totvs.com.br/protheuslojabra>;
   * Caso a URL não seja exibida corretamente ou o erro 404 (Not found) não ocorra, solicite ao responsável pela infraestrutura do servidor que contém o Application Server, a liberação da URL citada.
2. LIB desatualizada e/ou Application Server desatualizado  
   * Acesse o Portal de Downloads ([https://suporte.totvs.com/portal/p/10098/download](https://suporte.totvs.com/portal/p/10098/download#company/?cliente=)) e realize o download do último Application Server e LIB disponíveis;
   * Após isto, efetue a atualização do RPO com a LIB e a atualização do binário do Application Server.
3. Parâmetro MV\_PAISLOC com conteúdo inválido
   * O parâmetro MV\_PAISLOC é utilizado para realizar a montagem das URLs para exibição do TOTVS News, assim sendo, o mesmo deve estar conforme exemplo abaixo:  
     ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047303373)
   * Caso em sua empresa o arquivo SX6 não seja compartilhado (X6\_FILIAL diferente de vazio), verifique por meio da ferramenta APSDU todos os parâmetros MV\_PAISLOC para validar se todas estão com o conteúdo correto.
4. Página inexistente para o módulo  
   * Como citado o item 1, é possível que alguns módulos ainda não tenham TOTVS News disponível;
   * Isto posto, acessa a URL <http://redirect.engpro.totvs.com.br/protheus[MOD_NAME][COUNTRY]> para verificar se há página disponível;
   * Caso seja retornado o erro 404 (Not found), ainda não há TOTVS News para o módulo (vide abaixo):  
     ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047308733)
