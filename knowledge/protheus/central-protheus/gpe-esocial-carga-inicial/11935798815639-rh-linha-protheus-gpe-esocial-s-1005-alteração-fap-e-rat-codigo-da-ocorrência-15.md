---
article_id: 11935798815639
category: GPE - eSocial - Carga Inicial
content_hash: cfadc49ee4b76e668a23da39c6235037279195be57797b2907781a6e79672047
fetched_at: '2026-06-28T22:45:03.154714+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1005 - Alteração FAP e RAT - Codigo
  da ocorrência: 150 e Codigo da ocorrência: 173'
type: support-article
updated_at: '2023-09-28T20:55:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11935798815639-RH-Linha-Protheus-GPE-eSocial-S-1005-Altera%C3%A7%C3%A3o-FAP-e-RAT-Codigo-da-ocorr%C3%AAncia-150-e-Codigo-da-ocorr%C3%AAncia-173
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17887928218647) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**Alteração FAP e RAT - Codigo da ocorrência: 150 e Codigo da ocorrência: 173  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa****Sequência: 000001 - Tipo: Erro - Codigo da ocorrência: 173**  
Localização: /eSocial/evtTabEstab/infoEstab/inclusao/dadosEstab/aliqGilrat/fap  
Descrição: Campo Fap nao pode ser preenchido.Acao sugerida: Campo FAP so pode ser informado quando nao existe a informacao cadastrada na Tabela FAP no ano vigente, ou quando o valor e diferente e existe processo em [procAdmJudFap].

**Sequência: 000002 - Tipo: Erro - Codigo da ocorrência: 150**  
Localização: /eSocial/evtTabEstab/infoEstab/inclusao/dadosEstab/aliqGilrat/aliqRat  
Descrição: A aliquota informada devera ser diferente da aliquota definida na legislacao vigente para o codigo CNAE preponderante informado (neste caso, devera haver informacoes de processo em procAdmJudRat).  
  
**Solução**A empresa **não precisa informar o percentual da alíquota RAT e nem do FAP no evento S-1005**, pois o Governo sabe o percentual **RAT** de acordo com o **CNAE da empresa** e do **FAP valida o valor  diretamente no *site*<https://fap.dataprev.gov.br/>**

**Somente** se o **% for diferente da regra do CNAE** a empresa precisa informar, mas neste caso terá que informar o processo no **evento S-1070**.  
  
Validação leiaute 1.1 - Evento S-1005 - tag aliqRat   
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11938584177943)

Validação leiaute 1.1 - Evento S-1005 - tag fap  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11938624462743)  
  
  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[RH - Linha Protheus - GPE - eSocial - S-1005 - Por que o Fap não deve ser informado na versão do leiaute S-1.0](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406992890391-RH-Linha-Protheus-GPE-eSocial-S-1005-Por-que-o-Fap-n%C3%A3o-deve-ser-informado-na-vers%C3%A3o-do-leiaute-S-1-0?source=search)  
[FAP 2024](https://www.totvs.com/blog/fiscal-clientes/fap-2024-novo-portal-de-consulta-e-contestacao/)  
[Artigos S-1005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050822873)   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
