---
article_id: 8659127787031
category: Evento S-2220
content_hash: 3bb2df5debe28b63c4a78ac901a7e357c52a29ba1f8990d5f124200be9193d3f
fetched_at: '2026-06-28T22:45:25.524637+00:00'
product: protheus
section_id: 8260535758103
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2220 - Não existem exames do tipo ocupacionais
  relacionados ao aso
type: support-article
updated_at: '2025-03-03T18:16:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8659127787031-RH-Linha-Protheus-MDT-eSocial-S-2220-N%C3%A3o-existem-exames-do-tipo-ocupacionais-relacionados-ao-aso
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372805446295) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Após habilitar o parâmetro **MV\_NG2ESOC** e incluir um Atestado ASO no módulo SIGAMDT, o sistema passa a validar as informações para o eSocial e quando identifica alguma divergência é apresentado mensagem:  
**"Não existem exames do tipo ocupacional relacionado ao aso".**  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as Versões  
  
**Solução**  
Verifique as configurações destacadas abaixo.  
   
No cadastro de Exames (Atualizações > PCMSO > Exames) deve ter o campo "Procedimento Diagnóstico" (TM4\_PROCRE).  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8658794446231)  
  
No cadastro de Exames do Funcionário (Atualizações > PCMSO > Exames do Funcionário), deve ser verificado o preenchimento dos campos abaixo:  
"Origem Exame" (TM5\_ORIGEX), "Obs. Resultado" (TM5\_OBSERV) e "Data Resultado" (TM5\_DTRESU).  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8658971826327)  
  
Ao incluir o Atestado ASO (Atualizações > Atendimento Médico > Atestado (ASO)), o campo "Data Emissão" (TMY\_DTEMIS) deve ficar vazio, pois é preenchido automaticamente ao imprimir o ASO.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8659109610135)  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
