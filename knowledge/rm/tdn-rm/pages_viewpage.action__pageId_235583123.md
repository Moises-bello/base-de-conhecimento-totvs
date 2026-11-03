---
content_hash: 70359414f3bf33276041a5b3f8432ad41c89ff09602793e6333c9e028114307c
fetched_at: '2026-06-29T00:08:04.834845+00:00'
page_id: '235583123'
product: rm
source: tdn-rm
title: Manual_Revitalização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235583123
version: 6
---

|  |  |
| --- | --- |
| Descrição | Manual para Versão de Revitalização TOTVS Incorporação |
| Observações | A versão de revitalização TIN está disponível a partir da versão 12.1.9, e somente os clientes autorizados pela Equipe de Inovação do Produto poderão participar do projeto piloto, tendo acesso às alterações, com isso os demais clientes não sofrerão nenhum impacto. |

# 1. Objetivo

A versão de Revitalização do produto TOTVS Incorporação visa trazer melhorias arquiteturais e visuais a fim de torná-lo mais sustentável e flexível a inovações, bem como eliminar informações redundantes e processos obsoletos.

Os objetivos principais são:

* Eliminar Redundâncias de informações financeiras;
* Validar a Base de Dados a fim de garantir o legado e incorporar as inovações;
* Unificar o Modelo de Baixa Financeira;
* Modernizar o produto (arquitetura) e padronizar telas e processos;
* Melhorar a Performance;
* Eliminar processos Obsoletos;
* Permitir a entrada de Dados e Processos de forma mais ágil;
* Tornar os Layouts mais Simples com modelos de Cockpit;

 Neste documento serão descritas somente as alterações realizadas apresentando o cenário antes e depois quando houver. Não é objetivo deste documento descrever demais processos que não sofreram alteração.

# 2. Introdução

A versão de revitalização do TOTVS Incorporação está disponível a partir da versão 12.1.9 (linha RM) e modificou os seguintes recursos:

* Cadastro de Vendas;
* Geração do Contrato;
* Plano de Financiamento;
* Aditivos;
* Distratos;
* Permissões de acesso do Perfil Incorporação;
* Acesso rápido aos processos mais utilizados;
* Mensagens mais claras ao usuário;
* Logs detalhados.

Com a eliminação da redundância de dados e com a Unificação do Modelo de Baixa, o financeiro passa a ser o único provedor das informações financeiras.

A versão de revitalização TIN não estará disponível a todos os clientes na versão 12.1.9, e somente os clientes autorizados que participarão do projeto piloto terão acesso às alterações, com isso os demais clientes não terão nenhum impacto.

Para que o cliente Piloto possa utilizar a versão, será necessário migrar para a versão 12.1.9 padrão a partir daí se submeter a um processo de conversão especifica que será detalhado no tópico de conversão.

Salientamos que a responsabilidade pela conversão da base de dados do cliente fica a cargo do mesmo que poderá contratar o serviço de migração junto a TOTVS. Durante a fase de piloto os clientes terão acompanhamento da equipe de Inovação do Produto durante os testes limitando este tratamento até a entrada em produção, onde todos os processos já devem estar homologados pelo cliente.

Em caso de customizações desenvolvidas pela fabrica TOTVS, deverão ser atualizadas pelo processo de BSO TOTVS.

Os testes serão realizados baseados no processo do cliente e terão como apoio este manual disponibilizado pela TOTVS, que registra as modificações funcionais.

A revitalização não deve causar impacto nos Objetos Gerenciais uma vez que as estruturas modificadas foram transformadas em views afim de manter todo legado o relacionado.

## 2.1. Conversão: Requisitos Necessários

Antes de instalar a versão revitalizada é necessário passar pela validação do seu processo específico de conversão, atualizando a versão para 12.1.9 ou superiores e somente depois atualizar para a versão de revitalização.

A seguir os processos que devem ser executados e validações que devem feitas, bem como suas ações corretivas.

### 2.1.1. Executar “Conversor Revitalização”

 A fim de equalizar os dados permitindo o correto funcionamento da versão revitalizada será necessário executar a ferramenta “Conversor de Revitalização”, que corrige inconsistências de dados que teriam impacto nas novas funcionalidades.

Acesse  e siga as instruções.

# Principais alterações

A seguir serão apresentadas as principais mudanças ocorridas nas regras de negócio, estruturas de banco de dados, cadastros, anexos e processos.
