---
article_id: 9070502632343
category: RH - Fechamento Período
content_hash: e6dda3a8c6a84819d31ab524f3ca36d42cff9b65974a06a38e1ee3f81c997866
fetched_at: '2026-06-28T22:43:24.487785+00:00'
product: protheus
section_id: 360011909793
source: central-protheus
title: RH - Linha Protheus - GPE - Quais os parâmetros utilizados para o fechamento
  do período
type: support-article
updated_at: '2025-04-16T11:51:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9070502632343-RH-Linha-Protheus-GPE-Quais-os-par%C3%A2metros-utilizados-para-o-fechamento-do-per%C3%ADodo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22369572481431) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Quais os parâmetros utilizados para o fechamento do período?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Os parâmetros que envolvem o fechamento do período são:  
**MV\_AUTOSRC** - Calcular somente para autônomos que possuam lançamentos mensais. .T.  Calcula apenas se possuir movimento, .F.  Calcula todos os ativos.   
**MV\_CALCTHD** - Quantidade de threads que serão utilizada no no cálculo de múltiplos roteiros e no fechamento.   
**MV\_CATNPGT** - Identifica as categorias que não deverão validar o numero de pagamento informado.   
**MV\_CONSIG** - Chave de ativação TOTVS Consignado   
**MV\_DIASPER** - Determina Quantidade. de Dias do Período para Cálculo. (1=Se o divisor será a quantidade de dias do mês do período;2=Se o divisor será sempre 30).   
**MV\_FASESOC** - Responsável por gerenciar o faseamento do eSocial. (Vazio) - 1a Fase / 1 - 1a Fase + 2a Fase 2 - 1a Fase + 2a Fase + 3a Fase  
**MV\_FECFOL** - Bloqueia fechamento do roteiro ordinário (FOL/AUT) em conjunto com outros roteiros. Se ativo ele deverá ser fechado sozinho após fechar os demais.    
**MV\_IORGGPE** - Define se haverá substituição de postos no módulo Gestão Pessoal - SIGAGPE (0-sem substituição de posto; 1-com substituição de posto)   
**MV\_ITMCLVL** - Informe 1 para utilização do Item contábil e Classe de valor, 2 para não utilizar, ou 3 para utilizar item/classe sem obrigatoriedade de ambos.   
**MV\_MID** - Habilita a integração de dados do eSocial com o Middleware. Se .T. Integra e se .F. não integra   
**MV\_MODFOL** - Determina qual a versão que está sendo utilizada (1=Padrão e 2=Modelo 2)   
**MV\_ORGCFG** - Configura o modo de uso do modulo Arquitetura Organizacional. 0=Não utiliza;1=Utiliza com controle de postos;2=Utiliza sem controle de Postos;   
**MV\_PERMOD2** - Utiliza o Cadastro de Períodos Simplificado disponível para a Folha de Pagamento Modelo 2 (.F. = não utiliza (padrão); .T. = utiliza).   
**MV\_REPLRAT** - Replica a programação de rateio de um mês para o outro durante o fechamento da folha.   
**MV\_RHTAF**- Habilita a integração de dados do eSocial com TAF Se .T., passa a integrar dados de eventos não periódicos do SIGAGPE com o SIGATAF   
**MV\_VDDFADE** - Dia do mês que será limite para considerar Faltas devoluções na reprogramação dos períodos Aquisitivos da licença Premio.   
**MV\_VDFALIC** - Faltas para prorrogação do Período Aquisitivo da Licença Prêmio.   
**MV\_VDMELIC** - Numero de Meses para prorrogação do período Aquisitivo da licença Premio, para cada ocorrência de Faltas >= MV\_VDFALIC.   
**MV\_VDTRAPD** - Destino da verba a ser transportada, sendo: Destino da verba a ser transportada, sendo: "3" – próxima semana do período em fechamento.   
  
**Saiba mais:**

[RH - Fechamento Período](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011909793-RH-Fechamento-Per%C3%ADodo)
