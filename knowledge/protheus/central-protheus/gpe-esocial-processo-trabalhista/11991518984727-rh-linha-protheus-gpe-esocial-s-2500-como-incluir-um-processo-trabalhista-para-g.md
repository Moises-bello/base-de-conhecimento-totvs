---
article_id: 11991518984727
category: GPE - eSocial - Processo Trabalhista
content_hash: 4d3bfd30a7b3cd9a893292a684466b0d3322a138b6b864ea23a8d8d15bc12572
fetched_at: '2026-06-28T22:45:00.316618+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2500 - Como incluir um processo trabalhista
  para geração do evento S-2500, leiaute S-1.3
type: support-article
updated_at: '2025-03-27T18:03:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11991518984727-RH-Linha-Protheus-GPE-eSocial-S-2500-Como-incluir-um-processo-trabalhista-para-gera%C3%A7%C3%A3o-do-evento-S-2500-leiaute-S-1-3
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18743301030039) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como incluir um processo trabalhistas para geração do evento S-2500 no leiaute S-1.3?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para que o sistema gere o evento S-2500 é necessário verificar alguns itens:

**1.** Estar com o ambiente devidamente atualizado de acordo com os pacotes disponibilizados na pagina de entregas legais: **[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)**  
**2.** Registrar as informações decorrentes de processos trabalhistas, através do Cadastro de Processos (APTA100), no módulo SIGAGPE: **[RH - Linha Protheus - GPE - Como cadastrar um processo trabalhista](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050723993)**  
**3.** Conforme definição do eSocial, os eventos do Processo Trabalhista estão disponíveis a partir da versão S-1.1, veja as premissas do sistema: **[RH - Linha Protheus - GPE - eSocial - Processos Trabalhistas - Premissas para geração dos eventos do eSocial para Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13317899021847)**  
Após realizar a inclusão do processo trabalhista na rotina APTA100, o sistema levará as informações para rotina de Dados eSocial (TAFA552D), onde será necessário realizar outras inclusões:  
  
**Caminho: Atualizações > Processos Trabalhistas > Processos > Dados eSocial (TAFA552D)   
Clique [AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12409243591703) para saber como incluir a rotina no menu.**Apresentando os processos previamente cadastrados através do módulo SIGAGPE, cadastro de processos (APTA100).   
Para realizar a alteração, clique nos lápis, localizado ao lado direito da tela em ações:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30974521145367)  
  
O sistema demonstrará ao editar o processo, as seguintes informações:  
Aba **Identificação do Processo.** Essas informações vieram do cadastro do processo na rotina Processo APTA100:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30974521149207)  
  
**Aba Identificação de pessoa trabalhadora e contrato de trabalho**As informações de identificação são levadas a partir da rotina Processos APTA100: **![](https://centraldeatendimento.totvs.com/hc/article_attachments/30974521151255)**Para adicionar as informações do processo, clique em Adicionar Contrato, ou caso já tenha realizado a inclusão, clique para alterar no lápis em Ações:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30974537523607)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30974537527191)  
  
Ao clicar, o sistema demonstrará 3 abas, Informações Gerais, Informações complementares e Informações de Vínculo.  
  
Para aba **Informações Gerais** teremos as seguintes informações:

* Sessão de Informações sobre o contrato de trabalho e identificação do estabelecimento
* Identificação do ano base em que houve indenização substitutiva de abono salarial
* Identificação do período
* Informação do novo código de categoria e/ou da nova natureza, no caso de reconhecimento judicial nesse sentido
* Vínculos do início do TSVE  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/30974521162647)

Na aba **Informações Complementares** teremos as seguintes informações:

* Informações complementares do contrato de trabalho
* Informações da remuneração e periodicidade de pagamento  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/30974521163543)  
    
  Na aba **Informações do Vínculo**, teremos campos sobre o novo vínculo que deve ser informado:  
  **![](https://centraldeatendimento.totvs.com/hc/article_attachments/30974537538967)** **Atenção**  
  Para que o botão **SALVAR** fique habilitado é **necessário que todos os campos obrigatórios sejam preenchidos** em todas as abas exibidas.   
    
  A geração do XML será executado através da rotina de Geração de Processos Trabalhistas (GPEM038) no módulo SIGAGPE:   
  [RH - Linha Protheus - GPE - eSocial - Processos Trabalhistas - Como realizar a geração dos eventos de processo trabalhista na rotina GPEM038](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12412564333719-RH-Linha-Protheus-GPE-eSocial-Processos-Trabalhistas-Como-realizar-a-gera%C3%A7%C3%A3o-dos-eventos-de-processo-trabalhista-na-rotina-GPEM038)  
  **Saiba Mais**  
  Para saber mais consulte os *links*abaixo:   
  [Artigos RH Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971467-RH-Processos-Trabalhistas)  
  [eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
  [MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
  [Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
    
  *Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"  
  Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade****WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
