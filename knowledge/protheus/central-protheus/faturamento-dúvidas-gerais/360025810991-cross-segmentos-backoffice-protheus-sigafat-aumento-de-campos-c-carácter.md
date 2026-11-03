---
article_id: 360025810991
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 84d0bd02d9e62f4427e8786581f836806b47fa3921c712e0c8ee79f0802d5e01
fetched_at: '2026-06-28T22:38:28.763802+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT -  Aumento de campos "C - Carácter"
type: support-article
updated_at: '2025-07-24T11:03:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025810991-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Aumento-de-campos-C-Car%C3%A1cter
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33683359949463) Tempo aproximado para leitura: **00:03:30 min******

**Dúvida**

Existe algum impacto de alterar o tamanho de campo do tipo carácter no Faturamento?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões - Todas as versões

**Solução**

Os campos de descrição/nome no Protheus são, geralmente, do tipo “**1 - Caracter**”, a alteração de tamanho destes campos, como por exemplo: "Nome do Cliente (A1\_NOME)" ou "Descrição do Produto no Cliente (A7\_DESCCLI)", não causam nenhum impacto.

Porém, para o ajuste é necessário realizar o aumento de todos os campos das tabelas relacionadas que recebem a informação deste campo.

**Exemplo:** Caso aumente o campo Nome do Cliente **(A1\_NOME)**, basta seguir o passo a passo:

1. Acessar ao Configurador (SIGACFG);

2. Acesse Base de Dados -> Dicionário -> Base de Dados;

3. Verifique no campo **A1\_NOME** da tabela Cadastro de Cliente (**SA1**) qual o grupo de campos:

**Observação 1:** O campo A1\_NOME atualmente possui grupo apenas na release 2410, entretanto o exemplo serve para alteração de campos "tipo Caracter":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33683346311831)

4. Acesse Dicionário de dados -> Grupo de campos e procure por "175 - Nome do Cliente" e clique no ícone de edição conforme exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33683346318231)

5. Realize o ajuste do tamanho desejado respeitando o tamanho mínimo e tamanho máximo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33683359958167)

6. Por fim, basta salvar a alteração:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33683359960471)

**Observação 2**: Pode ocorrer um desposicionamento de campo, se for utilizado em relatórios, por exemplo, pois o relatório estará parametrizado para um tamanho mínimo de caracteres relacionado ao campo em questão, sendo necessário ajustar a visualização.

**Observação 3:**Caso o campo "tipo Caracter" não possuir um "Grupo de Campos" basta alterar o tamanho diretamente no X3\_TAMANHO do campo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33683359963671)
