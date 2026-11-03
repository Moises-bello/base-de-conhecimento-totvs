---
article_id: 4402505796247
category: SIGAEST - LEGAIS
content_hash: e405fbc9992641f93f270ec656e3c172b89c992ea4b9cbea73a19047336c1005
fetched_at: '2026-06-28T22:38:51.791845+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR949 - Configuração
  para o Relatório Mapa de Produtos Controlados - Comando Militar - Exército
type: support-article
updated_at: '2021-06-11T20:10:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402505796247-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR949-Configura%C3%A7%C3%A3o-para-o-Relat%C3%B3rio-Mapa-de-Produtos-Controlados-Comando-Militar-Ex%C3%A9rcito
---

**Dúvida**

Como configurar o Protheus para emitir o Mapa Demonstrativo de Entradas e Saídas de Produtos Controlados (Mapa do Exército)?  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Nesta documentação abordaremos como configurar e preparar o ambiente do Protheus para a correta emissão do relatório do Mapa do Exército - MATR949.

## **Criação do Menu do Relatório e dos Parâmetros envolvidos**

1° - Caso não tenha o relatório MATR949 em seu menu, basta,  via Configurador (SIGACFG), selecionar a opção “*Ambiente/Cadastros/Menus*” e incluir, no menu do ambiente Livros Fiscais, a opção para execução do MATR949, com os dados abaixo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nome do Menu** | **Submenu** | **Nome da Rotina** | **Programa** | **Tabelas** |
| Relatórios | List. Conferência | Prod. Contr. - Ex. | MATR949 | SA1, SA2, SB1,  SB5, SD1, SD2 |

2° - No próprio configurador, acessar ao caminho: “*Ambiente/Cadastros/Parâmetros*” e criar os parâmetros a seguir:

|  |  |
| --- | --- |
| **Nome** | MV\_MTR949A |
| **Tipo** | Caracter |
| **Descrição** | Campo da tabela SB5 que identifica se o produto é controlado ou não pelo exército. |
| **Conteúdo** | Informe o nome do campo da tabela SB5. |
| **Exemplo** | B5\_PRODEX |

|  |  |
| --- | --- |
| **Nome** | MV\_MTR949B |
| **Tipo** | Caracter |
| **Descrição** | Campo da tabela SA1 que contém o nome do país de origem do cliente. |
| **Conteúdo** | Informe o nome do campo da tabela SB1. |
| **Exemplo** | A1\_PAISORI |

|  |  |
| --- | --- |
| **Nome** | MV\_MTR949C |
| **Tipo** | Caracter |
| **Descrição** | Campo da tabela SA2 que contém o nome do país de origem do fornecedor. |
| **Conteúdo** | Informe o nome do campo da tabela SA2. |
| **Exemplo** | A2\_PAISORI |

|  |  |
| --- | --- |
| **Nome** | MV\_MTR949D |
| **Tipo** | Caracter |
| **Descrição** | Informar o campo da tabela SB5, que contenha a descrição do produto (consultar boletim Mapa de Prod. Contr. - Exército) |
| **Conteúdo** | Informe o nome do campo da tabela SB5. |
| **Exemplo** | B5\_DESC |

**Observação:** Caso não seja necessária a criação de um novo campo para tal tratamento, pode-se utilizar o campo padrão (B5\_CEME).

## **Verificação/Inclusão dos campos que serão utilizados no Relatório MATR949**

1° Via Configurador (SIGACFG), acessar ao caminho “Base de Dados/Dicionário/Base de Dados” e incluir/ou verifique os campos informados nos parâmetros da rotina:

|  |  |
| --- | --- |
| **Tabela** | SB5 |
| **Nome** | <critério do cliente > |
| **Exemplo** | B5\_PRODEX |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Formato** | @! |
| **Título** | <critério do cliente > |
| **Descrição** | Produto controlado pelo exército. |
| **Opções** | S=Sim; N=Não |

|  |  |
| --- | --- |
| **Tabela** | SB5 |
| **Nome** | <critério do cliente > |
| **Exemplo** | B5\_DESC |
| **Tipo** | Caracter |
| **Tamanho** | 30 |
| **Formato** | @! |
| **Título** | <critério do cliente > |
| **Descrição** | Descrição do produto a ser impresso no relatório. |

|  |  |
| --- | --- |
| **Tabela** | SA1 |
| **Nome** | <critério do cliente > |
| **Exemplo** | A1\_PAISORI |
| **Tipo** | Caracter |
| **Tamanho** | 25 (tamanho sugerido, mas pode ser menor). |
| **Formato** | @! |
| **Título** | <critério do cliente > |
| **Descrição** | País de origem do cliente. |

|  |  |
| --- | --- |
| **Tabela** | SA2 |
| **Nome** | <critério do cliente > |
| **Exemplo** | A2\_PAISORI |
| **Tipo** | Caracter |
| **Tamanho** | 25 (tamanho sugerido, mas pode ser menor). |
| **Formato** | @! |
| **Título** | <critério do cliente > |
| **Descrição** | País de origem do fornecedor. |

## **Configurando a pergunta "Informe a RM ?" para aceitar com até 2 caracteres**

Para realizar o processo no grupo de perguntas siga os passos abaixo:  
  
1. Acesse o Configurador (SIGACFG) no caminho Base de Dados > Dicionário > Bases de Dados  
2. Expanda a árvore do painel à esquerda e clique na opção "Perguntas"  
3. Pesquise pelo grupo de perguntas MTR949 e clique para "Editar"  
4. Na pergunta 4 (Informe a RM ?) informe o conteúdo @E 99 no campo **Formato** conforme abaixo e clique para Confirmar.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402519052183/mceclip0.png)

## **Parametrizando o relatório MATR949**

No ambiente Livros Fiscais, opção “Relatórios/List.Conferência/Prod. Contr. - EX” (MATR949), observe o preenchimento dos parâmetros da rotina, conforme instruções a seguir:

|  |  |
| --- | --- |
| **Produto ?** | Informe o código para imprimir apenas um determinado produto, ou deixe em branco para imprimir todos os produtos com movimentação. |
| **Data Inicial ?** | Informe o período inicial para processamento. |
| **Data Final ?** | Informe o período final para processamento. |
| **Informe a RM ?** | Informe a RM - Região Militar, conforme a tabela abaixo no artigo.  **Exemplo**: **1** – para Rio de Janeiro e Espírito Santo ou **2** – para São Paulo, etc... |
| **Informe o CR ?** | Informe o número do CR - Certificado de Registro no Exército. **Exemplo:** 6.251 |

|  |
| --- |
| **Tabela de Regiões Militares** |
| 1ª Região Militar - Rio de   Janeiro e Espírito Santo |
| 2ª Região Militar - São Paulo |
| 3ª Região Militar - Rio Grande   do Sul |
| 4ª Região Militar - Minas   Gerais (exceto o Triângulo Mineiro) |
| 5ª Região Militar - Paraná e   Santa Catarina |
| 6ª Região Militar – Bahia |
| 7ª Região Militar - Rio Grande   do Norte, Paraíba, Pernambuco, Alagoas e Sergipe |
| 8ª Região Militar - Pará,   Maranhão e Amapá |
| 9ª Região Militar - Mato Grosso   do Sul e Mato Grosso |
| 10ª Região Militar - Ceará e   Piauí |
| 11ª Região Militar - Distrito   Federal, Goiás, Tocantins e Triângulo Mineiro |
| 12ª Região Militar - Amazonas, Acre, Rondônia e Roraima |

**Informações Adicionais**

**- A quem se destina:** Às pessoas físicas e jurídicas que exercem atividades que envolvem produtos controlados pelo exército;

**- Objetivo:**Demonstrar, em forma de relatório ou mapa, as movimentações de entradas e saídas dos produtos controlado.

**- Prazo de Entrega:** Trimestral, mas pode ser enviado mensalmente.

**- Competência:** Federal.

**- Aplicativo disponibilizado pelo fisco:** Não há

**- Legislação contemplada:** Decreto nº. 3.665, de 20 de novembro de 2000.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)*
