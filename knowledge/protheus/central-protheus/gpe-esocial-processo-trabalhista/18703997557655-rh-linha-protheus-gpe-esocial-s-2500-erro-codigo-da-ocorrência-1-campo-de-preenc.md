---
article_id: 18703997557655
category: GPE - eSocial - Processo Trabalhista
content_hash: 0dbecab990474021f8d3423a23eb0d8ea92aa70f808fb3da07ecb0a0bad5237a
fetched_at: '2026-06-28T22:45:00.576661+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-2500 - Erro - Codigo da ocorrência:
  1 - Campo de preenchimento obrigatorio: Matricula atribuida ao trabalhador'
type: support-article
updated_at: '2023-10-31T19:30:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18703997557655-RH-Linha-Protheus-GPE-eSocial-S-2500-Erro-Codigo-da-ocorr%C3%AAncia-1-Campo-de-preenchimento-obrigatorio-Matricula-atribuida-ao-trabalhador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18703985836439) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Localização: /eSocial/evtProcTrab/ideTrab/infoContr/matriculaErro - Codigo da ocorrência: 1 - Campo de preenchimento obrigatorio: Matricula atribuida ao trabalhador  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O eSocial retorna a ocorrência 1, pois na validação do leiaute vigente a Matricula é um campo obrigatório. **Se [indContr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/index.html#2500_ideTrab_infoContr_indContr) = [N]**, deve ser criada uma matrícula para o trabalhador.  
**Se [indContr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/index.html#2500_ideTrab_infoContr_indContr) = [S]**, deve corresponder à matrícula informada pelo empregador no evento S-2190, S-2200, S-2300 ou S-8200 do respectivo contrato. O **campo não deve ser informado** somente no **caso de TSVE cadastrado em versão do leiaute anterior a S-1.0.**  
Se [infoContr/tpContr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/index.html#2500_ideTrab_infoContr_tpContr) = [9], deve ser preenchida a matrícula que incorporará as demais (informadas no grupo[unicContr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/index.html#2500_ideTrab_infoContr_unicContr)).  
**Validação**: Se [indContr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/index.html#2500_ideTrab_infoContr_indContr) = [N], deve ser aplicada a regra de validação abaixo. Além disso, o valor informado neste campo não pode conter a expressão 'eSocial' nas 7 (sete) primeiras posições. Se [indContr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/index.html#2500_ideTrab_infoContr_indContr)= [S], deve corresponder a uma matrícula existente no Registro de Eventos Trabalhistas - RET para o respectivo trabalhador.  
  
No sistema a matricula deve ser informada na rotina **Dados eSocial** (TAFA552D), em **Contrato de Trabalho**, aba **Informações Gerais**, campo **Matricula**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18707152055191)  
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[Artigos RH Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971467-RH-Processos-Trabalhistas)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
**Próximos Treinamentos**[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
