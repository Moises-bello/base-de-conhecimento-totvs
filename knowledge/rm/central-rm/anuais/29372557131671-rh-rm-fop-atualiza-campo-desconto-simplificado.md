---
article_id: 29372557131671
category: Anuais
content_hash: e2961dabb73021d18c04f5187d234d341ce9034e4caef8da427b644796f37b07
fetched_at: '2026-06-28T22:46:50.999340+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: RH - RM - FOP - Atualiza Campo Desconto Simplificado
type: support-article
updated_at: '2026-02-27T13:07:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29372557131671-RH-RM-FOP-Atualiza-Campo-Desconto-Simplificado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29372557102615) Tempo aproximado para leitura: **00:03:41 min** **Dúvida**Como executar e parametrizar o processo Atualiza Campo Desconto Simplificado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patchs

* 12.1.2402.267
* 12.1.2406.222
* 12.1.2410.153
* 12.1.2502 e superiores

**Solução**Processo utilizado para atualização dos campos IRRFSIMPLIFICADOCAIXA, IRRF13SIMPLIFICADOCAIXA e IRRFFERSIMPLIFICADOCAIXA.

Esse processo deve ser executado para o ano de 2024 porque os campos serão preenchidos para informações no processo da DIRF ano base 2024  
  
Acesse **Administração de Pessoal | Funcionário | Processos | Atualiza Campo Desconto Simplificado**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29372526020119)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29372526021015)  
  
Ao acessar a tela de parâmetros, preencha os campos conforme necessário para garantir a correta geração dos dados. A seguir, apresentamos a descrição de cada campo:

**Quebra de Seção:** Informar a quebra da seção

**Seleção de funcionários:** Informar a seleção de funcionários

**Caixa Inicial:** Informar o mês que iniciará o processo

**Caixa Final:** Informar o mês que finaliza o processo

**Ano:** Esse processo deve ser executado para o ano de 2024 porque os campos serão preenchidos para informações no processo da DIRF ano base 2024

**Atualizar Somente Campos diferente de 2 ou 3:** Analisa a ficha financeira do funcionário onde encontrar campos diferente de 2 ou 3 será atualizado referentes ao período solicitado

**Atualizar Todos os Campos:** Analisa a ficha financeira do funcionário e atualiza todos os campos referentes ao período solicitado  
  
Após executar o processo os campos IRRFSIMPLIFICADOCAIXA, IRRF13SIMPLIFICADOCAIXA e IRRFFERSIMPLIFICADOCAIXA serão atualizados.  
  
Para mais detalhes sobre como os campos são preenchidos acesse:   
[DT - Desconto Simplificado para a DIRF](https://tdn.totvs.com/display/public/LRM/DT+-+Desconto+Simplificado+para+a+DIRF)

**Importante:** Esse processo serve apenas para preenchimento dos campos citados acima na tabela PEFPERFF portanto não altera nada em cálculo da folha.

Para mais informações sobre o processo Atualiza Campo Desconto Simplificado **[CLIQUE AQUI](https://tdn.totvs.com/display/LRM/Atualiza+Campo+Desconto+Simplificado)**
