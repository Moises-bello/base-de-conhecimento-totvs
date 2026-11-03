---
article_id: 360036059834
category: GPE - eSocial - Não Periódicos
content_hash: 4abfaf502744c531ea1a69a779d29595f0212fa5cd1fef87f6a4aecdfa3afe60
fetched_at: '2026-06-28T22:45:05.809824+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2299 - Como enviar ao eSocial Rescisão
  com data de demissão retroativa (Judicial)
type: support-article
updated_at: '2026-06-16T11:49:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036059834-RH-Linha-Protheus-GPE-eSocial-S-2299-Como-enviar-ao-eSocial-Rescis%C3%A3o-com-data-de-demiss%C3%A3o-retroativa-Judicial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24514080976791)** Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**S-2299 - Como enviar ao eSocial Rescisão com data de demissão retroativa (Judicial)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Até o momento isso não é possível através do módulo de Folha de Pagamento (SIGAGPE), pois só é possível realizar cálculo de rescisão com data de demissão contemplada no período "aberto".  
Há situações que por ordem judicial, ou outros, é reconhecida a data de Demissão de um Trabalhador com data retroativa, **[clique aqui para acessar ao artigo de nossa Consultoria de Segmentos](https://tdn.totvs.com/pages/releaseview.action?pageId=372550080)**, nestes casos sugerimos o seguinte procedimento:  
  
1. Realize o cálculo da rescisão com a data de desligamento no período atual pela rotina **Rescisão** **(GPEM040)** através do seguinte caminho **GPE > Miscelânia > Cálculos > Rescisão** , integre o S-2299 com o TAF, mas mantenha o evento **pendente de envio**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24514055899159)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24514055905815)  
  
2. Realize o cálculo da rescisão complementar com a data de desligamento retroativa e integre o S-2299 com o TAF através da rotina **Rescisão** no **GPE (GPEM040)**, para mais detalhes verifique a documentação a seguir:  
[RH - Linha Protheus - GPE - Como alterar a data de demissão na rescisão complementar usando o parâmetro MV\_MDDTDEM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411589885335-RH-Linha-Protheus-GPE-Como-alterar-a-data-de-demiss%C3%A3o-na-rescis%C3%A3o-complementar-usando-o-par%C3%A2metro-MV-MDDTDEM?source=search)  
  
**Obs.: O evento S-2299 referente a rescisão complementar será integrado com o TAF com a tag indRetif igual a 1, ou seja, evento original**  
  
3. Para que o eSocial aceite o evento, mesmo que existam eventos S-1200 em períodos posteriores a data de Desligamento, realize o ajuste dos campos Num Processo (**CMD\_NRPROC**), Ind. Remuner (**CMD\_INDREM**) e Data Fim Rem (**CMD\_DTFREM**) do S-2299 gerado através do cálculo da rescisão complementar e salve:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24514016536855)  
  
**Obs.: Os campos devem ser preenchidos de acordo com a regra do Leiaute: [CMD\_NRPROC](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-nt-02-2024/index.html#2299_infoDeslig_verbasResc_procJudTrab_nrProcJud), [CMD\_INDREM](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-nt-02-2024/index.html#2299_infoDeslig_remunAposDeslig) e [CMD\_DTFREM](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-nt-02-2024/index.html#2299_infoDeslig_remunAposDeslig).**4. Com o período ao qual a data de desligamento retroage aberto, realize a transmissão do evento S-2299 ajustado diretamente no TAF com todas as informações corretas:  
[RH - Linha Protheus - GPE - eSocial - S-1298 - É possível reabrir o período no esocial através do GPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025816453-RH-Linha-Protheus-GPE-eSocial-S-1298-%C3%89-poss%C3%ADvel-reabrir-o-per%C3%ADodo-no-esocial-atrav%C3%A9s-do-GPE)  
  
**Obs.: O evento S-2299 referente a rescisão original pode ser excluído no TAF, pois ficara somente para registro no GPE**  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
