---
article_id: 360018252251
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: f0016758bbf3fd01b4df7c8c0b57466434188238e0125b71db129747ec2643a2
fetched_at: '2026-06-28T22:42:07.877506+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T013
  Conta Contábil C20_CODCTA inexistente
type: support-article
updated_at: '2022-08-18T17:39:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018252251-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T013-Conta-Cont%C3%A1bil-C20-CODCTA-inexistente
---

**Dúvida**  
O valor '6101030200' informado na coluna 17 para o campo Cod Conta Contábil (**C20\_CODCTA**) não existe na base de dados.  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, quando a conta contábil utilizada não existe na tabela **C1O - Plano de Contas** do TAF.   
  
Este item é levado para o TAF, através da extração do *Layout* **T010 - Plano de Contas.****Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o Extrator Fiscal;  
2. Configure as perguntas:   
  
**"Deseja integrar:" =** **Somente Cadastros**;

**"Filtra Apenas Reinf"** = **Não**

3. Selecione o *Layout* **T010 - Plano de Contas e T011 - Centro de custo** e confirme a extração;  
4. Acesse o módulo **TOTVS Automação Fiscal** -> Miscelânea -> Integração -> Processamentos para processar os dados extraídos;  
5. Confirme na tela do gerenciador de integração se houveram inconsistências na importação do *Layout*;   
6. Acesse o gerenciador de integração e posicione o cursor no registro que houve   
inconsistência e acione as opções: Outras Ações -> Habilitar Re-integração para que  
o registro que obteve a inconsistência seja integrado novamente ao TAF.
