---
content_hash: ff740f056241ae695d545f385c1925fdc81052286c539185a65308189c5f454b
fetched_at: '2026-06-29T00:11:05.414302+00:00'
page_id: '630840982'
product: rm
source: tdn-rm
title: Faturamento para Convênios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=630840982
version: 10
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Faturamento**
3. **Reprocessamento**
4. **Refaturamento**
5. **Tabelas utilizadas**

Aviso

Informamos que a versão TISS 4.02.00 já está disponível para utilização nas versões de mercado 12.1.2502, 12.1.2506 e 12.1.2510 do produto, contemplada nos patches liberados a partir de 01/10/2025.

Para utilizar a nova versão, basta acessar o cadastro Condições Contratuais com Convênio e alterar a versão TISS para 4.02.00.

Recomendamos que sua instituição realize esta configuração e verifique eventuais adequações necessárias em seus processos de faturamento e integração com as operadoras de saúde.

## **01. VISÃO GERAL**

O processo de faturamento compreende um conjunto de contas que estão encerradas/liberadas e prontas para envio para seus respectivos Convênios, formando assim a Fatura/Remessa.

O processo de faturamento no sistema TOTVS Gestão Hospitalar Saúde é o mesmo para todos os convênios. Deve-se selecionar as contas que **NÃO** serão enviadas ao convênio e que **NÃO** irão compor a fatura/remessa

Na modalidade Faturamento Eletrônico são gravadas as informações (em arquivos ou mídias) exigidas pelos convênios de acordo com um layout pré-estabelecido entre o convênio e o prestador/hospital. Dessa forma, o convênio realiza a importação para começar o processo de Auditoria de Contas.

A maioria dos Convênios (Operadoras de Saúde) envia o arquivo de faturamento eletrônico no padrão TISS (Troca de Informação de Saúde Suplementar), definido pela ANS (Agencia Nacional de Saúde Suplementar).

Ao fim do processo de faturamento, é emitido um relatório informando o valor total de cada conta e ao fim do relatório o valor geral com a soma de todas as contas que foram encaminhadas ao convênio. Acompanha ainda o espelho da conta onde há a distribuição por Grupo de Gastos do valor apurado. Estes relatórios são encaminhados juntamente com as contas impressas para que sejam conferidas ou auditadas pelos convênios

Na tela de **Faturamento para Convênios** é feito o Faturamento, Reprocessamento e o Refaturamento das contas/faturas de convênios. Após o faturamento, caso o convênio utilize padrão TISS, será gerado um arquivo XML, que deverá ser enviado para o convênio. Caso use outros padrões de faturamento eletrônico, será gerado um arquivo txt.

## **02. Faturamento**

1. Acesse Faturamento =>Faturamento para Convênios;
2. Incluía uma nova fatura;
3. Selecione a Unidade de Faturamento e o Convênio e clique em salvar;
4. A Unidade de Atendimento, o Responsável pela Liberação da conta e o Plano são informações opcionais.

Em Processo, selecione Faturamento de Convênio:

Na opção Faturamento é realizado o faturamento das contas liberadas, gerando uma remessa para o Convênio.

1. Selecione a opção Faturamento
2. Marque a caixa Faturar contas zeradas para que somente as contas zeradas de pacientes sejam exibidas no filtro.
3. Marque a caixa Somente contas auditadas para que somente as contas que passaram pelo processo de pré-auditoria sejam exibidas no filtro.
4. Selecione o tipo de paciente (Interno ou Externo).
5. Para pacientes Externos e convênios que utilizam padrão TISS, é possível selecionar quais guias do Padrão de Faturamento TISS serão faturadas:  
   * Guias de Consulta: serão exibidas as contas de pacientes externos com guias de consulta.
   * Guia de SP/SADT: serão exibidas as contas de pacientes externos com guias de SP/SADT.
   * Guias de Honorários: serão exibidas as contas de pacientes externos com guias de honorários.
6. Preencha a Competência  e clique em avançar

Selecione manualmente as contas  e clique em avançar

Preencha a Data de Vencimento e clique em executar.

Será informado que o processo foi concluído e informado o número da Remessa.

Processo que permite alterar a competência da fatura, sem a necessidade de cancelamento da mesma.

## **03. Refaturamento**

1. Acesse Faturamento =>Faturamento para Convênios;
2. Pesquise a Remessa que deseja fazer o refaturamento;
3. Em Processo, selecione Faturamento de Convênio;
4. Selecione a opção Refaturamento, e clique em avançar.

No próximo passo será exibido as contas existente na remessa. clique em avançar

Para realizar o refaturamento:

1. Preencha a data  de vencimento e data da fatura e   clique em executar.

## **04. Reprocessamento**

1. Acesse Faturamento =>Faturamento para Convênios;
2. Pesquise a Remessa que deseja que seja Reprocessamento;
3. Em Processo, selecione Faturamento de Convênio;
4. Selecione a opção Reprocessamento, e clique em avançar.

Nela é possível :

* Excluir conta da remessa;
* Retornar conta para correções (Auditoria);
* Retornar conta para correções (Faturamento);
* Cancelar remessa.

Selecione manualmente as contas que deseja  realizar uma ação sobre a remessa, exceto cancelar remessa, que excluíra todas as contas da remessa e clique em avançar

Selecione o motivo para reprocessamento e observação se necessário clique em executar.
