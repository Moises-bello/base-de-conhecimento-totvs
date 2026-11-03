---
article_id: 360034641454
category: GPE - eSocial - Não Periódicos
content_hash: 49a9480bd34500c0fe96ce9ecf61f4ad683d14a0637079310d7206ff1ebf7c3f
fetched_at: '2026-06-28T22:45:06.065736+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2299 - Para que serve os campos P.C.Social
  (RG_NPROCS) e Nº Processo (RG_NPROC) na rotina calculo de rescisão
type: support-article
updated_at: '2021-04-13T15:05:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034641454-RH-Linha-Protheus-GPE-eSocial-S-2299-Para-que-serve-os-campos-P-C-Social-RG-NPROCS-e-N%C2%BA-Processo-RG-NPROC-na-rotina-calculo-de-rescis%C3%A3o
---

**Dúvida**Para que serve os campos**P.C.Social** (RG\_NPROCS) e **Nº Processo** (RG\_NPROC) na rotina calculo de rescisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Na rotina calculo de rescisão (aba EFD/Homolognet) existe os campos **P.C.Social** e **Nº Processo** responsáveis por alimentar TAGs com informação de processo no XML do evento **S-2299** no eSocial.  
  
Abaixo está detalhado a TAG e função de cada campo para o eSocial:  
1. TAG **procCS:**vinculado ao campo **P.C.Social** (RG\_NPROCS)serve para informações sobre processo judicial que suspende a exigibilidade da Contribuição Social Rescisória.  
Nesse caso conforme o layout do esocial deve existir uma evento S-1070 com esse processo no TAF.  
**Link:** [Onde cadastrar o evento S-1070 Processos Administrativos/Judiciais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012057432)  
  
Regras dessa TAG conforme descrito no layout:  
Informar um número de processo judicial cadastrado através do evento S-1070, cujo {*indMatProc*} seja igual a [*1, 7*].   
Validação: Deve ser um número de processo judicial válido e existente na Tabela de Processos (S-1070), com {*indMatProc*} = [*1, 7*].  
  
![](https://totvssuporte.zendesk.com/attachments/token/X5YXZfiYvb8IZMaBJVVbH1Acn/?name=inline-1686702459.png)​  
  
2. TAG **nrProcTrab:**Vinculado ao campo **Nº Processo** (RG\_NPROC)serve para informar o Número que identifica o processo trabalhista, quando o desligamento se der por decisão judicial.  
  
**![](https://totvssuporte.zendesk.com/attachments/token/r5vaGPjDDCi9Zo52Ey2jfVBXD/?name=inline-1058106112.png)​****Saiba Mais**Para saber mais consulte os links abaixo:   
[Erro 8 - Descrição : Grupo #39;Informacoes da Suspensao#39](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034639874)  
[Como funciona a Reintegração para envio ao eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034833693)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)
