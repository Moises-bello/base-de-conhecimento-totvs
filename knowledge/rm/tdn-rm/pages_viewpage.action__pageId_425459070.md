---
content_hash: 30eb3f7918c46c5e1de6bafb9076b6e38181f3cba6ba0d37b607512b88787cee
fetched_at: '2026-06-29T00:09:33.865063+00:00'
page_id: '425459070'
product: rm
source: tdn-rm
title: 'Integração: TOTVS Educacional e TOTVS Gestão de Relacionamento com Clientes'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459070
version: 2
---

O objetivos desta tela de parâmetros é definir a forma como o Educacional integra com o CRM. Esta integração possibilita um melhor controle por parte da instituição do andamento de cada solicitação feita pelo aluno

**Atendimento - Geral 1/3**   
 Nesta primeira etapa são configurados os parâmetros gerais que definem como o sistema vai se comportar no momento em que o aluno faz uma solicitação. É definido se no momento da abertura da requisição o sistema vai:

* Utilizar a data de vencimento dos contratos com dia fixo
* Enviar e-mail ao solicitante na abertura do atendimento
* Calcular automaticamente a data de vencimento da parcela

**Atendimento – Geral 2/3**  
 Nesta etapa será definida qual solicitação de atendimentos será utilizada

* **Portal Cliente Online:** Quando opta pelo Portal Cliente Online, as configurações são feitas no CRM, restando apenas algumas parametrizações no TOTVS Educacional. O Portal Cliente Online é um módulo do TOTVS Gestão de Relacionamento com Cliente onde é possível seu acesso pelo portal Classis Net.
* **Portal Classis Net:** A utilização pelo portal do Classis Net implica em uma série de configurações que terão de realizadas, em sua maioria no TOTVS Educacional. O aluno acessa o Portal e pelo menu Solicitação faz o requerimento. A única diferença é que no momento da solicitação alguns recursos são limitados.
  + Valores padrões para as solicitações
    - Usar usuário logado no sistema como atendente para abertura de atendimento
    - Atendente para abertura de atendimento: *EX: 3209 - PESSOA 512588*
    - Categoria Geral: *EX: 7 - Atendimento*
    - Classificação do atendimento: *EX: 00007 - Alteração de Documentos*
    - Tipo de contato: *EX: 1 - Automático*
    - Produto: *EX: 123 - AT - Gestão da Informação e do Conhecimento*
    - Origem do contato: *EX: 2 - Secretaria*
    - Detalhe do produto *EX: 11.06 - Gestão da biblioteca*

**Atendimento – Geral 3/3**  
 Nesta última etapa configure as parcelas geradas caso a requisição seja de um serviço que necessite gerar lançamento.

* Informe a data final de cada parcela (Data de solicitação) e de vencimento para o cadastro dos serviços extras pelo CRM.
