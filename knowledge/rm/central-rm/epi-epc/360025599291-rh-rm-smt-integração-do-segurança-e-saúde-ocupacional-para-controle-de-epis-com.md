---
article_id: 360025599291
category: EPI/ EPC
content_hash: f884ce2141fc9920f970488a5c1961156aa0fed2ebf1175f444a5d742d54f046
fetched_at: '2026-06-28T22:47:38.353655+00:00'
product: rm
section_id: 1500000835001
source: central-rm
title: RH - RM - SMT - Integração do Segurança e Saúde Ocupacional para controle de
  EPIs com sistema externo
type: support-article
updated_at: '2025-10-30T18:00:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025599291-RH-RM-SMT-Integra%C3%A7%C3%A3o-do-Seguran%C3%A7a-e-Sa%C3%BAde-Ocupacional-para-controle-de-EPIs-com-sistema-externo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16036174268695) Tempo aproximado para leitura:****00:01:30 min****Dúvida**Como realizar a integração do SSO com sistema externo para controle de EPIs?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Segurança e Saúde Ocupacional - - Todas as Versões.  
  
**Solução**Para realizar a integração com sistema sistema externo para controle do EPI's, acesse o Parametrizador do SSO em **Opções** | **Parametrizador** | **Etapa EPI** e marque a opção **'Integração com sistema externo'**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31621195028759)

Quando integrado com um sistema externo terá seu controle de estoque totalmente realizado através deste sistema, isso significa que todo e qualquer tipo de movimento, entrada, saída, empréstimo e devolução será controlado neste sistema externo. Neste tipo de integração, o Catálogo de EPI deverá possuir os seguintes anexos:

• **Utilização de EPI's por Função:** Possui apenas uma visão que trará todos os EPIs que estão fornecidos, agrupados Cargo, Função, Local de Trabalho e nome de quem está com o EPI, podendo ser uma Pessoa, Funcionário ou um Local de Trabalho.

• **Utilização de EPI's por Seção:** Possui apenas uma visão que trará todos os EPIs que estão fornecidos, agrupados Filial, Departamento, Seção, e nome de quem está com o EPI, podendo ser uma Pessoa, Funcionário ou um Local de Trabalho.

• **EPI do catálogo:** Cadastro que possui todas as informações do lote do EPI, além de:

**Histórico de Fornecimento:** Será exibida uma visão informando todo o histórico de Fornecimento, contendo as informações: data do fornecimento, data da devolução, para quem foi fornecido, data de validade, se foi eficaz ou não e o motivo da devolução.

**Histórico de Higienização:** Será exibida uma visão informando todo o histórico de Higienização, contendo todas as datas que o EPI foi higienizado.

**Possuir um processo para enviar/retornar EPI á higienização:** Este processo permite ao usuário definir a data de higienização do EPI.

**Possuir um processo para definir a periodicidade de higienização:** Este processo permite ao usuário definir a periodicidade para higienização do EPI.

**Possuir um processo para invalidar** **EPI:** Este processo permite que o usuário defina o EPI como inválido.

• **Lote:** Para importação do lote com informações do estoque, o sistema exibirá o processo 'Importar Arquivo de Lote', que será executado através de um arquivo XML. Caso o arquivo esteja num formato inválido, no final do processo será exibida uma mensagem informando ao usuário este erro.

A importação do arquivo é realizada no menu **EPI/EPC** | **Catálogo** | **Processos** | **Importar Arquivo de Lote.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26899462508055)

**Atenção:** Quando integrado com um sistema externo, o sistema deverá possuir um processo para geração dos EPI's provenientes do lote, 'Gerar Itens do EPI', a execução deste processo é fundamental para que o sistema realize o fornecimento de EPI para os funcionários.

Para isso acesse o menu **EPI/EPC** | **Catálogo** e selecione o EPI desejado e acesse a opção **Anexos** | **Lote** selecione o lote e acesse a opção **Processos** | **Gerar itens do EPI/EPC**.

Abaixo segue o link com o modelos de XML's para a importar as informações:

* [Estrutura do Arquivo XML](https://tdn.totvs.com/display/LRM/Estrutura+do+Arquivo+XML)
* [Exemplo Arquivo XML](https://tdn.totvs.com/display/LRM/Exemplo+Arquivo+XML)

Ainda será possível importar também os dados de fornecimento de EPI, para isso acesse o menu **EPI/EPC** | **Importação de Fornecimento**. As importações irão ocorrer através de SQL ou arquivo TXT. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26899477945751)

**Saiba Mais**

Para maiores informações, acesse:

- [Importação de Fornecimento](https://tdn.totvs.com/pages/viewpage.action?pageId=452719512)
