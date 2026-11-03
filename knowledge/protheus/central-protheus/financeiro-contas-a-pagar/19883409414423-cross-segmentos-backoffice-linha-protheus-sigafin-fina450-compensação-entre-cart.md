---
article_id: 19883409414423
category: Financeiro - Contas a Pagar
content_hash: 0bccf04a03f42b362bafc2e3f15ba9148dd4492dad33c863ae79a892773c3b66
fetched_at: '2026-06-28T22:38:09.700096+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA450 - Compensação
  entre Carteiras - HELP:A450PERM
type: support-article
updated_at: '2023-12-15T20:27:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19883409414423-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA450-Compensa%C3%A7%C3%A3o-entre-Carteiras-HELP-A450PERM
---

**Ocorrência**Ao realizar o processo de Compensação entre Carteiras, como também durante a execução do execauto FINA450, operação de estorno, é retornado a mensagem de HELP: **A450PERM**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA450 - Todas as versões  
  
**Causa**O retorno da mensagem com o help ocorre, quando o usuário não tem acesso para alterar dados de outras filiais  
   
Durante o processo é validada a xFilial da tabela SE2, que não pode estar em branco (se seu compartilhamento = exclusivo) e validado também se usuário tem o acesso de alterar dados de outras filias(Acesso 115).  
   
**Solução**Acessar o ambiente Configurador - Usuários - Cadastro de Usuários - aba Restrição de Acesso e habilitar a opção 115 - Mbrowse - Edita Registros de outras filiais.
