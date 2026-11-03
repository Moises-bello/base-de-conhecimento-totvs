---
content_hash: f963beb3d97b784b86499f2a6747ebef1b760bb40cf5a17b70f3d7462fca6161
fetched_at: '2026-06-29T00:08:11.947131+00:00'
page_id: '243631642'
product: rm
source: tdn-rm
title: DT_CPMOV001-357_Enviar_Email_Contatos_Fornecedor
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_CPMOV001-357_Enviar_Email_Contatos_Fornecedor
version: 119
---

# ENVIAR E-MAIL PARA CONTATOS DO FORNECEDOR

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | **Gestão de Compras*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Envio de Ordens de Compra Via E-mail* | *MovEnviaEmailMovAction* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Cotação* | *CmpCotacaoAction* | | *Enviar E-mail para Cliente/Fornecedor.* | *MovEnviaEmailMovAction* | |
| **Cadastros Iniciais:** | *O **Status da Cotação** deve ser igual a **Pedido de Compra*** |
| **Parâmetro(s):** | *Perfil do usuário deve possuir permissão para **Enviar OC via Email**.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Chamados Relacionados** | *Não se aplica.* |
| **Requisito (ISSUE):** | *PCREQ-9558 e CPMOV001-357* |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | *Oracle ou SQL Server.* |
| **Tabelas Utilizadas:** | **TTMVEXT - Tipos de movimento**  *TMOV - Movimentos.* |
| **Sistema(s) Operacional(is):** | *Windows 7 SP1 ou superior.* |

## Descrição

**Enviar** **E-mail para Cliente/Fornecedor**

Disponibilizado na rotina **Enviar** **E-mail para Cliente/Fornecedor** uma opção para que seja feito o envio do e-mail apenas para os contatos do fornecedor, ignorando o e-mail principal:**E-mail para contatos Cliente/Fornecedor**.

O e-mail principal será uma opção na tela de envio e será exibida marcada por padrão: **E-mail para o fornecedor.**

Será permitido enviar e-mail individualmente para as demais opções e a única opção que será enviada como cópia será a opção **Cópia de e-mail para Usuário Logado**.

**Visão de Movimentos**

Disponibilizado na visão de **Movimentos** uma coluna para identificar o **Status de Envio de E-mail**. Os status serão: **Enviado** e **Não Enviado**. Esse campo também será visualizado através da **Cotação** pelo anexo **Pedido Gerados.**

**Observação:**na visão de Movimento este campo ficará disponível somente se o parâmetro **Envia E-mail** estiver habilitado para o tipo de movimento selecionado. Consulte o tópico Procedimento para Configuração para verificar como parametrizar o tipo de movimento para exibir esta informação.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PERMISSÃO PARA ENVIAR ORDEM DE COMPRAS VIA E-MAIL PELA COTAÇÃO**

1. Acesse módulo **Serviços Globais / Segurança / Perfis** selecione o contexto de **Sistema: Gestão de Estoque, Compras e Faturamento.**
2. Edite o perfil e na pasta **Acesso a Menus permitir acesso** ao item**[03.01.02.07] Enviar OC via Email*****.***

**CONFIGURAÇÃO DE TIPO DE MOVIMENTO PARA EXIBIR STATUS DE E-MAIL NA VISÃO DE MOVIMENTOS E EXIBIR OPÇÃO DE ENVIAR E-MAIL PARA CONTATOS CLIENTE/FORNECEDOR**

1.  Acesse **Gestão de Estoque, Compras e Faturamento/Parâmetros/**Gestão de Estoque, Compras e Faturamento/04.06 - Gestão de Compras/04.06.04 - Ordem de Compra****

2. **Parametrizar Tipo de Movimento**. Avance até a **Etapa Mov - Impressão 2/2**

3. Marque a opção **Envia E-mail** para que a coluna **Status Envio de E-mail** fique disponível na visão de **Movimentos.**

4. Marque a opção **Usar contato do fornecedor no envio de email** para exibir a opção **E-mail para contatos Cliente/Fornecedor** no assistente de **Enviar** **E-mail para Cliente/Fornecedor.**

## Procedimento para Utilização

       1. No Gestão de Estoque, Compras e Faturamento, acesse **Compras / Cotação**.

O sistema apresenta a janela de **Filtros - Cotação - Composição.**

       2. Selecione uma opção de filtro e clique em Executar.

       3. Na visão de Cotação selecione uma Cotação com **Status Negociação da Melhor Oferta** e clique em **Gerar Ordem de Compra**.

O sistema apresenta a janela **Gerar Ordem de Compra**.No passo **Parametrização Geração Ordem de Compra** marque a opção **Gerar Ordem de Compra para fornecedores que venceram a Cotação** avance e clique em **Executar.**

       4. Após a geração da ordem de compra, edite a cotação e clique em **Envio de Ordens de Compra via Email.**

O sistema apresenta a janela **Enviar E-mail para Clientes/Fornecedores**.

       5. Informe os dados e selecione os destinatários e execute o processo.

divs
