---
article_id: 360038252953
category: Evento S-2220
content_hash: 73e786504476984114be4592ae526dd9b84133bd725b656459e2d4115aa6d5b3
fetched_at: '2026-06-28T22:45:25.478739+00:00'
product: protheus
section_id: 8260535758103
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2220 - Aviso "Não existem exames relacionados
  ou para os exames relacionados não foi indicado o campo 'Proc. Realiz' ou ainda
  o(s) exame(s) relacionado(s) não é(são) do tipo 'Ocupacional'"
type: support-article
updated_at: '2025-03-03T18:06:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038252953-RH-Linha-Protheus-MDT-eSocial-S-2220-Aviso-N%C3%A3o-existem-exames-relacionados-ou-para-os-exames-relacionados-n%C3%A3o-foi-indicado-o-campo-Proc-Realiz-ou-ainda-o-s-exame-s-relacionado-s-n%C3%A3o-%C3%A9-s%C3%A3o-do-tipo-Ocupacional
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372478655511)** Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Não existem exames relacionados ou para os exames relacionados não foi indicado o campo **'Proc. Realiz'** ou ainda o(s) exame(s) relacionado(s) não é(são) do tipo '**Ocupacional**'.**"** **Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões   
 **Causa**Após habilitar parâmetro **MV\_NG2ESOC** e efetuar cadastros no módulo SIGAMDT (medicina e segurança do trabalho) ou SIGAGPE (gestão de pessoal), o sistema passa a validar as informações para o eSocial. O sistema gera essa mensagem quando não possui informação no campo **Proc. Realiz** (TM4\_PROCRE) disponível no cadastro do exames. Essa informação é importante para geração do evento S-2220 Monitoramento da Saúde do Trabalhador.  
 **Solução**Deve ser relacionado ao menos um exame ao **Atestado ASO**, os exames relacionados devem possuir o campo Procedimento Realizado preenchido, que fica localizado no cadastro dos Exames no caminho (SIGAMDT): atualizações > PCMSO > exames.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049566114)  
  
Os exames relacionados devem ser do tipo **Ocupacional**, que é definido no cadastro de Exames por Funcionário no caminho (SIGAMDT): atualizações > PCMSO > exames do funcionário.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049566154)  
  
**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
