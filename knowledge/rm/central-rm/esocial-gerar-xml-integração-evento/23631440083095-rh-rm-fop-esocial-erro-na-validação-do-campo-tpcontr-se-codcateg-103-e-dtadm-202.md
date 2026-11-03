---
article_id: 23631440083095
category: eSocial - Gerar XML/ Integração Evento
content_hash: a4f77c1366c0a6f552fd5b57a0336a8fe3cdd4bc005afa23b80dd9ae215e9470
fetched_at: '2026-06-28T22:47:12.988983+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro na validação do campo ''tpContr'': Se codCateg
  = [103] e dtAdm >= [2024-04-22], deve ser informado [2] Prazo determinado, definido
  em dias'
type: support-article
updated_at: '2026-06-01T14:06:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23631440083095-RH-RM-FOP-eSocial-Erro-na-valida%C3%A7%C3%A3o-do-campo-tpContr-Se-codCateg-103-e-dtAdm-2024-04-22-deve-ser-informado-2-Prazo-determinado-definido-em-dias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23631447180311) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Ao realizar a geração do XML dos eventos S-2190, S-2200 e S-2206 é apresentado a mensagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23636641404823)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões.  
  
**Causa**  
Esse incidente ocorre, pois esta sendo gerado com a tag **<tpContr>1<tpContr>;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23635642755863)

De acordo com as novas regras da [Nota Técnica S-1.2 N° 01/2023](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-2-01-2023.pdf) é exigido que o contrato de aprendiz seja por prazo determinado, definido em dias a partir ou igual a data 22/04/2024. Ou seja a tag deverá ser gerado com o **tpContr 2.**  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse **Administração de Pessoal | Funcionários;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23635659343383)

2. Selecione o **Funcionário | Registro | Dados do Contrato;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23635141572887)

3. Marque a flag **Contrato com Prazo** e preencha os campos com as informações, lembre-se que o tipo de contrato é **Prazo Determinado, Definido em dias;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23635141595287)

4. Após gere novamente o XML e envie para o eSocial;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23635157577111)

**Saiba mais**  
[Mapeamento dos eventos eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409020102679-RH-RM-FOP-eSocial-Mapeamento-dos-eventos-eSocial?source=search)
