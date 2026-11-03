---
article_id: 1500002718542
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 68a76faefeecf0cb9fef5c4644f9126cb4b84458d660755d4d988547fe6d4bb8
fetched_at: '2026-06-28T22:42:11.622774+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Geração do
  Arquivo - Apuração Consolidada '
type: support-article
updated_at: '2022-08-17T20:30:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002718542-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Gera%C3%A7%C3%A3o-do-Arquivo-Apura%C3%A7%C3%A3o-Consolidada
---

**Dúvida**  
Ao configurar a Wizzard de geração do arquivo da DIME SC selecionando na tela inicial "Processamento da DIME SC" os parâmetros "Apuração Consolidada? = É estabelecimento consolidador" e "Seleciona Filiais = Não" o arquivo da DIME SC não é gerado.

**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**O erro da não geração do arquivo da DIME-SC mencionado acima só ocorre com a combinação abaixo:  
  
Se a pergunta "Apuração Consolidada? = É estabelecimento consolidador" e na tela inicial estiver configurado "Seleciona Filiais = Não".  
  
Considerando que a geração do arquivo consolidado necessita de informações das filiais e assim consolidar *estes dados*, não há como gerar um arquivo sem selecionar filiais.  
  
Para correta geração deste arquivo é imprescindível que a pergunta Seleciona Filiais esteja configurada como "Sim".
