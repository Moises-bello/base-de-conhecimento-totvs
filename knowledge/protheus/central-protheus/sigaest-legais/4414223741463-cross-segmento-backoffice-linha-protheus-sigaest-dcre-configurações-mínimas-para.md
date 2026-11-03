---
article_id: 4414223741463
category: SIGAEST - LEGAIS
content_hash: ce6830bb605ad229220c6ffe31afe01907e775de9f94e8419e5b1bcd766ea076
fetched_at: '2026-06-28T22:38:51.639251+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - DCRE - Configurações
  mínimas para geração
type: support-article
updated_at: '2021-11-29T11:14:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414223741463-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-DCRE-Configura%C3%A7%C3%B5es-m%C3%ADnimas-para-gera%C3%A7%C3%A3o
---

**Dúvida**Como parametrizar e configurar o Protheus para a geração do DCRE?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Para configuração do DCRE, deve seguir os passos a seguir:

1. No **Configurador (SIGACFG)** acesse **Ambientes/Cadastros/Parâmetros (CFGX017)**. Crie/configure o(s) parâmetro(s) a seguir:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414223713815/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414223723671/mceclip1.png)

2. Caso os campos indicados nos parâmetros não existam, deve ser criados no módulo **Configurador (SIGACFG)**, opção **Base de Dados/Dicionário/Base de Dados (CFGX031)**, conforme a seguinte estrutura:

- Campo B5\_INDSUSP:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414223780631/mceclip6.png)

- Campo B5\_INDRED.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414230532503/mceclip5.png)

3. Como a DCRE faz validação dos componentes de um produto acabado (PA) é necessário que exista uma estrutura (MATA200), e Entradas de Notas dos componentes. Outro ponto importante é a Origem do Produto (B1\_ORIGEM) para definir se é um componente nacional ou importado.

**Geração do DCRE**

Importante: Copiar o arquivo **DCRE.INI**  para a pasta system do Protheus (arquivo disponível no final da documentação)

**Data Inicial ?**

Não há necessidade de informar este parâmetro, pois não será utilizado pelo sistema.

**Data Final ?**

Não há necessidade de informar este parâmetro, pois não será utilizado pelo sistema.

**Instr. Normativa ?**

Informe o nome do arquivo de configuração, sem a extensão .INI. Para este meio magnético, informe DCRE (para o DCRE v.3.0) ou LISTA (para o DCRE v.2.0).

**Arq. Destino ?**

Informe o nome do arquivo de destino.

**Diretório ?**

Informe o nome do diretório em que será gerado o arquivo destino.

**Seleciona Filiais?**

Informe se deseja selecionar as filias que serão processadas. Ao informar **Não**, apenas a filial corrente será considerada; ao informar **Sim**, o sistema apresenta uma tela para seleção das filiais a serem consideradas.

**Aglutina Obrigação?**

Informe se deseja algutinar a informação das filias que serão processadas, gerando um único arquivo. Ao informar **Não**, a informação das filiais continuará sendo gerada como anteriormente; ao informar **Sim**, o sistema aglutinará a informação das filiais selecionadas em um arquivo único.

4. Ao conferir os parâmetros, serão apresentados os dados específicos da DCRE:

**Data de Processamento ?**

Informe a data base para processamento das notas fiscais e D.I.

**Data de Validade ?**

Informe a data de validade dos componentes da estrutura.

**No. Revisão da Estrutura ?**

Informe o número de revisão da estrutura do produto.

Observação: Deixe o parâmetro em branco caso não necessite validar por revisão de estrutura.

**Produto ?**

Informe o código do produto que será internado (Selecionar o Produto Acabado).

**CPF do Representante Legal ?**

Informe o número do CPF do representante legal.

**Proc. Produtivo Básico (PPB) ?**

Informe a identificação do processo produtivo básico do produto (PPB) e Resolução SUFRAMA.

**Tipo de Coeficiente de Redução ?**

Informe o tipo de coeficiente de redução: F-Fixo ou V-Variável.

**Tipo do DCRE ?**

Informe o tipo de DCRE: N-Novo; R-Retificador ou S-Substitutivo.

**No. DCRE Anterior ?**

Informe o número do DCRE anterior que será retificado ou substituído, somente quando o Tipo do DCRE for R-Retificador ou S-Substitutivo, caso contrário, deixe este parâmetro em branco.

**No. Processo Retificador ?**

Informe o número do processo retificador, somente quando o parâmetro Tipo do DCRE for R-Retificador, caso contrário, deixe este parâmetro em branco.

**Moeda de Conversão dos Valores ?**

Informe o código da moeda para conversão em dólar.

Nota: Existem duas formas de conversão: 1. Quando não houver integração com o ambiente de Importação (SIGAEIC), será utilizado para conversão o Cadastro de Moedas; 2. Quando houver integração com o SIGAEIC, será utilizada a Tabela de Taxa de Conversão.

**Salários/Ordenados ?**

Informe o total dos custos com salários e ordenados, convertido na moeda selecionada.

**Encargos Sociais/Trabalhistas ?**

Informe o total dos custos com encargos sociais e trabalhistas, convertido na moeda selecionada.

**Saiba mais:**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - DCRE - Conceito e Informações Importantes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414230206871)*

*[Clique aqui e veja mais artigos sobre Relatórios Legais](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)*
