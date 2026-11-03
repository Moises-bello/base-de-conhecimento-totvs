---
article_id: 9783424284183
category: eSocial - Gerar XML/ Integração Evento
content_hash: 92aac4362fa07607c6e3c46646e09198fc33f87b736fa84a9ba1d67ba88bab6a
fetched_at: '2026-06-28T22:47:12.127724+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 381 na integração com o Governo: CPF inválido'
type: support-article
updated_at: '2024-12-26T15:47:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9783424284183-RH-RM-FOP-eSocial-Erro-381-na-integra%C3%A7%C3%A3o-com-o-Governo-CPF-inv%C3%A1lido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24296728537495) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao transmitir eventos ao eSocial é apresentada a inconsistência **Código do erro: 381 - Descrição: CPF inválido. Ação Sugerida: Confira os valores informados no campo****.**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9785453792919)**

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Essa mensagem de erro de validação ocorre, na integração com o Governo, quando o CPF do funcionário está com numeração inválida ou o tipo de inscrição não corresponde ao número de inscrição da remuneração outro emprego.  
  
**Solução**Para correção da ocorrência favor realizar as validações abaixo:  
  
• **CPF divergente** do que consta no eSocial  
1.  No módulo **Folha de Pagamento** acesse o menu **Administração de Pessoal | Funcionários**;2. Edite o funcionário desejado e altere o campo **CPF** com a informação correta.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9785177491991)

2. Após ajustes, gere o XML novamente e envie ao eSocial.

• CPF/CNPJ **Remuneração Outro Emprego**   
Quando o funcionário possui remuneração em outra Coligada na base de dados, o sistema irá considerar a marcação dos parâmetros **Pessoa Física**ou **Identificação pelo CNPJ** no cadastro da Seção, gerando o **CPF** ou **CNPJ**, respectivamente, na *tag* **nrInsc.**1. Acesse o menu **Administração de Pessoal | Seções** e faça a edição da seção vinculada ao funcionário;  
2. Faça os devidos ajustes e validações nos campos e parâmetros;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9785327480599)

3. Em seguida, gere o XML novamente e envie ao eSocial.
