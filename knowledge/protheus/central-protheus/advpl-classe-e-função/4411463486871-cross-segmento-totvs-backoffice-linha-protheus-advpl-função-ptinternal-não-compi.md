---
article_id: 4411463486871
category: ADVPL - Classe e Função
content_hash: 0b88876b656203f598f6ff73becbbfc370450e95693cc10f39d10d9730970e77
fetched_at: '2026-06-28T22:40:14.173185+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Função PTINTERNAL()
  não compila/mudou o comportamento
type: support-article
updated_at: '2022-03-18T19:54:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411463486871-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-PTINTERNAL-n%C3%A3o-compila-mudou-o-comportamento
---

**Ocorrência**Utilizo a função PTINTERNAL() mas não está compilando ou teve seu comportamento alterado.  
  
**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) – ADVPL – A partir da versão 12.1.33  
  
**Causa**Funções, classes e variáveis restritas em fontes customizados não estão previstas pelo suporte padrão, dado ao fato de que as mesmas não estão documentadas, assim sendo, podem vir a ser descontinuadas ou sofrer alterações de comportamento sem prévio aviso.  
A função PTINTERNAL() é de uso interno e restrito, para ações específicas, por isso não existe documentação oficial sobre ela ou recomendação de uso da mesma.  
  
**Solução**Caso o uso seja específico de PTINTERNAL( 1, <msg>), que é usado para dar uma mensagem no console do monitor, pode-se usar a função **[FWMONITORMSG](https://tdn.totvs.com/display/framework/FWMonitorMsg)**(<cMsg>).

**Saiba mais**  
[Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Funções, classes e variáveis de propriedade interna](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016461772)  
[FWMonitorMsg](https://tdn.totvs.com/display/framework/FWMonitorMsg)
