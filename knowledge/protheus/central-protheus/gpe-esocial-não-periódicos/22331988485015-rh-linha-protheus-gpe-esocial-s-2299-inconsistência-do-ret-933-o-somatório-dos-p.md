---
article_id: 22331988485015
category: GPE - eSocial - Não Periódicos
content_hash: d48a6c19c7b69e81d9b2f55d1fca60f9abd7fb94d53641ea14bf35a6022acf75
fetched_at: '2026-06-28T22:45:05.860896+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-2299 - Inconsistência do RET - 933
  - O somatório dos Proventos deve ser maior ou igual ao somatório dos Descontos no
  Demonstrativo de Pagamento '
type: support-article
updated_at: '2024-03-26T16:40:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22331988485015-RH-Linha-Protheus-GPE-eSocial-S-2299-Inconsist%C3%AAncia-do-RET-933-O-somat%C3%B3rio-dos-Proventos-deve-ser-maior-ou-igual-ao-somat%C3%B3rio-dos-Descontos-no-Demonstrativo-de-Pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22332018716439) Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida** S-2299 - Inconsistência do RET - 933 - O somatório dos Proventos deve ser maior ou igual ao somatório dos Descontos no Demonstrativo de Pagamento   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  Gestão de Pessoal - A partir da versão 12

**Causa**Esta inconsistência retornada pelo **eSocial** ocorre porque o valor total das **rubricas de** **Descontos** informados no S-2299 é maior do que o valor total das **rubricas de** **Proventos**.  
**Solução**Para a correção da mensagem de erro deverá ser realizada a seguinte conferência:  
**-** Gerar o [relatório de conferência do evento S-2299](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12927984951191-RH-Linha-Protheus-GPE-eSocial-S-2299-Como-gerar-o-relat%C3%B3rio-de-conferencia-do-evento-S-2299?source=search);  
- No relatório do evento S-2299 é possível filtrar as verbas de acordo com o Tipo. Sendo:

1 - Provento (vencimento)  
2 - Desconto  
3 - Base Provento (Informativa)  
4 - Base Desconto (Informativa Dedutora)  
  
Exemplo![](https://centraldeatendimento.totvs.com/hc/article_attachments/22331988480151)

- A somatória das verbas do tipo Desconto **NÃO** pode ser maior do que a somatória das verbas do tipo Provento.  
  
**Validações**:  
- caso seja identificado que existem mais Descontos do que Proventos, deve ser analisado o calculo, entender se os valores são devidos e, se o tipo da verba está correto, pois pode ser que houve um erro de cadastro;  
- se identificado erro no cadastro da (s) verba (s), deve ser realizado ajuste, envio do S-1010 com data igual ou anterior ao período de calculo, exclusão do evento S-2299 da base do TAF e uma nova integração do mesmo no GPE;  
- importante que seja revisado o cadastro das verbas relacionadas no Protheus e no RET (Governo), a fim de garantir que ambos estão iguais;  
  
  
**Saiba mais:**  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

**Próximos Treinamentos**

[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)

Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-BR/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
