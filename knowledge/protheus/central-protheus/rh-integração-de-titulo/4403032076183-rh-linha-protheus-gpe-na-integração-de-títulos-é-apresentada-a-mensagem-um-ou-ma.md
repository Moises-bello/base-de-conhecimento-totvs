---
article_id: 4403032076183
category: RH - Integração de Titulo
content_hash: 1f03aa6d8f4ba8aeb77af204c2bbca2cb1ecad903e9bc376e8919a7db9e18879
fetched_at: '2026-06-28T22:43:36.394148+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: 'RH - Linha Protheus - GPE - Na integração de títulos é apresentada a mensagem:
  Um ou mais campos obrigatórios não foram preenchidos Natureza'
type: support-article
updated_at: '2025-07-17T14:26:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403032076183-RH-Linha-Protheus-GPE-Na-integra%C3%A7%C3%A3o-de-t%C3%ADtulos-%C3%A9-apresentada-a-mensagem-Um-ou-mais-campos-obrigat%C3%B3rios-n%C3%A3o-foram-preenchidos-Natureza
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33531049005463) Tempo aproximado para leitura: **00:03:00 min**

**Ocorrência**Na integração de títulos é apresentada a mensagem: Um ou mais campos obrigatórios não foram preenchidos. Natureza  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**Esse incidente ocorre, pois no Módulo **Financeiro**, foi desenvolvido um gatilho customizado para o campo **Fornecedor** - **E2\_FORNECE**, para que na inclusão de registros na tabela o sistema busque a informação da Natureza diretamente do campo **Natureza** - **A2\_NATUREZ**, impactando na integração de Títulos integrados pelo módulo **Gestão de Pessoal**.  
  
**Solução**Erro apresentado: ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403037872791)  
Para solucionar essa ocorrência:   
  
1- Validar se foi adicionado um gatilho na sequencia 004 para o campo **E2\_FORNECE** com a regra para busca da informação de natureza diretamente do campo **A2\_NATUREZ**

**Acessar:** Configurador -> Base de Dados -> Dicionário -> Gatilhos -> Campo E2\_FORNECE  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403031435287)  
  
2. Para que essa validação não tenha impacto nos títulos integrados pelo Gestão de Pessoal, será necessário inverter a ordem dos campos **Natureza** - **E2\_NATUREZ** com o **Fornecedor** - **E2\_FORNECE**, deixando os campos **Fornecedor** e **Loja** que é um complemento anterior, a frente do campo **Natureza**.

**Acessar:** Configurador -> Base de Dados -> Dicionário -> Arquivos -> Tabela SE2, clicar em editar, em seguida clicar nas setas para que o campo assuma a posição conforme solicitado acima.  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403038034967)

3. Após este procedimento será possivel realizar a integração do Título com a natureza atribuída no campo **Cod. Natureza** - **RC1\_NATURE**.  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403038232727)  
  
**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
