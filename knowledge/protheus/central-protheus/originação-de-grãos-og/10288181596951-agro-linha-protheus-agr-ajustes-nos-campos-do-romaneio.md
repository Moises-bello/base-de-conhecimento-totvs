---
article_id: 10288181596951
category: Originação de Grãos (OG)
content_hash: 81070b222e46651ca1479e49e29552234fd1f51c59ddb996857cada5f82d0539
fetched_at: '2026-06-28T22:45:36.954372+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ajustes nos campos do romaneio
type: support-article
updated_at: '2025-01-09T19:50:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10288181596951-Agro-Linha-Protheus-AGR-Ajustes-nos-campos-do-romaneio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20054640038295) Tempo aproximado para leitura: **00:00:30 min** **Dúvida**Quais os campos que devem ser **reposicionados** no **Romaneio**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Oxiginação de Grãos (OG) - Versão 12  
  
**Solução**Foram criados novos campos no cadastro de **Romaneio com Pesagem - OGA250** e **Romaneio sem Pesagem - OGA251**. Caso este pacote seja executado após a implantação do sistema, estes campos devem ser **reposicionados** manualmente via configurador.   
Para tanto, após executar o **atualizador do dicionário de dados -** **upddistr**, acesse o configurador, edite a tabela **Romaneio - NJJ** e **reposicione** os campos **NJJ\_MOEGA**, **NJJ\_DESMOE**, **NJJ\_CULTIV**, **NJJ\_DESCTV** de forma que eles fiquem logo após o campo de unidade de medida:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10287916120471)

O preenchimento dos campos de produto, moega e cultivar vai gerar um gatilho para o campo local, justamente por isto é necessário que seja feita essa alteração na **posição** dos campos.
