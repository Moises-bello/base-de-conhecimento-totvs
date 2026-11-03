---
article_id: 19402364401559
category: eSocial - Gerar XML/ Integração Evento
content_hash: 85a87f6c9b2f7a859c3d55233e5c0021aab68a327c65fcdd36a790c17fad8bfb
fetched_at: '2026-06-28T22:47:12.105129+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 1861 no envio do S-1210: CPF do dependente
  XXX inválido. Deve ser um CPF de dependente cadastrado no RET do eSocial ou no grupo
  de Informações de Dependentes do próprio evento (S-1.2)'
type: support-article
updated_at: '2026-02-20T19:26:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19402364401559-RH-RM-FOP-eSocial-Erro-1861-no-envio-do-S-1210-CPF-do-dependente-XXX-inv%C3%A1lido-Deve-ser-um-CPF-de-dependente-cadastrado-no-RET-do-eSocial-ou-no-grupo-de-Informa%C3%A7%C3%B5es-de-Dependentes-do-pr%C3%B3prio-evento-S-1-2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19402355747991) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao transmitir o evento S-1210 ocorre erro **Código 1861**: **CPF do dependente XXXXXXXXXXX inválido. Ação sugerida: Deve ser um CPF de dependente cadastrado no RET do eSocial ou no grupo de Informações de Dependentes do próprio evento.**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir das versões 12.1.2302.235, 12.1.2306.182, 12.1.2310.116 e superiores.

**Causa**  
A inconsistência geralmente é apresentada na transmissão do S-1210 (leiaute S-1.2), quando há informação de dependente informada em um ou mais grupos da lista abaixo, porém não consta o cadastro do dependente no ambiente do Governo:

**penAlim** - Pensão Alimentícia  
**infoDepSau** - Plano de Saúde  
**dedDepen** - Dedução do Rendimento Tributável relativa a dependente  
**benefPen** - Dedução suspensa por dependente e beneficiário da pensão  
**infoReemDep** - Reembolso do dependente do plano de saúde

Conforme consta no leiaute, o cadastro do dependente é encaminhado ao governo através dos eventos de admissão (S-2200/S-2300) e  alteração de dados cadastrais (S-2205).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19482111824407)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19482111835671)

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse **Folha de pagamento | eSocial | Outros Processos | Gerar Gatilhos em Lotes**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19402328350487)

2. Selecione o evento **S-2205**, preencha o campo **Data de Alteração** (necessário que a data seja igual ou anterior ao período de apuração do S-1210 e igual ou posterior a data de admissão ou transferência do funcionário) e avance o processo para execução. Se necessário, poderá ser realizado filtro em **Seleção de funcionários**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19402351120535)

3. Será gerado um gatilho do S-2205 na fila de eventos para geração do XML, que irá constar então o grupo dependente preenchido;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19402338217879)

4. Faça a transmissão do evento para o governo e, após ser aceito, envie novamente o S-1210;

5. Caso o erro persista, verifique se consta alguma alteração cadastrada no portal do governo com data posterior ao S-2205 encaminhado com o CPF do dependente. Se houver, verifique se, para esta(s) alteração(alterações) no portal consta o CPF do dependente. Se houver alguma alteração cadastral com data superior ao S-2205 enviado e sem o CPF do dependente, será necessário alterar (para que seja carregado o CPF do dependente) ou excluir a alteração.  
Para acessar a movimentação trabalhista do funcionário no portal do governo, siga os seguintes passos: **Empregados | Gestão de Empregados | Informe o CPF desejado | Movimentações Trabalhistas**.  
  
**Importante**  
Para **autônomos**, também será gerado o S-2205.  
A partir do leiaute S-1.2, o sistema irá preencher os dados do dependente nos eventos de admissão e/ou alteração de dados cadastrais ou cadastrar o dependente. A geração do gatilho em lote, neste caso, só é necessário para ajustar no governo informações de dependentes já cadastrados no RM antes desta versão de leiaute, e que possuíam incidência apenas em Assistência Médica e Pensão.  
Para os funcionários **Entes Públicos**, será necessário a criação do gatilho **S-2405** manualmente na fila.  
  
**Saiba mais**  
Para mais informações, acesse:  
     - [Alterações - S-2205 - S-1.2](https://tdn.totvs.com/pages/viewpage.action?pageId=777274034)  
     - [RH - RM - FOP - eSocial - Gerar gatilho de XML em lote](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15636111893143-RH-RM-FOP-eSocial-Gerar-gatilho-de-XML-em-lote)
