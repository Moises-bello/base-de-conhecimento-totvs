---
article_id: 26621890211735
category: eSocial - Gerar XML/ Integração Evento
content_hash: 22b14c68b3e28581abb8055de5f55e7666eebbcf035e4049246c92434e24ef43
fetched_at: '2026-06-28T22:47:11.949509+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao gerar o XML S-2230 ocorre o erro: O campo ''codMotAfast''
  do registro ''iniAfastamento'' é obrigatório e não está preenchido'
type: support-article
updated_at: '2024-09-25T17:59:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26621890211735-RH-RM-FOP-eSocial-Ao-gerar-o-XML-S-2230-ocorre-o-erro-O-campo-codMotAfast-do-registro-iniAfastamento-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26621890182807) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Ao gerar o XML S-2230 ocorre o erro: O campo 'codMotAfast' do registro 'iniAfastamento' é obrigatório e não está preenchido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26622468114071)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro ocorre quando o tipo de afastamento não consta mapeado pelo sistema e não consta cadastrado o De/Para de Afastamento.   
  
**Solução**O sistema possuí alguns motivos de afastamento já mapeados, de acordo com o eSocial, para que sejam gerados no codMotAfast. Para conferência dos motivos que serão gerados automaticamente [**CLIQUE AQUI**](https://tdn.totvs.com/display/public/LRM/Evento+S-2230).

Quando o motivo de afastamento cadastrado na folha, não é mapeado pelo sistema para que seja gerado conforme Tabela 18 do eSocial, é necessário: realizar o De/Para de afastamento eSocial **[CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056309114-RH-RM-FOP-eSocial-De-Para-de-afastamento-eSocial)**. Após realizar o de/para e regerar o XML, o erro será sanado.
