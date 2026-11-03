---
article_id: 11277229779351
category: GPE - eSocial - Não Periódicos
content_hash: 81012b09126241a21c4bbd4da25ac75abea9925f1d1ea19c36d521f34cdf4527
fetched_at: '2026-06-28T22:45:04.699759+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2206 - Como gerar S-2206 para alteração
  de CBO via job
type: support-article
updated_at: '2026-06-16T13:46:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11277229779351-RH-Linha-Protheus-GPE-eSocial-S-2206-Como-gerar-S-2206-para-altera%C3%A7%C3%A3o-de-CBO-via-job
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24484436985367) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como enviar o evento S-2206 ao eSocial, quando há alteração de CBO ou descrição da função via *job*?  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
A partir do Leiaute S-1.0, não há envio do evento de tabela S-1030, sendo assim, ao alterar o CBO de uma função ou a descrição, deve ser disponibilizada opção de geração do evento S-2206 sem necessidade de alterar o campo função na SRA.  
  
Ao **alterar as informações de CBO ou descrição de uma função**, o registro será levado para o controle de *JOB* (tabela RJB), que executará o disparo dos **eventos S-2206/S-2306 filtrando os trabalhadores vinculados à função atualizada** (tabela RJC).  
  
Criada nova opção para o *job* GPEM026B() para integração de eventos de alteração contratual a partir da alteração das informações de descrição ou CBO no cadastro de funções (GPEA030).  
  
**Observações**

Para quem já utiliza o *job* **GPEM026B()**, esta nova execução **vem desabilitada por padrão (*****False*****)**, sendo **necessário habilitar a opção**. Para isso, no cadastro do ***Schedule*** no módulo **Configurador**, é preciso informar o sétimo parâmetro como *True* (verdadeiro): **GPEM026B(**.F.,.F.,.F.,.F.,.F.,.F.**,.T.)**

Abaixo todos os parâmetros da rotina. Nome das variáveis utilizado apenas como **exemplo**.

**GPEM026B( lAltSal, lAfast, lAltSindica, lConvoca, lAltDep, lAltTurno, lFunCargo )**

* **lAltSal**  - Informa se deve ou não executar a rotina de alteração salarial
* **lAfast**  - Informa se deve ou não executar a rotina de afastamentos
* **lAltSindica** - Informa se deve ou não executar a rotina de alteração sindical
* **lConvoca** - Informa se deve ou não executar a rotina de locais de convocação
* **lAltDep**  - Informa se deve ou não executar a rotina de alteração de dependentes
* **lAltTurno**- Informa se deve ou não executar a rotina de troca de turno.
* **lFunCargo**- Informa se deve ou não executar a rotina de alteração contratual por atualização de função.

Para mais informações sobre configuração do *schedule*:  
[RH - Linha Protheus - GPE - eSocial - S-2206/S-2230 - Como configurar o job schedule GPEM026B na tela PO UI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21979795766167-RH-Linha-Protheus-GPE-eSocial-S-2206-S-2230-Como-configurar-o-job-schedule-GPEM026B-na-tela-PO-UI)  
[RH - Linha Protheus - GPE - eSocial - S-2206/S-2230 - Como executar o Job/Schedule manualmente na tela PO UI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21983515224727-RH-Linha-Protheus-GPE-eSocial-S-2206-S-2230-Como-executar-o-Job-Schedule-manualmente-na-tela-PO-UI)  
  
**Consulte Também:** [Como funciona o Job/Schedule na prática referente a integração das Alterações Salariais, fim de afastamento e trocas de turno com o TAF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035063413)  
  
**Saiba mais**  
Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
