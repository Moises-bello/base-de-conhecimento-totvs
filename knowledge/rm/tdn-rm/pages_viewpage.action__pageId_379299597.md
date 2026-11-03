---
content_hash: 9cdb45f7364505e914684dfeb6545d72c243b4ff24f056d044388c95ce296056
fetched_at: '2026-06-29T00:09:02.251752+00:00'
page_id: '379299597'
product: rm
source: tdn-rm
title: DSAUGHCOM-455 DT Cadastro de CBO padrão para Prestador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379299597
version: 5
---

# Cadastro de CBO padrão para Prestador

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Cadastros > Prestador | Cadastro de Prestadores | | Cuidados com o Paciente > Centro Cirúrgico > Registro de Informações Cirúrgicas | Registro de Informações de Cirurgias | | Faturamento > Faturamento SUS > Lançamento de Procedimentos BPA | Lançamento de Procedimentos BPA | | Faturamento > Faturamento SUS > Elaboração de AIHs | Elaboração de AIHs | |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | DSAUGHCOM-455 |
| **Tabelas Utilizadas:** | SZREGRACBO |

## Descrição

Criação de campo para permitir informar um CBO padrão para o Profissional.

## Procedimento para Utilização

**Exemplo:**

       1.            No TOTVS RM Saúde, acesse Cadastros / Prestador.

       2.            Selecione um Prestador

       3.            Após abrir a tela de cadastro do Prestador, selecione Anexos > Ocupação SUS

       4.            Irá abrir a tela de Cadastro de CBO SUS do profissional

                   

       5.            Ao Inserir/Alterar um CBO irá aparecer o campo Padrão para poder selecionar. O profissional poderá ter somente um CBO padrão.

       6.            Confira os dados e confirme.

**Registro de Informações Cirúrgicas**

1. No TOTVS RM Saúde, acesse Cuidados com o Paciente / Centro Cirúrgico / Registro de Informações Cirúrgicas

         2.         Selecione o registro SUS que deseja enviar os dados para o faturamento no menu Processos / Enviar dados para faturamento

          3.         Caso o registro AIH a visualização do processo enviado pode ser visto em: Faturamento / Faturamento SUS / Elaboração de AIHs na aba Procedimentos

              4.           Caso o registro BPA a visualização do processo enviado pode ser visto em: Faturamento / Faturamento SUS / Lançamento de Procedimentos BPA

**Lançamento de Procedimentos BPA**

1. No TOTVS RM Saúde, acesse Faturamento / Faturamento SUS / Lançamento de Procedimentos BPA:
2. Selecione um registro de Lançamento de BPA ou inclua um novo registro. Na tela de lançamentos, informe o Prestador. Caso o prestador possua apenas um CBO, o sistema irá preencher automaticamente essa informação com esse CBO. Caso o prestador possua mais de um CBO, o sistema irá utilizar o CBO que estiver cadastrado como Padrão.

**Elaboração de AIHs**

1. No TOTVS RM Saúde, acesse Faturamento / Faturamento SUS / Elaboração de AIHs.
2. Selecione o registro de AIH desejado, e na aba de Procedimentos, inclua um novo registro ou altere um procedimento já existente. Ao informar o Executante, caso o prestador possua apenas um CBO, o sistema irá preencher automaticamente essa informação com esse CBO. Caso o prestador possua mais de um CBO, o sistema irá utilizar o CBO que estiver cadastrado como Padrão.  
     
            

   Importante

   Na elaboração de AIH e Lançamento de Procedimento BPA o campo CBO carregará somente os registros do prestador/Executante selecionado.
