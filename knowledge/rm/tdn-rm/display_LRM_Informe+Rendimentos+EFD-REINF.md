---
content_hash: 008d0244d562f489eb65516605002cd0a2bc5927281d16e818d65e3da90a45cd
fetched_at: '2026-06-29T00:05:50.891143+00:00'
page_id: '1043721433'
product: rm
source: tdn-rm
title: Informe Rendimentos EFD-REINF
type: documentation
url: https://tdn.totvs.com/display/LRM/Informe+Rendimentos+EFD-REINF
version: 32
---

# Conteúdo

Conteúdo

# 1. Visão Geral

Os eventos **R-4010** e **R-4020** da **Receita Federal do Brasil** integram a série **R-4000** da **EFD-Reinf** (Escrituração Fiscal Digital de Retenções e Outras Informações Fiscais).

Essa série foi instituída para centralizar a prestação de informações relativas a **pagamentos realizados e respectivas retenções de tributos federais**, especialmente:

* Imposto de Renda Retido na Fonte (IRRF)
* Contribuição Social sobre o Lucro Líquido (CSLL)
* Programa de Integração Social (PIS/Pasep)
* Contribuição para o Financiamento da Seguridade Social (COFINS)

### Diferença entre os eventos

* **R-4010**: destinado ao reporte de **pagamentos e retenções efetuados a pessoas físicas**.
* **R-4020**: utilizado para informar **pagamentos e retenções efetuados a pessoas jurídicas**.

Esses eventos permitem que a Receita Federal consolide as informações prestadas pelas fontes pagadoras, garantindo maior controle, rastreabilidade e cruzamento de dados com outras obrigações acessórias.

## 📄 Objetivo do Relatório – Informe de Rendimentos

O **Informe de Rendimentos** foi desenvolvido com a finalidade de:

* Discriminar, de forma clara e organizada, os **valores pagos** a cada Cliente/Fornecedor;
* Evidenciar os **valores de IRRF retidos** na fonte;
* Demonstrar eventuais **retenções de contribuições sociais (CSLL, PIS e COFINS)**, quando aplicável;
* Facilitar a conferência das informações transmitidas na EFD-Reinf;
* Servir como base para conciliações contábeis e fiscais;
* Apoiar o cumprimento de obrigações acessórias e a elaboração da declaração de Imposto de Renda pelo beneficiário.

O Objeto de Negócios utilizado para geração do Relatório do Informe de Rendimentos, de nome "**EFD-REINF - Eventos Autorizados**", recupera as informações à partir dos Lançamentos Fiscais e Lançamentos Financeiros que foram enviados e efetivamente autorizados nos eventos da REINF, garantindo assim o compliance fiscal.

# 2. Relatório.

SmartView

A impressão do **Informe Rendimentos** é realizada por meio do [SMART VIEW](https://tdn.totvs.com/display/TREP/SMART+VIEW). Para instalar e configurar o SMART VIEW, consulte o guia oficial disponível em: [Instalação Smart View](https://tdn.totvs.com/pages/viewpage.action?pageId=626926739)

## 2.1 Download e importação

O Download e importação do Relatório **FISTRP0031 - Informe de Rendimentos REINF.TotvsTReports**  pode ser realizado a partir do[Totvs Compartilhamento](https://tdn.totvs.com/display/public/LRM/TOTVS+Compartilhamento).

Imagem

## 2.2 Geração do Relatório

Relatórios FiscaisRelatórios Fiscais

Após configurar o SmartView e importar o Relatório através do TOTVS Compartilhamento o mesmo vai ficar disponível no menu **Obrigações Principais** | **Relatórios Fiscais**.  
  
Selecione o Relatório **Informe Rendimentos** e gere a partir do menu **Anexos** | **Execução de Recurso SmartView**

1. Clique no ícone de funil na barra lateral direita.
2. Preencha os campos **Coligada,** **Filial e** **Ano** com os valores dos parâmetros.  
   Caso deseje, informe também uma Informação Complementar, que será impressa no relatório.
3. Clique no botão "Enviar" para gerar o relatório com os filtros aplicados.

Veja o exemplo abaixo:

Vídeo

Segue um exemplo de relatório gerado:

250

## 2.3 Edição do Relatório

O relatório pode ser customizado livremente pela empresa, por exemplo incluindo o logotipo, alterando e incluindo outras informações que já estejam no Objeto de Negócios, bastando para tanto efetuar uma cópia do relatório clicando em duplicar, esse menu estará disponível na Tela SmartView aberta no navegador. 

Clique em duplicar:

Na cópia criada clique em editar:

Acesse a aba Design:

Imagem

Veja o exemplo abaixo:

Vídeo

Mais detalhes sobre a edição de relatórios podem ser obtidos na documentação própria do SmartView: 

# 3. Exemplos do ON EFD-REINF

## 3.1 Visão de Dados

A visão de dados permite uma visualização mais detalhada e extensa de cada informação.  
No exemplo abaixo, ao vincular o objeto de negócio da EFD-REINF a uma visão de dados, devem ser preenchidos os filtros de Coligada, Filial e Ano de Geração.

Para o **Informe de Rendimentos** utilize o objeto de Negócio EFD-REINF - Eventos Autorizados.

O objeto de negócio Eventos Reinf  também pode ser usado para conferência de valores no entanto este trará os dados desagrupados de todos os eventos e Lançamentos que não foram autorizados na REINF. 

Imagem

Exemplo de inclusão da Visão de dados:

Exemplo de visão de dados

# 4. Campos do objeto de negócio

O Objeto de Negócios é composto do objeto principal e um "objeto filho" aninhado, que discrimina os dados de valores.

Atualmente, são disponibilizados os seguintes campos no objeto de negócio:

Tabela de campos

| Nome | Tipo |
| --- | --- |
| Código da coligada | Literal |
| Código da filial | Literal |
| Natureza Rendimento | Literal |
| Data Fator Gerador (MM/yyyy) | Literal |
| Código do Cliente/Fornecedor | Literal |
| Tipo do Evento | Literal |
| Nome (*do Cliente/Fornecedor*) | Literal |
| CPF/CNPJ (*do Cliente/Fornecedor*) | Literal |
| Rendimento Isento/Não Tributável | Lógico |
| Código de Receita | Literal |
| Nome da Filial | Literal |
| CNPJ da Filial | Literal |
| Inscrição Estadual Filial | Literal |
| Número | Literal |
| CEP | Literal |
| Bairro | Literal |
| Município | Literal |
| UF | Literal |
| Rua | Literal |
| Complemento | Literal |
| País | Literal |
| Nome Contador | Literal |
| **CAMPOS DO "*OBJETO FILHO*"** | |
| Valor Original (Financeiro) | Decimal |
| Valor Total (Fiscal) | Decimal |
| Valor da Base de Cálculo do IRRF | Decimal |
| Valor do IRRF | Decimal |
| Valor de Isenção | Decimal |
| Valor da Base de Cálculo do IRRFPJ | Decimal |
| Valor IRRFPJ | Decimal |
| Valor da Base de Cálculo das Retenções agregadas | Decimal |
| Valor da Retenção Agregada | Decimal |
| Valor Base de Cálculo CSLL | Decimal |
| Valor CSLL | Decimal |
| Valor Base de Cálculo COFINS | Decimal |
| Valor COFINS | Decimal |
| Valor Base PIS | Decimal |
| Valor PIS | Decimal |
| Valor da Retenção Total | Decimal |

# 5. Outras Informações

O objeto de negócio da EFD-REINF - Eventos Autorizados requer 3 parâmetros para selecionar os lançamentos, sendo eles:

* Código da Coligada
* Código da Filial
* Ano de geração

Existe um parâmetro à mais, "Info Complementar", que não é obrigatório.

Após gerar o relatório, é possível exportar o resultado para PDF. Basta clicar no botão de imprimir.

Imprimir relatório em PDF

Para exportar a tabela dinâmica ou visão de dados em ".xlsx", basta clicar no ícone.

Exportar em xlsxFiltro do objeto de negócio

Não há filtros disponíveis diretamente no objeto de negócio. Os dados devem ser filtrados no tipo de visão escolhida para exibição dos dados.

**Reforçando:**

Diferente do objeto de negócio da REINF que permite gerar informações nas visões do Smart View (relatório, tabela dinâmica e visão de dados) antes que os eventos sejam gerados, este relatório retorna apenas os eventos 4010 e 4020 que já foram **autorizados**. 

---
