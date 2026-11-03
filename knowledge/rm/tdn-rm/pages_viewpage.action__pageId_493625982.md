---
content_hash: 161e4f13577c71227e8e89385f618a6a132fe4068b8083be2c039618706fe56d
fetched_at: '2026-06-29T00:10:21.761148+00:00'
page_id: '493625982'
product: rm
source: tdn-rm
title: Código de Atividade Econômica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=493625982
version: 9
---

Este cadastro possibilita ao usuário parametrizar os códigos default's  para apuração da CPRB diretamente Gestão Fiscal.   
Conforme Legislação as Empresas submetidas ao regime de tributação com base no Lucro Presumido, que tenham adotado o regime de caixa como critério de apuração tributária para IRPJ, CSLL e para as Contribuições de PIS e COFINS, poderão adotar o mesmo critério para a CPRB.   
Empresas submetidas ao regime de Tributação do Lucro Real, deve apurar a CPRB pelo Regime de Competência.

* **Regime de Competência**: as apurações são feitas com base na prestação do serviço/venda independentemente de terem sido recebidos.
* **Regime de Caixa**: as receitas e despesas da empresa só são contabilizadas quando ocorrer recebimento ou pagamento e não quando são negociadas, compradas ou vendidas. Dessa forma a empresa só é tributada pelos valores recebidos e não os valores registrados no momento de emissão da Nota Fiscal.

**Como habilitar o menu**

Para habilitar o novo menu, acesse Serviços Globais | Segurança | Perfil.  
Na tela de edição do perfil do Gestão Fiscal, clicar na aba  "Acesso a Menus" e posteriormente selecionar a permissão em Gestão Fiscal em Cadastros Específicos | Mais... | Código Atividade Econômica.   
Libere a permissão de Inclusão, Edição e Exclusão.

ATENÇÃO!!!

O Código de Atividade Econômica estará disponível a partir da versão 12.1.24, sendo que nessa versão será necessário executar os scripts de banco de dados.

**Como acessar o menu**

Para acessar o cadastro, vá ao Back-Office Fiscal e  localize o menu Cadastros (Específicos) |  Mais... | Código Atividade Econômica.

### Cadastrar um Código de Atividade Econômica

Para cadastrar um Código de Atividade Econômica,  preencha:

**Aba: Identificação**

* Cód. Atividade Econômica
* Descrição (Opcional)
* Alíquota

Se houver uma alteração na Alíquota o sistema irá irá criar um registro no Log com a Alíquota anterior e a Data de Vigência igual ao dia anterior a alteração. É possível Incluir,  Editar(Data Fim Vigência) e Excluir um Log de Alteração de Alíquota, que tem os seguintes campos:

**Aba: Log Alteração Alíquota**

* Alíquota
* Data Fim Vigência

### Associando o Código de Atividade Econômica a um Produto

Acessando o BackOffice Fiscal | Cadastros (Compras/Faturamento) | Produto , selecione um produto e vá em Anexos | Dados Fiscais do Produto.  
Na aba de Identificação existirá um lookup, onde todos os registros de Atividade Econômica cadastrados poderão ser associados a um ou mais produtos.

Algumas informações importantes sobre este Cadastro:

* Não podem existir dois registros com o mesmo Cód. Atividades Econômica;
* Alíquota deve estar entre 0% - 100%;
* Para um mesmo Código de Atividade Econômica, não pode existir no Log Alteração Alíquota, duas "Data Fim Vigência" iguais.
