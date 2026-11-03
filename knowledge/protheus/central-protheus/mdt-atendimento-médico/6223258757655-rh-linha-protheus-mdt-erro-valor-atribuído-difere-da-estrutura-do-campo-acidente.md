---
article_id: 6223258757655
category: MDT - Atendimento Médico
content_hash: 31a6c0bccfa66c3877b48e5b8f6cc8434ac23e8d8b9a1c697d58f1cf5cb832a4
fetched_at: '2026-06-28T22:44:20.707105+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Erro "Valor atribuído difere da estrutura do campo
  (acidente)"  quando informado o campo tipo de atendimento no cadastro Atestado Médico
type: support-article
updated_at: '2025-03-03T18:20:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6223258757655-RH-Linha-Protheus-MDT-Erro-Valor-atribu%C3%ADdo-difere-da-estrutura-do-campo-acidente-quando-informado-o-campo-tipo-de-atendimento-no-cadastro-Atestado-M%C3%A9dico
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372946512023)**Tempo aproximado para leitura:**00:02:00 min** **Ocorrência**Erro "Valor atribuído difere da estrutura do campo (acidente)" quando informado o campo tipo de atendimento (TNY\_OCORRE) no cadastro Atestado Médico.  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**Esse erro ocorre quando a consulta padrão (SBX) tem um registro incorreto ou falta de registro referente ao campo Ind. Atendimento (TNY\_OCORRE). Isso pode acontecer por motivo de manipulação de tabelas, ou algum problema na migração de dados / release ou também ocorre por conta do Dicionário de Dados (SX7). No campo TNY\_OCORRE dentro do configurador valide se esta conforme a imagem abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16948084479127)   
**Solução**  
A correção de validações de campos só ocorre por meio da atualização de dicionário. Nesse caso para correção execute em ambiente de homologação a atualização do ultimo dicionário diferencial (UPDDISTR) do modulo medicina e segurança do trabalho disponível na central de *downloads*.  
  
*Link*: [MP - MDT - Como fazer o download (baixar) do pacote de expedição continua (acumulado) do modulo medicina e segurança do trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057956773-MP-MDT-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-continua-acumulado-do-modulo-medicina-e-seguran%C3%A7a-do-trabalho?source=search)  
  
**Saiba Mais**[Artigos Atendimento Médico](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945694-MDT-Atendimento-M%C3%A9dico)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971487-RH-Medicina-e-Seguran%C3%A7a-do-Trabalho%20)  
[ChatBot Carol](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
