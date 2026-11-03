---
content_hash: 4e96eea33639a39cbfb1ba4988aefa1a1647daad20a0bfae820bf004ee628808
fetched_at: '2026-06-29T00:11:44.910028+00:00'
page_id: '817639163'
product: rm
source: tdn-rm
title: DT - TOTVS Folha Pagamento RM x Outros Backoffices (Autônomos) - Tratar dados
  dos Dependentes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=817639163
version: 4
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Mensageria - TOTVS Folha pagamento RM x Outros Backoffices (Autônomos) |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado): | DRHROTRM-8208 |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2310.133
* 12.1.2306.200
* 12.1.2302.249 e superiores

## **03. SITUAÇÃO/REQUISITO**

Evolução da integração de autônomos com Backoffice Protheus para atender ao "Leiaute S-1.2 do eSocial”, que substituirá a DIRF a partir do próximo ano, sendo necessário informar os dados dos dependentes.

## **04. SOLUÇÃO**

Implementado os novos campos na tabela PPAGTOAUTONOMOEXTDEPEND que trata das informações de deduções de dependentes.

Foi liberado uma nova versão da mensageria 1.007 contendo as informações da nova tabela PPAGTOAUTONOMOEXTDEPEND.

**O QUE FOI AJUSTADO?**

1) Após a liberação da versão será necessário executar os script's de adequação da tabela e dos campos do sistema através do sistema **RM.Atualizador.exe.**

2) Para obter a nova versão, é necessário executar a configuração em Integração | Ferramentas | Configurar. Essa ação garantirá que a versão mais recente, que inclui as implementações na tabela PPAGTOAUTONOMOEXTDEPEND, seja devidamente atualizada e esteja disponível para utilização.

3) Após executar o passo 2, acesse Integração | Integração | Mensagem única | Integrações, edite a sua integração e cadastre o novo mapeamento. Concluídos esses passos, basta realizar a integração com o Protheus utilizando a nova versão.
