---
article_id: 12757005282071
category: GPE - eSocial - Não Periódicos
content_hash: 5ade1b41daedbe7d8ee653579718fb391637aff0c6c339b66b048c091fcc4088
fetched_at: '2026-06-28T22:45:06.040710+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200 - Como enviar a admissão completa
  quando a admissão preliminar foi enviada por outro software
type: support-article
updated_at: '2023-02-28T23:17:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12757005282071-RH-Linha-Protheus-GPE-eSocial-S-2200-Como-enviar-a-admiss%C3%A3o-completa-quando-a-admiss%C3%A3o-preliminar-foi-enviada-por-outro-software
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como enviar a admissão completa quando a admissão preliminar foi enviada por outro *software*?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**A partir do leiaute simplificado S-1.0 não é mais enviado o numero do recibo da admissão preliminar, para realizar a baixa no portal do eSocial. O que amarra o colaborador da admissão completa com a preliminar são os dados idênticos entre os eventos S-2190 e S-2200.  
  
Quando a admissão preliminar foi enviada por outro software (sistema ou cadastrado diretamente pelo portal do eSocial) é primordial que seja mantido os mesmos dados enviados no evento S-2190 com o cadastro desse colaborador no GPE, para que quando realizada a transmissão da admissão completa não haja duplicidade no vínculo dentro do portal do eSocial.  
  
**Solução**Após cadastrar o funcionário no GPE, conferir se todos os dados informados são os mesmos que constam no S-2190 - Admissão Preliminar (CPF do Trabalhador, Data de Nascimento, Data de Admissão, Matricula eSocial, Categoria do Trabalhador no eSocial, Natureza da Atividade, CBO do Cargo, Valor do Salário, Unidade de Salário e Tipo de Contrato).  
  
Ao concluir o cadastro deste colaborador no GPE e integrar o S-2200, o sistema gera automaticamente uma matricula para o eSocial nos cadastro desse colaborado no GPE (Cód. Único - RA\_CODUNIC) e no TAF (Matricula C9V\_MATRIC). Essa matricula não será a mesma que já consta no portal do eSocial enviado pelo evento S-2190, sendo então necessário realizar o ajuste desses campos via banco de dados (esse processo não se enquadra no escopo de atendimento do suporte padrão). Somente após o ajuste da matricula, enviar o evento S-2200 para o eSocial.  
  
Abaixo segue um exemplo do formato do XML de transmissão de um evento da admissão preliminar e da admissão completa demonstrando os mesmos dados no S-2190 e S-2200:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12756558699415)

**Saiba Mais**Para saber mais consulte os *links*abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocia](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)
