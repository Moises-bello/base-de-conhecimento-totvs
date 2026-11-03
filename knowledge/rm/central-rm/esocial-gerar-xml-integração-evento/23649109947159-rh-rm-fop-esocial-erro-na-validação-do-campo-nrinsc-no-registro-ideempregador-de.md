---
article_id: 23649109947159
category: eSocial - Gerar XML/ Integração Evento
content_hash: 0e4fa1105bac479bd037e98a2a790a361d0a0732910183c58fa5dc8730bbed01
fetched_at: '2026-06-28T22:47:12.980102+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro na validação do campo ''nrInsc'' no registro
  ''ideEmpregador'': Deve ser um CNPJ válido se {TpInsc} = [1]'
type: support-article
updated_at: '2024-12-26T15:56:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23649109947159-RH-RM-FOP-eSocial-Erro-na-valida%C3%A7%C3%A3o-do-campo-nrInsc-no-registro-ideEmpregador-Deve-ser-um-CNPJ-v%C3%A1lido-se-TpInsc-1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23649109931415) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**  
Ao gerar o XML S-1005 ocorre o erro: erro na validação do campo 'nrInsc' no registro 'ideEmpregador': Deve ser um CNPJ válido se {TpInsc} = [1]  
**Ambiente**TOTVS  RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Causa**  
Este incidente ocorre quando a parametrização da Classificação Tributária não está alinhada com o Leiaute do eSocial. O problema surge ao gerar o evento S-1005 para uma pessoa física, caso a Classificação Tributária esteja preenchida com um CNPJ. Isso provoca divergências nas informações e resulta em erro na geração do XML.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24389565564183)

A regra exige que o campo seja preenchido com o código apropriado que corresponde ao tipo de inscrição, conforme especificado na Tabela 05. Os códigos válidos são:

* **1** para **CNPJ** (Cadastro Nacional da Pessoa Jurídica)
* **2** para **CPF** (Cadastro de Pessoas Físicas)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24389253521815)

Tabela 05 - Tipos de Inscrição:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24389565593367)

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o **eSocial | Informações do Empregador;**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24389951043863)**

2. Edite o campo **Classificação Tributária;**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24389951058327)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24391972559895)

3. Após gere o XML novamente e envie para o eSocial.  
  
**Saiba mais**Para maiores informações acesse: [Mapeamento dos Eventos eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409020102679-RH-RM-FOP-eSocial-Mapeamento-dos-eventos-eSocial?source=search)
