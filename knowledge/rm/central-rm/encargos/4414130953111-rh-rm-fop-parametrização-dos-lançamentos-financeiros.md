---
article_id: 4414130953111
category: Encargos
content_hash: 6c57b77ccc8f73d93f5fb9b70741c2608dbaf4f7301e5cefb769e8e24ac8e46e
fetched_at: '2026-06-28T22:46:53.209001+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Parametrização dos Lançamentos Financeiros
type: support-article
updated_at: '2025-01-16T20:33:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414130953111-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-dos-Lan%C3%A7amentos-Financeiros
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:04:20 min****Dúvida**Como realizar a parametrização dos Lançamentos Financeiros?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões **Solução**Para criar e parametrizar os Lançamentos Financeiros acesse: **Encargos | Cadastros Financeiros | Parâmetros**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10986781867287)

Após acessar os parâmetros, clique em incluir para criar um novo. Os campos em **negrito** são de preenchimento obrigatório.    
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10986821634071)  
  
**Código**: Preenchimento com descrição definida pela empresa.  
  
**Tipo do Lançamento Financeiro**: Selecione o tipo de lançamento financeiro que identificará sua finalidade. O cadastro de Tipos de Lançamentos Financeiros estão localizados em uma tabela dinâmica, no menu **Administração de Pessoal | Cadastros | Cadastros Globais | Tabelas Dinâmicas | Tabela CODLANFIN**. **Saiba mais: [RH - RM - FOP - Incluir Lançamentos Ativos na Geração de Lançamentos Financeiros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7763397883159-RH-RM-FOP-Incluir-Lan%C3%A7amentos-Ativos-na-Gera%C3%A7%C3%A3o-de-Lan%C3%A7amentos-Financeiros)**

**Tipo de Documento**: Selecione o tipo de documento, que será transferido para o RM Fluxus ao ser gerado o lançamento financeiro no RM Folha de Pagamento.  
  
**Cód. Fornecedor**: Informe o código para o cliente/fornecedor. Não é permitido a inclusão de códigos repetidos, portanto, um código somente refere-se a um determinado cliente/fornecedor. O campo é alfanumérico, definido através da máscara informada em **RM| Back Office| Gestão Financeira| Ambiente| Configuração| Parâmetros| TOTVS Gestão Financeira | Manutenção de Lançamentos | Cliente/ Fornecedor| Máscara do Código no RM Fluxus**.  
  
**Fórmula**: Se o tipo da ocorrência for **Valor calculado por fórmula** este campo indicará qual fórmula que deverá ser utilizada no lançamento financeiro.  
  
**Aplicar Arredondamento sobre o valor total do lançamento**: Marque este parâmetro para que o sistema faça a soma de todos os valores que compõem o lançamento antes de realizar o arredondamento.  
  
**Rateio que o lançamento segue**: Deve ser informado neste campo o código do rateio definido em **CADASTRO | RATEIO DE EVENTOS**. O Lançamento Financeiro com informação neste campo não seguirá o Rateio Fixo definido no cadastro de funcionários e SIM, seguirá ocorrência dos eventos que foram cadastrados no Rateio por Evento para que ele seja calculado. Ele só seguirá o Rateio Fixo definido no cadastro de funcionários, se os eventos cadastrados no Rateio por Evento não existirem na movimentação do funcionário.  
  
**Complemento de Histórico**: Este campo será utilizado pelo usuário que desejar acrescentar maiores informações no histórico de lançamentos financeiros.  
  
**Fórmula para complemento de histórico**: Além do histórico padrão e o complemento do histórico, o usuário poderá acrescentar mais informações no histórico do lançamento através de fórmulas. Para isto, o usuário deverá cadastrar previamente a fórmula desejada e selecioná-la neste campo.  
  
**Usar histórico padrão**: Com este parâmetro desmarcado, o sistema irá levar para o lançamento financeiro somente as informações do campo **Complemento do Histórico** e do campo **Fórmula para complemento de histórico**. Caso contrário, o histórico do lançamento financeiro será a composição do histórico padrão **Descrição do lançamento financeiro + Mês e Ano competência + Período**, do campo **Complemento do Histórico** e do campo **Fórmula para complemento de histórico**.  
  
**Período de Cálculo do Rateio**: Este campo é de preenchimento obrigatório caso o parâmetro **Rateio que o lançamento segue** seja marcado. Nele poderá ser informado os seguintes períodos:  
  
1. **Mês Atual**: fará o rateio conforme os rateios fixos informados no cadastro do funcionário

2. **Período Aquisitivo**: fará o rateio conforme os rateios realizados durante o período aquisitivo de Férias.

3. **Ano de Competência**: fará o rateio conforme os rateios realizados durante o ano de competência atual.

4. **Mês Anterior**: fará o rateio de acordo com o rateio por centro de custo utilizado no mês anterior, tomando como base, a ficha financeira por centro de custo. Quando essa movimentação não existir o sistema deverá buscar o centro de custo do Rateio Fixo do funcionário.

5. **Competência passada no Processo**:fará o rateio conforme os rateios realizados durante o ano competência passada.   
  
**Importante**Para mais detalhes e informações sobre o preenchimento de algumas informações especificas na parametrização dos Lançamentos Financeiros **Acesse-o neste link**: [Parametrização dos Lançamentos Financeiros](https://tdn.totvs.com/display/public/LRM/Cadastros+Financeiros) **Saiba mais**[Lançamento Financeiro - Documentos de Referência](https://tdn.totvs.com/pages/releaseview.action?pageId=452719571)
