---
article_id: 360058886033
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: fb988aea4d5d655cb47e215b0db8f779b435544c1c0ab023e384f19ec7be4a57
fetched_at: '2026-06-28T22:42:47.230668+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: MP - SIGAPCP - Mensagem A09ERRCOD ao deixar uma família de produtos disponível
  para uso
type: support-article
updated_at: '2020-12-07T17:55:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058886033-MP-SIGAPCP-Mensagem-A09ERRCOD-ao-deixar-uma-fam%C3%ADlia-de-produtos-dispon%C3%ADvel-para-uso
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:10 min**  
**Ocorrência**Na rotina **MATA093 - Configuração**, quando é especificado que um produto não possui código padrão, através do conteúdo do campo **BP\_CODPAD - Cod Padrao** com o conteúdo **Não** e se disponibiliza a família para uso, preenchendo no campo **BP\_DISPUSO - Disp. p/ Uso** o conteúdo **Sim**, o Sistema apresenta a mensagem **A09ERRCOD - Alguma característica foi omitida na expressão do código do produto**  
  
**Ambiente**Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
  
**Causa**Quando se preenche no campo **BP\_CODPAD**, o Sistema não monta o **código do produto** final através de uma concatenação do **código da família** e as características selecionadas, mas é necessário que se determine de que forma essa informação deve ser preenchida.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Na rotina **MATA093** seleciona a **família**;  
2. Clique em **Outras Ações** e em seguida em **Descrição**;  
3. Preenchendo o campo **BP\_ESTCOD - Resultado - Estrutura do Código**, descreva de que maneira o **código do produto** deve ser preenchido, lembrando que todas as características devem ser adicionadas;  
4. Ao concluir edite novamente a família e preencha o campo **BP\_DISPUSO** com o conteúdo **Sim**.
