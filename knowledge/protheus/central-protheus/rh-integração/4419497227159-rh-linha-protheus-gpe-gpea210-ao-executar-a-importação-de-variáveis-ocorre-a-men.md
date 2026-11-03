---
article_id: 4419497227159
category: RH - Integração
content_hash: 911deeec9c720ff7d36dd983af75dd21d6b75170d9581f9335b2b800f142bb47
fetched_at: '2026-06-28T22:43:44.954569+00:00'
product: protheus
section_id: 360003115611
source: central-protheus
title: 'RH - Linha Protheus - GPE - GPEA210 - Ao executar a importação de variáveis
  ocorre a mensagem: Condição do código não está retornando valor lógico'
type: support-article
updated_at: '2025-09-11T12:10:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419497227159-RH-Linha-Protheus-GPE-GPEA210-Ao-executar-a-importa%C3%A7%C3%A3o-de-vari%C3%A1veis-ocorre-a-mensagem-Condi%C3%A7%C3%A3o-do-c%C3%B3digo-n%C3%A3o-est%C3%A1-retornando-valor-l%C3%B3gico
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28432028719383)** Tempo aproximado para leitura: **00:01:00** min**Ocorrência**Ao executar a **importação de variáveis - GPEA210**, ocorre a mensagem: **Condição do código não está retornando valor lógico**  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Esse incidente ocorre, pois falta informar a **condição de gravação** do registro na rotina de **Layout de Importação**  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse a rotina **Atualizações -> Def. de Cálculo -> Layout de Importação - GPEA200**;  
2. Selecione o código do **Layout que está tentando importar** e clique em **Editar**;  
3. Altere o campo **Cond. Gravação Registro,** informe o conteúdo **.T.** e clique em Confirmar; **![](https://centraldeatendimento.totvs.com/hc/article_attachments/28432049248151)**4. Após isso, acesse novamente a rotina de Importação de Variáveis - GPEA210, e faça a importação onde a mesma deve ser gerada com sucesso.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28432049249047)

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Importação de variáveis tabela RGB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058289233-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-tabela-RGB?source=search)  
[RH - Linha Protheus - GPE - Importação de variáveis tabela RHO - Coparticipação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5743820814487-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-tabela-RHO-Coparticipa%C3%A7%C3%A3o?source=search)  
[RH - Linha Protheus - GPE - Importação de variáveis tabela SRK](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000579482-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-tabela-SRK?source=search)
