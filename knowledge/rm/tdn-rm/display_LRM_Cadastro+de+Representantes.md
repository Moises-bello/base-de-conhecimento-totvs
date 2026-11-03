---
content_hash: 664313ac824ca77b3394f9e10425a7f2bf95bf3db1b3926dfe8690f01431ab74
fetched_at: '2026-06-29T00:09:26.050326+00:00'
page_id: '423938231'
product: rm
source: tdn-rm
title: Cadastro de Representantes
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastro+de+Representantes
version: 2
---

A descrição "Representantes" para esta tabela é default do sistema, podendo ser alterada através do Menu Opções | Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetros Gerais | Tabelas | Representante.  
O Cadastro de Representantes tem a finalidade de registrar os parceiros de negócios da empresa, armazenando informações deste relacionamento, como percentuais de Comissão e Repasse, Endereço de Pagamento, Site, E-mail.   
Além das informações cadastrais acima, o sistema disponibiliza o cadastro de Tabelas para a Integração Financeira e Defaults Contábeis, para que a contabilização de Movimentos possa ocorrer a partir destes defaults e, desta forma, todo o processo contábil e financeiro possa ocorrer de acordo com as informações do Representante.  
O sistema ainda permite que o cadastro seja configurado com o parâmetro 'Fatura Cliente Direto', que pode ser filtrado no momento de imprimir um documento de Nota Fiscal, o qual retorna os dados do Cliente/Fornecedor do Movimento ou os dados do Representante relacionado a este Movimento.   
O campo código é um campo obrigatório.   
A tela de Defaults Contábeis não será implementado na primeira versão da migração, por se tratar de uma tela de outro produto, que é customizada pelo TOTVS Gestão de Estoque, Compras e Faturamento.  
No TOTVS Gestão de Estoque, Compras e Faturamento o Cadastro de Representantes está localizado no seguinte caminho: BackOffice | Gestão de Estoque, Compras e Faturamento | Cadastros | Representantes Regras e Campos. Apenas o campo código é obrigatório, porém ele pode ser editado após a inclusão.  
No seguinte caminho BackOffice | Gestão de Estoque, Compras e Faturamento | Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.01 Parâmetros Gerais | 04.01.04 Tabelas | 04.01.04.08 Representante é possível parametrizar os seguintes itens:

* Máscara do campo código;
* Nome da Tabela;
* Descrição Representante.

Migração Para o Cadastro de Representantes do TOTVS Gestão de Estoque, Compras e Faturamento serão desenvolvidas telas Web utilizando o TOTVS HTML Framework.   
Uma vez que as telas Web forem desenvolvidas, estas serão inserida na plataforma Fluig e/ou Portal RM para que o usuário possa ter um acesso mais ágil e prático do cadastro.

1
incomplete
Tabelas Utilizadas **TRPR**
