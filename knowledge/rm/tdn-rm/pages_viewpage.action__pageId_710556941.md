---
content_hash: 92bdf03dec4100f131bd341a016d3c039e7ebea8abfeb9187dcca1d2f1bcea17
fetched_at: '2026-06-29T00:11:25.541058+00:00'
page_id: '710556941'
product: rm
source: tdn-rm
title: Serviços para Taxas da Biblioteca
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=710556941
version: 50
---

Ao acessar o módulo da Biblioteca, será exibido a seguinte mensagem: Á partir da **versão 12.1.2302** a geração de taxas da biblioteca para alunos, será associada a um contrato do aluno, por isso será obrigatória a parametrização de um serviço do TOTVS Educacional no cadastro 'Serviço para Taxas da Biblioteca' localizado na aba Parâmetros / Configurações.

## **CONTEÚDO**

Quando houver integração financeira e integração com o **TOTVS Educacional** os valores relacionados a Taxas de multa, Taxa de empréstimo () e/ou Taxas de cadastro do usuário não serão mais gerados diretamente no **TOTVS Gestão Financeira**, a partir de agora será criado um contrato para o aluno, com o Tipo do contrato TOTVS Gestão Bibliotecária, vinculado ao usuário do **TOTVS Gestão Bibliotecária.**

Neste contrato serão geradas as parcelas, do tipo Parcela Adicional (nas versões anteriores a 12.1.2302.), correspondentes aos valores processados e, a geração de lançamento/boleto passará a seguir as regras do **TOTVS Educacional**,permitindo assim a visualização de boletos relacionados a Taxas de multa, Taxa de empréstimo e/ou Taxas de cadastro no extrato financeiro do **Portal do Aluno**. Portanto será necessário cadastrar no **TOTVS Gestão Bibliotecária** para todas as unidadesos serviços que serão utilizados na geração das parcelas do contrato.

Em **Serviço para Taxas da Biblioteca** foi implementada a possibilidade do usuário escolher um tipo de parcela (**parcela do plano, adicional ou extra**) para cada **Tipo de Taxa da Biblioteca**,permitindo que o tipo de parcela seja alterado pelo usuário a qualquer momento. Na geração da parcela para o contrato do educacional, essa parcela passará a ser gerada com o tipo de parcela que foi escolhido pelo usuário na associação com o serviço.

As parcelas criadas antes da implementação permanecerão com o mesmo tipo de parcela com que foram criadas.

Essa funcionalidade está disponível a partir dos patches: **12.1.2302.**

Importante

Caso o usuário da biblioteca seja um aluno, porém matriculado em uma coligada que não seja a coligada corrente da operação bibliotecária, as taxas não serão geradas no **TOTVS Educacional,** serão geradas no T**OTVS Gestão Bibliotecária,** sendo possível visualizar a taxa gerada na aba **"Lançamentos"** do usuário na tela de movimentação.

## **Serviços para Taxas da Biblioteca**

Esse cadastro tem como objetivo mapear os serviços que serão utilizados na geração do contrato quando forem gerados Taxas de multa, Taxa de empréstimo e/ou Taxas de cadastro do usuário.

Para que o menu "**Serviços para Taxas da Biblioteca**" fique disponível:

* É importante validar as permissões de acesso ao menu no cadastro do perfil de usuário.
* É necessário que opção "Utilizar a integração com o TOTVS Educacional" esteja marcada (ir em Parâmetros do Sistema> Integração)

**Regras:**  
• Não será permitido incluir dois ou mais tipos de **Serviços** para um mesmo **Tipo de taxa da Biblioteca**, regra se aplica quando se tratar do mesmo nível de ensino cadastrado.

• Não será permitido cadastrar o mesmo Serviço, para todos os Tipos de Taxas.

• Não será permitido a edição dos campos **Nível de ensino** e **Tipo de Taxa da Biblioteca**.

• Somente pode ser editado o campo Serviço.

## Informações do cadastro

**Nível de ensino:** Informar o Nível de ensino para o qual a regra será aplicada.

**Serviço:** Informar o Serviço (serão exibidos todos os serviços cadastros para o nível de ensino selecionado).

**Tipo de Taxa da Biblioteca:** Informar quais as taxas que serão aplicadas para o nível de ensino selecionado.

Opções: Taxa de cadastro de usuário, Taxa de empréstimo e Taxa de multa.

A opção "**Preencher data de competência com mês e ano do vencimento da parcela?**" foi adicionada na tela de cadastro dos "**Serviços para Taxas da Biblioteca**". Com esta opção marcada, as parcelas geradas terão a data de competência com o mesmo ano e mês da data de vencimento

Essa funcionalidade está disponível a partir dos patches: **12.1.2306.174** e **12.1.2310.108**.

**Centro de Custo/Departamento:**

O Centro de Custo/Departamento que será preenchido nos lançamentos que serão gerados no **TOTVS Educacional**, será o que está parametrizado na Unidade Bibliotecária do **TOTVS Gestão Bibliotecária.**
