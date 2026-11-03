---
article_id: 35175511631767
category: GPE - eSocial - Saneamento de Base
content_hash: 11a8ad9c4e2fc4e9634e91d7f61d3a7a08d6c5db91f0788054d81d4290ac4938
fetched_at: '2026-06-28T22:45:01.498681+00:00'
product: protheus
section_id: 360007319754
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Como se adequar e atualizar o ambiente
  para nota técnica S-1.3 Nº 04/2025
type: support-article
updated_at: '2026-06-24T14:54:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35175511631767-RH-Linha-Protheus-GPE-eSocial-Como-se-adequar-e-atualizar-o-ambiente-para-nota-t%C3%A9cnica-S-1-3-N%C2%BA-04-2025
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35175535490839) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como se adequar e atualizar o ambiente para nota técnica S-1.3 Nº 04/2025?  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Foi divulgada pelo governo a [Nota Técnica S-1.3 nº 04/2025](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-3-04-2025.pdf)  
Essa Nota Técnica tem como objetivo apresentar os ajustes dos leiautes do eSocial.  
  
As alterações realizadas estão com datas de início faseadas pelo governo conforme descrito abaixo:

* [DRHROTPRT-24067 DT Alteração das Tabelas](https://tdn.totvs.com/pages/viewpage.action?pageId=976144672)
  + Alteradas as Tabelas de Natureza de Rubrica, Benefícios e Afastamentos
* [DRHROTPRT-24068 DT Cadastro de Verbas: Novas validações](https://tdn.totvs.com/pages/viewpage.action?pageId=977192825)
  + Validações relacionadas a verbas com incidência de Previdência Social apenas para a parte de Segurados
* [DRHROTPRT-24272 DT eSocial S-1.3 NT 04/2025 S-2500 - Tipo de Origem](https://tdn.totvs.com/pages/viewpage.action?pageId=977861849)
  + Implementado no cadastro de Processos validação para conferir o Tipo de Origem dos demais Nros. Sequenciais do Nro. do Processo de forma que seja o mesmo entre todos os Nro. Sequenciais.
* [DRHROTPRT-24273 DT Processos Trabalhistas: Novas Regras - Matricula](https://tdn.totvs.com/display/PROT/DRHROTPRT-24273+DT+Processos+Trabalhistas%3A+Novas+Regras+-+Matricula)
  + Inclusão da nova regra no S-2500 que impede o envio de múltiplos eventos do mesmo processo vinculados à mesma matrícula.
* [DRHROTPRT-24207 DT S-2299: Nova validação da incidência RV\_INCCP](https://tdn.totvs.com/pages/viewpage.action?pageId=980987783)
* [DRHROTPRT-24208 DT S-2399: Nova validação da incidência RV\_INCCP](https://tdn.totvs.com/pages/viewpage.action?pageId=981002724)
  + Para os eventos remuneratórios incluímos a consistência Verbas X Natureza de Rubrica, onde o sistema passa a validar verbas com incidência INSS = 15 ou 16 (exclusiva trabalhador) frente ao novo campo da Tabela de Natureza de Rubricas

**Importante**  
Após realizar as atualizações realize o procedimento da documentação abaixo para atualizar as tabelas com as novas informações no SIGAGPE.  
[RH - Linha Protheus - GPE - eSocial - Como atualizar as tabelas S047, S048, S049, S054, S056 e S057, quando existe alteração das tabelas oficias no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034614474-RH-Linha-Protheus-GPE-eSocial-Como-atualizar-as-tabelas-S047-S048-S049-S054-S056-e-S057-quando-existe-altera%C3%A7%C3%A3o-das-tabelas-oficias-no-eSocial#:~:text=Atrav%C3%A9s%20do%20modulo%20SIGAGPE%20(07,3.)  
  
Para preparar o ambiente é **importante estar com todas as atualizações** descritas abaixo aplicadas:  
  
**GPE:**  
12.1.2210:<https://r.totvs.io/p/1211773> ; Apenas com Garantia Estendida  
12.1.2310:<https://r.totvs.io/p/1211771> ; Apenas com Garantia Estendida  
12.1.2410:<https://r.totvs.io/p/1211772> ;   
12.1.2510:<https://r.totvs.io/p/1211774> ;  
  
**TSS**  
[RH - Linha Protheus - TAF - eSocial - ATUALIZAÇÃO - Como atualizar o TSS do E-social](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18713174729367-RH-Linha-Protheus-TAF-eSocial-ATUALIZA%C3%87%C3%83O-Como-atualizar-o-TSS-do-E-social)  
  
**TAF**  
É importante que todos os itens da documentação abaixo estejam aplicados inclusive **Expedição Continua TAF**  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/18972648169239-RH-Linha-Protheus-TAF-ATUALIZA%C3%87%C3%83O-Como-atualizar-o-TAF-E-social-Expedi%C3%A7%C3%A3o-Cont%C3%ADnua>  
  
**Necessário realizar a atualização das autocontidas** do **TAF**:  
Automação Fiscal - CONFIGURAÇÃO - [Atualização das tabelas autocontidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034479973-Automa%C3%A7%C3%A3o-Fiscal-CONFIGURA%C3%87%C3%83O-Atualiza%C3%A7%C3%A3o-das-tabelas-autocontidas?source=search)  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
