---
article_id: 4409540632215
category: Evento S-2210
content_hash: 065aeb76e86e010e9bad9c54f7f6f28ff1257793b625f64adf423f4fe10d4a3e
fetched_at: '2026-06-28T22:45:24.510439+00:00'
product: protheus
section_id: 8260521640983
source: central-protheus
title: 'RH - Linha Protheus - MDT - eSocial - S-2210 - O sistema emite o log "Parte
  do Corpo Atingida: Em branco" ao tentar gerar a CAT com o evento S-2210 (Comunicação
  de Acidentes de Trabalho). Ou log "Deve ser um código valido e existente na tabela
  13"'
type: support-article
updated_at: '2023-12-21T17:21:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409540632215-RH-Linha-Protheus-MDT-eSocial-S-2210-O-sistema-emite-o-log-Parte-do-Corpo-Atingida-Em-branco-ao-tentar-gerar-a-CAT-com-o-evento-S-2210-Comunica%C3%A7%C3%A3o-de-Acidentes-de-Trabalho-Ou-log-Deve-ser-um-c%C3%B3digo-valido-e-existente-na-tabela-13
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20033613876887) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**O sistema emite o log "**Parte do Corpo Atingida: Em branco**" ao tentar gerar a CAT com o evento S-2210 (Comunicação de Acidentes de Trabalho). Ou log "Deve ser um código valido e existente na **tabela 13** do eSocial".  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**Isso ocorre quando o sistema está fazendo integração com o eSocial para geração do evento S-2210 (Acidente de Trabalho) e o código eSocial da parte do corpo atingida não foi preenchido, ou não está com o campo código de acordo com a tabela 13 do eSocial.  
  
**Solução**1. Acesse no modulo SIGAMDT o caminho: **atualizações > Acidente Trabalho > Parte do Corpo Atingida** (MDTA603). Nessa rotina é necessario que esteja cadastrado a parte do corpo atingida com o campo **Cod. eSocial** (TOI\_ESOC) preenchido.  
![parte_corpo.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4409540320023)  
  
2. O campo **Cod. eSocial** (TOI\_ESOC) deve ser com um código valido de acordo com a tabela 13 do eSocial.   
Para que o sistema esteja com as tabelas do eSocial é necessario estar atualizado com os pacotes de acumulado e expedição continua disponíveis na página **Entregas Legais**. Link:  
 [**https://tdn.totvs.com/x/4JQYEw**.](https://tdn.totvs.com/x/4JQYEw)   
E também caso efetue a integração com o TAF é necessario fazer o processo de atualização de autocontidas no TAF.  
  
3. Após preencher esses campos ao cadastrar a CAT no caminho: **atualizações > Acidente Trabalho > Acidentes** (MDTA640), preencha o campo Código Parte (TYF\_CODPAR) e Lateralidade (TYF\_LATERA).  
![acidadente_parte_corpo.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4409540286231)  
  
**Observação**  
Os código de tabelas do eSocial podem ser consultados no link: <https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica>.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409538262807)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409539753367)  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
