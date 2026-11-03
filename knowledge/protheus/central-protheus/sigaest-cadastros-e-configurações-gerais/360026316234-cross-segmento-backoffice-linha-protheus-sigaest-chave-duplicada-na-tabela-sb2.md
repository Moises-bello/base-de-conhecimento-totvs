---
article_id: 360026316234
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: df5c32b1c2f3e83fe9642956ca6b6fdc5726c79aa134109702e14bc51f8d4755
fetched_at: '2026-06-28T22:39:08.070459+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Chave duplicada na
  tabela SB2
type: support-article
updated_at: '2025-03-12T11:43:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026316234-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Chave-duplicada-na-tabela-SB2
---

**Dúvida**

Como analisar uma falha de chave duplicada na tabela SB2?

![chave duplicada sb2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/27445161632663)  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Para realizar esta analise, verifique os seguintes passos:

**1.** Avalie os campos envolvidos no X2\_ÚNICO da tabela SB2, conforme index:

Index (0) :\*\*SB20101  B2\_FILIAL+B2\_COD+B2\_LOCAL;

**2.** Validar o X2\_ÚNICO da tabela SB2, visando filtrar os registros com a mesma chave do registro duplicado:

Campos em questão (\*Conteúdo dos campos, ***apenas*** ilustrativo):

Field 1: B2\_FILIAL(C) :010101

Field 4: B2\_LOCAL(C) :01

Field 2: B2\_COD(C) :000004

**3.** Após realizar cópia da base de dados oficial, replicar em ambiente teste, apagar fisicamente os registros deletados logicamente (D\_E\_L\_E\_T\_ = '\*');

**4.** Com Acompanhamento de um analista "in loco", via APSDU realize um PACK dos registros deletados (\* cinza). Registros que estiverem com conteúdo idênticos nos campos do índice, porém deletados;

**5.** Verifique nos arquivos XX6 e XX7 a existência de funções de usuário e pontos de entrada. Valide o processo em fonte padrão;

**6.** Caso tenha efetuado manutenção direta pela SX3 no tamanho de campo \_COD, é necessário efetuar a manutenção pelo módulo Configurador utilizando o **Grupo de Campo 030 (Tamanho do Produto)**. **Obs.:** Não é permitido manutenção diretamente pela SX3.

**7.** Caso tenha alterado o tamanho do **Grupo de Campo 030 (Tamanho do Produto)** [reinstale todas as STORED PROCEDURES](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-e-Incompat%C3%ADvel-quais-as-diferen%C3%A7as-%C3%89-poss%C3%ADvel-utilizar-as-rotinas) do ambiente para que os campos sejam atualizados nas STORED PROCEDURES.

![chave duplicada sb2 grupo de campo.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/27445161642647)

**8.** Caso não existam itens deletados e após as validações acima o incidente persista, entre em contato com o Suporte Técnico para avaliação do programa.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
