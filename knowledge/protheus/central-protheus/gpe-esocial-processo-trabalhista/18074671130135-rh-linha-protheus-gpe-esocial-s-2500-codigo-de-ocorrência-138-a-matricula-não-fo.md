---
article_id: 18074671130135
category: GPE - eSocial - Processo Trabalhista
content_hash: d909556118b758bc3b2241c6a124daf21ed82ce34320fb7a1f6304a943da701f
fetched_at: '2026-06-28T22:45:00.603210+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-2500 - Codigo de ocorrência 138: A
  matricula não foi identificada no eSocial para o trabalhador informado'
type: support-article
updated_at: '2024-08-26T17:14:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18074671130135-RH-Linha-Protheus-GPE-eSocial-S-2500-Codigo-de-ocorr%C3%AAncia-138-A-matricula-n%C3%A3o-foi-identificada-no-eSocial-para-o-trabalhador-informado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18074687654679) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Codigo de ocorrência 138 - Localização: /eSocial/evtProcTrab/ideTrab/infoContr/matricula  
Descrição: A matricula XXXX não foi identificada no eSocial para o trabalhador informado.  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O erro ocorre quando a *tag* **indContr** está com **S** e a matricula informada no xml S-2500 está divergente da matricula enviada ao eSocial.  
  
Matrícula atribuída ao trabalhador pela empresa ou, no caso de servidor público, a matrícula constante no Sistema de Administração de Recursos Humanos do órgão.  
Se [indContr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/#2500_ideTrab_infoContr_indContr) = [N], deve ser criada uma matrícula para o trabalhador.  
Se [indContr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/#2500_ideTrab_infoContr_indContr) = [S], deve corresponder à matrícula informada pelo empregador no evento S-2190, S-2200 ou S-2300 do respectivo contrato. O campo não deve ser informado somente no caso de TSVE cadastrado em versão do leiaute anterior a S-1.0.  
Se [indUnic](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/#2500_ideTrab_infoContr_indUnic) = [S], deve ser preenchida a matrícula que incorporará as demais (informadas no grupo [unicContr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/#2500_ideTrab_infoContr_unicContr)).  
**Validação:** Se [indContr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/#2500_ideTrab_infoContr_indContr) = [N], deve ser aplicada a regra de validação abaixo. Além disso, o valor informado neste campo não pode conter a expressão 'eSocial' nas 7 (sete) primeiras posições. Se [indContr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/#2500_ideTrab_infoContr_indContr) = [S], deve corresponder a uma matrícula existente no Registro de Eventos Trabalhistas - RET para o respectivo trabalhador.  
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[RH - Linha Protheus - GPE - eSocial - Processos Trabalhistas - Premissas para geração dos eventos do eSocial para Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13317899021847)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
