---
content_hash: 35c918982de2181447cd24b82c6a76b44668f3ef972e12119767b33269f47fbe
fetched_at: '2026-06-29T00:10:22.688594+00:00'
page_id: '498702401'
product: rm
source: tdn-rm
title: DT - Geração do Relatório RDT (Retificação de Dados do Trabalhador) da CEF.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=498702401
version: 15
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | RH |
| Módulo: | Folha de Pagamento |
| Função: | Gerar relatório RDT de retificação de dados do trabalhador para enviar a Caixa Econômica Federal, no caso de haver contas duplicadas para o mesmo funcionário. |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : |  |

## **02. SITUAÇÃO/REQUISITO**

Para o caso de haver contas duplicadas erroneamente no registro da caixa, torna-se necessário enviar a mesma um relatório de retificação de dados do trabalhador (RDT) solicitando a unificação das contas. Para isso foi criado um processo para a geração automática deste relatório, sendo necessário informar um arquivo .CSV de saldo de FGTS de todos os funcionários.

## **03. SOLUÇÃO**

 **1 – Solicitar o relatório de informação de Saldo através do “Conectividade Social” da Caixa Econômica.**

 

Após selecionar Solicitar Informação de Saldo, na tela seguinte preencha com os valores da empresa:

Após isso ira receber a confirmação da solicitação conforme abaixo:

**2 - Após solicitar o arquivo de Informação de Saldo, deve aguardar a sua disponibilização que ocorrerá no dia seguinte.**

Para verificar o arquivo, acesse a caixa postal, ainda na Conectividade Social:

Selecione caixa de entrada:

A informação aparecerá conforme abaixo, salve o arquivo RML na sua máquina:

Salvo o arquivo, selecione no Menu, o Visualizador:

Avance na primeira tela do Visualizador:

Em seguida clique em incluir e selecione o arquivo RML salvo anteriormente:

Tendo incluído o arquivo, clique em visualizar conforme abaixo:

**3 - Após clicar no “Visualizar” colar o texto gerado com os funcionários e dados do saldo no Excel conforme abaixo.**

**Atenção: D****everá formatar no Excel as colunas para receber os valores em texto.**

**Observação****: O arquivo deve ser salvo sem o cabeçalho com** **informações****da empresa, começar a partir dos nomes do campo, conforme abaixo:**

**Observação****: O arquivo deverá ser salvo no formato "CSV (separado por virgulas)":**

**Atenção: Após salvar o arquivo em CSV, não deve-se mais fazer alterações no mesmo, essas alterações causarão problemas no processo. No caso de necessitar alterações, deve se faze-las no arquivo XLSX e então salva-lo novamente como CSV (separado por virgulas).**

Importe o relatório **FOPREL00191 - RDT - Retificação de Dados do Trabalhador**no RM Reports. Relatório disponível em: **...\CorporeRM\ObjetosGerenciais\Relatórios\FOPREL00191 - RDT - Retificação de Dados do Trabalhador.**

**4 - Salvo o arquivo corretamente no formato CSV, acesse: Folha de Pagamento | Encargos | Sefip | Retificação de Dados do Trabalhador no SEFIP:**

Preencha os campos na tela conforme informações da empresa. No campo Arquivo do Saldo da Caixa Econômica Federal, selecione o arquivo CSV salvo anteriormente.

Após executar o processo, será gerado o relatório conforme abaixo, com o pedido de unificação das contas que foram encontradas duplicadas na Caixa Econômica Federal:
