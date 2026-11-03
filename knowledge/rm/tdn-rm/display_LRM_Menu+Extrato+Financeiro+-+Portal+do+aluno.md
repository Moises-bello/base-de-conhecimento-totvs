---
content_hash: 0daf47931c8b71e0f96a7d3776d34882aa0275d09baa6ed3338cc2492fe6c932
fetched_at: '2026-06-29T00:11:32.776331+00:00'
page_id: '748080102'
product: rm
source: tdn-rm
title: Menu Extrato Financeiro - Portal do aluno
type: documentation
url: https://tdn.totvs.com/display/LRM/Menu+Extrato+Financeiro+-+Portal+do+aluno
version: 24
---

O novo menu estará disponível á partir da **versão 12.1.2302.**

## **CONTEÚDO**

Foi criado um novo menu para a biblioteca, o menu "Extrato Financeiro" que ficará disponível no portal do aluno.

O novo menu somente será disponibilizado se o usuário possuir taxas em aberto (Taxa de cadastro de usuário, Taxa de empréstimo e Taxa de multa), ou seja, taxas geradas fora do contrato.

O menu poderá ser acessado por alunos e usuários que não são alunos. Quando o acesso for realizado por aluno, será apresentado uma mensagem informativa orientando o aluno a consultar as novas multas no extrato financeiro.

Na opção "Ver Detalhes" será exibido em uma nova tela os valores agrupados do mesmo boleto, quando houver valores agrupados de multas. Os valores serão agrupados quando forem realizadas duas ou mais movimentações e devoluções simultâneas. Para os valores serem agrupados é necessário marcar o parâmetro de "Agrupar valores em um único lançamento".  Caminho: Biblioteca > Integração > Financeiro 2/4

Quando houver integração financeira e integração com o **TOTVS Educacional** os valores relacionados a Taxas de multa, Taxa de empréstimo ([Movimentações Bibliotecárias](https://tdn.totvs.com/pages/viewpage.action?pageId=444618799)) e/ou Taxas de cadastro do usuário não serão mais gerados diretamente no **TOTVS Gestão Financeira**, a partir de agora será criado um contrato para o usuário vinculado ao**TOTVS Gestão Bibliotecária.**

Neste contrato serão geradas as parcelas correspondentes ao valores processados e a geração de lançamento /boleto passará a seguir as regras do **TOTVS Educacional**,permitindo assim a visualização de boletos relacionados a Taxas de multa, Taxa de empréstimo e/ou Taxas de cadastro no extrato financeiro do **Portal do Aluno**.

Para que o menu "**Extrato Financeiro**" fique disponível é necessário liberar a permissão: Serviços Globais > Segurança > perfis > **Permitir o acesso a Taxas da biblioteca**. Conforme segue abaixo: 

## **MENU EXTRATO FINANCEIRO**

**Veja abaixo como será exibido no portal do aluno:**

## **BOLETO**

É necessário parametrizar o TOTVS Gestão Bibliotecária para realizar o registro online do boleto, para que o boleto seja exibido. Com o parâmetro marcado o boleto será registrado no momento da emissão. Quando clicar no boleto será possível imprimir. Se desejar salvar o boleto, é só mandar imprimir o boleto e realizar o download.

Caminho do parâmetro: TOTVS Gestão Bibliotecária > Parâmetros do sistema > Integração > Financeiro 1/4
