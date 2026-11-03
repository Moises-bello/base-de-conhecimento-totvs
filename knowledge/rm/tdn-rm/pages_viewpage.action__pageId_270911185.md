---
content_hash: f23047d0eef15b43a6bce90e13c3a0e599784ce9bf09a35587c43e590aef7637
fetched_at: '2026-06-29T00:08:25.058455+00:00'
page_id: '270911185'
product: rm
source: tdn-rm
title: RMEDU00001_Relatório - Complemento de Disciplina
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270911185
version: 7
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Educacional |
| **Versões:** | 12.1.14 |
| **Observações:** | Extrair dados Inseridos no Complemento da Disciplina |

Os dados digitados no complemento da disciplina são armazenados na tabela SCOMPLDISC campo DESCRICAO, no formato HTML, para extração dos dados por relatório é necessário seguir os passos a seguir.

**TOTVS Educacional | Gestão | RM Reports**

Acessar o RM Reports

Criar um novo Relatório

Os campos

Código

Exemplos:

Edu - Para relatórios do Gestão Educational

Bib - Para relatórios do Gestão Bibliotecária

Fin - Para relatorios do Gestão Financeira

Descrição

São livres, recomendamos que sejam seguidos padrões da criação dos relatórios afim de agrupa-los por produto assim a localização dos mesmos se torna mais fácil e intuitiva.

O campo Aplicação é importante para definição de qual aplicativo pertence o Relatório

**Início | Adicionar Fonte de Dados**

Digitar o nome da tabela onde são armazenados os complementos digitados nas disciplinas, “SCOMPLDISC” e clicar na lupa para localizar.

Após localizar clicar na tabela, posteriormente em Adicionar e OK.

Após adicionar a tabela máster no relatório é necessário inserir o campo onde o complemento digitado será exibido

1 – Detalhe 1

2 – Clicar em Caixa de Ferramentas

3 – Clicar em Controles Avançados

4 – Clicar no Ícone “Texto Rico” e Arrastar para o Detalhe 1 do Relatórios

Após arrastar o campo ajudar o mesmo para impressão dos dados

1 – Clicar no Campo

2 – Clicar no Grade de Propriedades

3 – Dados, Clicar em Ligação de Dados - HTML -  Ligação

4 – Selecionar os Campos da Tabela inserida como Master no Detalhe 1

Criação do Filtro para teste do relatório

Neste exemplo arrastamos o campo “Código da Disciplina” para o detalhe 1 do relatório para criação do filtro para testar a funcionalidade.

Clicar em Filtros – (...) – Filtro do Relatório – Modificar – Código da Disciplina – Inserir o Código da Disciplina e Adicionar e salvar.

Obs. O Filtro foi criado apenas para testar a funcionalidade, o mesmo pode ser utilizado de outras formas.

Salvar o relatório

**Currículo e Oferta | Disciplinas**

Complemento Gravado na disciplina

Selecionar a Disciplina – Anexos – Complemento da Disciplina

Complemento inserido com formatação.

**Gestão | RM Reports**

Emissão do Relatório

Selecionar e executar o Relatório

Relatório será executado com o filtro previamente criados, o mesmo pode ser criado por parâmetros e ser inserido pelo usuário no momento da execução, para mais informações gentileza acionar a equipe de BI.
