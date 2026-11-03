---
content_hash: 796e45918ada66eb17fe09034f141583936ae051f42ed1c908679cc3f4563df5
fetched_at: '2026-06-29T00:10:52.025376+00:00'
page_id: '569505073'
product: rm
source: tdn-rm
title: Validações Atendimento Unimed BH
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=569505073
version: 12
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Registro de Atendimento**
4. **Tabelas utilizadas**

itensVisão Geral

## **01. VISÃO GERAL**

Quando o padrão de informação do convênio é UNIMED BH, é necessário que:

* O Motivo Alta do paciente INTERNO seja um dos exigidos pela UNIMED BH (Administrativa, Evasão, Normal, Óbito, Transferência, Voluntária);
* O Tipo de Atendimento utilize um dos valores de 1 a 7 (Internação Clínica, Internação Cirúrgica, Internação Obstétrica, UTI, UTI Neo Natal, Acidente de Trabalho ou nulo);
* O código da Classe de Atendimento seja um dos seguintes valores: (E)letivo, (U)rgência ou (A)cidente no Trabalho;

Caso o atendimento não atenda todos esse critérios, não é possível encerrar a parcial.

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Log relacionado à validação:

Encerramento da Parcial

Iniciando processo de encerramento da conta.

Paciente: 39944 - PACIENTE UNIMED BH  
Prontuário: 39944. Atendimento: 9.  
Parcial 1:

Motivo de alta está incorreto. Verifique os Motivos de alta exigidos pela UNIMED-BH.  
Tipo de atendimento está incorreto. Informe o tipo correto no cadastro do atendimento, na página Dados do Atendimento pressionando o botão OUTRAS INFORMAÇÕES.  
Código da Classe de atendimento está incorreta. Informe (E)letivo, (U)rgência ou (A)cidente no Trabalho.

Processo Finalizado

## **03. TELA REGISTRO DE ATENDIMENTO**

É possível alterar o padrão de informação na tela de Registro de Atendimento → Dados de Atendimento → Convênio → Padrão de Informação

## **04. TABELAS UTILIZADAS**

* SZATENDIMENTO
* SZCADGERAL
* SZPACIENTE
]]>
