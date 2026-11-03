---
article_id: 4414054296855
category: Financeiro - Contas a Pagar
content_hash: f89b2407051a1f9baec668a46cb3b8466b383bfac9ce7cfbc0eb9de792d813b9
fetched_at: '2026-06-28T22:38:08.357437+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - BackOffice Linha Protheus - SIGAFIN X RM Labore Integração
  - Erro no cancelamento, Estorno ou Exclusão de titulo pelo RM
type: support-article
updated_at: '2021-11-24T18:19:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414054296855-Cross-Segmento-BackOffice-Linha-Protheus-SIGAFIN-X-RM-Labore-Integra%C3%A7%C3%A3o-Erro-no-cancelamento-Estorno-ou-Exclus%C3%A3o-de-titulo-pelo-RM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **03****:00:00 min**

**Ocorrência**

Ao tentar realizar Estorno, Cancelamento ou Exclusão de registros integrados do **RM** ao **Protheus** porem solicitados via **RM** - o **Protheus** apresenta Mensagem retornada pelo 'App: [**PROTHEUS**] - [**RM**]':

O Título a ser excluído não foi encontrado na base Protheus!"

**Ambiente**

Cross Segmento - TOTVS BackOffice (Linha Protheus) - TOTVS Financeiro - Todas as versões

**Causa**

Esse incidente ocorre, pois a parametrização e integridade entre cadastros do RM com o Protheus pode estar divergente, vale lembrar que por se tratar de uma integração a validação entre os sistemas é realizada por cadastros pré configurados e esse processo é determinante na validação de cada ação realizada entre **PROTHEUS** X **RM**.

**Solução**

Para solucionar essa ocorrência, realize as seguintes validações e passos para correção.

**1.** **Cadastro de Fornecedor** - Existem casos de o Fornecedor estar inativo ou mesmo excluídos no **RM** e com isso o processo de integração remove o mesmo do **PROTHEUS**, então em uma situação **posterior** de cancelamento, estorno ou Exclusão a validação feita entre sistemas verifica a existência do mesmo antes de executar a ação solicitada então ao constatar divergência, apresenta a mensagem.

**2. Cadastro do DE/PARA** - Pode ocorrer a falta de preenchimento do cadastro do **DE/PARA** ou até mesmo preenchimento incorreto, vale ressaltar a necessidade de avaliar se o preenchimento esta correto tanto para conteúdo incluído, falta de conteúdo (campo em branco) que deveria conter dados de validação pré cadastrado ou até mesmo a quantidade de caracteres espaçamentos e caracteres especiais como Exemplo o **"|"** ou **";"** incluídos em cada campo.

Realizando essas validações e solicitando novamente o processo desejado via RM a validação será concluída com sucesso.

**Mais informações:   
<https://tdn.totvs.com/display/public/INT/Manual_Doc_Integracao_RMLabore_BackOfficeProtheus>**
