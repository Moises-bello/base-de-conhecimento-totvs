---
content_hash: 8452678bef6fa063ebf0f095ce508aaa96ba07a60d62cf5e63e48113f2da90bd
fetched_at: '2026-06-29T00:10:14.578545+00:00'
page_id: '461909270'
product: rm
source: tdn-rm
title: 11.80.0 (Estoque, Compras e Faturamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=461909270
version: 3
---

A partir da versão 11.80 todos os menus em .NET só estarão disponíveis através da MDI.Net e os antigos módulos só conterão funcionalidades ainda não migradas ou com restrições em suas versões .Net. Para maiores informações, favor consultar  a documentação do [Atualizador](http://tdn.totvs.com/display/public/LRM/Atualizador+RM).

**[Segurança de Menus](http://www.totvsconnect.blogspot.com.br/2012/05/conversor-de-seguranca-de-menu-para.html)**

Seguindo a norma que todos os menus em .NET só estarão disponíveis através da MDI.Net, a segurança dos menus de movimento foi alterada. Para que os usuários continuem acessando todos os tipos de movimentos que eram acessados através do antigo módulo, será necessário classificar todos os tipos de movimento conforme os processos no qual ele se enquadra e executar o Conversor de segurança dos menus antigos para a MDI.Net.

**[Contratos](http://wikihelp.totvs.com.br/WikiHelp/EST/EST.ManutencaoContratos.aspx)**

- Finalizada a migração dos módulos de Manutenção de Contratos e Faturamento por Lotes de Contratos para a plataforma .NET.  
- Inclusão da cópia entre coligadas das tabelas de contratos

* Tipos de Contrato
* Status de Contrato
* Motivos de Cancelamento
* Tipos de Produto para Faturamento
* Tipos de Produto por Filial

**Cadastros**

- Aumento na capacidade do campo e-mail no cadastro de transportadoras de 40 para 60 caracteres.  
- Limitado o campo 'Ref.' da 'Procedência' fiscal aos valores 0, 1, 2 e vazio além de bloquear o campo 'Descrição' para edição.  
- Adicionado o campo Condição de Pagamento na configuração de colunas e grid do histórico de últimas compras do produto.

**Movimento**

- Disponibilizada a opção para enviar email para usuário logado no processo de enviar e-mail de movimento,  
- Disponibilizado o envio automático de nota fiscal eletrônica no no processo de nota fiscal.  
- Disponibilizada separação de itens em movimentos parcialmente faturados.  
- Disponibilizada a opção de agendamento no faturamento automático.  
- Disponibilizado o faturamento de movimentos onde o valor excedente do orçamento é menor que R$ 0,01 com a parametrização Ação ao Exceder o Orçamento da etapa Orçamento esteje como Barra.  
- Criada da rotina responsável por inserir itens pelo código de barras através da tela de edição do movimento.

**Cotação**

- Migração do Relatório de Cotação para .NET.  
- Disponibilizada a opção de envio de email apenas para contatos quando utilizar a opção "Exportar orçamento p/Web".  
- Disponibilizado na tela de orçamento os campos "ICMS" e "ICMSST" para que seja possível fazer uma atualização multipla de registros.  
- Disponibilizado no processo de comunicar fornecedores a opção de selecionar relatórios do novo gerador.  
- Disponibilizada tag de segurança para processo de cancelar cotação.

**Fiscal**

Atualização para permitir dar permissão a perfis de incluir/excluir/editar Regras de ICMS e Regras de IPI no Nucleus não integrado ao Liber.

**Financeiro**

Criação da cópia de meio de pagamento entre coligadas.

Parâmetros

Criado no parametrizador da cotação um parâmetro para usuário definir o relatório padrão para exportação para web.

**Outras atualizações**

- Criação do processo responsável por copiar permissões de usuários entre coligadas.  
- Disponibilizada a impressão de relatórios criados no gerador de relatórios antigos para que sejam rodados na nova MDI.
