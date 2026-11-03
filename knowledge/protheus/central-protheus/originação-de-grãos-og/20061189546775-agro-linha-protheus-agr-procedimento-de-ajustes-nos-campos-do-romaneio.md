---
article_id: 20061189546775
category: Originação de Grãos (OG)
content_hash: adbfb49a14567e81ea16de5f3387f678567ebbbf9513c19d1a1d72071ecc7def
fetched_at: '2026-06-28T22:45:43.371951+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Procedimento de ajustes nos campos do romaneio
type: support-article
updated_at: '2025-06-23T20:09:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20061189546775-Agro-Linha-Protheus-AGR-Procedimento-de-ajustes-nos-campos-do-romaneio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20061205510423) Tempo aproximado para leitura: **00:01:15 min****Ocorrência**  
No módulo **Comercialização (Linha Protheus) - Originação de Grãos (OG)**, ao realizar o processo para saber os campos que devem ser reposicionados no romaneio é apresentada a mensagem **Ajustes nos campos do romaneio**.  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**Esse incidente ocorre, pois é necessário realizar o processo para saber os campos que devem ser reposicionados no romaneio.  
  
**Solução**  
Para solucionar essa ocorrência, foram criados novos campos no cadastro de **Romaneio com Pesagem - OGA250** e **Romaneio sem Pesagem - OGA251**. Caso este pacote seja executado após a implantação do sistema, estes campos devem ser **reposicionados** manualmente via configurador.   
Para tanto, após executar o **atualizador do dicionário de dados -** **upddistr**, acesse o configurador, edite a tabela **Romaneio - NJJ** e **reposicione** os campos **NJJ\_MOEGA**, **NJJ\_DESMOE**, **NJJ\_CULTIV**, **NJJ\_DESCTV** de forma que eles fiquem logo após o campo de unidade de medida:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20061189536663)

O preenchimento dos campos de produto, moega e cultivar vai gerar um gatilho para o campo local, justamente por isto é necessário que seja feita essa alteração na **posição** dos campos.
