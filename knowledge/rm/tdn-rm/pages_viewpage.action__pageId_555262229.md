---
content_hash: d4b420d6d5c40648d8cf8a8f0368e1063eec70cb52241cad7378c18613846287
fetched_at: '2026-06-29T00:10:46.613988+00:00'
page_id: '555262229'
product: rm
source: tdn-rm
title: Solicitação de emissão de nota fiscal no ato do encerramento da conta do paciente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=555262229
version: 20
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplos de****Utilização**
3. **Processo** **Encerramento da Conta**
4. **Parâmetros**
5. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Processo de solicitação de emissão de nota fiscal no ato do encerramento da conta do paciente.

## **02. EXEMPLOS DE UTILIZAÇÃO**

Solicitação de emissão de nota fiscal ao encerrar a conta do paciente.

## **03. PROCESSO ENCERRAMENTO DA CONTA**

Se a parcial é Particular e o parâmetro "Emite nota fiscal ao encerrar conta de pacientes particulares" estiver marcado, ao encerrá-la o processo de Geração de Pedido de Nota Fiscal é executado. O processo muda o status do pedido para "**G**erado" e integra com o Backoffice RM. 

**Etapas do Processo:**

* Clicar no botão "Encerra"
* Confirmar o Encerramento
* Validar os dados da tela de Solicitação  de NF
* Caso necessário, selecione o usuário que deve ser usado para integrar
* Executar o processo

Importante!

Para solicitar a emissão da Nota Fiscal ao encerrar a conta do paciente, certifique-se que o parâmetro "Emite nota fiscal ao encerrar conta de pacientes particulares" (Parâmetros Gerais->Aba Faturamento) está marcado.

Caso esteja integrado com o Backoffice RM, é possível exibir a tela do Movimento gerado assim que o mesmo for criado com a solicitação da nota fiscal. Basta marcar o parâmetro conforme imagem abaixo.

Para mais informações, acesse a documentação: [Controle de Solicitação p/ Emissão de Nota Fiscal / Recibos](https://tdn.totvs.com/pages/viewpage.action?pageId=549512868).

**04. PARÂMETROS**

****Principais Campos e Parâmetros****

| Parâmetro | Descrição |
| --- | --- |
| Emite nota fiscal ao encerrar conta de pacientes particulares | Habilita a opção de solicitar a nota fiscal no ato do encerramento da conta do paciente |
| Exibe tela de movimentação do Nucleus após integrar | A tela de Movimento é exibida ao final da solicitação da nota fiscal |

## **05. TABELAS UTILIZADAS**

* SZPARCIALATEND
* SZPACIENTE
* SZGRUPOCOMPRAD
* SZCADGERAL
* SZATENDIMENTO
* SZATENDRESUMO
