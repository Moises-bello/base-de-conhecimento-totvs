---
article_id: 360018601511
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 4658aa480cd0c0877d48a758f254171878bfe12fd6b06e65f9a638e8198d27eb
fetched_at: '2026-06-28T22:42:07.894740+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T013
  Número da Declaração C4F_NRODE inexistente
type: support-article
updated_at: '2022-08-18T17:43:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018601511-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T013-N%C3%BAmero-da-Declara%C3%A7%C3%A3o-C4F-NRODE-inexistente
---

**Ocorrência**Erro 1 - Linha: 1- Coluna: 3 - Campo obrigatório não informado: Número da Declaração (**C4F\_NRODE**)  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, pois o número da declaração de exportação não foi informado no cadastro de origem do dado.   
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse a rotina **Nota fiscal manual de saída**, posicione o cursor sobre a nota e acione as opções **Outras Ações -> Complemento -> Exportação** e preencha o campo **Num Dec (CDL\_NUMDE)**;  
2. Acesse o Extrator Fiscal;  
3. Responda a pergunta: **"Deseja integrar:" igual a 1-Somente Cadastros;**  
4. Selecione o *Layout***T013- Documento Fiscal**e confirme a extração;  
5. Acesse o módulo **TOTVS** **Automação Fiscal -> Miscelânea -> Integração -> Processamentos** para processar os dados extraídos;  
6. Confirme na tela do gerenciador de integração se houveram inconsistências na importação do *Layout.*7. Acesse o gerenciador de integração e posicione o cursor no registro que houve   
inconsistência e acione as opções: Outras Ações -> Habilitar Re-integração para que  
o registro que obteve a inconsistência seja integrado novamente ao TAF.

**Importante**

Caso a nota seja originada do módulo **SIGAEEC**, o número da declaração de exportação deverá ser preenchido no respectivo módulo de origem.
