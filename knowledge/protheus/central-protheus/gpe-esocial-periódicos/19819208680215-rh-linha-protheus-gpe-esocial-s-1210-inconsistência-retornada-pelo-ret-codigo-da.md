---
article_id: 19819208680215
category: GPE - eSocial - Periódicos
content_hash: d7abe3b55f4a101aea34e09d9099833ea84166203250cffab43c5bc6cabdba2a
fetched_at: '2026-06-28T22:45:08.983482+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1210 - Inconsistência retornada pelo
  RET: Codigo da ocorrência: 186 Localização: /eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/dedDepen[1]/cpfDep'
type: support-article
updated_at: '2024-11-04T13:35:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19819208680215-RH-Linha-Protheus-GPE-eSocial-S-1210-Inconsist%C3%AAncia-retornada-pelo-RET-Codigo-da-ocorr%C3%AAncia-186-Localiza%C3%A7%C3%A3o-eSocial-evtPgtos-ideBenef-infoIRComplem-infoIRCR-dedDepen-1-cpfDep
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19819238597655) Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**S-1210 - Inconsistência retornada pelo RET: Codigo da ocorrência: 186  
Localização: /eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/dedDepen[1]/cpfDep  
Descrição: CPF do dependente XXXXXXXXXXX invalido.Acao sugerida: Deve ser um CPF de dependente cadastrado no RET do eSocial ou no grupo de Informacoes de Dependentes do proprio evento.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão P12.1.2210  
  
**Causa**  
A partir do leiaute S-1.2 é obrigatório envio do CPF do Dependente no evento S-1210 grupo dedDepen tag **cpfDep.** O erro pode ocorrer devido a três motivos:  
  
**1)** Evento S-1210 integrando com CPF de dependentes de outros funcionários no conjunto de *tags* infoIRComplem. Para este cenário **aplicar o pacote** abaixo, [**excluir o evento S-1210**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036104773?source=search) no TAF e realizar uma **nova integração** do mesmo no SIGAGPE.  
  
<https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA>   
  
**2)** Cadastro do Dependente enviado ou alterado no evento **S-2205** está com **data posterior ao período de envio do S-1210**.   
**Exemplo**: S-2205 enviado no período 12/2023 e S-1210 referente ao período 11/2023, neste caso será necessário excluir o S-2205 da base do eSocial e realizar uma nova transmissão com período igual ou anterior ao período de envio do S-1210;  
  
**3)** Quando não existe informação do Dependente do IRRF na base do eSocial. Neste caso será necessário enviar o cadastro do Dependente através do evento S-2205 **sempre com período anterior ou igual ao do evento de pagamento, nunca superior.**  
  
**Observação**: Para integrar o evento S-2205 com data retroativa, **altere a data base do sistema**.   
 **Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
