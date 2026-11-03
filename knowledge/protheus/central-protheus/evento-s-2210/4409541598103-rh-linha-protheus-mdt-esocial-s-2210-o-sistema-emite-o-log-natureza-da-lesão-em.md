---
article_id: 4409541598103
category: Evento S-2210
content_hash: ba6eaa6b14f4e6cc8413220e845cb8eb11a590db05d479d4e79d219d2f9cc7cc
fetched_at: '2026-06-28T22:45:24.506017+00:00'
product: protheus
section_id: 8260521640983
source: central-protheus
title: 'RH - Linha Protheus - MDT - eSocial - S-2210 - O sistema emite o log "Natureza
  da Lesão: Em branco" ao tentar gerar a CAT com o evento S-2210 (Comunicação de Acidentes
  de Trabalho). Ou log "Deve ser um código valido e existente na tabela 17"'
type: support-article
updated_at: '2025-03-03T18:03:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409541598103-RH-Linha-Protheus-MDT-eSocial-S-2210-O-sistema-emite-o-log-Natureza-da-Les%C3%A3o-Em-branco-ao-tentar-gerar-a-CAT-com-o-evento-S-2210-Comunica%C3%A7%C3%A3o-de-Acidentes-de-Trabalho-Ou-log-Deve-ser-um-c%C3%B3digo-valido-e-existente-na-tabela-17
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372360684951) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**O sistema emite o log "**Natureza da Lesão: Em branco**" ao tentar gerar a CAT com o evento S-2210 (Comunicação de Acidentes de Trabalho). Ou log "Deve ser um código valido e existente na **tabela 17** do eSocial".  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**Isso ocorre quando o sistema está fazendo integração com o eSocial para geração do evento S-2210 (Acidente de Trabalho) e o código eSocial do campo Natureza da Lesão não foi preenchido, ou não está com o campo código de acordo com a tabela 17 do eSocial.  
  
**Solução**1. Acesse no modulo SIGAMDT o caminho: **atualizações > Acidente Trabalho > Natureza de Lesão** (MDTA604). Nessa rotina é necessario que esteja cadastrado a parte do corpo atingida com o campo **Cod. eSocial** (TOJ\_ESOC) preenchido.  
![natureza_lesao.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4409541527703)  
  
2. O campo **Cod. eSocial** (TOJ\_ESOC) deve ser com um código valido de acordo com a tabela 17 do eSocial.   
Para que o sistema esteja com as tabelas do eSocial é necessario estar atualizado com os pacotes de acumulado e expedição continua disponíveis na página **Entregas Legais**. Link:  
 [**https://tdn.totvs.com/x/4JQYEw**.](https://tdn.totvs.com/x/4JQYEw)   
E também caso efetue a integração com o TAF é necessario fazer o processo de atualização de autocontidas no TAF.  
  
3. Após preencher esses campos ao cadastrar a CAT no caminho: **atualizações > Acidente Trabalho > Acidentes** (MDTA640), preencha o campo Natur. Lesão (TNC\_CODLES).  
![2021-09-27_14-28-17.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4409548412183)  
  
**Observação**  
Os código de tabelas do eSocial podem ser consultados no link: <https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica>.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372375504023)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372375504919)  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
